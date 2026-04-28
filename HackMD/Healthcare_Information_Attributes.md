
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

## Healthcare Information Attributes: Changes to US Core Profiles


<!-- image of summary of changes-->
![image](https://hackmd.io/_uploads/Hk1BVoywZx.png)

<!-- **:new: Definition :point_down:** -->

![image](https://hackmd.io/_uploads/Sy3v4sJDbl.png)

### Summary of USCDI Comments:

*This content was developed with the assistance of Claude.*

### Reason Not Performed

| Position | Organizations | Reasons |
|---|---|---|
| **OPPOSE** | Epic (EHR vendor) | Only mature in narrow quality-measurement context; no generic capability exists; quality-measurement programs are a better vehicle than USCDI |
| **OPPOSE / REDESIGN** | TMA (state physician society) | Defer until correlating vocabulary standard is specified |
| **MIXED / OPPOSE** | AHA (hospital trade association), FAH (hospital trade association), Allina Health (provider/health system), Oracle Health (EHR vendor) | AHA & FAH: reasons often live in ancillary lab/imaging systems, not the EHR; risks noise without scope guidance; AHA also asks ONC to address insurance-coverage denials. Allina: patient-driven factors don't fit a discrete codified field; clarify clinician-driven vs. patient-driven scope. Oracle: misplaced in Healthcare Information Attributes — relocate to Clinical Tests, Diagnostic Imaging, Laboratory, Medications, Orders, Procedures, Vital Signs, or scope it in the definition |
| **SUPPORT / with CHANGES** | ANI (nursing informatics), HL7 (SDO), SHIELD (lab data standards coalition), APHL (public health labs association), WEDI (admin trade association), Regenstrief Institute (research/informatics), Wolters Kluwer (clinical content vendor), Vizient (GPO/performance improvement), david_rocha (individual) | ANI: explicit vocabulary specification with nursing-specific reasons. HL7/SHIELD/APHL: clarify scope to cover order cancellations and specimen-reject reasons; possibly DME, nutrition, PT/OT/ST. WEDI: structured category guidance, burden-reduction note encouraging reuse of existing artifacts, clarify association rules. Regenstrief: provide implementation guidance linking the element to the procedure/immunization/medication it modifies. Wolters Kluwer: also add Negation Rationale to Medications class. Vizient: support as-is. david_rocha: require SNOMED CT (Procedure/Vaccine/Medication declined codes) for CMS QPP alignment |
| **SUPPORT** | UI Health (academic medical center), PACIO Project (post-acute care interop community) | UI Health: directly impacts eCQMs (VTE-1, VTE-2); standardization enables automated patient exclusions and eliminates manual chart abstraction. PACIO: substantiates treatment decisions inconsistent with documented advance directives |

### Diagnostic Report Date

| Position | Organizations | Reasons |
|---|---|---|
| **OPPOSE** | *(no outright opposition)* | — |
| **OPPOSE / REDESIGN** | TMA (state physician society) | Defer until correlating vocabulary standard is specified |
| **MIXED / OPPOSE** | FAH (hospital trade association), Oracle Health (EHR vendor), EHR Association (vendor trade association), LisaRNelsonRI (standards consultant) | FAH: diagnostic reports already carry multiple timestamps — unclear what gap this fills, risks duplicative confusion. Oracle: misplaced in Healthcare Information Attributes; relocate to Laboratory and Diagnostic Imaging. EHR Association: more appropriate for specific clinical contexts (lab, imaging, procedures), not universally across USCDI. Nelson: generalize and rename to "Document Creation Date" so it applies to notes, discharge summaries, EOBs, and other document types — not just diagnostic reports |
| **SUPPORT / with CHANGES** | ACLA (clinical lab trade association), HL7 (SDO), SHIELD (lab data standards coalition), APHL (public health labs association), CDC (federal agency/public health), Regenstrief Institute (research/informatics) | ACLA, HL7, SHIELD, APHL: rename to "Diagnostic Report Date/Time" — date alone is insufficient for many use cases. HL7/SHIELD/APHL/CDC: add usage note clarifying it's an administrative date updated with each version (preliminary, final, corrected, amended, addended) and timestamp preserved for each version; APHL adds that it's distinct from the date/time providing temporal context for the patient's health. Regenstrief: provide FHIR implementation guidance on how this attribute links to its parent DiagnosticReport resource — isolated exchange is clinically meaningless |
| **SUPPORT** | *(no clean support — every supporter wants refinements)* | — |

For a complete summary of the comments, see the Appendix below:

<!-- markdown table summary of proposal use adobe to convert to excel and then script to markdown or just copy/paste -->

## US Core Proposed Design

### Summary

DATA ELEMENT|<br/>Standards listed are required.<br/>If more than one is listed,<br/> at least one is required unless<br/>otherwise noted.<br/>Standards versions represent the most recent <br/>available at time of publication.</center>|US Core V10 Proposal
---|---|---
| **Reason Not Performed ➕**<br>Explanation or justification provided when an order or practice guideline is not carried out.<br>Usage note: Should be included with a procedure, immunization, and medication. |  | See Proposals Below |
| **Diagnostic Report Date ➕**<br>Date and time a report containing test results or clinical interpretation was made available to providers.|  | **No Change**: `DiagnosticReport.issued` already a US Core *Must Support* element in all relevant profiles  |
<!--
| **Performance Time ➕**<br>Time and/or date a care activity is performed.<br>Examples include but are not limited to vaccine and medication administration times, surgery start time, time ultrasound performed, and laboratory specimen collection time. |  | **No Change**:  Is already a US Core *Must Support* element in all relevant profiles (see appendix below)
| **Indication**<br>Sign, symptom, or medical condition that is the reason for a care activity.<br>Usage note: Indication may be included with a procedure, medication, and an order. | •        SNOMED Clinical Terms (SNOMED CT) U.S. Edition, September 2025 Release<br>•        International Classification of Diseases, Tenth Revision, Clinical Modification<br>(ICD-10-CM) 2026 |  | -->

➕ In USCDI+

### CCDA Design Notes

### Issues

1. See choices in Observation Proposal below
2. See choices in MedicationDispense proposal below
3. See choices in DiagnosticReport proposal
### Proposal

1. All US Core Observation Profiles: `Observation.dataAbsentReason` min = 0 *Additional USCDI* vs [Event status reason extension](https://hl7.org/fhir/extensions/StructureDefinition-event-statusReason.html) or [Workflow Status Reason Extension](https://build.fhir.org/ig/HL7/fhir-extensions/StructureDefinition-workflow-statusReason.html)
1. US Core CarePlan Profile: [Workflow Status Reason Extension](https://build.fhir.org/ig/HL7/fhir-extensions/StructureDefinition-workflow-statusReason.html)
1. US Core DiagnosticReport Profile for Laboratory Results Reporting: [Event status reason extension](https://hl7.org/fhir/extensions/StructureDefinition-event-statusReason.html) or [Workflow Status Reason Extension](https://build.fhir.org/ig/HL7/fhir-extensions/StructureDefinition-workflow-statusReason.html) min = 0 *Additional USCDI*
1. US Core DiagnosticReport Profile for Report and Note Exchange:[Event status reason extension](https://hl7.org/fhir/extensions/StructureDefinition-event-statusReason.html) or [Workflow Status Reason Extension](https://build.fhir.org/ig/HL7/fhir-extensions/StructureDefinition-workflow-statusReason.html) min = 0 *Additional USCDI*
1. US Core Goal Profile: `Goal.statusReason` FHIR R5 Cross Version extension min=0 *Additional USCDI*
1. US Core Immunization Profile: `Immunization.statusReason` min = 0  *Additional USCDI*
1. US Core MedicationDispense Profile: `MedicationDispense.statusReason[x]` or  `MedicationDispense.statusReasonCodeableConcept` min = 0  *Additional USCDI*
1. US Core MedicationRequest Profile: `MedicationRequest.statusReason` min = 0  *Additional USCDI*
1. US Core Procedure Profile: `Procedure.statusReason` min = 0  *Additional USCDI*
1. US Core QuestionnaireResponse Profile: [Workflow Status Reason Extension](https://build.fhir.org/ig/HL7/fhir-extensions/StructureDefinition-workflow-statusReason.html) min = 0  *Additional USCDI*
1. US Core ServiceRequest Profile: [Workflow Status Reason Extension](https://build.fhir.org/ig/HL7/fhir-extensions/StructureDefinition-workflow-statusReason.html) min = 0  *Additional USCDI*

### Decisions

1.
2.
3.

### IG Updates

- [ ] USCDI Mapping Table
<!-- - [ ] Update US Core Profile
- [ ] Update Introduction
- [ ] Implementation Specific Guidance
- [ ] New Example(s) pending final review of decisions
- [ ] Update Example(s) pending final review of decisions -->

---

## Appendix

### Performance Time Elements

List of all *Must Support* performance times elements in US Core Version 9.0.0-ballot for each relevant clinical event profile:


- All US Core Observation Profiles (not verified !): `Observation.effective[x]`
- US Core ADI DocumentReference Profile:?
- US Core CarePlan Profile: ?
- US Core DiagnosticReport Profile for Laboratory Results Reporting: `DiagnosticReport.effective[x]`
- US Core DiagnosticReport Profile for Report and Note Exchange: `DiagnosticReport.effective[x]`
- US Core DocumentReference Profile: `DocumentReference.context.period`
- US Core Goal Profile: `Goal.start[x]`
- US Core Immunization Profile: `Immunization.occurance[x]`
- US Core MedicationDispense Profile: `MedicationDispense.whenHandedOver`
- US Core MedicationRequest Profile: `MedicationRequest.authoredOn`
- US Core Procedure Profile: `Procedure.performed[x]`
- US Core QuestionnaireResponse Profile: `QuestionnaireResponse.authored`
- US Core ServiceRequest Profile: `ServiceRequest.authoredOn`

### Prior Art

### Reason Not Performed (Healthcare Information Attributes data class) — Comment Position Summary

**Comments grouped by position:**

**Strongly supportive**
- **UI Health (University of Illinois Health)** [academic medical center] — Strong Support. Directly impacts eCQMs such as VTE-1 and VTE-2; standardization allows automated patient exclusions, eliminating the need for manual chart abstraction. UI Health's letter pairs Reason Not Performed with Indication and Performance Time as the foundational Healthcare Information Attributes elements that protect clinician quality scores by providing discrete evidence for legitimate care decisions in measures like TJC PC-02 and MIPS #005 (Heart Failure).
- **PACIO Project** [post-acute care interoperability community] — Supports inclusion in final v7. Useful for substantiating why treatment decisions were made that aren't consistent with documented advance directive information; supports measurement of quality and expressed individual treatment preferences.

**Supportive with refinements**
- **Alliance for Nursing Informatics / ANI** [nursing informatics professional society] — Strongly supports. Considers it one of the most critical additions in Draft v7 for nursing documentation integrity. Argues nurses routinely document clinical omissions (medications refused, procedures deferred due to deterioration, immunizations contraindicated), but this documentation has historically been free text in nursing notes or absent entirely from structured exchange. The absence of a standardized element systematically distorts quality measure performance, causing clinically justified omissions to appear as failures of care and creating inequitable measurement outcomes for providers serving higher-acuity or more complex populations. Wants explicit vocabulary specification with nursing-specific reason codes (patient refusal, clinical contraindication, patient not present, patient condition precluding the intervention).
- **HL7** [SDO] — Supports inclusion but flags scope ambiguity. Notes clarification needed that the element covers order cancellations as well as reasons results could not be obtained — there are many reasons tests aren't performed, including specimen condition. Suggests "cancelation reason" or "specimen reject reason" as alternative phrasings. Also asks whether the element covers DME, nutrition, physical, speech, and occupational therapies — if so, definition and usage note should be updated. Proposed usage note: "Should be included with procedures, immunizations, medications, laboratory results and orders when they are not performed."
- **SHIELD (Strengthening Health through Interoperability and Effective Laboratory Data)** [lab/diagnostic data standards coalition] — Mirrors HL7's position (SHIELD informed it). Supports inclusion but flags need to clarify scope covers order cancellations and specimen-reject scenarios.
- **APHL (Association of Public Health Laboratories)** [public health labs trade association] — Same scope clarification: covers order cancellations and reasons results couldn't be obtained (specimen condition, etc.). Requests usage notes give examples of use cases — procedures, immunizations, medications, laboratory results, orders.
- **WEDI** [administrative/transactions trade association] — Cites Reason Not Performed among the v7 additions that "could materially reduce administrative burden and improve interoperability." Three specific recommendations: (1) provide structured category guidance and examples to prevent text-based narrative reasons; (2) add a burden-reduction note encouraging reuse of existing workflow artifacts instead of requiring new documentation; (3) clarify association rules to link to the specific intended activity — strong potential to reduce administrative churn but only if captured consistently and computably.
- **Regenstrief Institute** [research/informatics institute] — Frames the new Healthcare Information Attributes class as a "pragmatic structural decision" consolidating contextual metadata previously scattered or implicit. Flags an ontological challenge: these elements are inherently contextual (they modify other data elements) rather than standalone. Recommends ONC provide implementation guidance clarifying how the attributes are expected to be associated with parent elements in FHIR-based exchange — Reason Not Performed should be explicitly linked to the procedure, immunization, or medication it modifies, rather than exchanged as an isolated observation. Without this guidance, implementers may produce data that is "technically USCDI-compliant but clinically disconnected."
- **Wolters Kluwer** [clinical content vendor] — Supports promoting Negation Rationale from Level 2 to add it to the Medications data class. Promotes more accurate quality measure reporting and overall care quality improvement by informing the care team about deviations from standard treatments.
- **Vizient** [GPO / healthcare performance improvement company] — Supports the addition. Has potential to improve clarity around clinical decision-making and the reasons an order or practice guideline is not carried out.
- **david_rocha** [individual / standards commenter] — Recommends SNOMED CT as a **required** (not just applicable) standard for Reason Not Performed, citing the SNOMED CT Situation hierarchy: Procedure declined (situation) 1296859006, Vaccine declined by patient (situation) 591000119102, Medication declined (situation) 406149000, and all descendants. Required designation maintains consistency with CMS Quality Payment Program technical specifications.

**Mixed / oppose**
- **American Hospital Association / AHA** [provider trade association] — Lists Reason Not Performed among the v7 elements that need "clarifying guidance and vocabulary standards prior to adoption." Appreciates the intent but notes EHRs don't always reflect reasons tests aren't performed — those tend to be captured in ancillary lab or imaging systems. Scope is unclear. Before adoption, ONC should develop guidance with illustrative examples to help providers know what to capture in EHRs and reduce free-text entry. AHA also asks ONC to explore reasons related to **insurance coverage and insurance denials** (a category not currently in the element's example set) and to clarify what existing workflow artifacts (order management reason codes, clinical notes, scheduling tools, radiology systems, lab systems) should be reused instead of requiring new documentation.
- **Federation of American Hospitals / FAH** [hospital trade association] — Appreciates the intent but reasons for non-performance are "highly variable, frequently unstructured, and often captured in ancillary systems" rather than the EHR. In practice, "a procedure was either performed or not, and the reasons it was not performed... are not consistently documented in a manner that lends itself to standardized, structured exchange." Without clear constraints on scope and representation, the element risks introducing noise into the data exchange, compromising the quality of information receiving providers rely upon, and generating inconsistent and difficult-to-interpret data.
- **Allina Health** [provider / health system] — Appreciates the intent but raises feasibility and clarity concerns. Reasons for not performing are often documented in unstructured clinical notes rather than discrete fields. Patient-driven factors (declining an immunization, not adhering to pre-procedure instructions) may not fit neatly into a discrete codified field. Asks ASTP to clarify intended use cases — clinician-driven decisions, patient-driven decisions, or both — and provide additional guidance on scope, standardization, and workflow integration. Asks whether this can be reliably captured in structured format across diverse care settings.
- **Oracle Health** [EHR vendor] — Generally supports inclusion of the element, but argues placing it in the Healthcare Information Attributes data class doesn't provide adequate guidance on what healthcare information it's collected for. Urges ONC to put it in the appropriate data classes where it's relevant — specifically Clinical Tests, Diagnostic Imaging, Laboratory, Medications, Orders, Procedures, and Vital Signs. Alternatively (less preferred), include in the element definition the specific data classes/elements to which it applies. "It is critical to dispel ambiguity regarding the intended usage and scoping of the data element."

**Oppose / redesign**
- **TMA (Texas Medical Association)** [state physician professional society] — Lists Reason Not Performed among 15 elements ONC should not adopt until each has a correlating vocabulary standard.

**Oppose**
- **Epic** [EHR vendor] — Recommends ONC not include this data element in the final USCDI v7. Where Reason Not Performed is currently implemented in EHR systems, it is scoped to specific, well-defined contexts — most notably quality measurement, where a limited set of standardized reasons (medical, patient, and facility exceptions) is used to document why a measure action was not taken. Epic has implemented this concept in that context but states there is "no generic or universal capability to document reasons not performed, suggesting that it is not mature enough for inclusion in USCDI." If the intent is to support quality measurement, encourages ONC to consider whether USCDI is the appropriate vehicle — quality measurement programs already address this concept through existing reporting standards better suited to the use case.

**Summary of Comments:** Reason Not Performed is one of the more technically supported v7 additions but draws sharp scope and placement criticism. The supporting voices — ANI [nursing informatics professional society], UI Health [academic medical center], PACIO [post-acute care interop community], Vizient [GPO], Wolters Kluwer [clinical content vendor], WEDI [administrative trade association], and the standards bodies (HL7, SHIELD, APHL) — converge on the same value proposition: structured capture of why a measure action wasn't taken protects clinician quality scores by distinguishing clinically justified omissions from failures of care, eliminates manual chart abstraction in eCQM workflows like VTE-1/VTE-2 and TJC PC-02, and reduces administrative burden if captured consistently. **Three concerns recur across the critical voices.** First, **scope and placement**: Oracle Health [EHR vendor] argues the element is misfiled in the new Healthcare Information Attributes class — it should live in the data classes where it actually applies (Clinical Tests, Diagnostic Imaging, Laboratory, Medications, Orders, Procedures, Vital Signs). Regenstrief [research/informatics institute] makes a related ontological point: these are inherently *contextual* attributes that modify other elements, so without explicit FHIR linkage guidance, implementations will produce data that is "technically USCDI-compliant but clinically disconnected." HL7, SHIELD, and APHL all want the usage note to clarify that the element covers order cancellations and specimen-reject scenarios as well as completion non-performance. Second, **EHR capture maturity**: AHA [provider trade association], FAH [hospital trade association], and Allina Health [provider/health system] all argue reasons for non-performance are typically captured in unstructured notes or ancillary systems (lab, imaging) rather than the EHR, and that patient-driven factors don't fit a discrete field. Epic [EHR vendor] takes the strongest version of this position — recommending non-adoption — arguing Reason Not Performed is mature only in the narrow quality-measurement context and that quality programs themselves are a better vehicle. Third, **vocabulary**: TMA [state physician society] would defer entirely until a vocabulary is named, while david_rocha and the SNOMED-leaning commenters point to existing SNOMED CT Situation-hierarchy codes (1296859006 Procedure declined, 591000119102 Vaccine declined, 406149000 Medication declined) and CMS QPP alignment as the obvious answer. AHA's request to extend the example reason set to **insurance coverage denials** is a unique addition not raised by other commenters and would meaningfully expand the element's value for revenue-cycle interoperability.

**Notably absent:** AMIA, AMA, AHIP, NCQA, AQIPS, EHR Association, MEDITECH, Emory Healthcare, Altarum Institute, FDA, CDC, CSTE, AHIMA, CARIN Alliance, and Vega Health are all silent on Reason Not Performed despite filing v7 comment letters. The EHR Association's silence is particularly notable since two member companies (Epic, Oracle Health) take strikingly different positions — Epic wanting non-adoption, Oracle Health wanting relocation. AHIP's absence is conspicuous given AHA's request to extend the element to capture insurance-coverage denials, which would directly involve payer workflows. Patient advocacy and consumer groups, which would have a stake in how patient refusals are coded and exchanged, are entirely absent.

---

Ready for the next element — **Diagnostic Report Date** is also in the Healthcare Information Attributes class and has overlapping commenters, so it's a natural follow-on. Or pick another?

### Diagnostic Report Date (Healthcare Information Attributes data class) — Comment Position Summary

**Comments grouped by position:**

**Strongly supportive (with refinements)**
- **American Clinical Laboratory Association / ACLA** [clinical laboratory trade association] — Suggests renaming to "Diagnostic Report Date/Time." Notes this should already be provided in laboratory results/reports — implying the data is captured today and the question is purely how it's named and exchanged.
- **HL7** [SDO] — Recommends renaming the element to "Diagnostic Report Date/Time" and adding a usage note: "This is an administrative date/time. It is updated every time a new version of the report is made available. It is not the same as the date/time that provides the temporal context for the patient's health." HL7 also recommends supporting synonyms across USCDI elements for clarity.
- **SHIELD (Strengthening Health through Interoperability and Effective Laboratory Data)** [lab/diagnostic data standards coalition] — Supports inclusion as a commonly exchanged data element across many use cases. In the lab data exchange context, corresponds to the CLIA requirement at 42 CFR 493.1291(c)(3) "The test report date." Notes that while CLIA identifies it as date only, including time matters in many situations. Recommendations: rename to "Diagnostic Report Date/Time" or at minimum "Report Date/Time"; add usage note "This element will change every time a new version of the report is released, covering preliminary, final, corrected, amended or addended reports. For each version the timestamp should be preserved."
- **APHL (Association of Public Health Laboratories)** [public health labs trade association] — Supports as providing temporal context for when results are available for clinicians' use. Has been included in HL7 v2 exchanges as OBR-22 (Results Rpt/Status Chng - Date/Time) for a long time. Same CLIA reference as SHIELD. Recommends rename to "Diagnostic Report Date/Time" and adds usage note: "This is an administrative date/time. It is updated every time a new version of the report is made available. It is not the same as the date/time that provides the temporal context for the patient's health."
- **CDC (DSMH Working Group)** [federal agency / public health] — Supports inclusion. Important element in clinical care covered under CLIA at 42 CFR 493.1291(c)(3). Proposes ASTP add a usage note indicating the data element may change each time a new version of the report is released (preliminary, final, corrected, amended, addended) and the timestamp should be preserved for each released report. Submits two extensive use cases illustrating clinical importance: (1) procalcitonin (PCT) decision-making for antibiotic stewardship, where pre-analytical specimen delays of 12% and analytical/biological variability of 10–30% can move results across decision thresholds (0.10, 0.25, 0.5, 2.0 µg/L) and impact whether antibiotics are stopped — knowing specimen collection time and test run time is "clinically relevant to making critical clinical decisions"; (2) hemolysis from delayed centrifugation in serum lactate samples affecting result accuracy. The use cases tie Diagnostic Report Date to Performance Time and Specimen Collection Date/Time as a coordinated set.
- **Regenstrief Institute** [research/informatics institute] — Supports with caveat. Notes the element is "inherently relational — it modifies a diagnostic report, not standalone" — same ontological concern Regenstrief raises about all the new Healthcare Information Attributes elements. Recommendation: provide FHIR implementation guidance on how this attribute links to its parent DiagnosticReport resource. "Isolated exchange is clinically meaningless." Aligns with public-health surveillance use cases where report timing is critical.

**Mixed / oppose**
- **Federation of American Hospitals / FAH** [hospital trade association] — Diagnostic reports already include multiple associated timestamps; unclear how this proposed element differs from those existing data points or what specific interoperability gap it fills. "Adding a potentially duplicative timestamp without clear differentiation from existing fields risks creating confusion rather than advancing interoperability." FAH lists this among elements where they're "open to inclusion" but require further specification from ONC on data granularity and vocabulary before finalization.
- **Oracle Health** [EHR vendor] — Generally supports inclusion, but argues the placement in Healthcare Information Attributes data class doesn't provide adequate guidance. Says the element "would have been more appropriately included in Laboratory and Diagnostic Imaging, but not in Medications or Patient Demographics and many other data classes." Urges ONC to relocate to Laboratory and Diagnostic Imaging specifically. Same general argument Oracle makes for Reason Not Performed and Indication: USCDI's class structure should communicate scope, not just group similar metadata.
- **EHR Association** [vendor trade association] — Argues Diagnostic Report Date and Reason Not Performed are "more appropriate for specific clinical contexts, such as laboratory, imaging, or procedures, rather than universally across USCDI." Recommends ONC assign these data elements to the specific data classes where they are most applicable. If not feasible, clearly define the scope of each element to indicate where it should be used. More broadly, suggests USCDI would benefit from closer alignment with FHIR as a modeling framework to clarify relationships and identify gaps before inclusion.
- **Lisa Nelson / LisaRNelsonRI** [individual standards consultant] — Proposes a substantive redesign: rename to "Document Creation Date" and generalize the definition to "Date and Time a document was made available for access." This generalization would apply the attribute to all kinds of documents (clinical notes, discharge summaries, explanations of benefits) accessed by providers or patients — not just diagnostic reports. Argues if generalized and moved into the Healthcare Information Attributes class as Document Creation Date, the element would offer "greater interoperability value."

**Oppose / redesign**
- **TMA (Texas Medical Association)** [state physician professional society] — Lists Diagnostic Report Date among 15 elements ONC should not adopt until each has a correlating vocabulary standard.

**Summary of Comments:** Diagnostic Report Date draws no outright opposition but no clean support either — every supporting commenter has refinements, and four organizations want substantive redesign. The supporting voices converge tightly on three asks. **First, rename to capture time as well as date** — ACLA [clinical lab trade association], HL7 [SDO], SHIELD [lab/diagnostic data standards coalition], APHL [public health labs trade association], and (via the use cases) CDC [federal agency/public health] all say the date-only framing is insufficient because clinical decision-making depends on the full timestamp; SHIELD's fallback ("at minimum 'Report Date/Time'") and ACLA's framing ("Diagnostic Report Date/Time") would represent the consensus minimum. **Second, add a usage note clarifying that this is an administrative timestamp** — distinct from clinical temporal context — that updates with each version of the report (preliminary, final, corrected, amended, addended) with timestamps preserved per version. APHL and HL7 propose nearly identical language; CDC endorses the same usage note. The lab-side commenters explicitly tie the element to CLIA's 42 CFR 493.1291(c)(3) test report date requirement, framing USCDI conformance as harmonization with existing federal lab reporting law. **Third, the structural ontology problem.** Regenstrief Institute [research/informatics institute] frames the issue most cleanly: Diagnostic Report Date and the other Healthcare Information Attributes elements are inherently *contextual* — they modify other data elements rather than standing alone — and without explicit FHIR implementation guidance linking the attribute to its parent DiagnosticReport resource, exchanging it in isolation is "clinically meaningless." Oracle Health [EHR vendor], the EHR Association [vendor trade association], and FAH [hospital trade association] make the same point in placement rather than ontological terms: the element belongs in the data classes where it actually applies (Laboratory, Diagnostic Imaging, Procedures), not in a metadata catch-all class. FAH goes one step further, questioning whether the element fills any real gap given that diagnostic reports already carry multiple timestamps. The most distinctive position comes from Nelson [individual standards consultant], who argues the element should be **generalized** away from diagnostic reports entirely and renamed Document Creation Date to apply across notes, discharge summaries, EOBs, and other document types — broadening rather than narrowing the scope. CDC's [federal agency / public health] use cases are the most clinically grounded contribution, demonstrating why temporal precision matters at decision thresholds in procalcitonin-guided antibiotic stewardship and serum lactate interpretation.

**Notably absent:** AHA, AHIP, AMA, AMIA, NCQA, AQIPS, Epic, MEDITECH, Allina Health, Emory Healthcare, UI Health, ANI, Wolters Kluwer, WEDI, Vizient, Altarum Institute, FDA, AHIMA, CARIN Alliance, and Vega Health are all silent on Diagnostic Report Date despite filing v7 letters. Epic's silence is the most striking given Epic's strong opposition to Reason Not Performed in the same data class — they evidently view Diagnostic Report Date as a less consequential element. The hospital-side absence (AHA silent, only FAH commenting) is also notable. Patient advocacy and consumer groups, which would have a stake in how report-availability timestamps are exchanged with patient-access apps, are entirely absent.


