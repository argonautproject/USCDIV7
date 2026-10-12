<style>
#doc.markdown-body, .ui-infobar, .container-thiner {
    max-width: 1080px; /* Adjust this value to make wider, e.g., 1200px or 1550px */
}
.ui-content #doc.markdown-body, .ui-content .ui-infobar {
    max-width: 1550px; /* Set a wider max-width for content */
}
@media (min-width: 768px) {
    #doc.markdown-body, .ui-infobar {
        max-width: 750px; /* Optional: Adjust for smaller screens */
    }
}
@media (min-width: 1200px) {
    #doc.markdown-body, .ui-infobar {
        max-width: 1170px; /* Optional: Adjust for larger screens */
    }
}
</style>

source: https://hackmd.io/@erichaas/SJo4QLYL-g

![argo_small](https://hackmd.io/_uploads/SyiP7bKrR.png)![US_Core_Design_Logo](https://hackmd.io/_uploads/HyUyU6W9ze.png)

# US Core V10 Design

## References

- [ASTP USCDI website](https://isp.healthit.gov/united-states-core-data-interoperability-uscdi#uscdi-v7)
- [ASTP USCDI V7 PDF](https://isp.healthit.gov/sites/default/files/2026-07/USCDI-Version-7-Standard-Document.pdf)
    - [USCDI v7: Draft (January 2026) vs. Final (July 2026)](/mHqlwgfyTnyIpIqWJADdTg)
- [United States Core Data for Interoperability Version 7 Standard Bulletin](https://healthit.gov/standards-and-technology/onc-standards-bulletin/onc-standards-bulletin-2026-2/)
- [USCDI v7 New Data Elements — USCDI+ Domain and USCDI+ Quality v2 Mapping](/WoGZh1mVRTek92MmpBtwlA)

## US Core Design Principles

- [US Core Design](/r-VtK_20Rw25Vf81p5Lyvg#Design-Principles)

## US Core Design Decisions Overview

For Detailed notes click on the Data Class links in the table below.

| Symbol | Meaning |
|---|---|
| ✅ | Decided — no open questions recorded |
| 🟡 | Decided — details (binding, search, elements) still open |
| 🔴 | Open — no disposition chosen yet |
| :new: | New profile, value set, or element |

| Data Element | Data Class | US Core V10 Design Decision | Status |
|---|---|---|---|
| **Reason Not Performed** | [Healthcare Information Attributes](/uwyK8MoTReG1ev02XIY-lA) (NEW) | Follow the US Quality Core negation pattern on four profiles only: `Immunization.statusReason`, `MedicationAdministration.statusReason`, :new: `Procedure.statusReason` + R5 `.recorded` cross-version extension. Defer extending to other Profiles. | 🟡 Scope decided — binding and search conformance open |
| **Diagnostic Report Date and Time** | [Healthcare Information Attributes](/uwyK8MoTReG1ev02XIY-lA) (NEW) | **No change** — `DiagnosticReport.issued` is already Must Support in all relevant profiles | ✅ Decided |
| **Adverse Event Condition** | [Adverse Events](/CKyBxeRYQJ6SrkYPj3zUbw) (NEW) | No AdverseEvent resource. Map to the existing profiles that records the event including AllergyIntolerance, Immunization., Condition, DocumentReference, Simple Observation, possibly Procedure.  Document in guidance page and on profile pages| ✅ Decided - review|
| **Adverse Event Outcome** | [Adverse Events](/CKyBxeRYQJ6SrkYPj3zUbw) (NEW) | No AdverseEvent resource. Map to the existing profiles that records the event including Encounter (discharge disposition), CarePlan, Condition, DocumentReference, Simple Observation, possibly Procedure.|  ✅ Decided - review|
| **Appointment** | [Encounter Information](/5VD6Yd4WQ5m929CrY7X3jw) | Add a :new: US Core Appointment Profile; add `Encounter.appointment` min = 0 *Additional USCDI* to the US Core Encounter Profile | ✅ Decided |
| **Diagnostic Imaging Reference** | [Diagnostic Imaging](/CNYwm7OsQ7S4EBxct2yvkg) | Add `DiagnosticReport.media.link`, `DiagnosticReport.imagingStudy`, `DiagnosticReport.identifier`, and `ServiceRequest.identifier` as min = 0 *Additional USCDI* to the DiagnosticReport Profile for Report and Note Exchange. Add a :new: US Core ImagingStudy Profile; | ✅ Decided - review|
| **Healthcare Agent** | [Care Team Members](/5VanJRHKQ12dIPtS-16hWQ) | Terminology only. Map to `CareTeam.participant.role` (add LOINC 81335-2 to Care Team Member Function,DPOWATT or HPOWATT)) and `RelatedPerson.relationship` (DPOWATT or HPOWATT), change binding *preferred* → *extensible*, point to the PACIO ADI guidance | ✅ Decided |
| **Medication Administration** | [Medications](/2654oTa6R7CNK1T-CsKvdQ) | Add a :new: US Core MedicationAdministration Profile; same medication terminology as MedicationRequest and MedicationDispense; Must Support choice on `.effective[x]`; author Provenance = `.performer.actor` | ✅ Decided |
| **Medication Dispense Quantity** | [Medications](/2654oTa6R7CNK1T-CsKvdQ) | **No change** — `MedicationRequest.dispenseRequest.quantity` and `MedicationDispense.quantity` are already Must Support | ✅ Decided |
| **Accommodation** | [Patient Demographics/Information](/VoQgkVxsQsKmBRei3Oxi4Q) | Narrowed to two Observation options: a :new: US Core Accommodation Observation Profile, or the existing Assessments framework with Simple Observation and a new category. Free text in the near term | 🔴 Open — review option|
| **Deceased Indicator** | [Patient Demographics/Information](/VoQgkVxsQsKmBRei3Oxi4Q) | **No change** — `Patient.deceased[x]` is already an *Additional USCDI* element | ✅ Decided |
| **Patient Identifier** | [Patient Demographics/Information](/VoQgkVxsQsKmBRei3Oxi4Q) | **No change** — `Patient.identifier` is already Must Support | ✅ Decided |
| **Medical Device Order** | [Orders](/2c5wMyJaSRORwN5F-F5CAQ) | Add a :new: US Core DeviceRequest Profile with a ServiceRequest-style search API, scopes SHALL `-rs`, Provenance = requester, plus an implementation bullet that ServiceRequest or MedicationRequest may be used instead | 🟡 Decided — `code[x]` Must Support binding choices open |
| **Nutrition Order** | [Orders](/2c5wMyJaSRORwN5F-F5CAQ) | Add a :new: US Core NutritionOrder Profile with a ServiceRequest-style search API, scopes SHALL `-rs`, Provenance = orderer | 🟡 Decided — `.enteral`/`.supplements`, `oralDiet.instruction` Must Support, and binding open |
| **Referral Order** | [Orders](/2c5wMyJaSRORwN5F-F5CAQ) | Guidance only on the US Core ServiceRequest Profile: add category code 3457005 Patient referral (procedure); `code` binding stays unconstrained | ✅ Decided |
| **Allergy Intolerance Criticality** | [Allergies and Intolerances](/ziEuzkenRnqZ55h7L7vV_Q) | Add `AllergyIntolerance.criticality` 0..1 as *Additional USCDI*; terminology inherited from base (required binding to AllergyIntoleranceCriticality, THO); no new search parameter | ✅ Decided |
| **Nutrition Assessment** | [Health Status Assessments](/_s1WbP-9SxGOEt8IcST0Ow) | Use the existing Assessments/Observations framework; add terminology to the Screening and Assessments guidance page; category code 75305-3, SNOMED CT result values | 🟡 Decided — LOINC code choice and binding open |
| **Tobacco Use** | [Health Status Assessments](/_s1WbP-9SxGOEt8IcST0Ow) | Update and rename the US Core Smoking Status Observation Profile: review terminology, add product and mode-of-consumption guidance, multiple Observations per question | ✅ Decided — rename and update the terminology |
| **Specimen Collection Method** | [Laboratory](/38xa1BZ7TjaPMao6LJHuCA) | Add `Specimen.collection.method` min = 0 *Additional USCDI* to the US Core Specimen Profile; *preferred* binding; value set in VSAC | 🟡 Decided — concept list TBD with the terminology reviewers |
| **Specimen Collection Date and Time** | [Laboratory](/38xa1BZ7TjaPMao6LJHuCA) | Add `Specimen.collection.collected[x]` min = 0 *Additional USCDI*; note that Laboratory Result Observation `effective[x]` also maps here | ✅ Decided |
| **Facility Telecom** | [Facility Information](/osTHZxJpRveYPTwpDQDmVg) | **No change** — `Location.telecom` is already Must Support | ✅ Decided |
| **Health Insurance Coverage Period** | [Health Insurance Information](/fTF4vhmGTneSxejvpdOuBA) | **No change** — `Coverage.period` is already Must Support | ✅ Decided |
| **Health Insurance Payer** | [Health Insurance Information](/fTF4vhmGTneSxejvpdOuBA) | **No change** — `Coverage.payor` is already Must Support | ✅ Decided |
| **Health Insurance Plan** | [Health Insurance Information](/fTF4vhmGTneSxejvpdOuBA) | **No change** — `Coverage.class:plan` is already Must Support | ✅ Decided |
| **Health Insurance Plan Identifier** | [Health Insurance Information](/fTF4vhmGTneSxejvpdOuBA) | **No change** — `Coverage.class:plan.value` and `Coverage.class:plan.name` are already Must Support | ✅ Decided |
| **Immunization Status** | [Immunizations](/mcuKzClMQYCtWyODyfLJdQ) | **No change** — `Immunization.status` is already Must Support | ✅ Decided |
| **Immunization Record Source** | [Immunizations](/mcuKzClMQYCtWyODyfLJdQ) | **No change** — `Immunization.primarySource` is already Must Support; `.reportOrigin` deliberately not profiled | ✅ Decided |
| **Device Type** | [Medical Devices](/Q7IK0ASkRVWrJQF4t3zJTQ) | **No change** — `Device.type` is already Must Support | ✅ Decided |
| **Condition Status** | [Problems](/nsjWBx5WQlKQHua_xKhLEQ) | **No change** — `Condition.clinicalStatus` is already Must Support with a required binding | ✅ Decided |
| **Procedure Status** | [Procedures](/TLixyzIBRs6Wz_ulqrWUzA) | **No change** — `Procedure.status` is already Must Support; the "not done" case is handled under Healthcare Information Attributes | ✅ Decided |
| **Referral Note** | [Clinical Notes](/5YMuiYySSzmhFSymS2PHnA) | Add Referral note (LOINC 57133-1) to the minimum Clinical Note Type value set and the Common Clinical Notes list |  ✅ Decided  |




### [Other USCDI v7 Changes](/D5TZacmHQKqkcniD-aT-Ag) 

|Item | Decision |
|---|---|
| **Coverage Type** (standard added) | **No change** — SOPT 9.2 is already used by the US Core Coverage Profile |
| **Patient Goal** (standard added)  | **No change** — LOINC and SNOMED CT are already used; the value set definition could be constrained to a subset | 
| **Pregnancy Status** (standard added) | **No change** — LOINC is already used for `Observation.code` in the US Core Pregnancy profiles |
| **Renames, reclassifications, and consolidations** (19 elements) | Documentation only — reconcile the USCDI mapping and profile narrative with the revised categories, names, and definitions | 

## Summary By Data Class

[US Core V10 — Summary of USCDI v7 Design Decisions](/mDRKbShqSQ26rCICHfSGJQ)





