
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

## Patient Demographics: Changes TBD


<!-- image of summary of changes-->
![image](https://hackmd.io/_uploads/HJjA4glPbx.png)
*No narrative summary for the 
Patient Identifer Data Element in the ASTP/ONC Standards Bulletin 2026-1.*

<!-- **:new: Definition :point_down:** -->

![image](https://hackmd.io/_uploads/rkNOHgevbl.png)

<!-- markdown table summary of proposal use adobe to convert to excel and then script to markdown or just copy/paste -->

➕ In USCDI+

DATA ELEMENT|<br/>Standards listed are required.<br/>If more than one is listed,<br/> at least one is required unless<br/>otherwise noted.<br/>Standards versions represent the most recent <br/>available at time of publication.</center>|US Core V10 Proposal
---|---|---
| **Accommodation ➕**<br>Modifications, tools, technologies, and other supports necessary to access care. | • SNOMED Clinical Terms (SNOMED CT) U.S. Edition, September 2025 Release | See proposal below | 
| **Deceased Indicator ➕**<br>Indicates if the person is deceased or not. |  |**No Change**: `Patient.deceased[x]` already is a US Core *Additional USCDI* element |
| **Patient Identifier**<br>Sequence of characters assigned by an organization to uniquely refer to a patient.<br>Examples include but are not limited to Medical Record Number. |  |**No Change**: `Patient.identifier` already is a US Core *Must Support* element|

### CCDA Design Notes

### Issues

- Terminology

### Proposal

1.  Options
    - Add the standard [Patient Disability Extension](http://hl7.org/fhir/StructureDefinition/patient-disabilityextension) to US Core Patient (aligns with prior design)
    - Add New US Core Note Profile ( see the [NHS England Reasonable Adjustment Flag](https://digital.nhs.uk/services/reasonable-adjustment-flag))
    - Add New US Core Observation Profile

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


