You are updating a US Core example resource (YAML) that conforms to a target
US Core profile and illustrates a specific USCDI v7 use case.

INPUTS — read from .claude/config/update-example.yml
  - source_example   : path to the example to edit
  - target_profile   : US Core profile id the result must conform to
  - uscdi.class       / uscdi.element : the USCDI v7 data class/element
  - update            : natural-language description of the change to make
  - read_uscdi_source : if true, perform STEP 3
  - output_dir        : where to write the result
If update-example.yml is absent, STOP and report which inputs are missing.

STEP 1 — Read these 6 US Core examples in full as exemplars:
  - Do not alter these files

  1. Patient Example: /Users/ehaas/Documents/FHIR/US-Core/input/examples-yaml/patient-example.yml
    - US Core Patient Profile: /Users/ehaas/Documents/FHIR/US-Core/input/resources-yaml/StructureDefinition-us-core-patient.yml
  2. Encounter 1 Example: /Users/ehaas/Documents/FHIR/US-Core/input/examples-yaml/encounter-example-1.yml
    - US Core Encounter Profile: /Users/ehaas/Documents/FHIR/US-Core/input/resources-yaml/StructureDefinition-us-core-encounter.yml
  3. Condition Duodenal Ulcer Example: /Users/ehaas/Documents/FHIR/US-Core/input/examples-yaml/condition-duodenal-ulcer.yml
    - US Core Condition Problems and Health Concerns Profile: /Users/ehaas/Documents/FHIR/US-Core/input/resources-yaml/StructureDefinition-us-core-condition-problems-health-concerns.yml
  4. Serum Chloride Example: /Users/ehaas/Documents/FHIR/US-Core/input/examples-yaml/observation-serum-chloride.yml
    - US Core Laboratory Result Observation Profile: /Users/ehaas/Documents/FHIR/US-Core/input/resources-yaml/StructureDefinition-us-core-observation-lab.yml
  5. ServiceRequest EKG Example: /Users/ehaas/Documents/FHIR/US-Core/input/examples-yaml/servicerequest-ekg.yml
    - US Core ServiceRequest Profile: /Users/ehaas/Documents/FHIR/US-Core/input/resources-yaml/StructureDefinition-us-core-servicerequest.yml
  6. Clinician Authored Discharge Summary Example: /Users/ehaas/Documents/FHIR/US-Core/input/examples-yaml/documentreference-discharge-summary.yml
    - US Core DocumentReference Profile: /Users/ehaas/Documents/FHIR/US-Core/input/resources-yaml/StructureDefinition-us-core-documentreference.yml

  Note: how Must Support and additional USDCDI elements are populated, how references are formatted.

STEP 2 — Read the source_example and its target_profile StructureDefinition.
  Treat the source as a known-good scaffold. Change ONLY the elements implied
  by `update`; preserve all other content unchanged.


STEP 3 (only if read_uscdi_source is true) — Read the USCDI v7 sources:
   —  USCDI v7 Data Class / Data Element description for the
intended use case at /Users/ehaas/Documents/FHIR/US-Core/my-notes/USCDIV7/USCDI_Draft_Version7.pdf
   - /Users/ehaas/Documents/FHIR/US-Core/my-notes/USCDIV7/healthit.gov-ONC Standards Bulletin 2026-1.pdf
   - tables summary at /Users/ehaas/Documents/FHIR/US-Core/my-notes/USCDIV7/USCDIV7_tables.md

  Identify the named Data Element and any "Usage note" text, and use it to
  choose realistic clinical content (status, codes, dates, narrative).

STEP 4 — If updating a reference type element, resolve all references to existing US Core example instances only.
  - Allowed source: /Users/ehaas/Documents/FHIR/US-Core/input/examples-yaml/
  - Discover candidates by listing the examples directory; do NOT hardcode ids.
    (The ids below are illustrative, not authoritative — verify each.)
  - For each reference element on the profile, pick an existing example whose
    `resourceType` and (where applicable) `meta.profile` matches a `targetProfile`
    permitted by the profile.
  - Common targets and canonical example ids:
      Patient            → Patient/example
      Practitioner       → Practitioner/practitioner-1
      Location           → Location/hospital
      Encounter          → Encounter/example-1
      Organization       → check /Users/ehaas/Documents/FHIR/US-Core/input/examples-yaml/ for organization-*.yml
      RelatedPerson      → RelatedPerson/relatedperson-shaw-niece
      PractitionerRole   → check examples-yaml for practitionerrole-*.yml
   - references must resolve within the OUTPUT project's example set.
    Confirm referenced instances exist under output_dir's IG, not only US-Core.
  - Do NOT invent new reference ids. If no existing example fits a required
    reference, STOP and ask the user how to proceed.


STEP 5 -OUTPUT
- The YAML resource only
- write to  - /Users/ehaas/Documents/FHIR/USCDIV7/input/examples-yaml/.
- Follow the resource file naming convention `{ResourceType}-{descriptive-id}.yml`.
- After examples are written or modified, apply the
`us-core-example-self-check` skill to each. Address FAIL findings;
flag UNVERIFIED.
- If no other example of this type are in `/Users/ehaas/Documents/FHIR/USCDIV7/input/examples-yaml/`, use `/Users/ehaas/Documents/FHIR/USCDIV7/prompts/group_examples.md`  to create a new group.
- run build



