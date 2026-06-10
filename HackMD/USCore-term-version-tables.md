# US Core Terminology Version Comparisons

Comparison of US Core Terminology Artifacts across versions 6.1.0, 8.0.1, and 9.0.0.

**Legend:** ✓ present · ➕ added · ⛔ removed/retired · ⚠️ deprecated (concept-level `status` property)

## Code Systems

### 1. US Core CarePlan Category Extension Codes

Canonical: `http://hl7.org/fhir/us/core/CodeSystem/careplan-category`

| code | 6.1.0 | 8.0.1 | 9.0.0 | notes |
|---|---|---|---|---|
| assess-plan | ✓ | ✓ | ⛔ | Concept unchanged, but the entire CodeSystem `status` was flipped to `retired` in 9.0.0. |

### 2. US Core Condition Category Extension Codes

Canonical: `http://hl7.org/fhir/us/core/CodeSystem/condition-category`

| code | 6.1.0 | 8.0.1 | 9.0.0 | notes |
|---|---|---|---|---|
| problem | ⚠️ | ⚠️ | ⚠️ | Present + carries `status=deprecated` property in all three versions. 8.0.1 added a deprecation note to the definition pointing to THO `condition-category#problem-list-item`. |
| health-concern | ✓ | ✓ | ✓ | Same in all three (definition text trimmed in 8.0.1). |

### 3. US Core Category

Canonical: `http://hl7.org/fhir/us/core/CodeSystem/us-core-category`

| code | 6.1.0 | 8.0.1 | 9.0.0 | notes |
|---|---|---|---|---|
| sdoh | ✓ | ✓ | ✓ | |
| functional-status | ✓ | ✓ | ✓ | |
| disability-status | ✓ | ✓ | ✓ | |
| cognitive-status | ✓ | ✓ | ✓ | |
| treatment-intervention-preference | | ➕ | ✓ | Added in 8.0.1. |
| care-experience-preference | | ➕ | ✓ | Added in 8.0.1. |
| observation-adi-documentation | | ➕ | ✓ | Added in 8.0.1. |
| PMO | | | ➕ | Added in 9.0.0 (Portable Medical Order). |

### 4. US Core DocumentReferences Category Codes

Canonical: `http://hl7.org/fhir/us/core/CodeSystem/us-core-documentreference-category`

| code | 6.1.0 | 8.0.1 | 9.0.0 | notes |
|---|---|---|---|---|
| clinical-note | ✓ | ✓ | ✓ | Same in all three versions. |

### 5. US Core Provenance Participant Type Extension Codes

Canonical: `http://hl7.org/fhir/us/core/CodeSystem/us-core-provenance-participant-type`

| code | 6.1.0 | 8.0.1 | 9.0.0 | notes |
|---|---|---|---|---|
| transmitter | ✓ | ✓ | ⛔ | Entire CodeSystem removed from US Core 9.0.0. |

## Value Sets

For each ValueSet, rows enumerate items from `compose` (codes, filter rules, whole-CodeSystem includes, or `valueSet` references). Cells flag whether each item is present in that version (✓), added (➕), or removed (⛔). Tables flagged **Not locally enumerable** rely on filters, whole-CodeSystem inclusions, or external/large/IP-restricted code systems (SNOMED CT, LOINC, CPT, HCPCS, ICD-10-CM/PCS, RxNorm, CDT, NUCC, HSLOC); expansion requires a terminology server.

### 1. Birth Sex

Canonical: `http://hl7.org/fhir/us/core/ValueSet/birthsex`  
Id: `birthsex`

**Notes:** Removed in 8.0.1. **Not locally enumerable** — `compose` includes filter / whole-CodeSystem / ValueSet references; expansion requires a terminology server.

| code | 6.1.0 | 8.0.1 | 9.0.0 | notes |
|---|---|---|---|---|
| Include ValueSet `http://cts.nlm.nih.gov/fhir/ValueSet/2.16.840.1.113762.1.4.1` | ✓ |  |  |  |
| Include ValueSet `http://cts.nlm.nih.gov/fhir/ValueSet/2.16.840.1.113762.1.4.1021.103` | ✓ |  |  |  |

### 2. Detailed ethnicity

Canonical: `http://hl7.org/fhir/us/core/ValueSet/detailed-ethnicity`  
Id: `detailed-ethnicity`

