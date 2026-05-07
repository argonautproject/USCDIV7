
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

## Appointments: <span style="font-size: 2em;">:new:</span> Appointment Profile


<!-- image of summary of changes-->
![image](https://hackmd.io/_uploads/BJkQsqywbg.png)


<!-- **:new: Definition :point_down:** -->

![image](https://hackmd.io/_uploads/HyjUo9yvWl.png)


### Summary of USCDI Comments:

*This content was developed with the assistance of Claude.*

| Position | Organizations | Reasons |
|---|---|---|
| **OPPOSE** | *(no outright opposition)* | — |
| **OPPOSE / REDESIGN** | TMA (state physician society) | Defer until correlating vocabulary standard is specified |
| **MIXED / OPPOSE** | Epic (EHR vendor), UI Health (academic medical center), Providence Health (provider/health system) | Epic: too complex for a single data element — make Appointment its own data class with sub-elements (service type, provider, date, time, duration). UI Health: redundant with existing Encounter Type and Encounter Time; risks duplicative burden without unique metadata (e.g., scheduling status, future-dated intent). Providence: concern that payers will use scheduled-procedure data to redirect patients to preferred facilities, harming patient choice and continuity |
| **SUPPORT / with CHANGES** | ANI (nursing informatics), HL7 (SDO), WEDI (admin trade association), Regenstrief Institute (research/informatics), Altarum Institute (research org), csnewman (individual) | ANI: clarify boundary with Encounter Time to prevent conflation in downstream analytics. HL7: clarify scope boundary with Encounter generally. WEDI: clarify minimum data expectations; align with Referral Order/Note workflows. Regenstrief: clarify relationship once an Appointment results in an actual Encounter. Altarum: no vocabulary specified — specify one or provide guidance. csnewman: clarify what attributes are expected when exchanging appointment data |
| **SUPPORT** | Oracle Health (EHR vendor), Wolters Kluwer (clinical content vendor) | Oracle: supports inclusion as proposed. Wolters Kluwer: enriches care coordination, transitions of care, and patient-centric planning |

For a complete summary of the comments, see the Appendix below:

<!-- markdown table summary of proposal use adobe to convert to excel and then script to markdown or just copy/paste -->

## US Core Proposed Design

### Summary

DATA ELEMENT|<br/>Standards listed are required.<br/>If more than one is listed,<br/> at least one is required unless<br/>otherwise noted.<br/>Standards versions represent the most recent <br/>available at time of publication.</center>|US Core V10 Proposal
---|---|---
| **Appointment**<br>A planned healthcare event for a future date/time.<br>Usage note: Created, tracked and managed for planned participation. An appointment may be called a future encounter and may result in one or more Encounters. |  | Add a :new: US Core Appointment Profiles |
<!-- ➕ In USCDI+ -->

### CCDA Design Notes

### Issues :thinking_face:

1. US Core can address Comments targeting the individual attributes and terminology with a :new: US Core Appointment Profiles :point_down: 
4. In the USCDI Usage notes, is  ***"An appointment may be called a future encounter..." *** relevant and an important consideration in our design?
5. Would accomodations be included in appointment ( see  [Patient Demographics/Information](/VoQgkVxsQsKmBRei3Oxi4Q)  )
6. Apply [Reason-not-performed data element](/uwyK8MoTReG1ev02XIY-lA)


### Proposal

1.  Add a :new: US Core Appointment Profiles
    - Based on prior art listed below
    

  Defines the minimum constraints on the Appointment resource to support the
  US Core scheduling use cases. Establishes Must Support on identifier, status,
  serviceType, start, end, participant.type, participant.actor, participant.status.  Inherits mandatory elements, status, participant.actor, and participant.status from the FHIR Base standard.


Elements (differential)

| Element | Must Support | Add'l USCDI | Cardinality | Type | Description |
|---|:---:|:---:|---|---|---|
| `Appointment` |  |  | 0..* |  | **A booking of a healthcare event among patient(s), practitioner(s), related person(s) and/or device(s) for a specific date/time. This may result in one or more Encounter(s)**<br>A booking of a healthcare event among patient(s), practitioner(s), related person(s) and/or device(s) for a specific date/time. This may result in one or more Encounter(s). |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `identifier` | ✅ |  | 0..* | `Identifier` | **External Ids for this item**<br>This records identifiers associated with this appointment concern that are defined by business processes and/or used to refer to it when a direct URL reference to the resource itself is not appropriate (e.g. in CDA documents, or in written / printed documentation). :point_right: See note in Appendix on making identifier Must Support in US Core Profiles    :point_left:|
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `status` | ✅ |  | 1..1 | `code` | **proposed \| pending \| booked \| arrived \| fulfilled \| cancelled \| noshow \| entered-in-error \| checked-in \| waitlist**<br>The overall status of the Appointment. Each of the participants has their own participation status which indicates their involvement in the process, however this status indicates the shared status.<br><small>**Binding:** http://hl7.org/fhir/ValueSet/appointmentstatus (required)</small> |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `serviceType` | ✅ |  | 0..* | `CodeableConcept` | **The specific service that is to be performed during this appointment**<br>The specific service that is to be performed during this appointment.<br><small>**Binding:** https://profiles.ihe.net/ITI/Scheduling/ValueSet/sct-services (example) — :point_right: Value Sets are typically bound to local service catalogs, and mapping to standard vocabularies can not be expected.  :point_left:</small> |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `start` | ✅ |  | 0..1 | `instant` | **When appointment is to take place**<br>Date/Time that the appointment is to take place. |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `end` | ✅ |  | 0..1 | `instant` | **When appointment is to conclude**<br>Date/Time that the appointment is to conclude. :point_right: Base FHIR Constraint (app-2) Either [both] start and end are specified, or neither [are] :point_left:|
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `participant` |  |  | 0..* | `BackboneElement` | **Participants involved in appointment**<br>List of participants involved in the appointment. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↳ `type` | ✅   |  | 0..* | `CodeableConcept` | **Role of participant in the appointment**<br>Role of participant in the appointment.  :point_right: Base FHIR Constraint (app-1)	Either the type or actor on the participant SHALL be specified :point_left:<br><small>**Binding:** http://hl7.org/fhir/ValueSet/encounter-participant-type (extensible)</small> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↳ `actor` | ✅ |  | 1..1 | `Reference`<br><small>target: http://hl7.org/fhir/us/core/StructureDefinition/us-core-patient</small >(✅ **MustSupport** )<br><small>target: http://hl7.org/fhir/us/core/StructureDefinition/us-core-practitioner</small>( :thinking_face: **MustSupport** )<br><small>target: http://hl7.org/fhir/us/core/StructureDefinition/us-core-practitionerrole</small>( :thinking_face: **MustSupport** )<br><small>target: http://hl7.org/fhir/us/core/StructureDefinition/us-core-relatedperson</small>( :thinking_face: **MustSupport** )<br><small>target: http://hl7.org/fhir/us/core/StructureDefinition/us-core-device</small><br><small>target: http://hl7.org/fhir/StructureDefinition/HealthcareService</small><br><small>target: http://hl7.org/fhir/us/core/StructureDefinition/us-core-location</small>( :thinking_face: **MustSupport** ) | **Person, Location/HealthcareService or Device**<br>A Person, Location/HealthcareService or Device that is participating in the appointment. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↳ `status` | ✅ |  | 1..1 | `code` | **accepted \| declined \| tentative \| needs-action**<br>Participation status of the actor.<br><small>**Binding:** http://hl7.org/fhir/ValueSet/participationstatus|4.0.1` (required) — The Participation status of an appointment.</small> |

    
3.  Add `Encounter.appointment` as a min = 0 *Additional USCDI* element to the US Core Encounter Profile to support links to the appointment that scheduled the encounter.
4. Pending publication of final, apply Reason-not-performed data element.
5. Search API
    - patient (SHALL)
    - patient + date (SHOULD)
    - patient + status (SHOULD)
6. Add resource level scopes (SHALL -rs)
7. Author Provenance is system level so no individual level provenance element to support.

### Decisions

1. Add US Core Appointment Profiles
2. 
3.

### IG Updates

- [ ] USCDI Mapping Table
- [ ] Create US Core Profile
- [ ] Update Search Profiles
- [ ] Update CapabilityStatement/Search
- [ ] Update Scopes page
- [ ] Update Provenance Profile pages
<!-- - [ ] Update IPA/IPS page -->
- [ ] Update versions page
- [ ] Implementation Specific Guidance
- [ ] New Examples

---

## Appendix


### Prior Art
- [Argonaut/IHE Scheduling](https://build.fhir.org/ig/IHE/ITI.Scheduling/StructureDefinition-ihe-sched-appt.html):  IHE geared toward cross-organizational slot discovery.
- [Da Vinci CRD](https://build.fhir.org/ig/HL7/davinci-crd/en/StructureDefinition-profile-appointment-base.html): Serves as the clinical intent signal sent to the payer at booking time.
- not in IPA/IPS

### Note on Must Support Identifier Element

For US Core STU 8.0.1 (the current published version), the profiles that mark `identifier`  as **Must Support** are:

**Administrative / participant profiles**
- **US Core Patient** — `Patient.identifier`, `Patient.identifier.system`, `Patient.identifier.value` (drives the MRN search)
- **US Core Practitioner** — `Practitioner.identifier` MS, with an `NPI` slice also MS
- **US Core PractitionerRole** — `PractitionerRole.identifier` MS, with an `NPI` slice MS
- **US Core Organization** — `Organization.identifier` is a Must Support slicer; only the `NPI` slice is MS (CLIA and NAIC slices are optional)
- **US Core Location** — `Location.identifier` MS
- **US Core RelatedPerson** — `RelatedPerson.identifier` MS

**Clinical / workflow profiles**
- **US Core Encounter** — `Encounter.identifier`, `.system`, `.value` MS
- **US Core DocumentReference** — `DocumentReference.identifier` MS
- **US Core MedicationDispense** — `MedicationDispense.identifier` MS
- **US Core Coverage** — `Coverage.identifier` MS (Member ID)
- **US Core ServiceRequest** — `ServiceRequest.identifier` MS
- **US Core Implantable Device (Device)** — `Device.identifier` MS (carries the UDI)
- **US Core Specimen** — `Specimen.identifier` MS


<!-- appended-from: appointment-draft.md -->

### Appointment (Encounter Information data class) — Comment Position Summary

**Element definition:** A planned encounter between a patient and a healthcare provider for the delivery of care, at a future date and time. The Appointment element is intended to distinguish scheduled care events from completed encounters captured by existing Encounter elements.

| Position | Organizations | Reasons |
|---|---|---|
| **OPPOSE** | *(no outright opposition)* | — |
| **OPPOSE / REDESIGN** | TMA (state physician society) | Defer until correlating vocabulary standard is specified |
| **MIXED / OPPOSE** | Epic (EHR vendor), UI Health (academic medical center), Providence Health (provider/health system) | Epic: too complex for a single data element — make Appointment its own data class with sub-elements (service type, provider, date, time, duration). UI Health: redundant with existing Encounter Type and Encounter Time; risks duplicative burden without unique metadata (e.g., scheduling status, future-dated intent). Providence: concern that payers will use scheduled-procedure data to redirect patients to preferred facilities, harming patient choice and continuity |
| **SUPPORT / with CHANGES** | ANI (nursing informatics), HL7 (SDO), WEDI (admin trade association), Regenstrief Institute (research/informatics), Altarum Institute (research org), csnewman (individual) | ANI: clarify boundary with Encounter Time to prevent conflation in downstream analytics. HL7: clarify scope boundary with Encounter generally. WEDI: clarify minimum data expectations; align with Referral Order/Note workflows. Regenstrief: clarify relationship once an Appointment results in an actual Encounter. Altarum: no vocabulary specified — specify one or provide guidance. csnewman: clarify what attributes are expected when exchanging appointment data |
| **SUPPORT** | Oracle Health (EHR vendor), Wolters Kluwer (clinical content vendor) | Oracle: supports inclusion as proposed. Wolters Kluwer: enriches care coordination, transitions of care, and patient-centric planning |

**Comments grouped by position:**

**Strongly supportive**
- **Oracle Health** [EHR vendor] — "We support the inclusion of the proposed Appointment data element." No qualifications. Notable contrast with Oracle's redesign concerns about Healthcare Agent and Diagnostic Imaging Reference.
- **Wolters Kluwer** [clinical content vendor] — Cites Appointment alongside Healthcare Agent, Accommodation, and Deceased Indicator as elements that "enrich the context required for efficient, safe, and equitable care delivery" and improve interoperability around transitions of care, referral workflows, and patient-centric planning.

**Supportive with refinements**
- **Alliance for Nursing Informatics / ANI** [nursing informatics professional society] — Strongly supports. Argues the distinction between a planned appointment and a completed encounter is "clinically and operationally significant" — the precise information gap that limits nurses, care managers, and transitional care teams from placing individual care events in longitudinal context. Notes health-equity value: patterns of missed or rescheduled appointments, when standardized and interoperable, signal SDOH barriers (transportation access, work schedule constraints, childcare) that enable nursing-led upstream outreach. Recommends implementation guidance clarify the distinction between Appointment and the existing Encounter Time element to prevent conflation of scheduled vs. completed care events in downstream data models and analytics.
- **HL7** [SDO] — Lists Encounter vs. Appointment among scope-boundary relationships ONC should clarify in v7, alongside Device Type vs. UDI, Procedures vs. Orders, and Events vs. Outcomes.
- **WEDI** [administrative/transactions trade association] — Cites Appointment among the v7 additions that "could materially reduce administrative burden and improve interoperability." Recommends ONC clarify minimum data expectations and encourage consistent workflows ("scheduling is foundational to operational interoperability and patient access, but 'appointment' can be implemented inconsistently without clear guidance"). Wants explicit linkage to Referral Order, Referral Note, and Encounter to support downstream coordination.
- **Regenstrief Institute** [research/informatics institute] — Supports inclusion. Notes no vocabulary specified; useful for care coordination and scheduling interoperability. Recommendation: clarify relationship to Encounter elements once an Appointment results in an actual Encounter — implementers will need explicit guidance on transition semantics.
- **Altarum Institute** [health-services research org] — Lists Appointment among elements without applicable vocabulary standards (alongside Adverse Event Outcome, Allergy Intolerance Criticality, Specimen Collection Method, and Healthcare Agent). Frames as "moderate risk" of inconsistent implementation. Recommends ASTP/ONC specify vocabulary standards before finalizing v7, or at minimum provide implementation guidance identifying commonly used code systems.
- **csnewman** [unaffiliated individual] — Asks for explicit clarification of expectations: a future appointment shares many attributes with a previous encounter (time, location, type). Does USCDI expect those attributes when exchanging appointment data? Does the Appointment data element simply indicate the encounter is in the future? Are there unique attributes for an Appointment that aren't associated with a past Encounter?

**Mixed / oppose**
- **Epic** [EHR vendor] — Identifies Appointment among the v7 elements with definitions lacking sufficient specificity (alongside Medication Administration and Nutrition Assessment) — risks inconsistent implementation across the industry. Two specific recommendations: (1) **Establish Appointment as its own data class, not a single element.** Treating it as a single element doesn't account for the inherent complexity of appointment data. ONC should specify constituent sub-elements (service type — e.g., follow-up, physical; provider; date; time; duration) and assess each one's maturity before inclusion. (2) **Acknowledge that scope varies by exchange context.** A FHIR-based API query may legitimately return historical appointments, while a transition-of-care document may warrant only future or pending ones. ONC should recognize this variation rather than prescribing a single approach. Epic's posture is constructive but explicit: "address significant definitional and structural concerns prior to finalizing."
- **UI Health (University of Illinois Health)** [academic medical center] — "Concern Regarding Redundancy." Argues that as currently proposed, Appointment lacks the discrete specificity required for effective exchange. Since Encounter Type and Encounter Time are already established elements, an Appointment element must be defined with unique metadata (e.g., specific scheduling status or future-dated intent). Without this clarity, it risks being a duplicative burden with negligible clinical utility.
- **Providence Health (nicole.toth@providence.org)** [provider / health system] — Distinct concern not raised by other commenters: with Appointment data exposed via USCDI, **payers may use scheduled-procedure information to redirect patients to their preferred facilities and providers**, impacting patient choice and continuity of care. Recognizes the value of enhanced transparency but believes the possibility warrants further stakeholder discussion before finalization.

**Oppose / redesign**
- **TMA (Texas Medical Association)** [state physician professional society] — Lists Appointment among 15 elements ONC should not adopt until each has a correlating vocabulary standard.

**Summary of Comments:** Appointment is among the more cleanly supported v7 additions on the surface — eight of the eleven substantive commenters take a supportive position — but the reasoning beneath the support reveals consistent unease about scope and redundancy. Three concerns recur. **Element vs. data class** is the most structural: Epic [EHR vendor] argues the proposal treats a complex multi-attribute concept (service type, provider, date, time, duration) as a single data element and recommends elevating it to its own data class, sub-element by sub-element. **Boundary with existing Encounter elements** is the most common: ANI [nursing informatics professional society], HL7 [SDO], Regenstrief [research/informatics institute], UI Health [academic medical center], and csnewman [individual] all ask ONC to clarify the relationship between Appointment and the existing Encounter Type / Encounter Time elements — UI Health goes furthest, framing Appointment as redundant without unique metadata distinguishing scheduled-future-intent from a past encounter. **Vocabulary** comes from Altarum [research org] and TMA [state physician society], who flag the absence of an applicable vocabulary standard; TMA goes further and would defer the element entirely. A unique concern comes from Providence Health [provider]: **payer behavioral risk** — that exposing scheduled-procedure data through USCDI's API channel will give payers a tool to redirect patients to in-network or preferred-network facilities ahead of the appointment, undermining patient choice and continuity of care. This is the only commenter raising a competitive/business-model concern about the element rather than a technical one. The supporting voices (ANI, WEDI, Wolters Kluwer, Oracle Health) emphasize care-coordination and administrative-burden-reduction value: appointment visibility supports nurse navigators, transitional care teams, referral workflows, value-based care, and SDOH-driven outreach. WEDI [administrative/transactions trade association] explicitly bundles Appointment with Referral Order, Referral Note, Reason Not Performed, Diagnostic Imaging Reference, and Patient Identifier as the v7 additions most likely to materially reduce administrative burden.

**Notably absent:** AHA, FAH, AHIP, AMA, AMIA, NCQA, AQIPS, EHR Association, MEDITECH, Allina Health, FDA, CDC, APHL, CSTE, AHIMA, SHIELD, AHRQ, CARIN Alliance, and Vega Health are all silent on Appointment despite filing v7 comment letters. The absence of payer voices (AHIP, AHA on the payer-relations question, CARIN) is striking given Providence's surfaced concern about payer use of scheduled-procedure data. The EHR Association's silence is also notable since their member companies (Epic, Oracle Health, MEDITECH) take divergent positions individually.

