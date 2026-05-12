prompt to generated an example title and description from claude-code

(Claude drafted:)

You are drafting an example title and description for a US Core example
Match the voice, structure, and level of detail of existing US Core examples.

STEP 1 — Read these 6 US Core examples in full:
and the associated US Core Profile they are based upon.
  - Do not alter these files

1. Patient Example: /Users/ehaas/Documents/FHIR/US-Core/input/examples-yaml/patient-example.yml
   - US Core Patient Profile: /Users/ehaas/Documents/FHIR/US-Core/input/resources-yaml/StructureDefinition-us-core-patient.yml
2. Encounter 1 Example: /Users/ehaas/Documents/FHIR/US-Core/input/examples-yaml/encounter-example-1.yml
   - US Core Encounter Profile: /Users/ehaas/Documents/FHIR/US-Core/input/resources-yaml/StructureDefinition-us-core-encounter.yml
3. Condition Duodenal Ulcer Example: /Users/ehaas/Documents/FHIR/US-Core/input/examples-yaml/condition-duodenal-ulcer.yml
   -  US Core Condition Problems and Health Concerns Profile: /Users/ehaas/Documents/FHIR/US-Core/input/resources-yaml/StructureDefinition-us-core-condition-problems-health-concerns.yml
4. Serum Chloride Example: /Users/ehaas/Documents/FHIR/US-Core/input/examples-yaml/observation-serum-chloride.yml
   - US Core Laboratory Result Observation Profile: /Users/ehaas/Documents/FHIR/US-Core/input/resources-yaml/StructureDefinition-us-core-observation-lab.yml
5. ServiceRequest EKG Example: /Users/ehaas/Documents/FHIR/US-Core/input/examples-yaml/servicerequest-ekg.yml
   - US Core ServiceRequest Profile: /Users/ehaas/Documents/FHIR/US-Core/input/resources-yaml/StructureDefinition-us-core-servicerequest.yml
6. Clinician Authored Discharge Summary Example: /Users/ehaas/Documents/FHIR/US-Core/input/examples-yaml/documentreference-discharge-summary.yml
   - US Core DocumentReference Profile: /Users/ehaas/Documents/FHIR/US-Core/input/resources-yaml/StructureDefinition-us-core-documentreference.yml


STEP 2 — Read the target Example: `.meta.extension` for instance-name and instance-description

STEP 3 — Draft the title and description as  yaml formated `.meta.extension` elements

STEP 4 — Apply voice constraints
- Present tense, third person. No "we," "you."
- RFC 2119 keywords (SHALL/SHOULD/MAY) used in the normative sense only.
  - Use "might" or "can" instead of "MAY"
- No marketing adjectives: "robust," "comprehensive," "seamless."
- No hedges: "typically," "generally," "may currently."
- Plain ASCII; straight quotes; no em dashes.
- Spell out acronyms on first use except FHIR, US Core, USCDI, HL7, SNOMED CT, LOINC.
- The history bracket is omitted unless the SD or its exemplars supply a concrete fact (deprecation, version change, derivation note). Do not invent history to fill the slot.

STEP 5 — Self-check:
- Compare voice/structure against exemplars
- Flag anything you're unsure about

OUTPUT: The description text only, ready to drop into the example as `.meta.extension`