**Notes:** Removed in 8.0.1. **Not locally enumerable** — `compose` includes filter / whole-CodeSystem / ValueSet references; expansion requires a terminology server.

| code | 6.1.0 | 8.0.1 | 9.0.0 | notes |
|---|---|---|---|---|
| Include ValueSet `http://cts.nlm.nih.gov/fhir/ValueSet/2.16.840.1.114222.4.11.877` | ✓ |  |  |  |
| Include ValueSet `http://cts.nlm.nih.gov/fhir/ValueSet/2.16.840.1.113762.1.4.1021.103` | ✓ |  |  |  |

### 3. Detailed Race

Canonical: `http://hl7.org/fhir/us/core/ValueSet/detailed-race`  
Id: `detailed-race`

**Notes:** Removed in 8.0.1. **Not locally enumerable** — `compose` includes filter / whole-CodeSystem / ValueSet references; expansion requires a terminology server.

| code | 6.1.0 | 8.0.1 | 9.0.0 | notes |
|---|---|---|---|---|
| Include ValueSet `http://cts.nlm.nih.gov/fhir/ValueSet/2.16.840.1.113883.1.11.14914` | ✓ |  |  |  |
| Include ValueSet `http://cts.nlm.nih.gov/fhir/ValueSet/2.16.840.1.113762.1.4.1021.103` | ✓ |  |  |  |

### 4. OMB Ethnicity Categories

Canonical: `http://hl7.org/fhir/us/core/ValueSet/omb-ethnicity-category`  
Id: `omb-ethnicity-category`

**Notes:** Removed in 8.0.1. **Not locally enumerable** — `compose` includes filter / whole-CodeSystem / ValueSet references; expansion requires a terminology server.

| code | 6.1.0 | 8.0.1 | 9.0.0 | notes |
|---|---|---|---|---|
| Include ValueSet `http://cts.nlm.nih.gov/fhir/ValueSet/2.16.840.1.114222.4.11.837` | ✓ |  |  |  |
| Include ValueSet `http://cts.nlm.nih.gov/fhir/ValueSet/2.16.840.1.113762.1.4.1021.102` | ✓ |  |  |  |

### 5. OMB Race Categories

Canonical: `http://hl7.org/fhir/us/core/ValueSet/omb-race-category`  
Id: `omb-race-category`

**Notes:** Removed in 8.0.1. **Not locally enumerable** — `compose` includes filter / whole-CodeSystem / ValueSet references; expansion requires a terminology server.

| code | 6.1.0 | 8.0.1 | 9.0.0 | notes |
|---|---|---|---|---|
| Include ValueSet `http://cts.nlm.nih.gov/fhir/ValueSet/2.16.840.1.114222.4.11.836` | ✓ |  |  |  |
| Include ValueSet `http://cts.nlm.nih.gov/fhir/ValueSet/2.16.840.1.113762.1.4.1021.102` | ✓ |  |  |  |

### 6. Language codes with language and optionally a region modifier

Canonical: `http://hl7.org/fhir/us/core/ValueSet/simple-language`  
Id: `simple-language`

**Notes:** Removed in 8.0.1. **Not locally enumerable** — `compose` includes filter / whole-CodeSystem / ValueSet references; expansion requires a terminology server.

| code | 6.1.0 | 8.0.1 | 9.0.0 | notes |
|---|---|---|---|---|
| `BCP-47 Languages` filter `ext-lang exists false` | ✓ |  |  |  |
| `BCP-47 Languages` filter `script exists false` | ✓ |  |  |  |
| `BCP-47 Languages` filter `variant exists false` | ✓ |  |  |  |
| `BCP-47 Languages` filter `extension exists false` | ✓ |  |  |  |
| `BCP-47 Languages` filter `private-use exists false` | ✓ |  |  |  |

### 7. US Core Simple Observation Codes

Canonical: `http://hl7.org/fhir/us/core/ValueSet/simple-observation`  
Id: `simple-observation`

**Notes:** Removed in 8.0.1. **Not locally enumerable** — `compose` includes filter / whole-CodeSystem / ValueSet references; expansion requires a terminology server.

