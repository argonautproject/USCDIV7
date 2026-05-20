---
name: fhir-terminology-verification
description: Validate US Core terminology. This skill should be used after generating or editing any profile differential, instance example, or value set, or whenever the user asks to "check," "validate," or "review" a profile.
- Verify if a code is present (or just text) this is discouraged.
- Verify if the code is a member of the value set
- Verify every coded value's `system`, `code`, and `display` against an authoritative source (SNOMED CT browser, LOINC, HL7 terminology):
   - LOINC CSV:  /Users/ehaas/Downloads/Loinc_2.82/LoincTableCore/LoincTableCore.csv  (see /Users/ehaas/Downloads/Loinc_2.82/LoincTableCore/LoincTableCoreReadMe.txt for table structure)
   - SNOMED CT description file: /Users/ehaas/Downloads/SnomedCT_ManagedServiceUS_PRODUCTION_US1000124_20260301T120000Z/Snapshot/Terminology/sct2_Description_Snapshot-en_US1000124_20260301.txt
   - HL7 CodesSystems: /Users/ehaas/.fhir/packages/hl7.terminology#5.5.0/package
   - VSAC ValueSets: /Users/ehaas/.fhir/packages/us.nlm.vsac#0.24.0
- Do not invent codes.
- Flag any code that cannot be
   verified.