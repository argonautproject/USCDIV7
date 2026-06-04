#!/usr/bin/env python3
"""
review_displays.py  --  Stage C + D of the US Core SNOMED display review.

Joins the VSAC expansion display strings (expansions.csv) to the local RF2
index (snomed-index.parquet), classifies every SNOMED (code, display) pair
against the flag taxonomy, and writes:

    output/review_flagged.csv    rows that need attention (problems only)
    output/review_summary.md     counts per flag, per value set, version status

Flag taxonomy (display match quality):
    OK_PREFERRED          display == active Preferred Term
    FSN                   display == active Fully Specified Name (not the PT)
    NOT_PREFERRED_ACTIVE  active synonym that is neither PT nor FSN
    INACTIVE_DESCRIPTION  matches only an inactive (retired) description
    CASE_OR_WHITESPACE    matches the PT only after normalization
    NO_MATCH              matches no description for this concept
    UNKNOWN_CONCEPT       concept id not present in this RF2 release

Concept retirement is reported separately (concept_active column): a row that is
OK_PREFERRED but sits on an inactive concept still needs attention.

Version alignment: the SNOMED edition in expansions.csv.meta.json is compared to
the RF2 release in snomed-index.parquet.meta.json. A mismatch does not stop the
run; it is stamped on every output row (version_aligned=False) so drift-driven
flags are never mistaken for real ones.

Classification is a vectorized merge (no per-row Python loop), so it scales to
the full expansion set.

Paths default to the skill directory (resolved from this file's location); all
are overridable.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import numpy as np
import pandas as pd

SNOMED_SYSTEM = "http://snomed.info/sct"

SKILL_DIR = Path(__file__).resolve().parents[1]  # scripts/ -> skill root
DEFAULT_INDEX = SKILL_DIR / "cache" / "snomed-index.parquet"
DEFAULT_EXPANSIONS = SKILL_DIR / "cache" / "expansions.csv"
DEFAULT_OUTDIR = SKILL_DIR / "output"

ATTENTION_ORDER = [
    "FSN", "NOT_PREFERRED_ACTIVE", "INACTIVE_DESCRIPTION",
    "CASE_OR_WHITESPACE", "NO_MATCH", "UNKNOWN_CONCEPT", "OK_PREFERRED",
]


def normalize(series: pd.Series) -> pd.Series:
    return series.str.strip().str.replace(r"\s+", " ", regex=True).str.lower()


# --------------------------------------------------------------------------- #
# Version alignment
# --------------------------------------------------------------------------- #
def expansion_versions(expansions_csv: Path) -> tuple[list[str], list[str]]:
    meta_path = Path(str(expansions_csv) + ".meta.json")
    if not meta_path.exists():
        return [], []
    m = json.loads(meta_path.read_text())
    uris = sorted({v for x in m.values() for v in x.get("snomed_versions", [])})
    dates = sorted({mm.group(1) for v in uris
                    if (mm := re.search(r"/version/(\d{8})", v))})
    return uris, dates


def index_release(index_path: Path) -> str | None:
    meta_path = Path(str(index_path) + ".meta.json")
    if not meta_path.exists():
        return None
    return json.loads(meta_path.read_text()).get("release_date")


# --------------------------------------------------------------------------- #
# Classification (vectorized)
# --------------------------------------------------------------------------- #
def classify(exp: pd.DataFrame, idx: pd.DataFrame) -> pd.DataFrame:
    exp = exp.reset_index(drop=True).copy()
    exp["row"] = exp.index
    exp["display_norm"] = normalize(exp["display"])

    # Concept-level facts.
    concept_active = idx.drop_duplicates("conceptId").set_index("conceptId")["conceptActive"]
    pt = idx[idx["is_pt"]].drop_duplicates("conceptId").set_index("conceptId")["term"]
    known = set(idx["conceptId"].unique())

    # Exact match: (code, display) == (conceptId, term).
    ex = exp.merge(
        idx[["conceptId", "term", "descActive", "is_pt", "is_fsn"]],
        left_on=["code", "display"], right_on=["conceptId", "term"], how="left",
    )
    ex["m_exact"] = ex["term"].notna()
    ex["m_active"] = ex["descActive"].eq("1")
    ex["m_inactive"] = ex["descActive"].eq("0")
    ex[["is_pt", "is_fsn"]] = ex[["is_pt", "is_fsn"]].fillna(False)
    agg = ex.groupby("row")[["m_exact", "is_pt", "is_fsn", "m_active", "m_inactive"]].max()

    # Soft match against the PT only (case / whitespace).
    sx = exp.merge(
        idx.loc[idx["is_pt"], ["conceptId", "term_norm"]],
        left_on=["code", "display_norm"], right_on=["conceptId", "term_norm"], how="left",
    )
    sx["soft_pt"] = sx["conceptId"].notna()
    soft = sx.groupby("row")["soft_pt"].max()

    res = exp.set_index("row").join(agg).join(soft.rename("soft_pt"))
    res["known"] = res["code"].isin(known)
    res["concept_active"] = res["code"].map(concept_active).eq("1")
    res["preferred_term"] = res["code"].map(pt).fillna("")

    conditions = [
        ~res["known"],
        res["m_exact"] & res["is_pt"],
        res["m_exact"] & res["is_fsn"],
        res["m_exact"] & res["m_active"],
        res["m_exact"] & ~res["m_active"],          # exact, only inactive description
        ~res["m_exact"] & res["soft_pt"].fillna(False),
    ]
    choices = ["UNKNOWN_CONCEPT", "OK_PREFERRED", "FSN",
               "NOT_PREFERRED_ACTIVE", "INACTIVE_DESCRIPTION", "CASE_OR_WHITESPACE"]
    res["flag"] = np.select(conditions, choices, default="NO_MATCH")

    # A row needs attention unless it is OK_PREFERRED on an active concept.
    res["needs_attention"] = ~((res["flag"] == "OK_PREFERRED") & res["concept_active"])
    return res.reset_index(drop=True)


# --------------------------------------------------------------------------- #
# Reporting
# --------------------------------------------------------------------------- #
def write_summary(res: pd.DataFrame, md_path: Path, aligned: bool,
                  exp_dates: list[str], idx_release: str | None) -> None:
    total = len(res)
    counts = res["flag"].value_counts()
    inactive_concepts = int((~res["concept_active"]).sum())

    lines = ["# US Core SNOMED Display Review", ""]

    if not exp_dates or idx_release is None:
        lines += ["> **Version check: INCONCLUSIVE** — missing metadata; "
                  "results stamped `version_aligned` accordingly.", ""]
    elif aligned:
        lines += [f"> **Version check: OK** — expansions and RF2 index both at "
                  f"`{idx_release}`.", ""]
    else:
        lines += [f"> **Version check: MISMATCH** — expansion SNOMED "
                  f"{', '.join(exp_dates)} vs index `{idx_release}`. "
                  f"Flags may reflect version drift, not real defects.", ""]

    lines += [f"- Rows reviewed: **{total:,}**",
              f"- Need attention: **{int(res['needs_attention'].sum()):,}**",
              f"- On inactive concepts: **{inactive_concepts:,}**", "",
              "## Counts by flag", "", "| Flag | Count |", "|---|---|"]
    for flag in ATTENTION_ORDER:
        if flag in counts:
            lines.append(f"| {flag} | {int(counts[flag]):,} |")

    lines += ["", "## By value set", ""]
    ct = pd.crosstab(res["valueSetName"], res["flag"])
    present = [f for f in ATTENTION_ORDER if f in ct.columns]
    ct = ct[present]
    header = "| Value set | " + " | ".join(present) + " |"
    sep = "|---" * (len(present) + 1) + "|"
    lines += [header, sep]
    for name, row in ct.iterrows():
        lines.append("| " + name + " | " + " | ".join(str(int(v)) for v in row) + " |")

    lines += ["", "_Problems-only rows are in review_flagged.csv "
              "(OK_PREFERRED on active concepts excluded)._"]
    md_path.write_text("\n".join(lines))


def main() -> None:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--expansions", type=Path, default=DEFAULT_EXPANSIONS,
                    help="SNOMED expansions CSV from expand_valuesets.py")
    ap.add_argument("--index", type=Path, default=DEFAULT_INDEX,
                    help="snomed-index.parquet from build_snomed-index.py")
    ap.add_argument("--out-dir", type=Path, default=DEFAULT_OUTDIR,
                    help="Directory for the flagged CSV and markdown summary")
    args = ap.parse_args()

    if not args.expansions.exists():
        sys.exit(f"ERROR: expansions CSV not found: {args.expansions}")
    if not args.index.exists():
        sys.exit(f"ERROR: index not found: {args.index}")

    exp = pd.read_csv(args.expansions, dtype=str, keep_default_na=False)
    idx = pd.read_parquet(args.index)

    exp_uris, exp_dates = expansion_versions(args.expansions)
    idx_release = index_release(args.index)
    aligned = bool(exp_dates) and idx_release is not None and all(d == idx_release for d in exp_dates)

    res = classify(exp, idx)
    res["expansion_snomed_version"] = ", ".join(exp_dates) if exp_dates else "unknown"
    res["index_release"] = idx_release or "unknown"
    res["version_aligned"] = aligned

    args.out_dir.mkdir(parents=True, exist_ok=True)
    cols = ["valueSetOid", "valueSetName", "code", "display", "flag",
            "preferred_term", "concept_active", "version_aligned",
            "expansion_snomed_version", "index_release"]
    flagged = res[res["needs_attention"]][cols].sort_values(["valueSetName", "flag", "code"])
    csv_path = args.out_dir / "review_flagged.csv"
    md_path = args.out_dir / "review_summary.md"
    flagged.to_csv(csv_path, index=False)
    write_summary(res, md_path, aligned, exp_dates, idx_release)

    print(f"Reviewed {len(res):,} rows; {len(flagged):,} need attention.")
    if not aligned:
        print(f"WARNING: version not aligned (expansion {exp_dates or '?'} vs "
              f"index {idx_release or '?'}); stamped on every row.")
    print(f"Wrote {csv_path}")
    print(f"Wrote {md_path}")
    print("\nFlag counts:")
    for flag in ATTENTION_ORDER:
        n = int((res["flag"] == flag).sum())
        if n:
            print(f"  {flag:<22}{n:,}")


if __name__ == "__main__":
    main()