| code | 6.1.0 | 8.0.1 | 9.0.0 | notes |
|---|---|---|---|---|
| All codes from `LOINC` | ✓ |  |  |  |
| `SNOMED CT` filter `concept is-a 404684003` | ✓ |  |  |  |

### 8. US Core Clinical Note Type

Canonical: `http://hl7.org/fhir/us/core/ValueSet/us-core-clinical-note-type`  
Id: `us-core-clinical-note-type`

**Notes:** `compose` changed in 8.0.1 vs 6.1.0: +5 item(s) added.

| code | 6.1.0 | 8.0.1 | 9.0.0 | notes |
|---|---|---|---|---|
| `18842-5` — LOINC | ✓ | ✓ | ✓ |  |
| `11488-4` — LOINC | ✓ | ✓ | ✓ |  |
| `34117-2` — LOINC | ✓ | ✓ | ✓ |  |
| `11506-3` — LOINC | ✓ | ✓ | ✓ |  |
| `28570-0` — LOINC | ✓ | ✓ | ✓ |  |
| `18748-4` — LOINC |  | ➕ | ✓ | Added in 8.0.1. |
| `11502-2` — LOINC |  | ➕ | ✓ | Added in 8.0.1. |
| `11526-1` — LOINC |  | ➕ | ✓ | Added in 8.0.1. |
| `11504-8` — LOINC |  | ➕ | ✓ | Added in 8.0.1. |
| `34111-5` — LOINC |  | ➕ | ✓ | Added in 8.0.1. |

### 9. US Core Clinical Result Observation Category

Canonical: `http://hl7.org/fhir/us/core/ValueSet/us-core-clinical-result-observation-category`  
Id: `us-core-clinical-result-observation-category`

| code | 6.1.0 | 8.0.1 | 9.0.0 | notes |
|---|---|---|---|---|
| `laboratory` *Laboratory* — THO/observation-category | ✓ | ✓ | ✓ |  |
| `exam` *Exam* — THO/observation-category | ✓ | ✓ | ✓ |  |
| `therapy` *Therapy* — THO/observation-category | ✓ | ✓ | ✓ |  |
| `imaging` *Imaging* — THO/observation-category | ✓ | ✓ | ✓ |  |
| `procedure` *Procedure* — THO/observation-category | ✓ | ✓ | ✓ |  |
| `vital-signs` *Vital Signs* — THO/observation-category | ✓ | ✓ | ✓ |  |
| `activity` *Activity* — THO/observation-category | ✓ | ✓ | ✓ |  |

### 10. US Core Condition Codes

Canonical: `http://hl7.org/fhir/us/core/ValueSet/us-core-condition-code`  
Id: `us-core-condition-code`

**Notes:** **Not locally enumerable** — `compose` includes filter / whole-CodeSystem / ValueSet references; expansion requires a terminology server.

| code | 6.1.0 | 8.0.1 | 9.0.0 | notes |
|---|---|---|---|---|
| `160245001` — SNOMED CT | ✓ | ✓ | ✓ |  |
| `SNOMED CT` filter `concept is-a 404684003` | ✓ | ✓ | ✓ |  |
| `SNOMED CT` filter `concept is-a 243796009` | ✓ | ✓ | ✓ |  |
| `SNOMED CT` filter `concept is-a 272379006` | ✓ | ✓ | ✓ |  |
| All codes from `ICD-10-CM` | ✓ | ✓ | ✓ |  |
| All codes from `ICD-9-CM` | ✓ | ✓ | ✓ |  |

### 11. US Core Condition Codes Current

Canonical: `http://hl7.org/fhir/us/core/ValueSet/us-core-condition-code-current`  
Id: `us-core-condition-code-current`

**Notes:** Added in 8.0.1. Removed in 9.0.0. **Not locally enumerable** — `compose` includes filter / whole-CodeSystem / ValueSet references; expansion requires a terminology server.

| code | 6.1.0 | 8.0.1 | 9.0.0 | notes |
|---|---|---|---|---|
| `160245001` — SNOMED CT |  | ✓ |  |  |
| `SNOMED CT` filter `concept is-a 404684003` |  | ✓ |  |  |
| `SNOMED CT` filter `concept is-a 243796009` |  | ✓ |  |  |
| `SNOMED CT` filter `concept is-a 272379006` |  | ✓ |  |  |
| All codes from `ICD-10-CM` |  | ✓ |  |  |

