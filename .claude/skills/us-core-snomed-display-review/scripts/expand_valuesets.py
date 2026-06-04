#!/usr/bin/env python3
"""
expand_valuesets.py  --  Stage A + B of the US Core SNOMED display review.

A) Read the US Core Terminology value-set list (CSV export) and keep only value
   sets defined in VSAC, identified by a VSAC ValueSet URL (cts.nlm.nih.gov).
B) Expand each selected value set and emit the SNOMED (code, display) pairs that
   the review step compares against the local RF2 index.

Expansion source (--source):
  tx   (default)  https://tx.fhir.org/r4/ValueSet/{OID}-{version}/$expand?_format=json
                  Open server, no auth. This is the expansion a US Core reader
                  actually sees when following a value set link, so it is the
                  right thing to review. The {version} comes from the CSV Version
                  column.
  vsac            https://cts.nlm.nih.gov/fhir/ValueSet/{OID}/$expand
                  HTTP Basic auth, username 'apikey', password = UMLS API key,
                  read from vsac_config.ini ([vsac] api_key) or UMLS_API_KEY.

Outputs:
  cache/expansions/<id>.json    cached assembled expansion (skip re-fetch)
  expansions.csv                valueSetOid,valueSetName,version,code,display
  expansions.csv.meta.json      per-value-set SNOMED version(s) + counts

Standard-library HTTP only (urllib). A fully-cached rerun works offline.

Usage:
  python expand_valuesets.py --terminology-csv valueset-ref-all-list.csv --dry-run
  python expand_valuesets.py --terminology-csv valueset-ref-all-list.csv --limit 1
  python expand_valuesets.py --terminology-csv valueset-ref-all-list.csv
"""

from __future__ import annotations

import argparse
import base64
import configparser
import csv
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

VSAC_FHIR_BASE = "https://cts.nlm.nih.gov/fhir"
TX_FHIR_BASE = "https://tx.fhir.org/r4"
SNOMED_SYSTEM = "http://snomed.info/sct"

# "Defined in VSAC" is signalled by the canonical URL host, not the OID root
# (HL7 assigns 2.16.840.1.113883 OIDs to its own value sets too).
VSAC_URL_RE = re.compile(
    r"(?:cts\.nlm\.nih\.gov/fhir/ValueSet/|vsac\.nlm\.nih\.gov/(?:fhir/)?[Vv]alue[Ss]et/)"
    r"([0-9][0-9.]+[0-9])"
)


class ExpandError(Exception):
    def __init__(self, status, url):
        super().__init__(f"HTTP {status} for {url}")
        self.status = status
        self.url = url


# --------------------------------------------------------------------------- #
# Stage A: select VSAC value sets (oid, name, version) from the CSV
# --------------------------------------------------------------------------- #
def read_value_sets(csv_path: Path) -> list[dict]:
    """Return [{oid, name, version}] for rows whose canonical URL is a VSAC URL.

    Uses the csv module (the US Core export has unquoted commas in trailing
    fields); URL/Version/Name sit ahead of those, so ragged rows are harmless.
    """
    with open(csv_path, newline="", encoding="utf-8") as fh:
        reader = csv.reader(fh)
        header = next(reader)

        def col(*names):
            for n in names:
                if n in header:
                    return header.index(n)
            return None

        i_url = col("URL", "Url", "url", "Canonical", "canonical")
        i_ver = col("Version", "version")
        i_name = col("Name", "name", "Title", "title")

        seen, out = set(), []
        for row in reader:
            url = row[i_url] if (i_url is not None and len(row) > i_url) else ""
            m = VSAC_URL_RE.search(url) or VSAC_URL_RE.search("  ".join(row))
            if not m:
                continue
            oid = m.group(1)
            if oid in seen:
                continue
            seen.add(oid)
            out.append({
                "oid": oid,
                "name": (row[i_name].strip() if (i_name is not None and len(row) > i_name) else oid),
                "version": (row[i_ver].strip() if (i_ver is not None and len(row) > i_ver) else ""),
            })
    return out


