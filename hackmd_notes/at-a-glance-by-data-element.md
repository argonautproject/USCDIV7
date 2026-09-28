## At a Glance

| Symbol | Meaning |
|---|---|
| ✅ | Decided — no open questions recorded |
| 🟡 | Decided — details (binding, search, elements) still open |
| 🟠 | Approach decided — substance still open |
| 🔴 | Open — no disposition chosen yet |
| :warning: | No CGP call decision recorded |
| ➕ | Element is also in USCDI+ |
| :new: | New profile, value set, or element |

| Data Element | Data Class | US Core V10 Disposition | Status |
|---|---|---|---|
| **Reason Not Performed ➕** | [Healthcare Information Attributes](/uwyK8MoTReG1ev02XIY-lA) (NEW) | Follow the US Quality Core negation pattern on four profiles only: `Immunization.statusReason`, `MedicationAdministration.statusReason`, :new: `MedicationRequest.doNotPerform`, :new: `Procedure.statusReason` + R5 `.recorded` cross-version extension. ServiceRequest, Task, DeviceRequest, NutritionOrder, DiagnosticReport, Appointment, CarePlan, and Goal deferred. | 🟡 Scope decided — binding and search conformance open |
| **Diagnostic Report Date and Time ➕** | [Healthcare Information Attributes](/uwyK8MoTReG1ev02XIY-lA) (NEW) | **No change** — `DiagnosticReport.issued` is already Must Support in all relevant profiles | ✅ Decided |
| **Adverse Event Condition ➕** | [Adverse Events](/CKyBxeRYQJ6SrkYPj3zUbw) (NEW) | No AdverseEvent resource. Map to the existing profile that records the event: `AllergyIntolerance.reaction`, `Immunization.reaction`, Condition, DocumentReference, Simple Observation, possibly Procedure | 🟠 Approach decided — profile list and guidance open |
| **Adverse Event Outcome** | [Adverse Events](/CKyBxeRYQJ6SrkYPj3zUbw) (NEW) | No AdverseEvent resource. Map to the existing profile that records the outcome: Encounter (discharge disposition), CarePlan | 🟠 Approach decided — profile list and guidance open |
| **Appointment** | [Encounter Information](/5VD6Yd4WQ5m929CrY7X3jw) | Add a :new: US Core Appointment Profile; add `Encounter.appointment` min = 0 *Additional USCDI* to the US Core Encounter Profile | 🟡 Decided — Must Support actor targets, search API, scopes, and Provenance open |
| **Diagnostic Imaging Reference ➕** | [Diagnostic Imaging](/CNYwm7OsQ7S4EBxct2yvkg) | Add `DiagnosticReport.media.link`, `DiagnosticReport.imagingStudy`, `DiagnosticReport.identifier`, and `ServiceRequest.identifier` as min = 0 *Additional USCDI* to the DiagnosticReport Profile for Report and Note Exchange | 🟠 Approach OK — ImagingStudy profile, server choice, reference depth, and search open |
| **Healthcare Agent ➕** | [Care Team Members](/5VanJRHKQ12dIPtS-16hWQ) | Terminology only. Map to `CareTeam.participant.role` (add LOINC 81335-2 to Care Team Member Function) and `RelatedPerson.relationship` (DPOWATT or HPOWATT), with a pointer to the PACIO ADI guidance | 🟡 Mapping decided — one code vs. three and *preferred* → *extensible* open |
| **Medication Administration ➕** | [Medications](/2654oTa6R7CNK1T-CsKvdQ) | Add a :new: US Core MedicationAdministration Profile; same medication terminology as MedicationRequest and MedicationDispense; Must Support choice on `.effective[x]`; author Provenance = `.performer.actor` | 🟡 Decided — search API, scopes, and individual Provenance open |
| **Medication Dispense Quantity ➕** | [Medications](/2654oTa6R7CNK1T-CsKvdQ) | **No change** — `MedicationRequest.dispenseRequest.quantity` and `MedicationDispense.quantity` are already Must Support | ✅ Decided |
| **Accommodation ➕** | [Patient Demographics/Information](/VoQgkVxsQsKmBRei3Oxi4Q) | Narrowed to two Observation options: a :new: US Core Accommodation Observation Profile, or the existing Assessments framework with Simple Observation and a new category. Free text in the near term | 🔴 Open — choice deferred to the fall |
| **Deceased Indicator ➕** | [Patient Demographics/Information](/VoQgkVxsQsKmBRei3Oxi4Q) | **No change** — `Patient.deceased[x]` is already an *Additional USCDI* element | ✅ Decided |
| **Patient Identifier** | [Patient Demographics/Information](/VoQgkVxsQsKmBRei3Oxi4Q) | **No change** — `Patient.identifier` is already Must Support | ✅ Decided |
| **Medical Device Order ➕** | [Orders](/2c5wMyJaSRORwN5F-F5CAQ) | Add a :new: US Core DeviceRequest Profile with a ServiceRequest-style search API, scopes SHALL `-rs`, Provenance = requester, plus an implementation bullet that ServiceRequest or MedicationRequest may be used instead | 🟡 Decided — `code[x]` Must Support choices and binding strength (HCPCS/CPT) open |
| **Nutrition Order ➕** | [Orders](/2c5wMyJaSRORwN5F-F5CAQ) | Add a :new: US Core NutritionOrder Profile with a ServiceRequest-style search API, scopes SHALL `-rs`, Provenance = orderer | 🟡 Decided — `.enteral`/`.supplements`, `oralDiet.instruction` Must Support, and binding open |
| **Referral Order** | [Orders](/2c5wMyJaSRORwN5F-F5CAQ) | Guidance only on the US Core ServiceRequest Profile: add category code 3457005 Patient referral (procedure); `code` binding stays unconstrained | ✅ Decided |
| **Allergy Intolerance Criticality** | [Allergies and Intolerances](/ziEuzkenRnqZ55h7L7vV_Q) | Add `AllergyIntolerance.criticality` 0..1 as *Additional USCDI*; terminology inherited from base (required binding to AllergyIntoleranceCriticality, THO); no new search parameter | 🟡 Decided — source-concept extension for the lossy mapping open |
| **Nutrition Assessment ➕** | [Health Status Assessments](/_s1WbP-9SxGOEt8IcST0Ow) | Use the existing Assessments/Observations framework; add terminology to the Screening and Assessments guidance page; category code 75305-3, SNOMED CT result values | 🟡 Decided — LOINC code choice and binding open |
| **Tobacco Use** | [Health Status Assessments](/_s1WbP-9SxGOEt8IcST0Ow) | Update and rename the US Core Smoking Status Observation Profile: review terminology, add product and mode-of-consumption guidance, multiple Observations per question | 🟡 Decided — rename vs. deprecate-and-replace open pending the gap review |
| **Specimen Collection Method** | [Laboratory](/38xa1BZ7TjaPMao6LJHuCA) | Add `Specimen.collection.method` min = 0 *Additional USCDI* to the US Core Specimen Profile; *preferred* binding; value set in VSAC | 🟡 Decided — concept list TBD with the terminology reviewers |
| **Specimen Collection Date and Time** | [Laboratory](/38xa1BZ7TjaPMao6LJHuCA) | Add `Specimen.collection.collected[x]` min = 0 *Additional USCDI*; note that Laboratory Result Observation `effective[x]` also maps here | ✅ Decided |
| **Coverage Type** (standard added) | [Other USCDI v7 Changes](/D5TZacmHQKqkcniD-aT-Ag) | **No change** — SOPT 9.2 is already used by the US Core Coverage Profile | ✅ Decided |
| **Patient Goal** (standard added) | [Other USCDI v7 Changes](/D5TZacmHQKqkcniD-aT-Ag) | **No change** — LOINC and SNOMED CT are already used; the value set definition could be constrained to a subset | ✅ Decided |
| **Pregnancy Status** (standard added) | [Other USCDI v7 Changes](/D5TZacmHQKqkcniD-aT-Ag) | **No change** — LOINC is already used for `Observation.code` in the US Core Pregnancy profiles | ✅ Decided |
| **Renames, reclassifications, and consolidations** (19 elements) | [Other USCDI v7 Changes](/D5TZacmHQKqkcniD-aT-Ag) | Documentation only — reconcile the USCDI mapping and profile narrative with the revised categories, names, and definitions | ✅ Decided |
| **Facility Telecom** | [Facility Information](/osTHZxJpRveYPTwpDQDmVg) | **No change** — `Location.telecom` is already Must Support | ✅ Decided |
| **Health Insurance Coverage Period ➕** | [Health Insurance Information](/fTF4vhmGTneSxejvpdOuBA) | **No change** — `Coverage.period` is already Must Support | ✅ Decided |
| **Health Insurance Payer** | [Health Insurance Information](/fTF4vhmGTneSxejvpdOuBA) | **No change** — `Coverage.payor` is already Must Support | ✅ Decided |
| **Health Insurance Plan ➕** | [Health Insurance Information](/fTF4vhmGTneSxejvpdOuBA) | **No change** — `Coverage.class:plan` is already Must Support | ✅ Decided |
| **Health Insurance Plan Identifier ➕** | [Health Insurance Information](/fTF4vhmGTneSxejvpdOuBA) | **No change** — `Coverage.class:plan.value` and `Coverage.class:plan.name` are already Must Support | ✅ Decided |
| **Immunization Status ➕** | [Immunizations](/mcuKzClMQYCtWyODyfLJdQ) | **No change** — `Immunization.status` is already Must Support | ✅ Decided |
| **Immunization Record Source ➕** | [Immunizations](/mcuKzClMQYCtWyODyfLJdQ) | **No change** — `Immunization.primarySource` is already Must Support; `.reportOrigin` deliberately not profiled | ✅ Decided |
| **Device Type ➕** | [Medical Devices](/Q7IK0ASkRVWrJQF4t3zJTQ) | **No change** — `Device.type` is already Must Support | ✅ Decided — HCPCS question from comments unanswered |
| **Condition Status ➕** | [Problems](/nsjWBx5WQlKQHua_xKhLEQ) | **No change** — `Condition.clinicalStatus` is already Must Support with a required binding | ✅ Decided |
| **Procedure Status ➕** | [Procedures](/TLixyzIBRs6Wz_ulqrWUzA) | **No change** — `Procedure.status` is already Must Support; the "not done" case is handled under Healthcare Information Attributes | ✅ Decided |
| **Referral Note** | [Clinical Notes](/5YMuiYySSzmhFSymS2PHnA) | Add Referral note (LOINC 57133-1) to the minimum Clinical Note Type value set and the Common Clinical Notes list | :warning: **No CGP decision recorded** — proposal only |


