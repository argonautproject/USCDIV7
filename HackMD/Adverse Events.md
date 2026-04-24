
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

## Adverse Events: New Profile Needed


<!-- image of summary of changes-->
![image](https://hackmd.io/_uploads/B1VkaKRIbg.png)


<!-- **:new: Definition :point_down:** -->

![image](https://hackmd.io/_uploads/H1NpnK0LWg.png)


<!-- markdown table summary of proposal use adobe to convert to excel and then script to markdown or just copy/paste -->

➕ In USCDI+

DATA ELEMENT|<center>APPLICABLE VOCABULARY STANDARD(S)<br/>Standards listed are required.<br/>If more than one is listed,<br/> at least one is required unless<br/>otherwise noted.<br/>Standards versions represent the most recent <br/>available at time of publication.</center>|US Core V10 Proposal
---|---|---
| **Adverse Event ➕**<br>A change to patient condition that could be an unintended effect of clinical interventions. | • SNOMED Clinical Terms® (SNOMED CT®)<br>U.S. Edition, September 2025 Release | 🆕 US Core AdverseEvent Profile with `AdverseEvent.event` Must Support 0..1 with *extensible* binding to FHIR R6 or equivalent [AdverseEvent Type](https://hl7.org/fhir/6.0.0-ballot4/valueset-adverse-event-type.html) |
| **Adverse Event Outcome**<br>Result or impact of an adverse event.<br>Examples include but are not limited to **hospitalized**, *recovered*, *recovered with sequelae*, and *death*. |  |🆕 US Core AdverseEvent Profile with `AdverseEvent.outcome` Must Support 0..1 with *required* binding to FHIR R4 [AdverseEventOutcome](https://hl7.org/fhir/R4/valueset-adverse-event-outcome.html) (*resolved*, **recovering**, **ongoing**, *resolvedWithSequelae*, *fatal*, unknown) |

### CCDA Design Notes

### Issues :thinking_face: 

1.  AdversEffect is FMM = 0 FHIR R4, part of FHIR R6 
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

1. hl7.fhir.us.qicore
2. fhir.hrsa.uds-plus