# --------------------------------------------------------------------------- #
# Auth (vsac only)
# --------------------------------------------------------------------------- #
def load_api_key(config_path: Path) -> str:
    if config_path and Path(config_path).exists():
        cp = configparser.ConfigParser()
        cp.read(config_path)
        if cp.has_option("vsac", "api_key"):
            key = cp.get("vsac", "api_key").strip()
            if key:
                return key
    env = os.environ.get("UMLS_API_KEY", "").strip()
    if env:
        return env
    sys.exit(
        "ERROR: no UMLS API key found (needed for --source vsac).\n"
        "  Create vsac_config.ini with:\n    [vsac]\n    api_key = YOUR-UMLS-API-KEY\n"
        "  or set the UMLS_API_KEY environment variable."
    )


# --------------------------------------------------------------------------- #
# Stage B: expand (paging + cache), source-aware URL + auth
# --------------------------------------------------------------------------- #
def cache_id(source: str, oid: str, version: str) -> str:
    return f"{oid}-{version}" if (source == "tx" and version) else oid


def page_url(source: str, oid: str, version: str, count: int, offset: int) -> str:
    if source == "tx":
        return (f"{TX_FHIR_BASE}/ValueSet/{oid}-{version}/$expand"
                f"?_format=json&count={count}&offset={offset}")
    return f"{VSAC_FHIR_BASE}/ValueSet/{oid}/$expand?count={count}&offset={offset}"


def _get_json(url: str, api_key):
    req = urllib.request.Request(url)
    if api_key:
        token = base64.b64encode(f"apikey:{api_key}".encode()).decode()
        req.add_header("Authorization", f"Basic {token}")
    req.add_header("Accept", "application/fhir+json")
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        raise ExpandError(e.code, url) from e
    except urllib.error.URLError as e:
        raise ExpandError(None, url) from e


def _versions_from_expansion(exp: dict) -> set:
    """SNOMED edition URIs, from per-concept version and expansion.parameter."""
    out = set()
    for c in exp.get("contains", []):
        if str(c.get("system", "")).startswith(SNOMED_SYSTEM) and c.get("version"):
            out.add(c["version"])
    for p in exp.get("parameter", []):
        val = p.get("valueUri") or p.get("valueString") or ""
        if "snomed.info/sct" in val and "/version/" in val:
            out.add(val)
    return out


def _fetch_all(source: str, oid: str, version: str, api_key, page: int):
    contains, versions, total, offset = [], set(), None, 0
    while True:
        data = _get_json(page_url(source, oid, version, page, offset), api_key)
        exp = data.get("expansion", {})
        if total is None:
            total = exp.get("total")
        versions |= _versions_from_expansion(exp)
        batch = exp.get("contains", [])
        contains.extend(batch)
        offset += len(batch)
        if not batch or (total is not None and offset >= total):
            break
    return contains, total, sorted(versions)


def get_expansion(source, vs, get_key, cache_dir, refresh, page) -> dict:
    cid = cache_id(source, vs["oid"], vs["version"])
    cache_file = cache_dir / f"{cid}.json"
    if cache_file.exists() and not refresh:
        return json.loads(cache_file.read_text())

    api_key = get_key() if source == "vsac" else None
    contains, total, versions = _fetch_all(source, vs["oid"], vs["version"], api_key, page)
    obj = {"oid": vs["oid"], "version": vs["version"], "source": source,
           "total": total, "versions": versions, "contains": contains}
    cache_file.write_text(json.dumps(obj))
    return obj


def snomed_pairs(contains: list):
    return [(c.get("code"), c.get("display")) for c in contains
            if str(c.get("system", "")).startswith(SNOMED_SYSTEM)]