### 12. US Core Diagnostic Report Category Codes

Canonical: `http://hl7.org/fhir/us/core/ValueSet/us-core-diagnosticreport-category`  
Id: `us-core-diagnosticreport-category`

| code | 6.1.0 | 8.0.1 | 9.0.0 | notes |
|---|---|---|---|---|
| `LP29684-5` *Radiology* — LOINC | ✓ | ✓ | ✓ |  |
| `LP29708-2` *Cardiology* — LOINC | ✓ | ✓ | ✓ |  |
| `LP7839-6` *Pathology* — LOINC | ✓ | ✓ | ✓ |  |

### 13. US Core Non Laboratory Codes

Canonical: `http://hl7.org/fhir/us/core/ValueSet/us-core-diagnosticreport-report-and-note-codes`  
Id: `us-core-diagnosticreport-report-and-note-codes`

**Notes:** **Not locally enumerable** — `compose` includes filter / whole-CodeSystem / ValueSet references; expansion requires a terminology server.

| code | 6.1.0 | 8.0.1 | 9.0.0 | notes |
|---|---|---|---|---|
| `LOINC` filter `CLASSTYPE = 2` | ✓ | ✓ | ✓ |  |

### 14. US Core Discharge Disposition

Canonical: `http://hl7.org/fhir/us/core/ValueSet/us-core-discharge-disposition`  
Id: `us-core-discharge-disposition`

**Notes:** Removed in 8.0.1. **Not locally enumerable** — `compose` includes filter / whole-CodeSystem / ValueSet references; expansion requires a terminology server.

| code | 6.1.0 | 8.0.1 | 9.0.0 | notes |
|---|---|---|---|---|
| All codes from `http://www.nubc.org/patient-discharge` | ✓ |  |  |  |

### 15. US Core DocumentReference Category

Canonical: `http://hl7.org/fhir/us/core/ValueSet/us-core-documentreference-category`  
Id: `us-core-documentreference-category`

**Notes:** **Not locally enumerable** — `compose` includes filter / whole-CodeSystem / ValueSet references; expansion requires a terminology server.

| code | 6.1.0 | 8.0.1 | 9.0.0 | notes |
|---|---|---|---|---|
| All codes from `us-core/documentreference-category` | ✓ | ✓ | ✓ |  |

### 16. US Core DocumentReference Type

Canonical: `http://hl7.org/fhir/us/core/ValueSet/us-core-documentreference-type`  
Id: `us-core-documentreference-type`

**Notes:** **Not locally enumerable** — `compose` includes filter / whole-CodeSystem / ValueSet references; expansion requires a terminology server. `compose` changed in 8.0.1 vs 6.1.0: +1 item(s) added, −1 item(s) removed.

| code | 6.1.0 | 8.0.1 | 9.0.0 | notes |
|---|---|---|---|---|
| `UNK` *unknown* — THO/v3-NullFlavor | ✓ | ✓ | ✓ |  |
| `LOINC` filter `SCALE_TYP = DOC` | ✓ | ⛔ |  | Removed in 8.0.1. |
| `LOINC` filter `SCALE_TYP = LP32888-7` |  | ➕ | ✓ | Added in 8.0.1. |

### 17. US Core Encounter Type

Canonical: `http://hl7.org/fhir/us/core/ValueSet/us-core-encounter-type`  
Id: `us-core-encounter-type`

**Notes:** Removed in 8.0.1. **Not locally enumerable** — `compose` includes filter / whole-CodeSystem / ValueSet references; expansion requires a terminology server.

| code | 6.1.0 | 8.0.1 | 9.0.0 | notes |
|---|---|---|---|---|
| `SNOMED CT` filter `concept is-a 308335008` | ✓ |  |  |  |
| All codes from `CPT` | ✓ |  |  |  |

### 18. US Core Goal Codes

Canonical: `http://hl7.org/fhir/us/core/ValueSet/us-core-goal-description`  
Id: `us-core-goal-description`

**Notes:** **Not locally enumerable** — `compose` includes filter / whole-CodeSystem / ValueSet references; expansion requires a terminology server.

