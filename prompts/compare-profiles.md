Compare profiles prompt

Compare these profiles and create a summary table listing them side by side

profile A = FlagAlertUvIps
    - IG: https://www.hl7.org/fhir/uv/ips/index.html
    - Profile page: https://www.hl7.org/fhir/uv/ips/StructureDefinition-Flag-alert-uv-ips.html
    - StructureDefinition attached
profile B = NHS England Reasonable Adjustment Flag
    - IG: not available
    - Profile page: /Users/ehaas/Documents/FHIR/USCDIV7/prior_art/Reasonable Adjustment Flag - NHS England Digital.pdf
    - StructureDefinition not available
profile C = QI Core Flag
    - IG: https://build.fhir.org/ig/HL7/fhir-qi-core/
    - Profile page: https://build.fhir.org/ig/HL7/fhir-qi-core/en/StructureDefinition-qicore-flag.html
    - StructureDefinition attached
profile D = Flag: Patient (EU core)
    - IG: https://build.fhir.org/ig/hl7-eu/base/
    - Profile page: https://build.fhir.org/ig/HL7/fhir-qi-core/en/StructureDefinition-qicore-flag.html
    - StructureDefinition attached

Create a wide summary table with rows for each element when at least one of element is in the profile StructureDefinition.differential as a mustSupport = true, min > 0, or have an obligation valueCode containing SHALL or SHOULD with the following columns:

have these columns

- element path
- Description which consists of short, description,

and for each profile:

- must support  flag
- mandatory (min: 1)  flag (note if it is inherited from base resource)
- modifier element flag
- cardinality  (N..M)
- type (list of targets if different from base resource)
- Comments which consists of any changes to short, description, if coded element: binding and binding strength , if any profile specific invariants  - ignore constraints inherited from base, list them here


summarize the comparison of use cases and any other narrative documentation as well.
