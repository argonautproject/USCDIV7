# Create a US Core Profile

You are creating a new US Core Profile (YAML) to meet a specific USCDI
v7 Data Element or Class. Match the voice, structure, and level of
detail of the US Core Profile(s) provided as exemplars.

## Paths

External paths come from @.claude/config/paths.yml:

- `us_core.structure_definitions` — exemplar StructureDefinition YAML
  files in the US Core repo
- `uscdi_v7.resources` — where the new profile YAML is written
- `fhir_r4.core_package` — base FHIR R4 package on disk

Internal project files use relative paths from the project root.

## Step 1: Gather requirements

Collect the following from the user:

1. **Profile name or ID** for the new profile.
2. **Exemplar StructureDefinition(s)** — one or more existing US Core
   profile YAML files to use as templates. Resolve filenames against
   `us_core.structure_definitions`.
3. **USCDI Data Element or Class** the profile represents.
4. **Element list** — Mandatory (m = mandatory in base), Must Support,
   and Additional USCDI elements to include.
5. **Constraints and bindings** to confirm.

### Example input

1. US Core MedicationAdministration Profile.
2. Exemplars: `StructureDefinition-us-core-medicationrequest.yml`,
   `StructureDefinition-us-core-medicationdosage.yml` (resolved
   against `us_core.structure_definitions`).
3. USCDI v7 Medications Data Class.
4. Mandatory and Must Support elements only: `status (m)`,
   `medication[x] (m)`, `subject (m)`, `effective[x] (m)`,
   `performer`, `request`, `dosageInstruction`.
5. Bindings reuse US Core MedicationRequest for:
   - `MedicationCategory.category:us-core`
   - `MedicationCategory.medication[x]`
   - `MedicationCategory.dosageInstruction` sub-elements

## Step 2: Reference the base FHIR R4 StructureDefinition

Reference the base FHIR R4 profile at `fhir_r4.core_package` (defined
in @.claude/config/paths.yml). Treat the base definition as the
authority for element cardinality, type, binding, binding
strength, short and description.

## Step 3: Add the FMM extension

Add the following extension block to the profile, including the
surrounding comments verbatim. The comments are load-bearing — they
flag the FMM value for review when the profile moves into named
regulation.

```yaml
#============= Update when version named in regs ====================
  - url: http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm
    valueInteger: 2
#======================================================================
```

## Step 4: Voice and style

Apply the voice and style rules defined in CLAUDE.md to all narrative
content: `instance-description`, intro notes, and any prose.
Non-negotiable.

## Step 5: Draft the profile

Produce the differential-only YAML profile based on the exemplar(s)
and the user's element list. Constraints:

- Differential only — no snapshot.
- Element order matches the base StructureDefinition.
- Each element includes the appropriate type and cardinality,
  binding and binding strength defined in the requirements in Step 1 or if not defined there, inherited from base.
- Element includes Must Support OR Additional USCDI (not both), if defined in Step 1
- Reference elements list ALL target types allowed by the base
  element, not just the Must Support ones. Map each base target to its
  US Core profile when one exists (per the conformance self-check
  rules, including the Observation, ADI DocumentReference, and
  PractitionerRole exceptions); otherwise keep the base
  `http://hl7.org/fhir/StructureDefinition/{Type}` canonical. Preserve
  the base target order. Tag Must Support per target with a parallel
  `_targetProfile` array whose entries carry the
  `elementdefinition-type-must-support` extension: `valueBoolean: true`
  for the targets named in the Step 1 requirements, `valueBoolean:
  false` for all others. The `_targetProfile` array MUST have one entry
  per `targetProfile` and stay in the same order. Do not drop the
  non-Must-Support targets.
- Element includes only short description and/or description if defined in the requirements in Step 1
- Do not invent codes, value sets, or extension URLs. Flag any
  binding or extension URL that cannot be verified.

## Step 6: Run the conformance self-check

Apply the `us-core-conformance-self-check` skill to the drafted YAML.
Address any FAIL findings before proceeding. Flag UNVERIFIED items in
the final summary.

## Step 7: Write the output

Write the YAML resource only — ready to drop into the directory
defined as `uscdi_v7.profiles` in @.claude/config/paths.yml.

- Naming convention: `{ResourceType}-{descriptive-id}.yml`.
- Final summary must flag every code, reference, or assumption that
  could not be verified.

## Step 8: Run the IG build

Run the IG publisher build to confirm the new profile compiles and
passes structural validation. Resolve any publisher errors before
proceeding to intro notes or examples.

## Step 9: Generate the introduction page

Run `.claude/scripts/generate_intros.py` to generate the intro-note
file for the new profile. The script writes to the path defined as
`uscdi_v7.intro_notes` in @.claude/config/paths.yml.

## Step 10: Generate example instances

Use @.claude/prompts/generate-example-from-profile.md to identify the
use cases the new profile must demonstrate.

1. Enumerate use cases first, then confirm with the user.
   - For MS elements with bound value sets, treat each code in the
     bound value set as a distinct use case
     (e.g., `criticality` {low | high | unable-to-assess} = 3 cases).
   - For reference elements with multiple `targetProfile`s, each
     target type can be a use case.
   - For coded elements with broad bindings, pick the USCDI Data
     Element variants (e.g., Medication vs Drug Class vs
     Non-Medication Allergy Intolerance).

2. For each enumerated use case, author one example using
   @.claude/prompts/generate-example-from-profile.md.

3. Do not stop after one example. Continue until every enumerated
   use case is covered.

Apply the `us-core-example-self-check` skill to each generated
example. Address FAIL findings; flag UNVERIFIED.