| code | 6.1.0 | 8.0.1 | 9.0.0 | notes |
|---|---|---|---|---|
| All codes from `SNOMED CT` | ✓ | ✓ | ✓ |  |
| All codes from `LOINC` | ✓ | ✓ | ✓ |  |

### 19. US Core Laboratory Test Codes

Canonical: `http://hl7.org/fhir/us/core/ValueSet/us-core-laboratory-test-codes`  
Id: `us-core-laboratory-test-codes`

**Notes:** **Not locally enumerable** — `compose` includes filter / whole-CodeSystem / ValueSet references; expansion requires a terminology server.

| code | 6.1.0 | 8.0.1 | 9.0.0 | notes |
|---|---|---|---|---|
| `LOINC` filter `CLASSTYPE = 1` | ✓ | ✓ | ✓ |  |

### 20. US Core Location Type Codes

Canonical: `http://hl7.org/fhir/us/core/ValueSet/us-core-location-type`  
Id: `us-core-location-type`

**Notes:** Added in 9.0.0. **Not locally enumerable** — `compose` includes filter / whole-CodeSystem / ValueSet references; expansion requires a terminology server.

| code | 6.1.0 | 8.0.1 | 9.0.0 | notes |
|---|---|---|---|---|
| Include ValueSet `http://terminology.hl7.org/ValueSet/v3-ServiceDeliveryLocationRoleType` |  |  | ✓ |  |
| Include ValueSet `http://cts.nlm.nih.gov/fhir/ValueSet/2.16.840.1.113762.1.4.1267.31` |  |  | ✓ |  |
| Include ValueSet `http://terminology.hl7.org/ValueSet/CMSPlaceOfServiceCodes` |  |  | ✓ |  |

### 21. US Core Narrative Status

Canonical: `http://hl7.org/fhir/us/core/ValueSet/us-core-narrative-status`  
Id: `us-core-narrative-status`

| code | 6.1.0 | 8.0.1 | 9.0.0 | notes |
|---|---|---|---|---|
| `additional` *additional* — http://hl7.org/fhir/narrative-status | ✓ | ✓ | ✓ |  |
| `generated` *generated* — http://hl7.org/fhir/narrative-status | ✓ | ✓ | ✓ |  |

### 22. US Core Status for Smoking Status Observation

Canonical: `http://hl7.org/fhir/us/core/ValueSet/us-core-observation-smoking-status-status`  
Id: `us-core-observation-smoking-status-status`

| code | 6.1.0 | 8.0.1 | 9.0.0 | notes |
|---|---|---|---|---|
| `final` — http://hl7.org/fhir/observation-status | ✓ | ✓ | ✓ |  |
| `entered-in-error` — http://hl7.org/fhir/observation-status | ✓ | ✓ | ✓ |  |

### 23. US Core Smoking Status Max-Binding

Canonical: `http://hl7.org/fhir/us/core/ValueSet/us-core-observation-smokingstatus-max`  
Id: `us-core-observation-smokingstatus-max`

**Notes:** Removed in 8.0.1. **Not locally enumerable** — `compose` includes filter / whole-CodeSystem / ValueSet references; expansion requires a terminology server.

| code | 6.1.0 | 8.0.1 | 9.0.0 | notes |
|---|---|---|---|---|
| All codes from `SNOMED CT` | ✓ |  |  |  |

### 24. US Core Observation Value Codes (SNOMED-CT)

Canonical: `http://hl7.org/fhir/us/core/ValueSet/us-core-observation-value-codes`  
Id: `us-core-observation-value-codes`

**Notes:** Removed in 8.0.1. **Not locally enumerable** — `compose` includes filter / whole-CodeSystem / ValueSet references; expansion requires a terminology server.

| code | 6.1.0 | 8.0.1 | 9.0.0 | notes |
|---|---|---|---|---|
| All codes from `SNOMED CT` | ✓ |  |  |  |

### 25. US Core Practitioner Role Specialty Codes

Canonical: `http://hl7.org/fhir/us/core/ValueSet/us-core-practitionerrole-specialty`  
Id: `us-core-practitionerrole-specialty`

**Notes:** Added in 9.0.0. **Not locally enumerable** — `compose` includes filter / whole-CodeSystem / ValueSet references; expansion requires a terminology server.

