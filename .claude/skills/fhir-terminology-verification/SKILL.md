---
name: fhir-terminology-verification
description: Validate US Core terminology. This skill should be used after generating or editing any profile differential, instance example, or value set, or whenever the user asks to "check," "validate," or "review" a profile.
- Verify if a code is present (or just text) this is discouraged.
- Verify if the code is a member of the value set
- Verify every coded value's `system`, `code`, and `display` against an authoritative source (SNOMED CT browser, LOINC, HL7 terminology):
   - LOINC CSV:  /Users/ehaas/Downloads/Loinc_2.82/LoincTableCore/LoincTableCore.csv  (see /Users/ehaas/Downloads/Loinc_2.82/LoincTableCore/LoincTableCoreReadMe.txt for table structure)
   - SNOMED CT US Edition description file: /Users/ehaas/Downloads/SnomedCT_ManagedServiceUS_PRODUCTION_US1000124_20260301T120000Z/Snapshot/Terminology/sct2_Description_Snapshot-en_US1000124_20260301.txt
   - HL7 CodesSystems: /Users/ehaas/.fhir/packages/hl7.terminology#5.5.0/package
   - VSAC ValueSets: /Users/ehaas/.fhir/packages/us.nlm.vsac#0.24.0
- Do not invent codes.
- Flag any code that cannot be verified.

## Display-name rules (treat mismatches as DEFECTS, not advisories)

- **LOINC** — `Coding.display` MUST be the **Long Common Name (LCN)** from `LoincTableCore.csv` column `LONG_COMMON_NAME`. The LOINC **SHORT name** (column `SHORTNAME`) is NOT acceptable as the FHIR display, even though it is an official LOINC term. Flag SHORT-name displays as defects to fix — do not pass them as "advisory" or "OK".
  - Example defect: `display: "Tobac smoke stat"` (SHORT) → should be `display: "Tobacco smoking status"` (LCN).
- **LOINC answer codes (`LA...`)** — `Coding.display` MUST exactly match `DisplayText` in `AnswerList.csv` for that `LocalAnswerCode`.
- **SNOMED CT** — `Coding.display` SHOULD match either the Fully Specified Name (without the trailing `(semantic tag)`) or an active English description for the concept. Flag any display that does not match any active description as a defect.
- **HL7 CodeSystems** — `Coding.display` MUST match the `display` of the concept in the source CodeSystem JSON.

When reporting, separate findings into:
- **Defects** — items that must be fixed (invalid code, wrong system, missing code, LOINC SHORT instead of LCN, display does not match canonical, code not in bound value set).
- **Advisories** — informational only (e.g., extensible-binding codings not in the preferred value set, UCUM curly-brace annotations without dimensional meaning).

Do not silently downgrade a defect to an advisory because the term is "technically valid". If FHIR/US Core convention calls for a specific form (e.g., LCN), failure to use that form is a defect.
