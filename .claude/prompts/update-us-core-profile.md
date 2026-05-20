prompt to update a US Core Profile

You are updating a US Core Profile (YAML) to meet a specific USCDI v7 Data element or class.
Match the voice, structure, and level of detail of existing US Core examples exactly.

Step 1 - Prerequisites:

1. Get the source US Core Profile file from the User - it should be a differential only yaml file.
2. Get the USCDI Data Element or Class from the User
3. Get the User constraints. For example, "add element foo.bar".
4. Confirm if there are any constraints or bindings.


5. Apply voice constraints to `instance-description` and any narrative:
- Present tense, third person. No "we," "you."
- RFC 2119 keywords (SHALL/SHOULD/MAY) used in the normative sense only.
  - Use "might" or "can" instead of "MAY"
- No marketing adjectives: "robust," "comprehensive," "seamless."
- No hedges: "typically," "generally," "may currently."
- Plain ASCII; straight quotes; no em dashes.
- Spell out acronyms on first use except FHIR, US Core, USCDI, HL7, SNOMED CT, LOINC.

1. Self Check:
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

1. OUTPUT: The YAML resource only, ready to drop into
/Users/ehaas/Documents/FHIR/USCDIV7/input/resources-yaml/.
Follow the resource file naming convention `{ResourceType}-{descriptive-id}.yml`.
Flag any code, reference, or assumption you could not verify.

1. use /Users/ehaas/Documents/FHIR/USCDIV7/scripts/generate_intros.py to generate the introduction page

2. use `/Users/ehaas/Documents/FHIR/USCDIV7/prompts/generate-example-from-profile.md`
to generate examples
