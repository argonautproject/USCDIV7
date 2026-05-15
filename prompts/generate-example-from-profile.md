prompt to generate a US Core example resource from a profile and a USCDI use case from claude-code


You are drafting a US Core example resource (YAML) that conforms to a target
US Core profile and illustrates a specific USCDI v7 use case.
Match the voice, structure, and level of detail of existing US Core examples exactly.

Prerequisites:

1. Get the Profile file or URL from the User
2. Get the USCDI Data Element or Class from the User
3. Get any other User constraints. For example, "use code x for foo.bar".

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

Note: opening sentence patterns for `instance-description`, indentation style,
how Must Support elements are populated, how references are formatted.

STEP 2 — Read the target US Core profile (path supplied by user) and extract:
  - `resourceType`, `type`, 2`baseDefinition`
  - Every element where `mustSupport: true` or `min >= 1` (these MUST be populated)
  - Every binding (`required`, `extensible`, `preferred`, `example`) — pick codes that satisfy the strength
  - Every reference `targetProfile` — these constrain which references are allowed
  - Slice definitions, invariants, and pattern values

STEP 3 — Read the USCDI v7 Data Class / Data Element description for the
intended use case at /Users/ehaas/Documents/FHIR/US-Core/my-notes/USCDIV7/USCDI_Draft_Version7.pdf
and  /Users/ehaas/Documents/FHIR/US-Core/my-notes/USCDIV7/healthit.gov-ONC Standards Bulletin 2026-1.pdf
and the tables summary at /Users/ehaas/Documents/FHIR/US-Core/my-notes/USCDIV7/USCDIV7_tables.md
  - Identify the specific Data Element and any "Usage note" text
  - Use that text to choose realistic clinical content (status, codes, dates, narrative)

STEP 4 — Resolve all references to existing US Core example instances only.
  - Allowed source: /Users/ehaas/Documents/FHIR/US-Core/input/examples-yaml/
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
  - Do NOT invent new reference ids. If no existing example fits a required
    reference, STOP and ask the user how to proceed.

STEP 5 — Draft the example as a YAML resource with this structure:

```yaml
resourceType: {ResourceType}
id: {short-descriptive-id}
meta:
  profile:
    - {target profile canonical URL}
  extension:
    - url: http://hl7.org/fhir/StructureDefinition/instance-name
      valueString: {Title-Cased Noun Phrase} Example
    - url: http://hl7.org/fhir/StructureDefinition/instance-description
      valueMarkdown: {One-sentence description ending in *{US Core Profile Name}*.}
{element population — Must Support and min>=1 elements first, then optional supporting elements}
```

  - `id`: short, lowercase, hyphenated; descriptive of the use case (e.g., `appt-booked-physical`)
  - `instance-name`: matches noun-phrase pattern of exemplars (`Serum Chloride Example`, `ServiceRequest EKG Example`)
  - `instance-description`: matches one of the exemplar patterns:
      - "This is a {use case} example for the *{Profile Name}*."
      - "This example of a *{Profile Name}* illustrates {use case detail}."

STEP 6 — Apply voice constraints to `instance-description` and any narrative:
- Present tense, third person. No "we," "you."
- RFC 2119 keywords (SHALL/SHOULD/MAY) used in the normative sense only.
  - Use "might" or "can" instead of "MAY"
- No marketing adjectives: "robust," "comprehensive," "seamless."
- No hedges: "typically," "generally," "may currently."
- Plain ASCII; straight quotes; no em dashes.
- Spell out acronyms on first use except FHIR, US Core, USCDI, HL7, SNOMED CT, LOINC.

STEP 7 — Self-check:
- Every Must Support and min>=1 element is populated.
- Every code is drawn from the profile's bound value set (or, for `example`
  strength, a reasonable code in the same code system).
- Every reference points to an existing example in
  /Users/ehaas/Documents/FHIR/US-Core/input/examples-yaml/ — verify by file
  presence, not memory.
- Every coded value's `system`, `code`, and `display` is verified against an
  authoritative source (SNOMED CT browser, LOINC, HL7 terminology) — do NOT
  invent codes. If a code cannot be verified, flag it.
- Dates are consistent with the use case (future for `booked` appointments,
  past for `fulfilled` / `finished` resources).
- All invariants on the profile are satisfied.

STEP 8 -OUTPUT
- The YAML resource only
- write to  - /Users/ehaas/Documents/FHIR/USCDIV7/input/examples-yaml/.
- Follow the resource file naming convention `{ResourceType}-{descriptive-id}.yml`.
- Flag any code, reference, or assumption you could not verify.
- If no other example of this type are in `/Users/ehaas/Documents/FHIR/USCDIV7/input/examples-yaml/`, use `/Users/ehaas/Documents/FHIR/USCDIV7/prompts/group_examples.md`  to create a new group.

yes
After the build is run, If there is a QA message error for an incorrect display for a code, then update the display names to match the first correct display name list in the QA message.
