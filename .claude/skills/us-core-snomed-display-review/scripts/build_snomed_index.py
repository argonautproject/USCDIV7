#!/usr/bin/env python3
"""
build_snomed-index.py

Build a per-description SNOMED CT index from RF2 Snapshot files for the US Core
display-name review skill.

Unlike a plain "preferred term" lookup, this index intentionally KEEPS inactive
descriptions and joins in concept-level active status, so the review step can flag
display names that:
  - are not the preferred term,
  - match an inactive (retired) description, or
  - belong to an inactive (retired) concept.

Outputs:
  <out>.parquet            one row per description, enriched for fast review
  <out>.parquet.meta.json  release metadata for SNOMED-version alignment checks

The parquet is a cache: build it once per RF2 release, then the review step loads
it with load_index() instead of re-parsing the (large) RF2 text files each run.

Usage:
  python build_snomed-index.py --snapshot-dir /path/to/.../Snapshot --out snomed-index.parquet
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
import time
from pathlib import Path

import pandas as pd

# --- SNOMED CT metadata concept IDs ---
FSN_TYPE     = "900000000000003001"  # Fully specified name
SYNONYM_TYPE = "900000000000013009"  # Synonym
US_EN_REFSET = "900000000000509007"  # US English language reference set
PREFERRED    = "900000000000548007"  # Acceptability: Preferred
ACCEPTABLE   = "900000000000549004"  # Acceptability: Acceptable

TYPE_LABELS   = {FSN_TYPE: "FSN", SYNONYM_TYPE: "Synonym"}
ACCEPT_LABELS = {PREFERRED: "Preferred", ACCEPTABLE: "Acceptable"}

SNOMED_SYSTEM = "http://snomed.info/sct"

# RF2 read options: keep 18-digit SCTIDs exact, don't treat embedded " as quoting,
# and don't coerce terms like "NA"/"Null" to NaN (also faster).
READ_KWARGS = dict(
    sep="\t",
    dtype=str,
    quoting=csv.QUOTE_NONE,
    keep_default_na=False,
    na_filter=False,
    encoding="utf-8",
)

DEFAULT_SNAPSHOT = (
    "/Users/ehaas/Downloads/"
    "SnomedCT_ManagedServiceUS_PRODUCTION_US1000124_20260301T120000Z/Snapshot"
)

# Columns written to the parquet cache (one row per description).
INDEX_COLS = [
    "conceptId", "conceptActive", "descriptionId", "term", "term_norm",
    "typeId", "type", "descActive", "acceptabilityId", "acceptability",
    "is_pt", "is_fsn",
]


# --------------------------------------------------------------------------- #
# File discovery + loading
# --------------------------------------------------------------------------- #
def find_one(directory: Path, pattern: str) -> Path:
    matches = sorted(directory.glob(pattern))
    if not matches:
        sys.exit(f"ERROR: no file matching {pattern!r} in {directory}")
    if len(matches) > 1:
        print(f"WARNING: multiple matches for {pattern!r}; using {matches[0].name}")
    return matches[0]


def load(path: Path, usecols=None) -> pd.DataFrame:
    t0 = time.time()
    df = pd.read_csv(path, usecols=usecols, **READ_KWARGS)
    print(f"  loaded {path.name}: {len(df):,} rows in {time.time() - t0:.1f}s")
    return df


def normalize(series: pd.Series) -> pd.Series:
    """Lowercase, strip, and collapse internal whitespace for soft matching."""
    return (
        series.str.strip()
        .str.replace(r"\s+", " ", regex=True)
        .str.lower()
    )


# --------------------------------------------------------------------------- #
# Build
# --------------------------------------------------------------------------- #
def build_index(snapshot_dir: Path) -> tuple[pd.DataFrame, dict]:
    term_dir = snapshot_dir / "Terminology"
    lang_dir = snapshot_dir / "Refset" / "Language"

    desc_file    = find_one(term_dir, "sct2_Description_Snapshot-en*.txt")
    concept_file = find_one(term_dir, "sct2_Concept_Snapshot*.txt")
    lang_file    = find_one(lang_dir, "der2_cRefset_LanguageSnapshot-en*.txt")

    print("Loading RF2 files (descriptions kept active AND inactive)...")
    desc = load(desc_file, usecols=["id", "active", "conceptId", "typeId", "term"])
    concept = load(concept_file, usecols=["id", "active"])
    lang = load(lang_file,
                usecols=["active", "refsetId", "referencedComponentId", "acceptabilityId"])

    # US English acceptability, active rows only -> one row per description.
    lang_us = lang[(lang["active"] == "1") & (lang["refsetId"] == US_EN_REFSET)]
    lang_us = lang_us.drop_duplicates("referencedComponentId", keep="first")

    # Concept active status, keyed by conceptId.
    concept_active = concept.set_index("id")["active"]

    idx = desc.rename(columns={"id": "descriptionId", "active": "descActive"})

    # Attach US-English acceptability to each description (left join keeps inactive
    # descriptions, which carry no active language-refset row).
    idx = idx.merge(
        lang_us[["referencedComponentId", "acceptabilityId"]],
        left_on="descriptionId",
        right_on="referencedComponentId",
        how="left",
    ).drop(columns=["referencedComponentId"])

    # Attach concept active status; a description whose concept is missing/retired
    # gets conceptActive "0".
    idx["conceptActive"] = idx["conceptId"].map(concept_active).fillna("0")

    idx["type"] = idx["typeId"].map(TYPE_LABELS).fillna(idx["typeId"])
    idx["acceptability"] = idx["acceptabilityId"].map(ACCEPT_LABELS)

    # Preferred Term = active synonym marked Preferred in US English.
    idx["is_pt"] = (
        (idx["typeId"] == SYNONYM_TYPE)
        & (idx["acceptabilityId"] == PREFERRED)
        & (idx["descActive"] == "1")
    )
    # FSN = active fully specified name.
    idx["is_fsn"] = (idx["typeId"] == FSN_TYPE) & (idx["descActive"] == "1")

    idx["term_norm"] = normalize(idx["term"])

    idx = idx[INDEX_COLS]

    m = re.search(r"_(\d{8})\.txt$", desc_file.name)
    release_date = m.group(1) if m else "unknown"
    module = next((tok for tok in desc_file.name.split("_") if re.fullmatch(r"[A-Z]{2}\d+", tok)),
                  "unknown")

    meta = {
        "snapshot_dir": str(snapshot_dir),
        "description_file": desc_file.name,
        "concept_file": concept_file.name,
        "language_file": lang_file.name,
        "release_date": release_date,
        "snomed_module": module,
        "code_system": SNOMED_SYSTEM,
        "n_descriptions": int(len(idx)),
        "n_concepts": int(idx["conceptId"].nunique()),
        "n_inactive_descriptions": int((idx["descActive"] == "0").sum()),
    }
    return idx, meta


# --------------------------------------------------------------------------- #
# Reuse helpers for the review step (review_displays.py imports these)
# --------------------------------------------------------------------------- #
def load_index(path) -> pd.DataFrame:
    """Load a previously built parquet index."""
    return pd.read_parquet(path)


def preferred_term(index: pd.DataFrame, concept_id) -> str | None:
    rows = index[(index["conceptId"] == str(concept_id)) & index["is_pt"]]
    return rows["term"].iloc[0] if len(rows) else None


def classify_display(index: pd.DataFrame, concept_id, display: str) -> dict:
    """
    Classify a single (concept_id, display) pair from a value set expansion.

    Returns a dict with the display-level flag plus orthogonal facts the report
    can combine (concept retirement is reported separately from display quality):

      flag (display match quality):
        OK_PREFERRED         display == active Preferred Term
        FSN                  display == active Fully Specified Name (not the PT)
        NOT_PREFERRED_ACTIVE matches an active synonym that is neither PT nor FSN
        INACTIVE_DESCRIPTION matches only an inactive (retired) description
        CASE_OR_WHITESPACE   matches the PT only after normalization
        NO_MATCH             matches no description for this concept
        UNKNOWN_CONCEPT      concept id not present in this RF2 release
    """
    cid = str(concept_id)
    rows = index[index["conceptId"] == cid]
    if rows.empty:
        return {"concept_id": cid, "display": display, "concept_active": None,
                "flag": "UNKNOWN_CONCEPT", "preferred_term": None,
                "matched_active": False, "matched_inactive": False}

    concept_active = bool((rows["conceptActive"] == "1").iloc[0])
    pt = rows.loc[rows["is_pt"], "term"]
    pt_value = pt.iloc[0] if len(pt) else None

    exact = rows[rows["term"] == display]
    norm = re.sub(r"\s+", " ", display.strip()).lower()
    soft = rows[rows["term_norm"] == norm]

    matched_active = bool((exact["descActive"] == "1").any()) if len(exact) else False
    matched_inactive = bool((exact["descActive"] == "0").any()) if len(exact) else False

    if len(exact):
        if exact["is_pt"].any():
            flag = "OK_PREFERRED"
        elif exact["is_fsn"].any():
            flag = "FSN"
        elif matched_active:
            flag = "NOT_PREFERRED_ACTIVE"
        else:
            flag = "INACTIVE_DESCRIPTION"
    elif len(soft) and soft["is_pt"].any():
        flag = "CASE_OR_WHITESPACE"
    else:
        flag = "NO_MATCH"

    return {"concept_id": cid, "display": display, "concept_active": concept_active,
            "flag": flag, "preferred_term": pt_value,
            "matched_active": matched_active, "matched_inactive": matched_inactive}


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #
def main() -> None:
    ap = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    ap.add_argument("--snapshot-dir", type=Path, default=Path(DEFAULT_SNAPSHOT),
                    help="Path to the RF2 Snapshot directory")
    ap.add_argument("--out", type=Path, default=Path("snomed-index.parquet"),
                    help="Output parquet path")
    args = ap.parse_args()

    if not args.snapshot_dir.is_dir():
        sys.exit(f"ERROR: snapshot dir not found: {args.snapshot_dir}")

    idx, meta = build_index(args.snapshot_dir)

    try:
        idx.to_parquet(args.out, index=False)
    except Exception as e:  # missing engine, etc.
        sys.exit(f"ERROR writing parquet ({e}).\nInstall an engine: pip install pyarrow")

    meta_path = args.out.with_suffix(args.out.suffix + ".meta.json")
    meta_path.write_text(json.dumps(meta, indent=2))

    print(f"\nWrote index:    {args.out}  "
          f"({meta['n_descriptions']:,} descriptions, {meta['n_concepts']:,} concepts, "
          f"{meta['n_inactive_descriptions']:,} inactive descriptions)")
    print(f"Wrote metadata: {meta_path}")
    print(f"SNOMED release: {meta['snomed_module']} {meta['release_date']}  "
          f"-- confirm this matches the VSAC expansion version before reviewing.")


if __name__ == "__main__":
    main()