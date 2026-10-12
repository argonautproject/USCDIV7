# Codes Suppressed by US Core ignoreWarnings Entry 60

Suppressed message (`input/ignoreWarnings.txt`, entry 60; `%` is the IG Publisher
wildcard):

```
None of the codings provided are in the value set 'Screening and Assessment Survey Codes'
(http://cts.nlm.nih.gov/fhir/ValueSet/2.16.840.1.113762.1.4.1267.13|20260422),
and a coding is recommended to come from this value set%
```

Reported as 21 uses in `output/qa.html`. Each row is one `Observation.code` in an
example claiming the US Core Observation Screening Assessment Profile whose code
is not in the VSAC value set expansion version 20260422. All codes are LOINC
(`http://loinc.org`).

| Code | Display | Example |
|------|---------|---------|
| 9271-8 | 10 minute Apgar Score | Observation-10-minute-apgar-score |
| 32401-2 | 10 minute Apgar Color | Observation-10-minute-apgar-color |
| 32402-0 | 10 minute Apgar Heart Rate | Observation-10-minute-apgar-heart-rate |
| 32403-8 | 10 minute Apgar Muscle Tone | Observation-10-minute-apgar-muscle-tone |
| 32404-6 | 10 minute Apgar Reflex Irritability | Observation-10-minute-apgar-reflex-irritability |
| 32405-3 | 10 minute Apgar Respiratory effort | Observation-10-minute-apgar-respiratory-effort |
| 32624-9 | Race | Observation-PRAPARE-multiselect-item-example-32624-9-answer0 |
| 32624-9 | Race | Observation-PRAPARE-multiselect-item-example-32624-9-answer1 |
| 54899-0 | Preferred language | Observation-PRAPARE-item-example-54899-0 |
| 56051-6 | Hispanic or Latino | Observation-PRAPARE-item-example-56051-6 |
| 56799-0 | Address | Observation-PRAPARE-item-example-56799-0 |
| 63512-8 | How many people are living or staying at this address [#] | Observation-PRAPARE-item-example-63512-8 |
| 63586-2 | What was your best estimate of the total income of all family members from all sources, before taxes, in last year [PhenX] | Observation-PRAPARE-item-example-63586-2 |
| 67875-5 | Employment status current | Observation-PRAPARE-item-example-67875-5 |
| 68519-8 | How many standard drinks containing alcohol do you have on a typical day | Observation-AUDIT-C-item-example-68519-8 |
| 68520-6 | How often do you have 6 or more drinks on 1 occasion | Observation-AUDIT-C-item-example-68520-6 |
| 76437-3 | Primary insurance | Observation-PRAPARE-item-example-76437-3 |
| 82589-3 | Highest level of educ | Observation-PRAPARE-item-example-82589-3 |
| 93038-8 | Stress level | Observation-PRAPARE-item-example-93038-8 |
| 96842-0 | How often have you used any tobacco product in past 12 months | Observation-TAPS-item-example-96842-0 |
| 96843-8 | How often have you used illegal or recreational drugs in past 12 months | Observation-TAPS-item-example-96843-8 |

Distinct codes: 20 (32624-9 appears in two examples).

The binding is `Observation.code`, strength `preferred`, in
`input/resources-yaml/StructureDefinition-us-core-observation-screening-assessment.yml`.
The value set holds LOINC panel codes, so panel examples validate and these
item-level codes do not; tracked as FHIR-56786.
