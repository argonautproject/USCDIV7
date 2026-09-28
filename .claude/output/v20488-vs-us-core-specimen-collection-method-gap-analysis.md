# Gap Analysis: HL7 v2 Table 0488 vs US Core Specimen Collection Method

**Source:** `http://terminology.hl7.org/CodeSystem/v2-0488` (specimenCollectionMethod, version 3.0.0)
from `.claude/config/v20488-codesystem.yml` -- 42 concepts, all active, none deprecated.

**Target:** `http://hl7.org/fhir/us/core/ValueSet/us-core-specimen-collection-method`
from `input/resources-yaml/ValueSet-us-core-specimen-collection-method.yml`.

The target value set is intensional (SNOMED CT `is-a 17636008 |Specimen collection|`
plus enumerated additions), so the comparison uses the built expansion in
`output/ValueSet-us-core-specimen-collection-method.html` -- 211 concepts,
SNOMED CT United States edition 01-Sep-2025.

Direction convention throughout: **source = v2-0488**, **target = US Core Specimen Collection Method**.

## Summary

| Measure | Count |
|---|---|
| v2-0488 concepts | 42 |
| Fully covered (`equivalent`) | 10 |
| **Gaps (no equivalent target)** | **32** |
| -- partially covered by a broader target (`source-is-narrower-than-target`) | 13 |
| -- partially covered by a narrower or oblique target (`source-is-broader-than-target`) | 3 |
| -- `related-to` only | 12 |
| -- no candidate target at all | 4 |

## Table 1 -- Gaps

v2-0488 concepts with no equivalent concept in the US Core value set.

| # | v2 code | v2 display | Nature of the gap | Closest concept in the value set |
|---|---|---|---|---|
| 1 | PNA | Arterial puncture | Value set has no generic "arterial puncture"; only the lab-collection concept and three named arteries | 32564009 Arterial specimen collection for laboratory test |
| 2 | BCAE | Blood Culture, Aerobic Bottle | Container and atmosphere distinction (aerobic bottle) not represented | 30088009 Blood culture |
| 3 | BCAN | Blood Culture, Anaerobic Bottle | Container and atmosphere distinction not represented | 30088009 Blood culture |
| 4 | BCPD | Blood Culture, Pediatric Bottle | Pediatric bottle distinction not represented | 30088009 Blood culture |
| 5 | CATH | Catheterized | v2 code is site-agnostic; value set has only site- and device-specific catheter collection concepts | 705156009 Collection of urine via straight catheter |
| 6 | EPLA | Environmental, Plate | No environmental (non-patient) specimen collection concept in the value set | 441378005 Collection of specimen by culture plate |
| 7 | ESWA | Environmental, Swab | No environmental (non-patient) specimen collection concept | 285570007 Taking of swab |
| 8 | CVP | Line, CVP | No central-venous-pressure-line collection concept | 243763007 Venous sampling catheter procedure |
| 9 | MARTL | Martin-Lewis Agar | Named culture medium not represented | 441378005 Collection of specimen by culture plate |
| 10 | ML11 | Mod. Martin-Lewis Agar | Named culture medium not represented | 441378005 Collection of specimen by culture plate |
| 11 | PACE | Pace, Gen-Probe | Proprietary collection and transport kit not represented | 439599008 Collection of specimen by device |
| 12 | MLP | Plate, Martin-Lewis | Named plate medium not represented | 441378005 Collection of specimen by culture plate |
| 13 | NYP | Plate, New York City | Named plate medium not represented | 441378005 Collection of specimen by culture plate |
| 14 | TMP | Plate, Thayer-Martin | Named plate medium not represented | 441378005 Collection of specimen by culture plate |
| 15 | ANP | Plates, Anaerobic | Plate form is lost; only the general anaerobic microbiology collection concept exists | 83917009 Specimen collection for microbiology, anaerobic |
| 16 | BAP | Plates, Blood Agar | Named plate medium not represented | 441378005 Collection of specimen by culture plate |
| 17 | PRIME | Pump Prime | Priming-fluid sample not represented | 243780006 Blood sampling from cardiopulmonary bypass circuit |
| 18 | PUMP | Pump Specimen | Generic "pump" sample not represented; value set names specific circuits | 243780006 Blood sampling from cardiopulmonary bypass circuit |
| 19 | QC5 | Quality Control For Micro | **No candidate.** Not a specimen collection method; quality control material has no analogue | -- |
| 20 | SCLP | Scalp, Fetal Vein | **No candidate.** No fetal scalp blood sampling concept in the expansion | -- |
| 21 | SHA | Shaving | No shave-biopsy or shaving collection concept (hair cutting and nail clipping exist but are different acts) | 240977001 Biopsy of skin |
| 22 | SWD | Swab, Dacron tipped | Swab tip material not represented | 285570007 Taking of swab |
| 23 | WOOD | Swab, Wooden Shaft | Swab shaft material not represented | 285570007 Taking of swab |
| 24 | TMOT | Transport Media, | No transport-medium concepts at all in the value set | 439599008 Collection of specimen by device |
| 25 | TMAN | Transport Media, Anaerobic | No anaerobic transport medium concept | 83917009 Specimen collection for microbiology, anaerobic |
| 26 | TMCH | Transport Media, Chalamydia [sic] | No chlamydia transport medium concept | 285586000 Taking swab for Chlamydia test |
| 27 | TMM4 | Transport Media, M4 | **No candidate.** Proprietary medium | -- |
| 28 | TMMY | Transport Media, Mycoplasma | No mycoplasma transport medium concept | 439599008 Collection of specimen by device |
| 29 | TMPV | Transport Media, PVA | **No candidate.** Polyvinyl alcohol fixative not represented | -- |
| 30 | TMSC | Transport Media, Stool Culture | No stool transport medium concept | 225105004 Collection of stool specimen |
| 31 | TMUP | Transport Media, Ureaplasma | No ureaplasma transport medium concept | 439599008 Collection of specimen by device |
| 32 | TMVI | Transport Media, Viral | No viral transport medium concept | 439599008 Collection of specimen by device |

