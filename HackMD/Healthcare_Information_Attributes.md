
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

<!-- markdown table summary of proposal use adobe to convert to excel and then script to markdown or just copy/paste -->

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


