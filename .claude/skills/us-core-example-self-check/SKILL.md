---
name: us-core-example-self-check
description: Validate a US Core example YAML file for common defects. This skill should be used after generating or editing any instance example, or whenever the user asks to "check," "validate," or "review" an example. Verifies Must Support coverage, value set conformance, reference integrity, code authenticity against SNOMED/LOINC/HL7, date plausibility, and invariant satisfaction. Flags unverified items rather than fabricating answers.
---

# US Core Example Self-Check

Run these checks against the target YAML file. Report findings as a table:
PASS / FAIL / UNVERIFIED, with the element path and a one-line reason.

## Checks

1. Every Must Support element and every min>=1 element is populated.
2. Every code is drawn from the bound value set, or — for `example`
   strength — a reasonable code in the same code system.
3. Apply terminology verification rules per fhir-terminology-verification skill before reporting findings.
4. Every example reference resolves to an existing example under
   `input/examples-yaml/`. Verify by file presence, not memory.
5. Dates are consistent with the use case: future for `booked`
   appointments, past for `fulfilled` or `finished` resources.
6. All inherited and new invariants are satisfied.
7. The `meta.profile` references an existing profile in `input/resources-yaml/`

## Output

A findings table followed by a one-paragraph summary. Do not modify
the source file. If a deterministic check script exists at
`scripts/run_checks.py`, run it first and use its output as input
to your review.
