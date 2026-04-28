
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

## Medications: New Profile Needed
<!-- image of summary of changes-->
![image](https://hackmd.io/_uploads/HJw2a0kDZl.png)
*No narrative summary for the Medication Dispense Quantity Data Element in the ASTP/ONC Standards Bulletin 2026-1.*

<!-- **:new: Definition :point_down:** -->

![image](https://hackmd.io/_uploads/ryKmACyvbx.png)

<!-- markdown table summary of proposal use adobe to convert to excel and then script to markdown or just copy/paste -->

DATA ELEMENT|<br/>Standards listed are required.<br/>If more than one is listed,<br/> at least one is required unless<br/>otherwise noted.<br/>Standards versions represent the most recent <br/>available at time of publication.</center>|US Core V10 Proposal
---|---|---
| **Medication Administration ➕**<br>Information about the event of a patient consuming or otherwise being given a medication.<br>Examples include but are not limited to swallowing a tablet, administering an injection, and a long running infusion. |  |🆕 US Core MedicationAdministration Profile (See Proposal)
| **Medication Dispense Quantity ➕**<br>The amount of medication dispensed or to be dispensed. |  |**No Change**: ` MedicationRequest.dispenseRequest.quantity` and `MedicationDispense.quantity` already are US Core *Must Support* elements|

➕ In USCDI+

### CCDA Design Notes

### Issues

### Proposal
1. 🆕 US Core MedicationAdministration Profile
   - Mandatory and Must Support elements: `status (m), statusReason, category, medication[x] (m), subject (m), effective[x] (m), performer, request, dosage`  (m = mandatory in base)
   - Terminology same as for MedicationRequest/Dispense
   - Search Parameters: patient, status, effective-time, medication, code
   - Edits to Medication List guidance page


1.  No Changes to US Core MedicationRequest Profile and US Core MedicationDispense Profile.
    - Possible updates to guidance because of new US Core MedicationAdministration Profile.

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

### Prior Art

- [pdmp-medicationadministration](https://packages2.fhir.org/xig/resource/hl7.fhir.us.pdmp%7Ccurrent/StructureDefinition/pdmp-medicationadministration)
- [Standardized Medication Profile - MedicationAdministration](	http://hl7.org/fhir/us/smp/StructureDefinition/smp-medicationadministration)
- [QI Core](https://packages2.fhir.org/xig/resource/hl7.fhir.us.qicore%7Ccurrent/StructureDefinition/qicore-medicationadministration)
- [US Public Health MedicationAdministration](https://packages2.fhir.org/xig/resource/hl7.fhir.us.ph-library%7Ccurrent/StructureDefinition/us-ph-medicationadministration)
- MCode
- 