| code | 6.1.0 | 8.0.1 | 9.0.0 | notes |
|---|---|---|---|---|
| Include ValueSet `http://cts.nlm.nih.gov/fhir/ValueSet/2.16.840.1.114222.4.11.1066` |  |  | ✓ |  |
| Include ValueSet `http://hl7.org/fhir/ValueSet/c80-practice-codes` |  |  | ✓ |  |

### 26. US Core Pregnancy Intent Codes

Canonical: `http://hl7.org/fhir/us/core/ValueSet/us-core-pregnancy-intent`  
Id: `us-core-pregnancy-intent`

**Notes:** Removed in 8.0.1. **Not locally enumerable** — `compose` includes filter / whole-CodeSystem / ValueSet references; expansion requires a terminology server.

| code | 6.1.0 | 8.0.1 | 9.0.0 | notes |
|---|---|---|---|---|
| Include ValueSet `http://cts.nlm.nih.gov/fhir/ValueSet/2.16.840.1.113762.1.4.1166.22` | ✓ |  |  |  |
| `UNK` *Unknown* — THO/v3-NullFlavor | ✓ |  |  |  |

### 27. US Core Pregnancy Status Codes

Canonical: `http://hl7.org/fhir/us/core/ValueSet/us-core-pregnancy-status`  
Id: `us-core-pregnancy-status`

**Notes:** Removed in 8.0.1. **Not locally enumerable** — `compose` includes filter / whole-CodeSystem / ValueSet references; expansion requires a terminology server.

| code | 6.1.0 | 8.0.1 | 9.0.0 | notes |
|---|---|---|---|---|
| Include ValueSet `http://cts.nlm.nih.gov/fhir/ValueSet/2.16.840.1.113762.1.4.1099.24` | ✓ |  |  |  |
| `UNK` *Unknown* — THO/v3-NullFlavor | ✓ |  |  |  |

### 28. US Core Problem or Health Concern

Canonical: `http://hl7.org/fhir/us/core/ValueSet/us-core-problem-or-health-concern`  
Id: `us-core-problem-or-health-concern`

| code | 6.1.0 | 8.0.1 | 9.0.0 | notes |
|---|---|---|---|---|
| `problem-list-item` — http://terminology.hl7.org/CodeSystem/condition-category | ✓ | ✓ | ✓ |  |
| `health-concern` — us-core/condition-category | ✓ | ✓ | ✓ |  |

### 29. US Core Procedure Codes

Canonical: `http://hl7.org/fhir/us/core/ValueSet/us-core-procedure-code`  
Id: `us-core-procedure-code`

**Notes:** **Not locally enumerable** — `compose` includes filter / whole-CodeSystem / ValueSet references; expansion requires a terminology server. `compose` changed in 9.0.0 vs 8.0.1: +1 item(s) added, −1 item(s) removed.

| code | 6.1.0 | 8.0.1 | 9.0.0 | notes |
|---|---|---|---|---|
| All codes from `CPT` | ✓ | ✓ | ✓ |  |
| `SNOMED CT` filter `concept is-a 71388002` | ✓ | ✓ | ✓ |  |
| All codes from `HCPCS (CMS https)` | ✓ | ✓ | ⛔ | Removed in 9.0.0. |
| All codes from `ICD-10-PCS (CMS)` | ✓ | ✓ | ✓ |  |
| All codes from `CDT` | ✓ | ✓ | ✓ |  |
| All codes from `LOINC` | ✓ | ✓ | ✓ |  |
| All codes from `HCPCS (CMS http)` |  |  | ➕ | Added in 9.0.0. |

### 30. US Core Provenance Participant Type Codes

Canonical: `http://hl7.org/fhir/us/core/ValueSet/us-core-provenance-participant-type`  
Id: `us-core-provenance-participant-type`

**Notes:** Removed in 9.0.0. **Not locally enumerable** — `compose` includes filter / whole-CodeSystem / ValueSet references; expansion requires a terminology server.

| code | 6.1.0 | 8.0.1 | 9.0.0 | notes |
|---|---|---|---|---|
| All codes from `us-core/provenance-participant-type` | ✓ | ✓ |  |  |
| All codes from `http://terminology.hl7.org/CodeSystem/provenance-participant-type` | ✓ | ✓ |  |  |

### 31. US Core Screening Assessment Condition Category

