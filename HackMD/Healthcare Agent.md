
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

## Healthcare Agent: See Options below


<!-- image of summary of changes-->
![image](https://hackmd.io/_uploads/HJD2scC8Ze.png)

<!-- **:new: Definition :point_down:** -->

![image](https://hackmd.io/_uploads/rkA0nqRU-x.png)

<!-- markdown table summary of proposal use adobe to convert to excel and then script to markdown or just copy/paste -->

➕ In USCDI+

DATA ELEMENT|<br/>Standards listed are required.<br/>If more than one is listed,<br/> at least one is required unless<br/>otherwise noted.<br/>Standards versions represent the most recent <br/>available at time of publication.</center>|US Core V10 Proposal
---|---|---
| **Healthcare Agent ➕**<br>Individual legally authorized to make healthcare decisions on behalf of a patient when the patient is unable to do so because of an illness or injury. |  |See Options below |


### CCDA Design Notes

### Issues

### Proposal Options:

1.  Use CareTeam: Add role code to the [Care Team Member Function](https://vsac.nlm.nih.gov/valueset/2.16.840.1.113762.1.4.1099.30/expansion) ValueSet
2.  Use Patient: Add code to the `Patient.contact.relationship` ValueSet
3.  Use RelatedPerson: Add code to RelatedPerson.relationship
4.  Consent Resource (see: https://build.fhir.org/ig/HL7/fhir-pacio-adi/StructureDefinition-ADI-HealthcareAgentConsent.html) 

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

[PACIO ADI](https://build.fhir.org/ig/HL7/fhir-pacio-adi)


