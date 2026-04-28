
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

## Allergies and Intolerances: Add New *Must Support* element to US Core AllergyIntolerance Profile


<!-- image of summary of changes-->
![image](https://hackmd.io/_uploads/rJ6v_9AIZx.png)


<!-- **:new: Definition :point_down:** -->

![image](https://hackmd.io/_uploads/ryFFOcRLWx.png)

<!-- markdown table summary of proposal use adobe to convert to excel and then script to markdown or just copy/paste -->

DATA ELEMENT|<br/>Standards listed are required.<br/>If more than one is listed,<br/> at least one is required unless<br/>otherwise noted.<br/>Standards versions represent the most recent <br/>available at time of publication.</center>|US Core V10 Proposal
---|---|---
| **Allergy Intolerance Criticality**<br>Estimate of the potential clinical harm, or seriousness, of a reaction to an identified substance. |  | Add `AllergyIntolerance.criticality` as 0..1 *Must Support* with a *required binding* to 	[AllergyIntoleranceCriticality](https://hl7.org/fhir/R4/valueset-allergy-intolerance-criticality.html)|

<!-- ➕ In USCDI+ -->

### CCDA Design Notes

### Issues

### Proposal

1.  Add `AllergyIntolerance.criticality` as 0..1 *Must Support* with a *required binding* to [AllergyIntoleranceCriticality](https://hl7.org/fhir/R4/valueset-allergy-intolerance-criticality.html)
2.  Add criticality+patient search parameter 

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


