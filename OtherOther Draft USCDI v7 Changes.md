
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

<DataElement: Summary >

## Other Draft USCDI v7 Changes

<!-- image of summary of changes-->

![image](https://hackmd.io/_uploads/SJqfhmakGx.png)



<!-- **:new: Definition :point_down:** -->




<!-- markdown table summary of proposal use adobe to convert to excel and then script to markdown or just copy/paste -->

| Category | Items | US Core V10 Changes|
|---|---|---|
| Reclassified | Health Concern, Indication, Performance Time | Reconcile USCDI mapping + profile narrative. |
| Names Revised | 19 elements incl. Problem, Procedure, Test, Patient Goal, Health Insurance cluster |  Reconcile USCDI mapping + profile narrative. |
| Definitions Revised | Author Role, Discharge Summary Note, Indication, Patient Goal, Performance Time, Problem, Procedure | Tweak usage notes if needed. |
| Standards Added | Tobacco Use, Coverage Type (SOPT 9.2), Patient Goal, Pregnancy Status | Verify bindings (see below :point_down: )|
| Consolidated | SDOH Goals → Patient Goal; SDOH Problems/Health Concerns → Problem; SDOH Interventions → Procedure | review documentation for realignment if needed |
| MS elements w/ existing home | Condition Status, Procedure Status, Patient Identifier, Device Type, Facility Telecom, HI cluster, Immunization Status/Source, Med Dispense Quantity, Diagnostic Report Date, Allergy Criticality, Deceased Indicator, Specimen Collection Method | Update USCDI mapping entries. |

:point_down: 


### CCDA Design Notes

### Issues

### Proposal

1. Applicable Standards Added:
      - Tobacco Use - see [Health Status Assessment](/_s1WbP-9SxGOEt8IcST0Ow)
      - Coverage Type: :new: SOPT 9.2 - No change needed, already used by US Core Coverage Profile (although the codesystem version discovery is unclear)
      - Patient Goal: :new: LOINC and SNOMED CT Vocabulary Standards. - No change needed, already used by US Core Coverage Profile (although the Value Set Definition could be updated to constrain the codes to a subset of LOINC and SNOMED)
      - Pregnancy Status: :new: LOINC Vocabulary Standards. - No change needed, LOINC use for Observation.code US Core Pregnancy Profiles (although the result values are SNOMED CT codes)


### Decisions

1.
2.
3.

### IG Updates

- [ ] USCDI Mapping Table
- [ ] Update US Core Profile Description
<!-- - [ ] deprecate US Core CarePlan Category Extension Codes code system
- [ ] notify publishing that pink deprecate box is not showing up for codesystems.
- [ ] Update Introduction
- [ ] Implementation Specific Guidance
- [ ] New Example(s) pending final review of decisions
- [ ] Update Example(s) pending final review of decisions -->

---

## Appendix

### Prior Art


