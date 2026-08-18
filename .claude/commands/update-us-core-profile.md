# Update a US Core Profile

You are updating a US Core Profile (YAML) to meet a specific USCDI v7
Data Element or Class. Match the voice, structure, and level of detail
of existing US Core profiles exactly.

## Paths

External repo paths come from @.claude/config/paths.yml. The keys this
command uses:

- `us_core.intro_notes` — source intro-note files in the US Core repo
- `uscdi_v7.profiles` — where to write the updated profile YAML
- `uscdi_v7.intro_notes` — where to write the updated intro note

Internal project files (scripts, prompts, skills) use relative paths
from the project root.

## Step 1: Prerequisites

Collect the following from the user before proceeding:

1. Source US Core Profile file — must be a differential-only YAML.
2. USCDI Data Element or Class to satisfy.
3. User constraints (e.g., "add element foo.bar").
4. Any additional constraints or bindings to confirm.

## Step 2: Voice and style

Apply the voice and style rules defined in CLAUDE.md to all narrative
content: `instance-description`, intro notes, and any prose.
Non-negotiable.

## Step 3: Generate the profile YAML

Produce the updated profile YAML resource only based on the user's defined requirements in Step 1

- Update `StructureDefinition.description` only if there is a new USCDI Data Class associated with the existing profile.
  - Any updated `StructureDefinition.description` must be reviewed with the user before applying to the existing profile.
- Differential only — no snapshot.
- Element order matches the base StructureDefinition.
- Each new element includes the appropriate type and cardinality. For a
  bound element, use the binding and strength from the Step 1
  requirements; if not specified there, restate the base binding
  `valueSet` and `strength` in the differential so they render. A
  binding left out of the differential is not shown in the differential
  view. Omit the base binding `description`.
- Each new element includes the Must Support or the Additional USCDI (not both) as defined in the requirements in Step 1
- Element includes only short description and/or description if defined in the requirements in Step 1
- Do not invent codes, value sets, or extension URLs. Flag any
  binding or extension URL that cannot be verified.

## Step 4: Run the conformance self-check

Apply the `us-core-conformance-self-check` skill to the generated
YAML. Address any FAIL findings before proceeding. Flag UNVERIFIED
items in the final summary.

## Step 5: Write the output

Produce the updated profile YAML resource only.

- Write to the path defined as `uscdi_v7.profiles` in
  @.claude/config/paths.yml.
- Follow the naming convention `{ResourceType}-{descriptive-id}.yml`.

## Step 6: Update the Profile Introduction markdown

Source file: `us_core.intro_notes` directory in
@.claude/config/paths.yml, filename
`StructureDefinition-us-core-<profile-id>-notes.md`.

Steps:

1. Insert the new element(s) into the appropriate list — "Must Have,"
   "Must Support," or "Additional USCDI" — in StructureDefinition
   element order.
2. Do NOT execute `.claude/scripts/generate_intros.py`. Read it to
   determine the correct naming convention for the list entries, then
   apply that convention manually.
3. Insert the following include block before the final include on the
   intro page (paste verbatim, including the Liquid escaping):

```liquid
{# remove this before move to US Core #}
{% include structure-table-block.md file_name="{{ file_name }}" %}
```
   1. Write the updated file to the path defined as
   `uscdi_v7.intro_notes` in @.claude/config/paths.yml.

## Step 7: Update or create examples

Use @.claude/prompts/generate-example-from-profile.md to identify the
use cases the profile must demonstrate. (follow the step to review USCDI for suggested examples)

1. Enumerate use cases first, then confirm with the user.
   - For new/modified MS elements with bound value sets, treat each
     code in the bound value set as a distinct use case
     (e.g., `criticality` {low | high | unable-to-assess} = 3 cases).
   - For reference elements with multiple `targetProfile`s, each
     target type can be a use case.
   - For coded elements with broad bindings, pick the USCDI Data
     Element variants (e.g., Medication vs Drug Class vs
     Non-Medication Allergy Intolerance).

2. For each enumerated use case:
   a. Check whether an existing example covers it. The authoritative
      inventory is the file defined as `uscore-ig-json`.
   b. If an existing example matches, add the new elements to it.
      -  Do not rename the id or Title of the example.
   c. If no existing example matches, create a new one using
      @.claude/prompts/generate-example-from-profile.md.

3. Do not stop after one example. Continue until every enumerated
   use case is covered by either an existing example (per
   `uscore-ig-json`) or a newly authored one.

After examples are written or modified, apply the
`us-core-example-self-check` skill to each. Address FAIL findings;
flag UNVERIFIED.