Canonical: `http://hl7.org/fhir/us/core/ValueSet/us-core-screening-assessment-condition-category`  
Id: `us-core-screening-assessment-condition-category`

**Notes:** **Not locally enumerable** — `compose` includes filter / whole-CodeSystem / ValueSet references; expansion requires a terminology server. `compose` changed in 8.0.1 vs 6.1.0: +1 item(s) added, −1 item(s) removed.

| code | 6.1.0 | 8.0.1 | 9.0.0 | notes |
|---|---|---|---|---|
| All codes from `us-core/us-core-category` | ✓ | ⛔ |  | Removed in 8.0.1. |
| `sdoh` — us-core/us-core-category |  | ➕ | ✓ | Added in 8.0.1. |

### 32. US Core Screening Assessment Observation Category

Canonical: `http://hl7.org/fhir/us/core/ValueSet/us-core-screening-assessment-observation-category`  
Id: `us-core-screening-assessment-observation-category`

**Notes:** **Not locally enumerable** — `compose` includes filter / whole-CodeSystem / ValueSet references; expansion requires a terminology server. `compose` changed in 8.0.1 vs 6.1.0: +6 item(s) added, −1 item(s) removed.

| code | 6.1.0 | 8.0.1 | 9.0.0 | notes |
|---|---|---|---|---|
| All codes from `us-core/us-core-category` | ✓ | ⛔ |  | Removed in 8.0.1. |
| `sdoh` — us-core/us-core-category |  | ➕ | ✓ | Added in 8.0.1. |
| `functional-status` — us-core/us-core-category |  | ➕ | ✓ | Added in 8.0.1. |
| `disability-status` — us-core/us-core-category |  | ➕ | ✓ | Added in 8.0.1. |
| `cognitive-status` — us-core/us-core-category |  | ➕ | ✓ | Added in 8.0.1. |
| `activity` — THO/observation-category |  | ➕ | ✓ | Added in 8.0.1. |
| `social-history` — THO/observation-category |  | ➕ | ✓ | Added in 8.0.1. |

### 33. US Core Screening Assessment Observation Maximum Category

Canonical: `http://hl7.org/fhir/us/core/ValueSet/us-core-screening-assessment-observation-maximum-category`  
Id: `us-core-screening-assessment-observation-maximum-category`

**Notes:** Added in 8.0.1. **Not locally enumerable** — `compose` includes filter / whole-CodeSystem / ValueSet references; expansion requires a terminology server.

| code | 6.1.0 | 8.0.1 | 9.0.0 | notes |
|---|---|---|---|---|
| All codes from `us-core/us-core-category` |  | ✓ | ✓ |  |
| All codes from `THO/observation-category` |  | ✓ | ✓ |  |
| EXCLUDE `survey` from THO/observation-category |  | ✓ | ✓ |  |

### 34. US Core ServiceRequest Category Codes

Canonical: `http://hl7.org/fhir/us/core/ValueSet/us-core-servicerequest-category`  
Id: `us-core-servicerequest-category`

**Notes:** **Not locally enumerable** — `compose` includes filter / whole-CodeSystem / ValueSet references; expansion requires a terminology server.

| code | 6.1.0 | 8.0.1 | 9.0.0 | notes |
|---|---|---|---|---|
| All codes from `us-core/us-core-category` | ✓ | ✓ | ✓ |  |
| `386053000` *Evaluation procedure (procedure)* — SNOMED CT | ✓ | ✓ | ✓ |  |
| `410606002` *Social service procedure (procedure)* — SNOMED CT | ✓ | ✓ | ✓ |  |
| Include ValueSet `http://hl7.org/fhir/ValueSet/servicerequest-category` | ✓ | ✓ | ✓ |  |

### 35. US Core Sexual Orientation

Canonical: `http://hl7.org/fhir/us/core/ValueSet/us-core-sexual-orientation`  
Id: `us-core-sexual-orientation`

**Notes:** Removed in 8.0.1.

| code | 6.1.0 | 8.0.1 | 9.0.0 | notes |
|---|---|---|---|---|
| `38628009` — SNOMED CT | ✓ |  |  |  |
| `20430005` — SNOMED CT | ✓ |  |  |  |
| `42035005` — SNOMED CT | ✓ |  |  |  |
| `OTH` *Other* — THO/v3-NullFlavor | ✓ |  |  |  |
| `UNK` *Unknown* — THO/v3-NullFlavor | ✓ |  |  |  |
| `ASKU` *Asked but no answer* — THO/v3-NullFlavor | ✓ |  |  |  |

