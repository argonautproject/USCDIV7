
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

## Other Changes

### Other Final USCDI v7 Changes

| Item | Change |
|---|---|
| Encounter Time | **Renamed** to Encounter Date and Time. Definition adjusted ("Date/times related to an encounter" → "Dates and times related to an encounter"). |
| Performance Time | **Renamed** to Performance Date and Time. Definition adjusted ("Time and/or date a care activity is performed" → "Date and time a care activity is performed"). Example "laboratory specimen collection time" removed. |
| Unique Device Identifier | **Definition revised**: presence of production identifiers (PI) is now conditioned on device risk class. |
| Medical Devices (class) | **Definition replaced** with an FD&C Act-style definition: instrument, apparatus, machine, equipment, implant, software, hardware, or related component or accessory intended to diagnose, treat, cure, mitigate, or prevent disease, or to affect the structure or function of the body. |

### Other Draft USCDI v7 Changes

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


### Issues

### Proposal

1. Applicable Standards Added:
      - Tobacco Use - see [Health Status Assessment](/_s1WbP-9SxGOEt8IcST0Ow)
      - Coverage Type: :new: SOPT 9.2 - No change needed, already used by US Core Coverage Profile (although the codesystem version discovery is unclear)
      - Patient Goal: :new: LOINC and SNOMED CT Vocabulary Standards. - No change needed, already used by US Core Coverage Profile (although the Value Set Definition could be updated to constrain the codes to a subset of LOINC and SNOMED)
      - Pregnancy Status: :new: LOINC Vocabulary Standards. - No change needed, LOINC use for Observation.code US Core Pregnancy Profiles (although the result values are SNOMED CT codes)


### Decisions

1. Sep 10th CGP Call
   - Will review US Core Documentaion for alignment with updated categories, names and description.
   - Update USCDI --> US Core Mappings
   - No changes to terminology identified


---

## Appendix

### Prior Art


