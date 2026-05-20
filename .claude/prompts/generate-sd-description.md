prompt to generated a SD description from claude-code

(Claude drafted:)


You are drafting the StructureDefinition.description for a US Core profile.
Match the voice, structure, and level of detail of existing US Core profiles exactly.

STEP 1 — Read these 6 exemplar profiles in full:
and the associated USCDI data Class and descriptions at /Users/ehaas/Documents/FHIR/US-Core/my-notes/USCDIV7/USCDI_Draft_Version7.pdf
  - Do not alter these files

1. US Core Patient Profile: /Users/ehaas/Documents/FHIR/US-Core/input/resources-yaml/StructureDefinition-us-core-patient.yml
   -  USCDI Patient Data Class
2. US Core Encounter Profile: /Users/ehaas/Documents/FHIR/US-Core/input/resources-yaml/StructureDefinition-us-core-encounter.yml
   - USCDI Encounter Data Class
3. US Core Condition Problems and Health Concerns Profile: /Users/ehaas/Documents/FHIR/US-Core/input/resources-yaml/StructureDefinition-us-core-condition-problems-health-concerns.yml
   - USCDI Problems Data Class
4. US Core Laboratory Result Observation Profile: /Users/ehaas/Documents/FHIR/US-Core/input/resources-yaml/StructureDefinition-us-core-observation-lab.yml
   - USCDI Laboratory Data Class
5. US Core ServiceRequest Profile: /Users/ehaas/Documents/FHIR/US-Core/input/resources-yaml/StructureDefinition-us-core-servicerequest.yml
   - USCDI Orders Data Class
   - USCDI Procedures Data Class
6. US Core DocumentReference Profile: /Users/ehaas/Documents/FHIR/US-Core/input/resources-yaml/StructureDefinition-us-core-documentreference.yml
   - USCDI Clinical Notes Data Class


Note: opening sentence patterns, paragraph structure, terminology choices,
where USCDI is mentioned, how mandatory elements are summarized.

STEP 2 — Read the target StructureDefinition:
Extract: `StructureDefinition.resourceType`, `StructureDefinition.baseDefinition`

STEP 3 — Review the FHIR base resources type (from `StructureDefinition.baseDefinition`) profile page narrative  "Scope and Usage" and "Boundaries and Relationships" sections at https://hl7.org/fhir/R4/[base-resource-type].html

STEP 3 — Draft the description following this structure in markdown format (note that variable content is in curly brackets {})

"The {Profile Name} inherits from the FHIR [{Base Profile}](https://hl7.org/fhir/R4/{base-profile}.html) resource; refer to it for scope and usage definitions. {Optional content about this profile's history} This profile meets the requirements of the U.S. Core Data for Interoperability (USCDI) *{Data Class(es) or Element(s)}*. It sets minimum expectations for the {Base Profile} resource to record, search, and fetch information about {what information this profile represents}. It specifies which core elements, extensions, vocabularies, and value sets SHALL be present in the resource and constrains how the elements are used. Providing the floor for standards development for specific use cases promotes interoperability and adoption."


STEP 4 — Apply voice constraints to bracketed fill-ins:
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
- Verify every factual claim against the SD
- Flag anything you're unsure about
- If the SD lacks a field an exemplar's description mentions (e.g., the exemplar references a binding the target doesn't have), omit rather than invent.

OUTPUT: The description text only, ready to drop into description:.
Do not include explanation or markdown unless the existing descriptions use it.