### 36. US Core Simple Observation Category

Canonical: `http://hl7.org/fhir/us/core/ValueSet/us-core-simple-observation-category`  
Id: `us-core-simple-observation-category`

**Notes:** **Not locally enumerable** — `compose` includes filter / whole-CodeSystem / ValueSet references; expansion requires a terminology server.

| code | 6.1.0 | 8.0.1 | 9.0.0 | notes |
|---|---|---|---|---|
| All codes from `us-core/us-core-category` | ✓ | ✓ | ✓ |  |
| All codes from `THO/observation-category` | ✓ | ✓ | ✓ |  |

### 37. US Core Smoking Status Observation Codes

Canonical: `http://hl7.org/fhir/us/core/ValueSet/us-core-smoking-status-observation-codes`  
Id: `us-core-smoking-status-observation-codes`

**Notes:** Removed in 8.0.1.

| code | 6.1.0 | 8.0.1 | 9.0.0 | notes |
|---|---|---|---|---|
| `72166-2` *Tobacco smoking status NHIS* — LOINC | ✓ |  |  |  |

### 38. US Core Specimen Condition

Canonical: `http://hl7.org/fhir/us/core/ValueSet/us-core-specimen-condition`  
Id: `us-core-specimen-condition`

**Notes:** Added in 8.0.1. **Not locally enumerable** — `compose` includes filter / whole-CodeSystem / ValueSet references; expansion requires a terminology server.

| code | 6.1.0 | 8.0.1 | 9.0.0 | notes |
|---|---|---|---|---|
| Include ValueSet `http://terminology.hl7.org/ValueSet/v2-0493` |  | ✓ | ✓ |  |
| Include ValueSet `http://cts.nlm.nih.gov/fhir/ValueSet/2.16.840.1.113762.1.4.1267.24` |  | ✓ | ✓ |  |

### 39. US Core Survey Codes

Canonical: `http://hl7.org/fhir/us/core/ValueSet/us-core-survey-codes`  
Id: `us-core-survey-codes`

**Notes:** Removed in 8.0.1. **Not locally enumerable** — `compose` includes filter / whole-CodeSystem / ValueSet references; expansion requires a terminology server.

| code | 6.1.0 | 8.0.1 | 9.0.0 | notes |
|---|---|---|---|---|
| `LOINC` filter `CLASSTYPE = 4` | ✓ |  |  |  |
| `LOINC` filter `CLASSTYPE = 2` | ✓ |  |  |  |
| `LOINC` filter `CLASS = PANEL.NEONAT` | ✓ |  |  |  |

### 40. USPS Two Letter Alphabetic Codes

Canonical: `http://hl7.org/fhir/us/core/ValueSet/us-core-usps-state`  
Id: `us-core-usps-state`

**Notes:** Removed in 8.0.1. **Not locally enumerable** — `compose` includes filter / whole-CodeSystem / ValueSet references; expansion requires a terminology server.

| code | 6.1.0 | 8.0.1 | 9.0.0 | notes |
|---|---|---|---|---|
| All codes from `USPS` | ✓ |  |  |  |

### 41. US Core Vital Signs ValueSet

Canonical: `http://hl7.org/fhir/us/core/ValueSet/us-core-vital-signs`  
Id: `us-core-vital-signs`

**Notes:** Removed in 8.0.1. **Not locally enumerable** — `compose` includes filter / whole-CodeSystem / ValueSet references; expansion requires a terminology server.

| code | 6.1.0 | 8.0.1 | 9.0.0 | notes |
|---|---|---|---|---|
| `59576-9` — LOINC | ✓ |  |  |  |
| `8289-1` — LOINC | ✓ |  |  |  |
| `77606-2` — LOINC | ✓ |  |  |  |
| `59408-5` — LOINC | ✓ |  |  |  |
| `3150-0` — LOINC | ✓ |  |  |  |
| `3151-8` — LOINC | ✓ |  |  |  |
| Include ValueSet `http://hl7.org/fhir/ValueSet/observation-vitalsignresult` | ✓ |  |  |  |

