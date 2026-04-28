
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

## Adverse Events: DEFER Pending final release of USCDI 7


<!-- image of summary of changes-->
![image](https://hackmd.io/_uploads/B1VkaKRIbg.png)


<!-- **:new: Definition :point_down:** -->

![image](https://hackmd.io/_uploads/H1NpnK0LWg.png)

<!-- markdown table summary of proposal use adobe to convert to excel and then script to markdown or just copy/paste -->

### Summary of USCDI Comments:

*This content was developed with the assistance of Claude.*

The Adverse Events class is the most contested element in Draft USCDI v7. The opposition includes both major EHR vendors (Epic, Oracle Health), the EHR Association [vendor trade association], major hospital trade associations (AHA, FAH), and the patient safety organization trade association (AQIPS).

| Position | Organizations | Reasons |
|---|---|---|
| **OPPOSE** | Epic (EHR vendor), Oracle Health (EHR vendor), AHA (hospital trade association), FAH (hospital trade association), AQIPS (patient safety/PSO trade association) | Adverse events not captured as such in routine EHR workflow; classification requires root cause analysis performed in separate risk-management/PSO systems; conflicts with Patient Safety and Quality Improvement Act privilege protections for Patient Safety Work Product; categorically excluded from EHI under 45 CFR 164.501; would duplicate existing FDA pharmacovigilance and PSO reporting pathways; FAH and AQIPS argue any inclusion requires formal notice-and-comment rulemaking, not a USCDI update |
| **OPPOSE / REDESIGN** | EHR Association (vendor trade association), TMA (state physician professional society) | Defer Adverse Event Outcome until industry develops consistent documentation standards, FHIR profiles mature, and a vocabulary standard is specified; data often lives outside EHRs in clinical trial management platforms |
| **MIXED / OPPOSE** | Vizient (GPO / healthcare performance improvement), SHIELD (lab/diagnostic data standards coalition), J.P. Systems / Jay Lyle (individual informatics consultant) | Vizient: Adverse Event Outcome lacks vocabulary — recommends ICH E2B(R3); SHIELD: scope unclear (CLIA LDT reporting vs. FDA post-market vs. NIH trials?); Lyle: term ambiguous between pharmacovigilance meaning (any negative effect) and patient-care meaning (care-provision error) — must pick one or split |
| **SUPPORT / with CHANGES** | AMA (physician professional society), AMIA (physician informatics professional society), Regenstrief Institute (research/informatics institute), Altarum Institute (health-services research org), UI Health (academic medical center), Wolters Kluwer (clinical content vendor), csnewman (unaffiliated individual) | AMA: clarify boundaries with complication/side effect/medical error/sentinel event; AMIA: tighten definition by replacing "could" with "deemed"; Regenstrief: specify Outcome vocabulary (SNOMED CT or HL7 FHIR AdverseEvent outcome value set), clarify boundary with Reaction element in Allergies and Intolerances; Altarum: add MedDRA usage note for VAERS/FAERS alignment, specify Outcome vocabulary; UI Health: add Actuality/Timing element to distinguish actual events from near-misses, map Outcome to SNOMED CT or ICD-10-CM; Wolters Kluwer: also add Adverse Event Date for analytics and surveillance; csnewman: add actuality and date elements |
| **SUPPORT** | ANI (nursing informatics professional society), CMS-CCSQ (federal agency / payer), SNOMED International (SDO — terminology) | ANI: long-overdue formal recognition of nursing's role in patient safety surveillance; standardization will let documentation follow patients across care transitions; recommends extending vocabulary to nursing-sensitive categories (falls, pressure injuries, medication errors); CMS-CCSQ: applauds inclusion of both elements; SNOMED International: supports SNOMED CT designation, recommends elevating it from "applicable" to "required" and naming it as the preferred terminology for Outcome |

**Notably absent:** FDA, CDC, APHL, CSTE (all active on public-health reporting elements but silent here), patient advocacy groups, AHIP (commented on USCDI v7 but didn't address Adverse Events), MEDITECH and other smaller EHR vendors.

For a complete summary of the comments, see the Appendix below:


## US Core Proposed Design

#### Summary

DATA ELEMENT|<center>APPLICABLE VOCABULARY STANDARD(S)<br/>Standards listed are required.<br/>If more than one is listed,<br/> at least one is required unless<br/>otherwise noted.<br/>Standards versions represent the most recent <br/>available at time of publication.</center>|US Core V10 Proposal
---|---|---
| **Adverse Event ➕**<br>A change to patient condition that could be an unintended effect of clinical interventions. | • SNOMED Clinical Terms® (SNOMED CT®)<br>U.S. Edition, September 2025 Release | 🆕 US Core AdverseEvent Profile with `AdverseEvent.event` Must Support 0..1 with *extensible* binding to FHIR R6 or equivalent [AdverseEvent Type](https://hl7.org/fhir/6.0.0-ballot4/valueset-adverse-event-type.html) |
| **Adverse Event Outcome**<br>Result or impact of an adverse event.<br>Examples include but are not limited to **hospitalized**, *recovered*, *recovered with sequelae*, and *death*. |  |🆕 US Core AdverseEvent Profile with `AdverseEvent.outcome` Must Support 0..1 with *required* binding to FHIR R4 [AdverseEventOutcome](https://hl7.org/fhir/R4/valueset-adverse-event-outcome.html) (*resolved*, **recovering**, **ongoing**, *resolvedWithSequelae*, *fatal*, unknown) |

➕ In USCDI+

### CCDA Design Notes

### Issues :thinking_face:

1.  AdverseEvent is FMM = 0 FHIR R4, part of FHIR R6
2.  Implementer Support?
3.  Duplication/Conflation with `Immunization.reaction`
4.  Terminology for outcomes. ( see FHIR R4 required vs example in FHIR R6)
5.  Outcome is 0..1 in FHIR R4 vs 0..* in FHIR R6

### Proposal

1.  🆕 US Core AdverseEvent Profile
2.  `AdverseEvent.event` Must Support 0..1 with *extensible* binding to FHIR R6 or equivalent [AdverseEvent Type](https://hl7.org/fhir/6.0.0-ballot4/valueset-adverse-event-type.html)
3.  `AdverseEvent.outcome` Must Support 0..1 with *required* binding to FHIR R4 [AdverseEventOutcome](https://hl7.org/fhir/R4/valueset-adverse-event-outcome.html) (*resolved*, **recovering**, **ongoing**, *resolvedWithSequelae*, *fatal*, unknown)
4. Other Mandatory and Must Support elements: Must Support elements: `actuality (m), category, subject (m), date, recordedDate, resultingCondition, suspectEntity`  (m = mandatory in base)
6. Search Parameters: _id, patient, date, category, event
7. Resource level scope

---

## Decisions

1. Because the AdverseEvents Data Class is the most contested, wait for the final USCDI V7 to be released, in case it is modified or removed.


<!-- ### IG Updates

- [ ] USCDI Mapping Table
  [ ] Update US Core Profile
- [ ] Update Introduction
- [ ] Implementation Specific Guidance
- [ ] New Example(s) pending final review of decisions
- [ ] Update Example(s) pending final review of decisions -->

---

## Appendix

### Prior Art

1. hl7.fhir.us.qicore
2. fhir.hrsa.uds-plus


### Adverse Events (data class) Comments Summary

**Class definition:** Unintended effects associated with clinical interventions. Comprises two new data elements: Adverse Event and Adverse Event Outcome. One of two new data classes introduced in Draft USCDI v7.

**Comments grouped by position:**

**Strongly supportive**
- **Alliance for Nursing Informatics / ANI** [clinical specialty professional society — nursing informatics] — Frames the class as long-overdue formal recognition of nursing's role in patient safety surveillance. Argues the absence of a standardized class has undermined cross-organizational safety exchange, particularly during care transitions where nursing leads handoffs. Asks ONC to extend vocabulary beyond SNOMED CT to nursing-sensitive categories (patient falls, pressure injury staging, medication errors) and to provide implementation guidance favoring point-of-care capture over siloed safety reporting systems.
- **CMS-CCSQ** [federal agency / payer] — Submitted parallel "applauds inclusion" comments on both Adverse Event and Adverse Event Outcome elements.
- **SNOMED International** [SDO — terminology] — Two comments. Supports SNOMED CT designation for Adverse Event and recommends elevating it from "applicable" to "required." Recommends SNOMED CT as the preferred terminology for Adverse Event Outcome, which currently lacks a vocabulary.
- **Wolters Kluwer** [clinical content vendor] — Strongly supports the class as a critical advancement for patient safety, care quality, and surveillance. Aligns the proposal with broader public-health goals. **Urges ONC to also add Adverse Event Date** (a Level 2 element they consider worthy of v7 inclusion) for analytics, clinical decision support, and cross-setting continuity.

**Supportive with refinements**
- **American Medical Association / AMA** [physician professional society] — Supports the class for patient safety, post-market surveillance, and learning health system functions. Recommends ONC (1) provide clear guidance distinguishing adverse event from related concepts (complication, side effect, medical error, sentinel event), (2) clarify the relationship between event, outcome, severity, and attribution including whether causality is represented, and (3) align examples and recommended vocabularies with widely implemented documentation patterns to avoid new burden.
- **AMIA** [physician informatics professional society] — Raised concerns about clarity and consistency of terminology. Specifically recommends replacing "could" with "deemed" in the Adverse Event definition, so it reads "A change to patient condition that was deemed to be an unintended effect of clinical interventions" — tightening the threshold for what counts as an adverse event.
- **Regenstrief Institute** [research/informatics institute] — "Welcomes" the class as filling a long-standing gap. Two observations: (1) Adverse Event Outcome lacks a vocabulary; given the example values (hospitalized, recovered, recovered with sequelae, death) align with MedDRA/FDA categories, recommends specifying SNOMED CT or the HL7 FHIR AdverseEvent outcome value set to prevent free-text drift. (2) Flags potential overlap with the existing Reaction element in Allergies and Intolerances class; asks ONC to provide explicit boundary guidance ("Allergies/Intolerances captures known patient sensitivities, while Adverse Events captures incident-level occurrences linked to specific clinical interventions").
- **Altarum Institute** [health-services research org] — Two adverse-event recommendations. (1) Adverse Event vocabulary alignment — while SNOMED CT is appropriate for clinical characterization, primary public-health adverse-event reporting systems (VAERS, FAERS/MedWatch) use MedDRA. Recommends a usage note acknowledging MedDRA as a commonly used vocabulary for adverse-event reporting workflows. (2) Adverse Event Outcome vocabulary gap — recommends specifying the HL7 FHIR AdverseEvent outcome value set or a SNOMED CT subset.
- **UI Health (University of Illinois Health)** [academic medical center / provider] — "Support with Recommendation." Recommends adding an "Adverse Event Actuality" or "Timing" element to distinguish actual events from near-misses for proactive safety protocols and quality benchmarking. Also asks that Adverse Event Outcome be explicitly mapped to SNOMED CT or ICD-10-CM.

**Scope clarification / neutral**
- **SHIELD (Strengthening Health through Interoperability and Effective Laboratory Data)** [lab/diagnostic data standards coalition] — Asks ASTP/ONC to specify which adverse-event types are in scope: CLIA-certified laboratory reporting on Laboratory Developed Tests (LDTs), FDA post-market surveillance, NIH clinical trials, or some combination.
- **Jay Lyle / J.P. Systems** [individual informatics consultant] — Flags that "adverse event" is ambiguous between two distinct use cases. **Pharmacovigilance**: any negative effect on the patient, reported regardless of perceived cause. **Patient care**: a care-provision error, reported whether the patient was harmed or not. Recommends ASTP/ONC choose one explicitly or split the concept.
- **csnewman** [unaffiliated individual] — Suggests two additional elements: (1) "actuality" to distinguish actual events from potential/avoided events (near-misses), and (2) a date element for event timing.
- **Vizient** [GPO / healthcare performance improvement company] — On Adverse Event Outcome: notes the missing vocabulary standard and recommends incorporating ICH E2B(R3), already in widespread hospital use for outcome reporting.

**Defer**
- **EHR Association** [vendor trade association] — Concerns about inconsistent definitions across systems, varying scope (clinical care vs. research), and frequent capture in non-EHR systems (clinical trial management platforms). Recommends ONC defer Adverse Event Outcome until industry develops more consistent documentation standards, FHIR profiles mature, and clear scope guidance is established.
- **Texas Medical Association / TMA** [state physician professional society] — Lists Adverse Event Outcome among 15 elements ONC should not adopt until each has a correlating vocabulary standard.

**Oppose**
- **Epic** [EHR vendor] — **Strongly discourages** ONC from creating the data class. Argument: (1) In routine clinical care, adverse events are not a mature concept for discrete documentation or exchange, are not consistently captured as "adverse events" across EHRs, and lack a standardized vocabulary; where they exist they're already captured through Problems, Encounter Information, and Clinical Notes. (2) In clinical research, adverse events are documented in specialized workflows; not all care settings (especially smaller and rural facilities) participate in trials, so the use case fails USCDI's intent as a universally applicable dataset. Recommends non-adoption.
- **Oracle Health** [EHR vendor] — Urges ONC not to adopt either element. EHRs document clinical events but do not classify them as adverse events or determine ultimate outcomes; that work happens in separate risk management systems. Originating providers may not even know an adverse event occurred (e.g., delayed immunization reaction). Offers an alternative: amend USCDI certification to apply only to the subset of data each HIT system is designed to capture, allowing risk management systems to be certified separately to the adverse event elements.
- **American Hospital Association / AHA** [provider trade association] — Urges non-adoption. Cites unclear definitions, misalignment with clinical workflows (events typically aren't labeled "adverse events" at point of documentation; root cause analysis happens outside the EHR), and conflict with the Patient Safety and Quality Improvement Act's privilege framework for Patient Safety Work Product. Suggests ONC issue an RFI on better tracking adverse-event patterns instead.
- **Federation of American Hospitals / FAH** [hospital trade association] — The most extensive legal opposition. Same workflow argument as AHA, plus a detailed Patient Safety Act analysis: records created for patient safety events and reported to a Patient Safety Organization are privileged and confidential Patient Safety Work Product when created within a Patient Safety Evaluation System; PSWP is generally not part of a HIPAA designated record set. Argues the proposal would duplicate established federal pathways for FDA-regulated product reporting, and that Congress already authorized a comprehensive learning channel through PSOs (reinforced by CMS through the IQR Patient Safety Structural Measure, with a 25% Medicare market-basket penalty for non-reporting). **Insists any move forward should not proceed via USCDI alone — only through formal notice-and-comment rulemaking** that addresses the PSQIA privilege regime, the HIPAA designated record set boundary, and EHI definition.
- **Alliance for Quality Improvement and Patient Safety / AQIPS** [patient safety/PSO trade association] — Three submissions. The Adverse Events data class and elements are categorically excluded from EHI under the Patient Safety Act because adverse-event determination requires patient safety activities outside the medical record; PSWP is excluded from the designated record set under 45 CFR 164.501. Failure to share is therefore not information blocking. Defining these as EHI would conflict with HIPAA, the Patient Safety Act, and the APA. Distinguishes appropriately from CDC NHSN HAI reporting, which does draw from EHR data.

**Summary of Comments:** The Adverse Events class is the most contested element in Draft USCDI v7. The opposition camp — both major EHR vendors (Epic, Oracle Health), the EHR Association [vendor trade association], both major hospital trade associations (AHA, FAH), and the patient safety organization trade association (AQIPS) — converges on three concerns: (1) routine EHR documentation doesn't classify events as "adverse" at point of capture; (2) determination requires root cause analysis performed in separate systems; and (3) bringing this content into EHI risks collision with the Patient Safety Act's privilege regime. Epic and Oracle Health frame the issue as workflow and capture mismatch; AHA, FAH, and AQIPS frame it as legal preemption requiring formal rulemaking. The supporters — ANI [nursing informatics professional society], CMS-CCSQ [federal agency/payer], SNOMED International [SDO], AMA [physician professional society], AMIA [physician informatics professional society], Regenstrief and Altarum [research/informatics institutes], UI Health [academic medical center], Wolters Kluwer [clinical content vendor], and CSTE-adjacent public health voices — generally agree the class fills a real interoperability gap but converge on a shared technical concern: **Adverse Event Outcome lacks a vocabulary standard** and will degrade to free text without one. Recommended vocabularies vary (SNOMED CT, ICD-10-CM, MedDRA, HL7 FHIR AdverseEvent outcome value set, ICH E2B(R3)). A second cluster of supportive feedback wants additional elements: an Actuality flag (UI Health, csnewman) to distinguish actual from near-miss events, an Adverse Event Date (Wolters Kluwer, csnewman) for temporal context, and explicit boundary guidance with the existing Reaction element in Allergies and Intolerances (Regenstrief). The "defer until ready" position (EHR Association [vendor trade association], TMA [physician professional society]) maps mainly to Adverse Event Outcome's missing vocabulary. Vizient [GPO/healthcare performance improvement company] occupies a middle position — recommends ICH E2B(R3) as the standard. Definitional ambiguity between pharmacovigilance and patient-care meanings (Lyle [individual informatics consultant], AMIA, AMA) is a cross-cutting concern not yet resolved in the draft.

Notably absent from this class debate: the **FDA** (despite being the original submitter via Mitra Rocca); the **CDC**, **APHL**, and **CSTE** (all active commenters elsewhere — particularly on public-health reporting elements — but silent on this class's framing); **patient advocacy groups** of any kind; **payer trade associations** other than CMS-CCSQ (AHIP submitted a substantive letter but didn't address Adverse Events at all); and **MEDITECH** and other smaller EHR vendors despite Epic's and Oracle Health's strong stances.

---



