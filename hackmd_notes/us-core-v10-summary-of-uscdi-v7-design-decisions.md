---
slideOptions:
  width: 1340
  height: 754
  margin: 0
  center: true
---


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

![argo_small](https://hackmd.io/_uploads/SyiP7bKrR.png)

# US Core V10 — Summary of USCDI v7 Design Decisions by Data Class

page link: https://hackmd.io/mDRKbShqSQ26rCICHfSGJQ?view

---

## Planned US Core V10 Changes — Counts

| Change Type | Committed | Conditional / still open | Total if all land |
|---|---:|---:|---:|
| New profiles | 4 | 3 | 7 |
| New extensions | 0 | 2 | 2 |
| New elements in existing profiles | 10 | 0 | 10 |
| Value sets — new | 2 | 0 | 2 |
| Value sets — existing, updated | 3 | 1 | 4 |

----

### New profiles (4 decided, 3 conditional)

| Profile | Data Class | Status |
|---|---|---|
| US Core Appointment Profile | Encounter Information | 🟠 Approach OK — details open |
| US Core MedicationAdministration Profile | Medications | 🟠 Approach OK — details open |
| US Core DeviceRequest Profile | Orders | 🟠 Approach OK — details open |
| US Core NutritionOrder Profile | Orders | 🟠 Approach OK — details open  |
| US Core Accommodation Observation Profile | Patient Demographics/Information | 🔴 Conditional — only if the one-off Observation option wins over Simple Observation |
| US Core Tobacco Use Observation Profile | Health Status Assessments | 🟡 Conditional — only if the gap review favors deprecate-and-replace over renaming Smoking Status |
| US Core ImagingStudy Profile | Diagnostic Imaging | 🟠 Conditional — open question whether US Core defines it or defers to others |

----

### New extensions (1 decided, 1 conditional)

| Extension | Applied to | Status |
|---|---|---|
| FHIR R5 `recorded` cross-version extension | `Procedure` (Reason Not Performed) | 🟡 Conditional — disambiguates `performed[x]` when `status` is "not-done" |
| US Core "source concept" extension | `AllergyIntolerance.criticality` | 🟡 Conditional — under exploration to avoid the lossy mapping (no "medium" concept) |

----

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

----

### Value sets (2 new, 3-4 existing updated)

| Value set | Change | Status |
|---|---|---|
| US Core Negation Reason Codes (VSAC) | :new: — extensible binding on `Immunization.statusReason`, `MedicationAdministration.statusReason`, `Procedure.statusReason` | 🟡 Proposed — adopt vs. keep the base *example* bindings |
| US Core Specimen Collection Method (VSAC) | :new: — 211 concepts, *preferred* binding on `Specimen.collection.method` | 🟡 Decided — concept list TBD with the terminology reviewers |
| Care Team Member Function (VSAC) | Add LOINC 81335-2 Patient healthcare agent | 🟡 Decided — one code vs. three still open |
| US Core ServiceRequest Category Codes | Add SNOMED CT 3457005 Patient referral (procedure) | ✅ Decided |
| US Core Clinical Note Type | Add LOINC 57133-1 Referral note |✅ Decided  |
| Personal And Legal Relationship Role Type | Binding strength *preferred* → *extensible* on `RelatedPerson.relationship` (no value set content change) | 🟠 Conditional — pending the PACIO follow-up call |


<!--
Counting notes:
- The new MedicationAdministration profile's `.statusReason` and `.effective[x]` count as part of that new profile, not as elements added to an existing profile.
- `Immunization.statusReason` is excluded: it is already Must Support and needs no profile change, only a possible binding change.
-->

<!-- **Design page (index of all strawman proposals):** [US Core V10 Design](/DSF-FPTFRvygvriuR9GJEA) · published view: <https://hackmd.io/@erichaas/SJo4QLYL-g>

This page rolls up the per-data-class strawman notes into a single view: the design decision for each
USCDI v7 data element, the USCDI definition and required vocabulary standard(s), the open issues, and the
next steps. Each section links back to its detailed design page, which is the authoritative source.

### Legend

| Symbol | Meaning |
|---|---|
| :exploding_head: | High level of effort — new profile(s) or substantial interpretation required |
| :thinking_face: | Medium level of effort — new elements and/or guidance on existing profiles |
| :slightly_smiling_face: | Low level of effort — already Must Support in US Core v9; mapping only |
| | Element is also in USCDI+ |
| :new: | New profile, value set, or element |

### References

- [ASTP USCDI website](https://isp.healthit.gov/united-states-core-data-interoperability-uscdi#uscdi-v7) · [USCDI v7 Standard (PDF)](https://isp.healthit.gov/sites/default/files/2026-07/USCDI-Version-7-Standard-Document.pdf)
- [USCDI v7: Draft (January 2026) vs. Final (July 2026)](/mHqlwgfyTnyIpIqWJADdTg)
- [USCDI v7 New Data Elements — USCDI+ Domain and USCDI+ Quality v2 Mapping](/WoGZh1mVRTek92MmpBtwlA)
- [US Core Design Principles](/r-VtK_20Rw25Vf81p5Lyvg#Design-Principles)
- Ballot/build of the strawman artifacts: <https://argonautproject.github.io/USCDIV7/>
-->

# Design Decisions by Data Class

---

## :exploding_head: Healthcare Information Attributes (NEW data class)

Data Class Design Notes link: https://hackmd.io/uwyK8MoTReG1ev02XIY-lA

---

| Data Element / USCDI Definition | Required Terminology | Design Decision |
|---|---|---|
| **Reason Not Performed**<br/>Explanation or justification provided when a planned care activity or practice guideline is not carried out.<br/>*Usage note: Included with at least procedure, immunization, and medication.* | None specified | Follow the [US Quality Core negation pattern](https://build.fhir.org/ig/HL7/fhir-us-quality-core/branches/params-table/en/negation.html) on **only** US Core Immunization, MedicationAdministration, and Procedure. **Defer** profiling other US Core Profiles <br/>• Immunization: unchanged<br/>• MedicationAdministration: See [Medications](https://hackmd.io/2654oTa6R7CNK1T-CsKvdQ)<br/>• Procedure: add `.statusReason` 0..1 MS (**new element**) and FHIR R5 `.recorded` as a cross-version extension 0..1 *Additional USCDI*<br/>|
| **Diagnostic Report Date and Time**<br/>Date and time a report containing test results or clinical interpretation was made available to providers. | None specified | **No change** — `DiagnosticReport.issued` is already Must Support in all relevant profiles. |

---

**Open issues**
- Distinguishing what is recorded as an adverse/negated event in the patient record vs. in a separate incident-reporting system.
- Binding for `.statusReason`
- Variance from US Quality Core
- Search API conformance for `patient + status`

---

**Next steps**
- Continue the detailed discussion on the fall CGP calls
- Settle the binding strength and value set, then update the USCDI mapping table.
- Align with US Quality Core

---

## :exploding_head: Adverse Events (NEW data class)

Data Class Design Notes link: https://hackmd.io/CKyBxeRYQJ6SrkYPj3zUbw

---

| Data Element / USCDI Definition | Required Terminology | Design Decision |
|---|---|---|
| **Adverse Event Condition**<br/>Change to patient condition that could be an unintended effect of clinical interventions. Examples include but are not limited to rash, fever.<br/>*Usage note: Include for at least immunizations and medications.* | SNOMED CT U.S. Edition, March 2026 Release | Instead of using the AdverseEvent Resource, map to the **existing** US Core profile that records the event — initial list: `AllergyIntolerance.reaction`, `Immunization.reaction`, Condition (problem list and encounter diagnosis), DocumentReference (clinical notes), Simple Observation, and possibly Procedure. |
| **Adverse Event Outcome**<br/>Resulting patient status or consequence following an unexpected condition change or clinical event. Examples include but are not limited to hospitalized, recovered, recovered with sequelae, and death.<br/>*Usage note: Include for at least immunizations and medications.* | None specified | Instead of using the AdverseEvent Resource, map to the **existing** US Core profile that records the outcome — initial list: Encounter (discharge disposition) |

---

**Open issues**
- The most contested class in draft USCDI v7 — opposed by Epic, Oracle Health, the EHR Association, AHA, FAH, and AQIPS.
- Many systems record these events only as unstructured notes.
- The USCDI footnote is a scope-of-exchange boundary, not an event-classification rule — the same incident can yield both USCDI clinical information and separate patient-safety work product.

---

**Next steps**
- Review and finalize the list of profiles that carry the condition and the outcome.
- Draft the guidance text explaining that adverse events surface as ordinary clinical records.
- Align with US Quality Core

---

## :exploding_head: Encounter Information — Appointment

Data Class Design Notes link: https://hackmd.io/5VD6Yd4WQ5m929CrY7X3jw

---

| Data Element / USCDI Definition | Required Terminology | Design Decision |
|---|---|---|
| **Appointment**<br/>Scheduled healthcare event for a specific date/time.<br/>*Usage note: Appointment is used to schedule and coordinate healthcare services and participation and is distinct from an Encounter.* | None specified | Add a :new: [US Core Appointment Profile](https://argonautproject.github.io/USCDIV7/StructureDefinition-us-core-appointment.html)<br/>Also add `Encounter.appointment` as a min = 0 *Additional USCDI* element to the US Core Encounter Profile. |

---

**Open issues**
- Which `Appointment.participant.actor` targets are Must Support
- `Appointment.serviceType` has an *example* binding; guidance is needed that local service-catalog concepts are the norm.
- Search API
- Author Provenance

---

**Next steps**
- Settle the the Must Support actor targets, search API, scopes, and provenance details.

---

## :exploding_head: Diagnostic Imaging — Diagnostic Imaging Reference

Data Class Design Notes link: https://hackmd.io/CNYwm7OsQ7S4EBxct2yvkg

---

| Data Element / USCDI Definition | Required Terminology | Design Decision |
|---|---|---|
| **Diagnostic Imaging Reference**<br/>The information that can be used to access a diagnostic imaging study. Examples include but are not limited to imaging study endpoint weblink, unique identifiers, and contextual information needed to retrieve a diagnostic imaging study. | None specified | Add `DiagnosticReport.media.link`, `DiagnosticReport.imagingStudy`, `DiagnosticReport.identifier`, and `ServiceRequest.identifier` as min = 0 *Additional USCDI* elements to the US Core DiagnosticReport Profile for Report and Note Exchange — `media.link` for patient-friendly content, `imagingStudy` for DICOM-capable systems, and the identifiers (for example accession numbers) for retrieval from external sources. |

---

**Open issues**
- Access: beyond pointing to [Argonaut SMART Imaging Access](https://confluence.hl7.org/spaces/AP/pages/161060067/SMART+Imaging+Access)? (new Argo project?)
- Should US Core define a lightweight [US Core ImagingStudy Profile](https://argonautproject.github.io/USCDIV7/StructureDefinition-us-core-imagingstudy.html)
- Servers choice or support all three access routes, (Vendor input pending.)
- Profile logical references (`DiagnosticReport.imagingStudy.identifier`)
- Search API requirements 
---

**Next steps**
- Resume design work to work out all the open issues and details

---

## :exploding_head: Care Team Members — Healthcare Agent

Data Class Design Notes link: https://hackmd.io/5VanJRHKQ12dIPtS-16hWQ

---

| Data Element / USCDI Definition | Required Terminology | Design Decision |
|---|---|---|
| **Healthcare Agent**<br/>Person legally authorized to make healthcare decisions on behalf of a patient when the patient is unable to do so because of an illness or injury. | None specified | Map to `CareTeam.participant.role` and `RelatedPerson.relationship`:<br/>• CareTeam: add LOINC **81335-2** (Patient healthcare agent) to VSAC's Care Team Member Function value set<br/>• RelatedPerson: use **DPOWATT** (durable power of attorney) or **HPOWATT** (healthcare power of attorney) from [Personal And Legal Relationship Role Type](https://tx.fhir.org/r4/ValueSet/2.16.840.1.113883.11.20.12.1-20251204), and point readers to the [PACIO ADI PACP guidance](https://build.fhir.org/ig/HL7/fhir-pacio-adi/pacp_guidance.html) and the [ADI Healthcare Agent Participant profile](https://build.fhir.org/ig/HL7/fhir-pacio-adi/StructureDefinition-ADI-HealthcareAgentParticipant.html) |

---

**Open issues**
- Use a single code in both the US Core CareTeam and RelatedPerson profiles vs. the three codes proposed.
- Strengthening the Personal And Legal Relationship Role Type binding from *preferred* to *extensible*.
- `Patient.contact` vs. `RelatedPerson` overlap in practice - what if any additional guidance is needed.

---

**Next steps**
- Vendors to review of currently used role codes
- Settle the code set and binding strength with Pacio team

---

## :exploding_head: Medications

Data Class Design Notes link: https://hackmd.io/2654oTa6R7CNK1T-CsKvdQ

---

| Data Element / USCDI Definition | Required Terminology | Design Decision |
|---|---|---|
| **Medication Administration**<br/>Information about the event of a patient consuming or otherwise being given a medication. Examples include but are not limited to date and time a patient ingested a tablet and who administered an injection. | None specified | Add a :new: [US Core MedicationAdministration Profile](https://argonautproject.github.io/USCDIV7/StructureDefinition-us-core-medicationadministration.html), with the same medication terminology as MedicationRequest/MedicationDispense, plus the reason-not-performed elements `.statusReason` and `.effective[x]`. Author Provenance = `MedicationAdministration.performer.actor`. |
| **Medication Dispense Quantity**<br/>Quantity of medication dispensed and requested to be dispensed. Examples include but are not limited to 480 mL of oral solution dispensed to a patient and 30 tablets ordered to be dispensed by a pharmacy. | None specified | **No change** — `MedicationRequest.dispenseRequest.quantity` and `MedicationDispense.quantity` are already Must Support. |

---

**Open issues**
- Search API
- Scope: Provider-administered events vs patient self-reported

---

**Next steps**
- Settle the search API, scopes, and provenance details.
- Edit the Medication List guidance page to account for the new profile

---

## :exploding_head: Patient Demographics / Information

Data Class Design Notes link: https://hackmd.io/VoQgkVxsQsKmBRei3Oxi4Q

---

| Data Element / USCDI Definition | Required Terminology | Design Decision |
|---|---|---|
| **Accommodation**<br/>Supports and services necessary to access care, including modifications, tools, and technologies. Examples include but are not limited to sign language interpreters, wheelchair accessibility requirements, and sensory accommodation. | None specified | Narrowed to **two Observation options**: (1) a :new: [US Core Accommodation Observation Profile](https://argonautproject.github.io/USCDIV7/StructureDefinition-us-core-observation-accommodation.html), or (2) the existing Assessments framework with the US Core Simple Observation Profile and a new "accommodation" category.  Add guidance that no terminology standard exists; free text is the real-world practice. |
| **Deceased Indicator**<br/>Indicates if the person is deceased or not. | None specified | **No change** — `Patient.deceased[x]` is already an *Additional USCDI* element. |
| **Patient Identifier**<br/>Sequence of characters assigned by an organization to refer to a patient. Examples include but are not limited to Medical Record Number. | None specified | **No change** — `Patient.identifier` is already Must Support. |

---

**Open issues**
- Accommodation conflates with disability; disability status overlaps with the USCDI/US Core SDOH assessments.
- Trade-off between a one-off Observation profile and reuse of Simple Observation within the Assessments framework.

---

**Next steps**
- Choose between the two Observation options.

---

## :exploding_head: Orders

Data Class Design Notes link: https://hackmd.io/2c5wMyJaSRORwN5F-F5CAQ

---

| Data Element / USCDI Definition | Required Terminology | Design Decision |
|---|---|---|
| **Medical Device Order**<br/>Provider-authored request for medical devices. Examples include but are not limited to pacemaker, home blood pressure monitor, therapeutic footwear, insulin infusion pump, and CPAP machine. | None specified | Add a :new: [US Core DeviceRequest Profile](https://argonautproject.github.io/USCDIV7/StructureDefinition-us-core-devicerequest.html). Search API modeled on ServiceRequest, resource-level scopes and individual-level provenance = requester. Add an implementation bullet noting ServiceRequest or MedicationRequest may be used instead depending on context. |
| **Nutrition Order**<br/>Provider-authored request for therapeutic diet, nutrition support, and nutrition to promote and maintain health. Examples include but are not limited to NPO, cardiac diet, Mediterranean diet, low FODMAP diet, whole food diet, clear liquid diet, enteral nutrition, and nutritional supplement. | None specified | Add a :new: [US Core NutritionOrder Profile](https://argonautproject.github.io/USCDIV7/StructureDefinition-us-core-nutritionorder.html). Search API modeled on ServiceRequest, resource-level scopes and individual-level provenance = orderer. |
| **Referral Order**<br/>Provider-authored request to another provider, specialist, or organization for care services. Examples include but are not limited to referral orders to a wound care specialist, housing services, and skilled nursing facility. | None specified (binding left unconstrained, as for Procedure Order) | Update the US Core ServiceRequest Profile: add category code **3457005** (Patient referral (procedure)) to the ServiceRequest category table, and state that the Referral Order `code` binding is unconstrained. |

---

**Open issues**
- `DeviceRequest.code[x]` is a choice of code or reference — which choices are Must Support? 
- DeviceRequest: terminology details
- NutritionOrder: should these be must support: 
    - `.enteral` and `.supplements`? 
    - `oralDiet.instruction`?
- NutritionOrder: terminology and search API details

---

**Next steps**
- Review binding and search API for both new profiles
- Decide on "shape" of NutritionOrder Profile.

---

## :thinking_face: Allergies and Intolerances

Data Class Design Notes link: https://hackmd.io/ziEuzkenRnqZ55h7L7vV_Q

---

| Data Element / USCDI Definition | Required Terminology | Design Decision |
|---|---|---|
| **Allergy Intolerance Criticality**<br/>Estimate of the potential clinical harm, or seriousness, of a reaction to an identified substance. | None specified | Add `AllergyIntolerance.criticality` 0..1 as an *Additional USCDI* element to the US Core AllergyIntolerance Profile. No new search parameter. |

---

**Open issues**
- Criticality vs. severity — a long-standing distinction that implementers conflate.
- The mapping into the three AllergyIntoleranceCriticality codes is **lossy**

---

**Next steps**
- Consider whether to add extension to keep source code

---

## :thinking_face: Health Status Assessments

Data Class Design Notes link: https://hackmd.io/_s1WbP-9SxGOEt8IcST0Ow

---

| Data Element / USCDI Definition | Required Terminology | Design Decision |
|---|---|---|
| **Nutrition Assessment**<br/>Assessment of a person's dietary intake. | LOINC version 2.82 | Use the existing Assessments/Observations framework and add terminology to the Screening and Assessments guidance page. Category code **75305-3** (Nutrition status); result values from SNOMED CT where applicable. |
| **Tobacco Use**<br/>Assessment of a patient's tobacco and nicotine product use behaviors, including smokeless tobacco, cigarettes, cigars, pipe tobacco, waterpipes (hookah), nicotine pouches, heated tobacco products, e-cigarettes, and other electronic nicotine delivery systems. Examples include but are not limited to duration and frequency of use, mode of consumption, and type of product used, and exclude prescribed nicotine replacement therapies. | LOINC version 2.82<br/>SNOMED CT U.S. Edition, March 2026 Release | Update and rename the *US Core Smoking Status Observation Profile* |

---

**Open issues**
- Both elements overlap functionally with the SDOH/Assessments content.
- Nutrition Assessment terminology
- Tobacco Use: rename only vs. "rip-n-replace" the Smoking Status profile with a new Profile.

---

**Next steps**
- Review *US Core Smoking Status Observation Profile* coverage gaps (mostly terminology)
- Finalize the Nutrition Assessment binding 

---

## :thinking_face: Laboratory

Data Class Design Notes link: https://hackmd.io/38xa1BZ7TjaPMao6LJHuCA

---

| Data Element / USCDI Definition | Required Terminology | Design Decision |
|---|---|---|
| **Specimen Collection Method**<br/>Technique or procedure used to obtain a specimen. Examples include but are not limited to venipuncture, swab, biopsy, aspiration, and catheter collection. | SNOMED CT U.S. Edition, March 2026 Release | Add `Specimen.collection.method` min = 0 as an *Additional USCDI* element to the US Core Specimen Profile, with a **preferred** binding to US Core value set published in VSAC; concepts TBD. |
| **Specimen Collection Date and Time**<br/>Date and time when the specimen was obtained. | None specified | Add `Specimen.collection.collected[x]` min = 0 as an *Additional USCDI* element to the US Core Specimen Profile. Note that per the base FHIR definition (`effective[x]` on the US Core Laboratory Result Observation Profile also maps to this element.) |

---

**Open issues**
- FHIR Specimen Collection Method Terminology

---

**Next steps**
- Finalize the terminology

---


## :slightly_smiling_face: Facility Information

Data Class Design Notes link: https://hackmd.io/osTHZxJpRveYPTwpDQDmVg

---

| Data Element / USCDI Definition | Required Terminology | Design Decision |
|---|---|---|
| **Facility Telecom**<br/>Phone or email contact information for a physical place of available services or resources. | ITU-T E.123 (notation for national and international telephone numbers, email addresses, and web addresses; incorporated by reference in § 170.299)<br/>ITU-T E.164 (international public telecommunication numbering plan) | **No change** — `Location.telecom` is already Must Support in the US Core Location Profile. |


**Open issues/Next steps**
- None 


---

## :slightly_smiling_face: Health Insurance Information

Data Class Design Notes link: https://hackmd.io/fTF4vhmGTneSxejvpdOuBA

---

| Data Element / USCDI Definition | Required Terminology | Design Decision |
|---|---|---|
| **Health Insurance Coverage Period**<br/>The time frame when the policy is in force. | None specified | **No change** — `Coverage.period` is already Must Support. |
| **Health Insurance Payer**<br/>Issuer of the policy. | None specified | **No change** — `Coverage.payor` is already Must Support. |
| **Health Insurance Plan**<br/>Health insurance offering or package. | None specified | **No change** — `Coverage.class:plan` is already Must Support. |
| **Health Insurance Plan Identifier**<br/>Sequence of characters used to uniquely refer to an insurance plan. | None specified | **No change** — `Coverage.class:plan.value` and `Coverage.class:plan.name` are already Must Support. |


**Open issues/Next steps**
- None (Coverage Type's new SOPT 9.2 standard is covered under [Other USCDI v7 Changes](/D5TZacmHQKqkcniD-aT-Ag).)


---

## :slightly_smiling_face: Immunizations

Data Class Design Notes link: https://hackmd.io/mcuKzClMQYCtWyODyfLJdQ

---

| Data Element / USCDI Definition | Required Terminology | Design Decision |
|---|---|---|
| **Immunization Status**<br/>State of an immunization event. Examples include but are not limited to completed, entered in error, and not done. | None specified | **No change** — `Immunization.status` is already Must Support. |
| **Immunization Record Source**<br/>Indicator that the information source is responsible for the administration of the vaccine. Examples include but are not limited to organization responsible for administering the immunization and an external record. | None specified | **No change** — `Immunization.primarySource` is already Must Support. |

**Open issues/Next steps**
- None

---


## :slightly_smiling_face: Medical Devices

Data Class Design Notes link: https://hackmd.io/Q7IK0ASkRVWrJQF4t3zJTQ

---

| Data Element / USCDI Definition | Required Terminology | Design Decision |
|---|---|---|
| **Device Type**<br/>Kind of instrument, machine, appliance, implant, software, and similar medical device. | SNOMED CT U.S. Edition, March 2026 Release | **No change** — `Device.type` is already Must Support. |

**Open issues**
- Whether to accommodate HCPCS codes (raised in the USCDI comments).


**Next steps**
- Review terminology

---

## :slightly_smiling_face: Problems

Data Class Design Notes link: https://hackmd.io/nsjWBx5WQlKQHua_xKhLEQ

---

| Data Element / USCDI Definition | Required Terminology | Design Decision |
|---|---|---|
| **Condition Status**<br/>State of a disease, problem, or condition at a given point in time. Examples include but are not limited to active, resolved, recurrence, and remission. | None specified in USCDI; US Core already applies a *required* binding to the FHIR Condition Clinical Status value set | **No change** — `Condition.clinicalStatus` is already Must Support in the US Core Condition Problems and Health Concerns Profile. |

**Open issues/Next steps**
- None 


---

## :slightly_smiling_face: Procedures

Data Class Design Notes link: https://hackmd.io/TLixyzIBRs6Wz_ulqrWUzA

---

| Data Element / USCDI Definition | Required Terminology | Design Decision |
|---|---|---|
| **Procedure Status**<br/>The status of planned or performed activity. Examples include but are not limited to in-progress, completed, and not done. | None specified | **No change** — `Procedure.status` is already Must Support. (The "not done" case is handled under [Healthcare Information Attributes](https://hackmd.io/uwyK8MoTReG1ev02XIY-lA)) |

**Open issues/Next steps**
- None


---

## :slightly_smiling_face: Clinical Notes — Referral Note

Data Class Design Notes link: https://hackmd.io/5YMuiYySSzmhFSymS2PHnA

---

| Data Element / USCDI Definition | Required Terminology | Design Decision |
|---|---|---|
| **Referral Note**<br/>Narrative summary requesting an opinion, advice, or service from a clinician. Examples include but are not limited to primary care referral to dermatology, dentistry, and acupuncture. | LOINC version 2.81<br/>At minimum: **Referral note (LOINC 57133-1)** | Add Referral note (LOINC 57133-1) to the US Core minimum Clinical Note Type value set and to the ["Common Clinical Notes" list](https://build.fhir.org/ig/HL7/US-Core/clinical-notes.html#clinical-notes) on the Clinical Notes guidance page. |

**Open issues/Next steps****
- Relationship to Referral Order (the existing Reason for Referral data element in the [Orders](https://hackmd.io/2c5wMyJaSRORwN5F-F5CAQ) class) — a narrative note vs. a ServiceRequest.


---

## :thinking_face: Other USCDI v7 Changes (renames, reclassifications, added standards)

Data Class Design Notes link: https://hackmd.io/D5TZacmHQKqkcniD-aT-Ag

---

| Change Category | Items | Design Decision |
|---|---|---|
| Reclassified | Health Concern, Indication, Performance Time | Reconcile the USCDI mapping and the profile narrative. |
| Names revised | 19 elements, including Problem, Procedure, Test, Patient Goal, and the Health Insurance cluster | Reconcile the USCDI mapping and the profile narrative. |
| Definitions revised | Author Role, Discharge Summary Note, Indication, Patient Goal, Performance Time, Problem, Procedure | Adjust usage notes if needed. |
| Standards added | Tobacco Use; Coverage Type (SOPT 9.2); Patient Goal (LOINC, SNOMED CT); Pregnancy Status (LOINC) | **No terminology changes identified.** Tobacco Use is handled in [Health Status Assessments](/_s1WbP-9SxGOEt8IcST0Ow). SOPT 9.2 is already used by the US Core Coverage Profile. Patient Goal already uses LOINC and SNOMED CT. Pregnancy Status already uses LOINC for `Observation.code`. |
| Consolidated | SDOH Goals → Patient Goal; SDOH Problems/Health Concerns → Problem; SDOH Interventions → Procedure | Review the documentation for realignment if needed. |
| Must Support elements with an existing home | Condition Status, Procedure Status, Patient Identifier, Device Type, Facility Telecom, Health Insurance cluster, Immunization Status/Source, Medication Dispense Quantity, Diagnostic Report Date, Allergy Criticality, Deceased Indicator, Specimen Collection Method | Update the USCDI mapping entries. |

---

## Next Steps

**Applies to every data class**
- [ ] Update the USCDI mapping table for all v7 elements (open on all 19 design pages).
- [ ] Reconcile the US Core narrative with the v7 renames, reclassifications, and revised definitions.

**Fall CGP calls — decisions still needed**
- [x] Healthcare Information Attributes: negation binding, search conformance, and the US Quality Core alignment now that its ballot has closed.
- [x] Adverse Events: finalize the list of profiles carrying condition and outcome, and draft the guidance.
- [ ] Diagnostic Imaging Reference: resolve the ImagingStudy profile, server choice, reference depth, and search questions (vendor input requested).
- [ ] Patient Demographics: choose between the Accommodation Observation profile and Simple Observation.
- [x] Healthcare Agent: one code vs. three, and *preferred* → *extensible*; needs PACIO subject-matter experts on the call.
- [ ] Appointment: Must Support actor targets, search parameters, scopes, and Provenance.
- [ ] Orders: binding reviews for DeviceRequest and NutritionOrder.
- [x] Health Status Assessments: Tobacco Use rename vs. deprecate, and the Nutrition Assessment LOINC choice.
- [ ] Laboratory: finalize the Specimen Collection Method concept list with the terminology reviewers.
- [ ] Allergies: decide on a source-concept extension.



