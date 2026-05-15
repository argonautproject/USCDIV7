Create a new US Core  Profile


You are updating a US Core Profile (YAML) to meet a specific USCDI v7 Data element or class.
Match the voice, structure, and level of detail of existing US Core examples exactly.

Step 1 - Prerequisites:


1. Provide the Profile Name or id
2. Get the source US Core Profile(s) file from the User to use as as example template StructureDefinition
3. Get the USCDI Data Element or Class from the User that is profile represents
4. Get the  Mandatory (m = mandatory in base), Must Support  and Additional USCDI elements from the User
5. Confirm if there are any constraints or bindings.

=========== Example Input ==================

1. US Core MedicationAdministration Profile
2. Use US Core MedicationRequest  and US Core MedicationDosage as example template StructureDefinitions
    -  /Users/ehaas/Documents/FHIR/US-Core/input/resources-yaml/StructureDefinition-us-core-medicationrequest.yml
    -  /Users/ehaas/Documents/FHIR/US-Core/input/resources-yaml/StructureDefinition-us-core-medicationdosage.yml
3. This for the USCDI V7 Medications Data Class
4. Include only these Mandatory (m = mandatory in base) and Must Support elements: status (m), medication[x] (m), subject (m), effective[x] (m), performer, request, dosageInstruction
5. Bindings are the  same as for US Core MedicationRequest for:
   - MedicationCategory.category:us-core
   - MedicationCategory.medication[x]
   - MedicationCategory.dosageInstruction sub elements

===============================================

Step 2 - Reference the Base FHIR R4 StructureDefinition

-  reference the base FHIR R4 DeviceRequestP Profile at
  /Users/ehaas/.fhir/packages/hl7.fhir.r4.core#4.0.1

Step 3 -  Apply voice constraints to `instance-description` and any narrative:
- Present tense, third person. No "we," "you."
- RFC 2119 keywords (SHALL/SHOULD/MAY) used in the normative sense only.
  - Use "might" or "can" instead of "MAY"
- No marketing adjectives: "robust," "comprehensive," "seamless."
- No hedges: "typically," "generally," "may currently."
- Plain ASCII; straight quotes; no em dashes.
- Spell out acronyms on first use except FHIR, US Core, USCDI, HL7, SNOMED CT, LOINC.

Step 4 - Self Check:
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
- All choice data type elements are present.
- All target references are present.
- For all target reference types that are represented by 1 or more US Core profiles need to reference the profile(s) instead of the base profiles.
  - Exceptions
      1. Observation:  Unless instructed in step 1, do not use US Core Observation Profiles since there are many US Core Observation Profile it would be unwieldy to list them all.
      2. US Core ADI DocumentReference Profile - prompt user before referencing if not instructed in step 1.
      3. PractitionerRole: do not use US Core PractitionerRole Profile is not a first class profile
- All invariants on the profile are satisfied.


Step 5  - Output and Summary

1. OUTPUT: The YAML resource only, ready to drop into
/Users/ehaas/Documents/FHIR/USCDIV7/input/resources-yaml/.
Follow the resource file naming convention `{ResourceType}-{descriptive-id}.yml`.
Flag any code, reference, or assumption you could not verify.

Step 6 -  Generate an introduction

1. use /Users/ehaas/Documents/FHIR/USCDIV7/scripts/generate_intros.py to generate the introduction page

Step 7 -  Generate example instances

2. use `/Users/ehaas/Documents/FHIR/USCDIV7/prompts/generate-example-from-profile.md`
to generate examples


