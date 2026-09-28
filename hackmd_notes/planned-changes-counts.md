## Planned US Core V10 Changes — Counts

| Change Type | Committed | Conditional / still open | Total if all land |
|---|---:|---:|---:|
| New profiles | 4 | 3 | 7 |
| New extensions | 1 | 1 | 2 |
| New elements in existing profiles | 10 | 0 | 10 |
| Value sets — new | 2 | 0 | 2 |
| Value sets — existing, updated | 3 | 1 | 4 |

### New profiles (4 committed, 3 conditional)

| Profile | Data Class | Status |
|---|---|---|
| US Core Appointment Profile | Encounter Information | ✅ Committed |
| US Core MedicationAdministration Profile | Medications | ✅ Committed |
| US Core DeviceRequest Profile | Orders | ✅ Committed |
| US Core NutritionOrder Profile | Orders | ✅ Committed |
| US Core Accommodation Observation Profile | Patient Demographics/Information | 🔴 Conditional — only if the one-off Observation option wins over Simple Observation |
| US Core Tobacco Use Observation Profile | Health Status Assessments | 🟡 Conditional — only if the gap review favors deprecate-and-replace over renaming Smoking Status |
| US Core ImagingStudy Profile | Diagnostic Imaging | 🟠 Conditional — open question whether US Core defines it or defers to others |

### New extensions (1 committed, 1 conditional)

| Extension | Applied to | Status |
|---|---|---|
| FHIR R5 `recorded` cross-version extension | `Procedure` (Reason Not Performed) | 🟡 Committed in the proposal — disambiguates `performed[x]` when `status` is "not-done" |
| US Core "source concept" extension | `AllergyIntolerance.criticality` | 🟡 Conditional — under exploration to avoid the lossy mapping (no "medium" concept) |

### New elements in existing profiles (10)

| Element | Profile | Flag | Status |
|---|---|---|---|
| `Encounter.appointment` | US Core Encounter | *Additional USCDI* | ✅ Decided |
| `AllergyIntolerance.criticality` | US Core AllergyIntolerance | *Additional USCDI* | ✅ Decided |
| `Specimen.collection.collected[x]` | US Core Specimen | *Additional USCDI* | ✅ Decided |
| `Specimen.collection.method` | US Core Specimen | *Additional USCDI* | ✅ Decided |
| `MedicationRequest.doNotPerform` | US Core MedicationRequest | Must Support | 🟡 Scope decided — binding and search open |
| `Procedure.statusReason` | US Core Procedure | Must Support | 🟡 Scope decided — binding and search open |
| `DiagnosticReport.media.link` | US Core DiagnosticReport for Report and Note Exchange | *Additional USCDI* | 🟠 Approach OK — details open |
| `DiagnosticReport.imagingStudy` | US Core DiagnosticReport for Report and Note Exchange | *Additional USCDI* | 🟠 Approach OK — details open |
| `DiagnosticReport.identifier` | US Core DiagnosticReport for Report and Note Exchange | *Additional USCDI* | 🟠 Approach OK — details open |
| `ServiceRequest.identifier` | US Core ServiceRequest | *Additional USCDI* | 🟠 Approach OK — details open |

### Value sets (2 new, 3-4 existing updated)

| Value set | Change | Status |
|---|---|---|
| US Core Negation Reason Codes (VSAC) | :new: — extensible binding on `Immunization.statusReason`, `MedicationAdministration.statusReason`, `Procedure.statusReason` | 🟡 Proposed — adopt vs. keep the base *example* bindings |
| US Core Specimen Collection Method (VSAC) | :new: — 211 concepts, *preferred* binding on `Specimen.collection.method` | 🟡 Decided — concept list TBD with the terminology reviewers |
| Care Team Member Function (VSAC) | Add LOINC 81335-2 Patient healthcare agent | 🟡 Decided — one code vs. three still open |
| US Core ServiceRequest Category Codes | Add SNOMED CT 3457005 Patient referral (procedure) | ✅ Decided |
| US Core Clinical Note Type | Add LOINC 57133-1 Referral note | :warning: No CGP decision recorded |
| Personal And Legal Relationship Role Type | Binding strength *preferred* → *extensible* on `RelatedPerson.relationship` (no value set content change) | 🟠 Conditional — pending the PACIO follow-up call |

<!--
Counting notes:
- The new MedicationAdministration profile's `.statusReason` and `.effective[x]` count as part of that new profile, not as elements added to an existing profile.
- `Immunization.statusReason` is excluded: it is already Must Support and needs no profile change, only a possible binding change.
-->
