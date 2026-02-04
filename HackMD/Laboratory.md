
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

## Laboratory: Changes to US Core Specimen Profile


<!-- image of summary of changes-->
![image](https://hackmd.io/_uploads/SkYvcayv-l.png)

<!-- **:new: Definition :point_down:** -->

![image](https://hackmd.io/_uploads/SJVxsaJw-x.png)

<!-- markdown table summary of proposal use adobe to convert to excel and then script to markdown or just copy/paste -->

<!-- ➕ In USCDI+ -->

DATA ELEMENT|<br/>Standards listed are required.<br/>If more than one is listed,<br/> at least one is required unless<br/>otherwise noted.<br/>Standards versions represent the most recent <br/>available at time of publication.</center>|US Core V10 Proposal
---|---|---
| **Specimen Collection Method**<br>Technique or procedure used to obtain a specimen.<br>Examples include but are not limited to venipuncture, swab, biopsy, aspiration, and<br>catheter collection. |  | Add `Specimen.collection.method` min = 0 *Additional USCDI* to the *US Core Specimen Profile*

### CCDA Design Notes

### Issues

1. Terminology - see options below.

### Proposal

1.  Add `Specimen.collection.method` min = 0 *Additional USCDI* to the *US Core Specimen Profile*
    - Terminology options:
        1. [v2-0488](https://terminology.hl7.org/ValueSet-v2-0488.html)
        2. [FHIR Specimen Collection Method](https://hl7.org/fhir/R4/valueset-specimen-collection-method.html) ~ dozen SNOMED Codes

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


