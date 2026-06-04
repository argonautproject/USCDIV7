---
name: us-core-snomed-display-review
description: Review the SNOMED CT display names used in US Core value set expansions against the official US edition descriptions, flagging displays that are not the Preferred Term, that use the Fully Specified Name, that match an inactive (retired) description, that match nothing, or that sit on a retired concept. Use this whenever the user wants to audit, QA, or check SNOMED display names / terms in US Core or VSAC value sets, compare what a US Core reader sees (tx.fhir.org expansions) against SNOMED RF2, validate value set expansion display strings, or find non-preferred / inactive SNOMED terms — even if they don't say "preferred term" or "RF2" explicitly.
---

# US Core SNOMED Display Review

Audits the SNOMED CT display strings that appear in US Core value set expansions
against a local SNOMED CT RF2 release, and reports which displays are not the
preferred description, use the FSN, are retired, or are otherwise off.

Scope: value sets **defined in VSAC** (the ones US Core references by a
`cts.nlm.nih.gov` canonical URL). By default the expansions are pulled from
**tx.fhir.org**, because that is the expansion a US Core reader actually sees
when following a value set link.

## Pipeline (run in order)

Three scripts in `scripts/`, each cached so reruns are cheap:

1. `build_snomed_index.py` — RF2 Snapshot → `cache/snomed_index.parquet`
2. `expand_valuesets.py` — terminology CSV → tx.fhir.org expansions → `cache/expansions.csv`
3. `review_displays.py` — join the two → `output/review_flagged.csv` + `output/review_summary.md`

Run all three from the skill root so the `cache/` and `output/` directories land
beside the scripts (step 3 anchors its defaults to the skill directory regardless
of cwd, but steps 1–2 use cwd-relative paths):

```bash
cd .claude/skills/us-core-snomed-display-review
```

## Prerequisites

- **Python ≥ 3.9** (NOT 3.7 — older envs cannot install a prebuilt `pyarrow`
  wheel and fall back to a source build that fails). Use the env behind the
  current Jupyter kernel, not a legacy IG-build env.
- `pip install pandas pyarrow`
- A downloaded SNOMED CT RF2 **US edition** release, unzipped. The pipeline reads
  the `Snapshot/` tree (Description, Concept, and Language refset files).
- The US Core value set list CSV (the "value set reference" export, e.g.
  `valueset-ref-all-list.csv`), which supplies each value set's OID **and**
  Version. Keep it under the skill or project config dir.
- A UMLS API key is **only** needed for `--source vsac`. The default tx source is
  open and needs no credentials.

## Step 1 — Build the SNOMED index

```bash
python scripts/build_snomed_index.py \
  --snapshot-dir "/path/to/SnomedCT_ManagedServiceUS_.../Snapshot" \
  --out cache/snomed_index.parquet
```

Writes `cache/snomed_index.parquet` (one row per description, **including inactive
ones**, with concept active status and US-English acceptability) plus a
`...parquet.meta.json` recording the RF2 release date/module. Build once per RF2
release; the review reads the parquet, not the raw text files.

## Step 2 — Expand the value sets (tx.fhir.org)

```bash
python scripts/expand_valuesets.py \
  --terminology-csv ../../config/valueset-ref-all-list.csv \
  --cache-dir cache/expansions \
  --out cache/expansions.csv
```

- Selects VSAC value sets by their `cts.nlm.nih.gov` URL (NOT by OID root — HL7
  assigns `2.16.840.1.113883` OIDs to its own value sets too).
- Builds `https://tx.fhir.org/r4/ValueSet/{OID}-{Version}/$expand?_format=json`
  using the CSV Version column, keeps SNOMED-system codes, and caches each raw
  expansion. A fully-cached rerun works offline.
- Use `--dry-run` first to confirm the selection, and `--limit 1` to smoke-test a
  single expansion before the full run.
- `--source vsac` switches to the authenticated VSAC server (needs the API key);
  useful to backfill value sets tx cannot expand.

Writes `cache/expansions.csv` and `cache/expansions.csv.meta.json` (per-value-set
SNOMED version, for the alignment check).

## Step 3 — Review the displays

```bash
python scripts/review_displays.py
```

Defaults read `cache/snomed_index.parquet` and `cache/expansions.csv` and write to
`output/`. Override with `--index`, `--expansions`, `--out-dir` if needed.

Writes `output/review_flagged.csv` (problems only) and `output/review_summary.md`
(counts by flag and by value set, plus the version banner).

## Flag taxonomy

| Flag | Meaning |
|---|---|
| `OK_PREFERRED` | display equals the active Preferred Term (excluded from the flagged CSV when on an active concept) |
| `FSN` | display equals the active Fully Specified Name, not the PT |
| `NOT_PREFERRED_ACTIVE` | active synonym that is neither PT nor FSN |
| `INACTIVE_DESCRIPTION` | matches only an inactive (retired) description |
| `CASE_OR_WHITESPACE` | matches the PT only after normalization |
| `NO_MATCH` | matches no description for the concept |
| `UNKNOWN_CONCEPT` | concept id absent from the RF2 release |

Concept retirement is orthogonal: a row that is `OK_PREFERRED` but sits on an
inactive concept (`concept_active=False`) still appears in the flagged CSV.

## Version alignment (do not skip)

tx.fhir.org may expand SNOMED against a different edition than the local RF2
index. `review_displays.py` compares the SNOMED version in
`expansions.csv.meta.json` to the RF2 release in `snomed_index.parquet.meta.json`,
stamps `version_aligned` on every output row, and prints a MISMATCH banner if they
differ. A mismatch does not stop the run, but flags under a mismatch may reflect
version drift rather than real defects — confirm alignment before trusting
results. Check the module too: `731000124108` is the US edition,
`900000000000207008` is International.

## Expansion failures (a real finding, not just noise)

Some value sets fail to expand on tx:
- **HTTP 422 "too many codes (>10000)"** — tx refuses oversized expansions
  (e.g. large groupers like the allergen set). This is reader-facing: the US Core
  link gives the reader an error too. Optionally backfill via `--source vsac`, but
  note in the report that tx cannot render it.
- **HTTP 500** — an upstream tx server fault, not a property of the value set;
  record it but do not work around it.

Skips are printed at the end of step 2. (They are not yet written to the review
output; treat the console skip list as part of the audit record.)

## Operational notes

- After editing any script, the change only takes effect once the file is copied
  into `scripts/` here — running a stale copy is the most common failure.
- The parquet cache is large, release-specific, and regenerable: gitignore
  `cache/`, `output/`, and `vsac_config.ini`. Never commit them.
- All caches key on inputs (RF2 release, OID-version), so deleting a cache file
  forces a clean re-fetch/rebuild of just that item.