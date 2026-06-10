# Common Specimen Collection Methods — coverage against `us-core-specimen-collection-method`

Source list: `.claude/output/common method.md` (20 methods).
ValueSet: `us-core-specimen-collection-method` = `<<17636008 |Specimen collection (procedure)|` (139 concepts) + 62 enumerated active + 3 enumerated inactive = 204 distinct codes.
SNOMED edition: US Edition 2026-03-01.

## The 20 methods

| # | Method (from source) | In VS? | SNOMED concept |
|---:|---|:---:|---|
| 1 | Blood Venipuncture | partial | `82078001 \|Collection of blood specimen for laboratory\|` covers the broad case (in VS via hierarchy); more specific `28520004 \|Venipuncture for blood test\|` is **not** in VS |
| 2 | Finger Prick Micro-sampling | yes | `278450005 \|Finger-prick sampling\|` |
| 3 | Bone Marrow Aspiration | yes | `49401003 \|Bone marrow aspiration procedure\|` (enumerated) |
| 4 | Bone Marrow Biopsy | **no** | suggest `234326005 \|Bone marrow sampling\|` (parent) or `56241004 \|Bone marrow biopsy, needle or trocar\|` (needle-based) |
| 5 | Urine Collection (Clean-Catch) | yes | `73416001 \|Urine specimen collection, clean catch\|` |
| 6 | Timed Urine Collection | yes | `225113003 \|Timed urine collection\|` |
| 7 | Cerebrospinal Fluid (CSF) Tap | yes | `277762005 \|Lumbar puncture\|` (enumerated) |
| 8 | Fine Needle Aspiration (FNA) | yes | `48635004 \|Fine needle biopsy\|` (enumerated) |
| 9 | Anal Pap Test | **no** | suggest `405281009 \|Anal pap smear\|` |
| 10 | Cervical Cytology (SurePath) | yes | `416107004 \|Cervical cytology test\|` (enumerated) |
| 11 | Cervical Cytology (ThinPrep) | yes | `416107004 \|Cervical cytology test\|` (enumerated) |
| 12 | Broncho-Alveolar Lavage (BAL) | **inactive only** | VS has `397394009 \|Bronchoalveolar lavage\|` but it is retired; add an active replacement — `397397002 \|Bronchoscopy and bronchoalveolar lavage\|` (bronchoscopic) and/or `782762003 \|Blind bronchoalveolar lavage\|` (non-bronchoscopic) |
| 13 | Sputum Expectoration | yes | `37705003 \|Collection of sputum\|` (and subtypes `386089008 \|Collection of coughed sputum\|`, `386088000 \|Collection of induced sputum\|`) |
| 14 | Surgical Tissue Biopsy | yes | `86273004 \|Biopsy\|` (enumerated) covers it generically |
| 15 | Lymphoma / Culture Tissue (fresh, unfixed) | partial | covered generically by `86273004 \|Biopsy\|`; no SNOMED concept for "fresh unfixed tissue for culture" — author's call whether to leave generic |
| 16 | Gout Crystal Analysis (joint fluid) | **no** | suggest `90131007 \|Arthrocentesis\|` |
| 17 | Body Fluid Cytology (pleural / ascitic / pericardial) | partial | pleural via `91602002 \|Thoracentesis\|` (enumerated), ascitic via `89305009 \|Abdominal paracentesis\|` (enumerated); pericardial is missing — suggest `309849004 \|Pericardiocentesis\|` |
| 18 | Endoscopic Brushings | yes | `235157009 \|Endoscopic brushings of gastrointestinal tract\|` (enumerated) and `36213007 \|Endoscopy and brush biopsy\|` (enumerated) |
| 19 | Acid Fast Sputum / Tissue Smear | partial | collection covered by `37705003 \|Collection of sputum\|`; "acid fast" describes the downstream stain method, not the collection |
| 20 | Blood Culture | **no** | suggest `30088009 \|Blood culture\|` (procedure; covers drawing and culturing for bacteremia) |

## Suggested additions to the ValueSet

| Method | SNOMED code | Display (en-US PT) |
|---|---|---|
| Bone Marrow Biopsy | `56241004` | Bone marrow biopsy, needle or trocar |
| Anal Pap Test | `405281009` | Anal pap smear |
| Broncho-Alveolar Lavage (active replacement for retired `397394009`) | `397397002` | Bronchoscopy and bronchoalveolar lavage |
| Broncho-Alveolar Lavage (non-bronchoscopic) | `782762003` | Blind bronchoalveolar lavage |
| Gout Crystal Analysis (joint fluid) | `90131007` | Arthrocentesis |
| Body Fluid Cytology (pericardial) | `309849004` | Pericardiocentesis |
| Blood Culture | `30088009` | Blood culture |
| Blood Venipuncture (optional, more specific than the in-VS parent `82078001`) | `28520004` | Venipuncture for blood test |

## Notes

- Methods that mention a vendor-specific medium (SurePath, ThinPrep, PreservCyt, CytoLyt, Tasso, BD Microtainer, formalin, alcohol) do not have dedicated SNOMED procedure concepts — they share the underlying specimen-collection concept regardless of medium.
- Items 13, 14, 15 and 19 are already covered by codes that live inside `<<17636008` but were not in the original input spreadsheet because they sit on different branches of the procedure hierarchy.
- Item 12 (BAL) is the only case where the existing VS entry is retired; adding an active replacement is recommended even if the broader policy is to keep the retired code for legacy mappings.