Three themes account for most of the gaps:

- **Culture media and plates:** MARTL, ML11, MLP, NYP, TMP, ANP, BAP
- **Transport media:** TMOT, TMAN, TMCH, TMM4, TMMY, TMPV, TMSC, TMUP, TMVI
- **Container and device attributes:** BCAE, BCAN, BCPD, SWD, WOOD

These are properties of the container or the medium rather than of the collection act,
which is why the SNOMED CT procedure hierarchy does not carry them. In FHIR they align
more closely with `Specimen.container.type` and `Specimen.processing` than with
`Specimen.collection.method`.

## Table 2 -- Mappings

| v2 code | v2 display | Target code | Target display | Relationship |
|---|---|---|---|---|
| FNA | Aspiration, Fine Needle | 48635004 | Fine needle biopsy | equivalent |
| PNA | Arterial puncture | 32564009 | Arterial specimen collection for laboratory test | source-is-narrower-than-target |
| BIO | Biopsy | 86273004 | Biopsy | equivalent |
| BCAE | Blood Culture, Aerobic Bottle | 30088009 | Blood culture | source-is-narrower-than-target |
| BCAN | Blood Culture, Anaerobic Bottle | 30088009 | Blood culture | source-is-narrower-than-target |
| BCPD | Blood Culture, Pediatric Bottle | 30088009 | Blood culture | source-is-narrower-than-target |
| CAP | Capillary Specimen | 1048003 | Capillary specimen collection | equivalent |
| CATH | Catheterized | 705156009 | Collection of urine via straight catheter | source-is-broader-than-target |
| EPLA | Environmental, Plate | 441378005 | Collection of specimen by culture plate | related-to |
| ESWA | Environmental, Swab | 285570007 | Taking of swab | related-to |
| LNA | Line, Arterial | 699873000 | Collection of blood via arterial catheter | equivalent |
| CVP | Line, CVP | 243763007 | Venous sampling catheter procedure | source-is-narrower-than-target |
| LNV | Line, Venous | 243763007 | Venous sampling catheter procedure | equivalent |
| MARTL | Martin-Lewis Agar | 441378005 | Collection of specimen by culture plate | source-is-narrower-than-target |
| ML11 | Mod. Martin-Lewis Agar | 441378005 | Collection of specimen by culture plate | source-is-narrower-than-target |
| PACE | Pace, Gen-Probe | 439599008 | Collection of specimen by device | related-to |
| PIN | Pinworm Prep | 21217000 | Collection of pinworm specimen | equivalent |
| KOFFP | Plate, Cough | 709500005 | Collection of specimen by cough culture plate | equivalent |
| MLP | Plate, Martin-Lewis | 441378005 | Collection of specimen by culture plate | source-is-narrower-than-target |
| NYP | Plate, New York City | 441378005 | Collection of specimen by culture plate | source-is-narrower-than-target |
| TMP | Plate, Thayer-Martin | 441378005 | Collection of specimen by culture plate | source-is-narrower-than-target |
| ANP | Plates, Anaerobic | 83917009 | Specimen collection for microbiology, anaerobic | source-is-narrower-than-target |
| BAP | Plates, Blood Agar | 441378005 | Collection of specimen by culture plate | source-is-narrower-than-target |
| PRIME | Pump Prime | 243780006 | Blood sampling from cardiopulmonary bypass circuit | related-to |
| PUMP | Pump Specimen | 243780006 | Blood sampling from cardiopulmonary bypass circuit | source-is-broader-than-target |
| QC5 | Quality Control For Micro | -- | *(no candidate)* | -- |
| SCLP | Scalp, Fetal Vein | -- | *(no candidate)* | -- |
| SCRAPS | Scrapings | 56757003 | Scraping | equivalent |
| SHA | Shaving | 240977001 | Biopsy of skin | related-to |
| SWA | Swab | 285570007 | Taking of swab | equivalent |
| SWD | Swab, Dacron tipped | 285570007 | Taking of swab | source-is-narrower-than-target |
| WOOD | Swab, Wooden Shaft | 285570007 | Taking of swab | source-is-narrower-than-target |
| TMOT | Transport Media, | 439599008 | Collection of specimen by device | related-to |
| TMAN | Transport Media, Anaerobic | 83917009 | Specimen collection for microbiology, anaerobic | related-to |
| TMCH | Transport Media, Chalamydia | 285586000 | Taking swab for Chlamydia test | related-to |
| TMM4 | Transport Media, M4 | -- | *(no candidate)* | -- |
| TMMY | Transport Media, Mycoplasma | 439599008 | Collection of specimen by device | related-to |
| TMPV | Transport Media, PVA | -- | *(no candidate)* | -- |
| TMSC | Transport Media, Stool Culture | 225105004 | Collection of stool specimen | related-to |
| TMUP | Transport Media, Ureaplasma | 439599008 | Collection of specimen by device | related-to |
| TMVI | Transport Media, Viral | 439599008 | Collection of specimen by device | related-to |
| VENIP | Venipuncture | 28520004 | Venipuncture for blood test | equivalent |

## Caveats

- The target set is the tx.fhir.org expansion from the last build. Re-expansion against a
  newer SNOMED CT US edition can shift a few rows.
- The mappings in Table 2 are proposed alignments produced by this analysis. They are not
  asserted in either source file; neither file contains a ConceptMap.
