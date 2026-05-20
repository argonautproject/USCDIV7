---
name: us-core-conformance-self-check
description: Validate a US Core StructureDefinition/S/CodeSystem/OperationDefinition/SearchParameter YAML file for common defects. This skill should be used after generating or editing any Profile/ValueSet/etc whenever the user asks to "check," "validate," or "review" a Profile/ValueSet/etc. Verifies complies with base conformance artifact, value set conformance, code authenticity against SNOMED/LOINC/HL7, and invariant satisfaction. Flags unverified items rather than fabricating answers.
---

# US Core Conformance Artifact Self-Check

Run these checks against the target YAML file. Report findings as a table:
PASS / FAIL / UNVERIFIED, with the element path and a one-line reason.

## Self Check:
- Except for extensions and slices, no new elements that are not in base
- Order of elements matches base
- Every element's cardinality >= to the base element
- Unless explicitly changed in the prerequisite requirements, every binding  and strength = base binding and binding strength
- Every code is drawn from the bound value set (or, for `example`
  strength, a reasonable code in the same code system).
- Apply terminology verification rules per fhir-terminology-verification skill before reporting findings.
- All choice data type elements are present.
- All target references are present.
- For all target reference types represented by one or more US Core profiles, reference the profile(s) instead of the base profiles.
  - Exceptions
      1. Observation:  Unless instructed in step 1, do not use US Core Observation Profiles since there are many US Core Observation Profile it would be unwieldy to list them all.
      2. US Core ADI DocumentReference Profile - prompt user before referencing if not instructed in step 1.
      3. PractitionerRole: do not use US Core PractitionerRole Profile is not a first class profile
- All invariants on the profile are satisfied.