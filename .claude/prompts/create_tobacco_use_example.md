---
name: LOINC candidates for USCDI v7 tobacco/nicotine use behavioral attributes
description: Mapping of USCDI v7 "behavioral attributes" sub-elements (type, mode, frequency, duration, assessment) to candidate LOINC codes, with gaps flagged.
type: project
originSessionId: aeff1ea4-5773-4abb-a3a0-9da511143eec
---
Candidate LOINC codes for USCDI v7 tobacco/nicotine use behavioral attribute elements:

- **Type of product used** — `81228-9` "Tobacco product" (Type / ^Patient / Nom). Variant: `64004-5` "Tobacco product [PhenX]".
- **Mode of consumption** — *no direct LOINC*. Inferred from product (cigarette = smoked, pouch = oral, etc.).
- **Frequency of use** — `96101-1` "Tobacco use frequency" (NRat / Ord). Adjacent: `96842-0` "How often have you used any tobacco product in past 12Mo"; `45434-8` "Use of tobacco products at least daily [MDS]"; `63640-7` "How many cigarettes per day…".
- **Duration of use** — `88029-4` "Tobacco use duration" (Time / Qn). Intensity×time: `8664-5` "Cigarettes smoked.total (pack per year)" — cigarette-only. Lifetime exposure: `74011-8` "Lifetime tobacco use".
- **Assessment of use behaviors (panel/use case)** — `88028-6` "Tobacco use panel". Status alternative: `112319-9` "Tobacco use status".

Gaps:
- No LOINC for *mode of consumption* — would need upstream request or derivation from product type.
- `8664-5` pack-year is cigarette-specific; no nicotine-pouch / vaping equivalent.




create  US Core Observation example
    - Structure: Single profile with components for each each tobacco related name value pair
    - Terminology based on the LOINC 88028-6 "Tobacco use panel" which is available at /Users/ehaas/Documents/FHIR/USCDIV7/.claude/prompts/source/loinc-88028-6.md
      - `Observation.code` = 88028-6 "Tobacco use panel"
      -  `Observation.component.code` =
         -  72166-2	Tobacco smoking status	 (answer: every day smoker)
         -  88031-0	Smokeless tobacco status  (answer: occasional)
         -  82769-1	Smoked or non-smoked tobacco	both
         -  81228-9	Tobacco product	 (answer: cigarettes, e-cigarettes)
         -  8663-7	Cigarettes smoked current (pack per day) - Reported   (answer: <1 )
         -  88029-4	Tobacco use duration (answer: 10 years )
         -  782516008	http://snomed.info/sct	Number of calculated pack years for cumulative lifetime tobacco exposure (observable entity)  (answer: calculate from above answer)

The answer lists for these loincs can be found in the LOINC CSV:  /Users/ehaas/Downloads/Loinc_2.82/LoincTableCore/LoincTableCore.csv  (see /Users/ehaas/Downloads/Loinc_2.82/LoincTableCore/LoincTableCoreReadMe.txt for table structure)

Use /Users/ehaas/Documents/FHIR/US-Core/input/examples-yaml/some-day-smoker.yml as an exemplar for the metadata and references
  - for `meta.profile` use a  sham url: `http://hl7.org/fhir/us/core/StructureDefinition/us-core-tobacco-use`



is the configuration file good practice and is toml considered better than yaml.fi