def snomed_versions(obj: dict):
    """Prefer stored versions (covers param-only servers); else recompute."""
    if obj.get("versions"):
        return obj["versions"]
    return sorted({c["version"] for c in obj.get("contains", [])
                   if str(c.get("system", "")).startswith(SNOMED_SYSTEM) and c.get("version")})


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #
def main() -> None:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--terminology-csv", type=Path, required=True)
    ap.add_argument("--source", choices=["tx", "vsac"], default="tx",
                    help="Expansion server (default: tx = tx.fhir.org, what readers see)")
    ap.add_argument("--config", type=Path, default=Path("vsac_config.ini"),
                    help="vsac source only: gitignored file holding [vsac] api_key")
    ap.add_argument("--cache-dir", type=Path, default=Path("cache/expansions"))
    ap.add_argument("--out", type=Path, default=Path("expansions.csv"))
    ap.add_argument("--limit", type=int, default=0, help="Expand only the first N (0 = all)")
    ap.add_argument("--page", type=int, default=1000, help="$expand page size")
    ap.add_argument("--refresh", action="store_true", help="Ignore cache; re-fetch")
    ap.add_argument("--dry-run", action="store_true", help="List selection and exit")
    args = ap.parse_args()

    if not args.terminology_csv.exists():
        sys.exit(f"ERROR: terminology CSV not found: {args.terminology_csv}")

    value_sets = read_value_sets(args.terminology_csv)
    if not value_sets:
        sys.exit("No VSAC value sets detected in the CSV. Check the file / column layout.")

    value_sets.sort(key=lambda v: v["name"].lower())
    if args.limit:
        value_sets = value_sets[: args.limit]

    print(f"Source: {args.source}  |  Selected {len(value_sets)} VSAC value set(s):")
    for vs in value_sets:
        print(f"  {vs['oid']}-{vs['version'] or '(no version)'}  {vs['name']}")
    if args.dry_run:
        print("\n--dry-run: stopping before any network calls.")
        return

    if args.source == "tx":
        missing = [vs for vs in value_sets if not vs["version"]]
        if missing:
            print(f"NOTE: {len(missing)} value set(s) lack a Version and will be skipped on tx.")

    args.cache_dir.mkdir(parents=True, exist_ok=True)
    _key = {}
    def get_key():
        if "k" not in _key:
            _key["k"] = load_api_key(args.config)
        return _key["k"]

    rows, meta, errors = [], {}, []
    for vs in value_sets:
        oid, name, version = vs["oid"], vs["name"], vs["version"]
        if args.source == "tx" and not version:
            errors.append((oid, "no version"))
            print(f"  SKIP {oid} ({name}): no version for tx")
            continue
        t0 = time.time()
        try:
            exp = get_expansion(args.source, vs, get_key, args.cache_dir, args.refresh, args.page)
        except ExpandError as ex:
            if ex.status == 401:
                sys.exit("ERROR: VSAC rejected the API key (HTTP 401). Check vsac_config.ini.")
            errors.append((oid, f"HTTP {ex.status}"))
            print(f"  SKIP {oid} ({name}): HTTP {ex.status}")
            continue

        pairs = snomed_pairs(exp["contains"])
        for code, display in pairs:
            rows.append({"valueSetOid": oid, "valueSetName": name,
                         "version": version, "code": code, "display": display})
        meta[oid] = {"name": name, "version": version, "total": exp.get("total"),
                     "snomed_count": len(pairs), "snomed_versions": snomed_versions(exp)}
        print(f"  expanded {oid} ({name}): {len(pairs)} SNOMED of {exp.get('total')} total"
              f"  [{time.time()-t0:.1f}s]")

    import pandas as pd  # only needed to write the CSV
    out_df = pd.DataFrame(rows, columns=["valueSetOid", "valueSetName", "version", "code", "display"])
    out_df.to_csv(args.out, index=False)
    meta_path = args.out.with_suffix(args.out.suffix + ".meta.json")
    meta_path.write_text(json.dumps(meta, indent=2))

    all_versions = sorted({v for m in meta.values() for v in m["snomed_versions"]})
    print(f"\nWrote {len(out_df):,} SNOMED (code,display) rows -> {args.out}")
    print(f"Wrote per-value-set metadata -> {meta_path}")
    if errors:
        print(f"Skipped {len(errors)} value set(s): "
              + ", ".join(f"{o} ({why})" for o, why in errors[:8])
              + (" ..." if len(errors) > 8 else ""))
    if all_versions:
        print("SNOMED version(s) reported by expansions:")
        for v in all_versions:
            print(f"  {v}")
        print("-- confirm these match your RF2 index release before running the review.")


if __name__ == "__main__":
    main()