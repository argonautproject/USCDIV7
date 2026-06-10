# Create a US Core ValueSet

You are creating a new US Core Valueset (YAML) to meet a specific USCDI
v7 Data Element or Class. Match the voice, structure, and level of
detail of the US Core Valueset(s) provided as exemplars.

## Paths

External paths come from @.claude/config/paths.yml:

- `us_core.value_sets` — exemplar ValueSets YAML
  files in the US Core repo
- `uscdi_v7.resources` — where the new profile YAML is written
- `fhir_r4.core_package` — base FHIR R4 package on disk
- terminology - use to validate codes from their respective code systems

Internal project files use relative paths from the project root.

## Step 1: Gather requirements

Collect the following from the user:

1. **Valueset name or ID** for the new profile.
2. **Compose elements** codesystems, valuesets or list of enumerates codes to include:

### Example input

1. US Core Specimen Collection Method
2. include:
     - SNOMED CT 17636008 | Specimen collection (procedure) hierarchy
     - list of enumerated codes at /Users/ehaas/Documents/FHIR/USCDIV7/.claude/output/SpecimenXmapCollectionMethodSCT-non-descendants.md
       - deduplicate the duplicate codea - choose preferred description
       - include the retired concepts
       - include the Non-procedure semantic-tag concepts

## Step 2: Add the FMM extension

Add the following extension block to the profile, including the
surrounding comments verbatim. The comments are load-bearing — they
flag the FMM value for review when the profile moves into named
regulation.

```yaml
#============= Update when version named in regs ====================
  - url: http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm
    valueInteger: 3
#======================================================================
```

## Step 3: Voice and style

Apply the voice and style rules defined in CLAUDE.md to all narrative
content: `instance-description`, intro notes, and any prose.
Non-negotiable.

## Step 4: Draft the profile

- Produce the YAML valueset based on the exemplar(s)
and the user's element list. Constraints:
- Display name rules
  - Use SNOMED CT preferred descriptions
  - Use LOINC Long Common Name
- Do not invent codes, value sets, or extension URLs. Flag any
  binding or extension URL that cannot be verified.

## Step 5: Run a self-check

- check that all code are valid concepts where possible

## Step 6: Write the output

Write the YAML resource only — ready to drop into the directory
defined as `uscdi_v7.profiles` in @.claude/config/paths.yml.

- Naming convention: `{ResourceType}-{kebab-case-name}.yml`.
- Final summary must flag every code, reference, or assumption that
  could not be verified.

## Step 7: Run the IG build

Run the IG publisher build to confirm the new valueset compiles and
passes structural validation. Resolve any publisher errors before
proceeding to intro notes or examples.
