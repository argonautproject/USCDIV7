# US Core OID comparison: v7.0.0 vs v8.0.1

Sources:
- v7: /Users/ehaas/Documents/FHIR/USCDIV7/USCORE7-oids.ini (constructed from `~/.fhir/packages/hl7.fhir.us.core#7.0.0/package`)
- v8: /Users/ehaas/Documents/FHIR/USCDIV7/USCORE8-oids.ini (authoritative oids.ini for v8.0.1)

Review date: 2026-05-11

---

## Headline numbers

| Type | v7 count | v8 count | same OID | OID changed | only v7 | only v8 |
|---|---:|---:|---:|---:|---:|---:|
| CodeSystem | 5 | 5 | 5 | **0** | 0 | 0 |
| ValueSet | 29 | 21 | 0 | **18** | 11 | 3 |
| StructureDefinition | 63 | 68 | 0 | **63** | 0 | 5 |
| OperationDefinition | 1 | 1 | 1 | **0** | 0 | 0 |
| SearchParameter | 110 | 108 | 74 | **34** | 2 | 0 |
| CapabilityStatement | 2 | 2 | 2 | **0** | 0 | 0 |
| Library | 0 | 6 | 0 | **0** | 0 | 6 |
| Questionnaire | 0 | 6 | 0 | **0** | 0 | 6 |

**Headline:** Every matched StructureDefinition OID changed (63 of 63), and every matched ValueSet OID changed (18 of 18). CodeSystem, OperationDefinition, and CapabilityStatement stayed stable. Library and Questionnaire are new in v8.

## Pattern

If the publisher had treated `oids.ini` as authoritative across releases, v7 tail numbers would have been preserved and only **new** resources would have received new tails. Instead the entire numbering reshuffled — the same regenerate-from-scratch behavior observed between 8.0.1 → dev. Examples:

- `head-occipital-frontal-circumference-percentile`: **.61 → .1** (then .68 in dev)
- `us-core-patient`: **.62 → .50** (then .69 in dev)
- `us-core-servicerequest`: **.63 → .60** (then .70 in dev)
- `us-core-vital-signs`: **.60 → .68** (then .67 in dev)

---

## ValueSet: ids with DIFFERENT OID (18)

| id | v7 OID | v8 OID |
|---|---|---|
| `us-core-clinical-note-type` | `2.16.840.1.113883.4.642.40.2.48.5` | `2.16.840.1.113883.4.642.40.2.48.1` |
| `us-core-clinical-result-observation-category` | `2.16.840.1.113883.4.642.40.2.48.6` | `2.16.840.1.113883.4.642.40.2.48.2` |
| `us-core-condition-code` | `2.16.840.1.113883.4.642.40.2.48.21` | `2.16.840.1.113883.4.642.40.2.48.16` |
| `us-core-diagnosticreport-category` | `2.16.840.1.113883.4.642.40.2.48.7` | `2.16.840.1.113883.4.642.40.2.48.4` |
| `us-core-diagnosticreport-report-and-note-codes` | `2.16.840.1.113883.4.642.40.2.48.8` | `2.16.840.1.113883.4.642.40.2.48.5` |
| `us-core-documentreference-category` | `2.16.840.1.113883.4.642.40.2.48.10` | `2.16.840.1.113883.4.642.40.2.48.6` |
| `us-core-documentreference-type` | `2.16.840.1.113883.4.642.40.2.48.11` | `2.16.840.1.113883.4.642.40.2.48.7` |
| `us-core-goal-description` | `2.16.840.1.113883.4.642.40.2.48.23` | `2.16.840.1.113883.4.642.40.2.48.17` |
| `us-core-laboratory-test-codes` | `2.16.840.1.113883.4.642.40.2.48.24` | `2.16.840.1.113883.4.642.40.2.48.18` |
| `us-core-narrative-status` | `2.16.840.1.113883.4.642.40.2.48.12` | `2.16.840.1.113883.4.642.40.2.48.8` |
| `us-core-observation-smoking-status-status` | `2.16.840.1.113883.4.642.40.2.48.13` | `2.16.840.1.113883.4.642.40.2.48.9` |
| `us-core-problem-or-health-concern` | `2.16.840.1.113883.4.642.40.2.48.25` | `2.16.840.1.113883.4.642.40.2.48.19` |
| `us-core-procedure-code` | `2.16.840.1.113883.4.642.40.2.48.26` | `2.16.840.1.113883.4.642.40.2.48.20` |
| `us-core-provenance-participant-type` | `2.16.840.1.113883.4.642.40.2.48.16` | `2.16.840.1.113883.4.642.40.2.48.10` |
| `us-core-screening-assessment-condition-category` | `2.16.840.1.113883.4.642.40.2.48.17` | `2.16.840.1.113883.4.642.40.2.48.11` |
| `us-core-screening-assessment-observation-category` | `2.16.840.1.113883.4.642.40.2.48.18` | `2.16.840.1.113883.4.642.40.2.48.12` |
| `us-core-servicerequest-category` | `2.16.840.1.113883.4.642.40.2.48.27` | `2.16.840.1.113883.4.642.40.2.48.21` |
| `us-core-simple-observation-category` | `2.16.840.1.113883.4.642.40.2.48.19` | `2.16.840.1.113883.4.642.40.2.48.14` |

## ValueSet: only in v7 (dropped in v8)

| id | OID |
|---|---|
| `detailed-ethnicity` | `2.16.840.1.113883.4.642.40.2.48.1` |
| `detailed-race` | `2.16.840.1.113883.4.642.40.2.48.2` |
| `omb-ethnicity-category` | `2.16.840.1.113883.4.642.40.2.48.3` |
| `omb-race-category` | `2.16.840.1.113883.4.642.2.575` |
| `simple-language` | `2.16.840.1.113883.4.642.40.2.48.4` |
| `us-core-discharge-disposition` | `2.16.840.1.113883.4.642.40.2.48.9` |
| `us-core-encounter-type` | `2.16.840.1.113883.4.642.40.2.48.22` |
| `us-core-pregnancy-intent` | `2.16.840.1.113883.4.642.40.2.48.14` |
| `us-core-pregnancy-status` | `2.16.840.1.113883.4.642.40.2.48.15` |
| `us-core-survey-codes` | `2.16.840.1.113883.4.642.40.2.48.20` |
| `us-core-usps-state` | `2.16.840.1.113883.4.642.3.40` |

## ValueSet: only in v8 (added since v7)

| id | OID |
|---|---|
| `us-core-condition-code-current` | `2.16.840.1.113883.4.642.40.2.48.3` |
| `us-core-screening-assessment-observation-maximum-category` | `2.16.840.1.113883.4.642.40.2.48.13` |
| `us-core-specimen-condition` | `2.16.840.1.113883.4.642.40.2.48.15` |

## StructureDefinition: ids with DIFFERENT OID (63)

| id | v7 OID | v8 OID |
|---|---|---|
| `head-occipital-frontal-circumference-percentile` | `2.16.840.1.113883.4.642.40.2.42.61` | `2.16.840.1.113883.4.642.40.2.42.1` |
| `pediatric-bmi-for-age` | `2.16.840.1.113883.4.642.40.2.42.1` | `2.16.840.1.113883.4.642.40.2.42.2` |
| `pediatric-weight-for-height` | `2.16.840.1.113883.4.642.40.2.42.2` | `2.16.840.1.113883.4.642.40.2.42.3` |
| `us-core-allergyintolerance` | `2.16.840.1.113883.4.642.40.2.42.3` | `2.16.840.1.113883.4.642.40.2.42.5` |
| `us-core-average-blood-pressure` | `2.16.840.1.113883.4.642.40.2.42.4` | `2.16.840.1.113883.4.642.40.2.42.7` |
| `us-core-birthsex` | `2.16.840.1.113883.4.642.40.2.42.5` | `2.16.840.1.113883.4.642.40.2.42.8` |
| `us-core-blood-pressure` | `2.16.840.1.113883.4.642.40.2.42.6` | `2.16.840.1.113883.4.642.40.2.42.9` |
| `us-core-bmi` | `2.16.840.1.113883.4.642.40.2.42.7` | `2.16.840.1.113883.4.642.40.2.42.10` |
| `us-core-body-height` | `2.16.840.1.113883.4.642.40.2.42.8` | `2.16.840.1.113883.4.642.40.2.42.11` |
| `us-core-body-temperature` | `2.16.840.1.113883.4.642.40.2.42.9` | `2.16.840.1.113883.4.642.40.2.42.12` |
| `us-core-body-weight` | `2.16.840.1.113883.4.642.40.2.42.10` | `2.16.840.1.113883.4.642.40.2.42.13` |
| `us-core-care-experience-preference` | `2.16.840.1.113883.4.642.40.2.42.11` | `2.16.840.1.113883.4.642.40.2.42.14` |
| `us-core-careplan` | `2.16.840.1.113883.4.642.40.2.42.12` | `2.16.840.1.113883.4.642.40.2.42.15` |
| `us-core-careteam` | `2.16.840.1.113883.4.642.40.2.42.13` | `2.16.840.1.113883.4.642.40.2.42.16` |
| `us-core-condition-encounter-diagnosis` | `2.16.840.1.113883.4.642.40.2.42.14` | `2.16.840.1.113883.4.642.40.2.42.17` |
| `us-core-condition-problems-health-concerns` | `2.16.840.1.113883.4.642.40.2.42.15` | `2.16.840.1.113883.4.642.40.2.42.18` |
| `us-core-coverage` | `2.16.840.1.113883.4.642.40.2.42.16` | `2.16.840.1.113883.4.642.40.2.42.19` |
| `us-core-diagnosticreport-lab` | `2.16.840.1.113883.4.642.40.2.42.17` | `2.16.840.1.113883.4.642.40.2.42.20` |
| `us-core-diagnosticreport-note` | `2.16.840.1.113883.4.642.40.2.42.18` | `2.16.840.1.113883.4.642.40.2.42.21` |
| `us-core-direct` | `2.16.840.1.113883.4.642.40.2.42.19` | `2.16.840.1.113883.4.642.40.2.42.22` |
| `us-core-documentreference` | `2.16.840.1.113883.4.642.40.2.42.20` | `2.16.840.1.113883.4.642.40.2.42.23` |
| `us-core-encounter` | `2.16.840.1.113883.4.642.40.2.42.21` | `2.16.840.1.113883.4.642.40.2.42.24` |
| `us-core-ethnicity` | `2.16.840.1.113883.4.642.40.2.42.22` | `2.16.840.1.113883.4.642.40.2.42.25` |
| `us-core-extension-questionnaire-uri` | `2.16.840.1.113883.4.642.40.2.42.23` | `2.16.840.1.113883.4.642.40.2.42.26` |
| `us-core-genderIdentity` | `2.16.840.1.113883.4.642.40.2.42.24` | `2.16.840.1.113883.4.642.40.2.42.27` |
| `us-core-goal` | `2.16.840.1.113883.4.642.40.2.42.25` | `2.16.840.1.113883.4.642.40.2.42.28` |
| `us-core-head-circumference` | `2.16.840.1.113883.4.642.40.2.42.26` | `2.16.840.1.113883.4.642.40.2.42.29` |
| `us-core-heart-rate` | `2.16.840.1.113883.4.642.40.2.42.27` | `2.16.840.1.113883.4.642.40.2.42.30` |
| `us-core-immunization` | `2.16.840.1.113883.4.642.40.2.42.28` | `2.16.840.1.113883.4.642.40.2.42.31` |
| `us-core-implantable-device` | `2.16.840.1.113883.4.642.40.2.42.29` | `2.16.840.1.113883.4.642.40.2.42.32` |
| `us-core-jurisdiction` | `2.16.840.1.113883.4.642.40.2.42.30` | `2.16.840.1.113883.4.642.40.2.42.35` |
| `us-core-location` | `2.16.840.1.113883.4.642.40.2.42.31` | `2.16.840.1.113883.4.642.40.2.42.36` |
| `us-core-medication` | `2.16.840.1.113883.4.642.40.2.42.33` | `2.16.840.1.113883.4.642.40.2.42.38` |
| `us-core-medication-adherence` | `2.16.840.1.113883.4.642.40.2.42.32` | `2.16.840.1.113883.4.642.40.2.42.37` |
| `us-core-medicationdispense` | `2.16.840.1.113883.4.642.40.2.42.34` | `2.16.840.1.113883.4.642.40.2.42.39` |
| `us-core-medicationrequest` | `2.16.840.1.113883.4.642.40.2.42.35` | `2.16.840.1.113883.4.642.40.2.42.40` |
| `us-core-observation-clinical-result` | `2.16.840.1.113883.4.642.40.2.42.36` | `2.16.840.1.113883.4.642.40.2.42.42` |
| `us-core-observation-lab` | `2.16.840.1.113883.4.642.40.2.42.37` | `2.16.840.1.113883.4.642.40.2.42.43` |
| `us-core-observation-occupation` | `2.16.840.1.113883.4.642.40.2.42.38` | `2.16.840.1.113883.4.642.40.2.42.44` |
| `us-core-observation-pregnancyintent` | `2.16.840.1.113883.4.642.40.2.42.39` | `2.16.840.1.113883.4.642.40.2.42.45` |
| `us-core-observation-pregnancystatus` | `2.16.840.1.113883.4.642.40.2.42.40` | `2.16.840.1.113883.4.642.40.2.42.46` |
| `us-core-observation-screening-assessment` | `2.16.840.1.113883.4.642.40.2.42.41` | `2.16.840.1.113883.4.642.40.2.42.47` |
| `us-core-observation-sexual-orientation` | `2.16.840.1.113883.4.642.40.2.42.42` | `2.16.840.1.113883.4.642.40.2.42.48` |
| `us-core-organization` | `2.16.840.1.113883.4.642.40.2.42.43` | `2.16.840.1.113883.4.642.40.2.42.49` |
| `us-core-patient` | `2.16.840.1.113883.4.642.40.2.42.62` | `2.16.840.1.113883.4.642.40.2.42.50` |
| `us-core-practitioner` | `2.16.840.1.113883.4.642.40.2.42.44` | `2.16.840.1.113883.4.642.40.2.42.51` |
| `us-core-practitionerrole` | `2.16.840.1.113883.4.642.40.2.42.45` | `2.16.840.1.113883.4.642.40.2.42.52` |
| `us-core-procedure` | `2.16.840.1.113883.4.642.40.2.42.46` | `2.16.840.1.113883.4.642.40.2.42.53` |
| `us-core-provenance` | `2.16.840.1.113883.4.642.40.2.42.47` | `2.16.840.1.113883.4.642.40.2.42.54` |
| `us-core-pulse-oximetry` | `2.16.840.1.113883.4.642.40.2.42.48` | `2.16.840.1.113883.4.642.40.2.42.55` |
| `us-core-questionnaireresponse` | `2.16.840.1.113883.4.642.40.2.42.49` | `2.16.840.1.113883.4.642.40.2.42.56` |
| `us-core-race` | `2.16.840.1.113883.4.642.40.2.42.50` | `2.16.840.1.113883.4.642.40.2.42.57` |
| `us-core-relatedperson` | `2.16.840.1.113883.4.642.40.2.42.51` | `2.16.840.1.113883.4.642.40.2.42.58` |
| `us-core-respiratory-rate` | `2.16.840.1.113883.4.642.40.2.42.52` | `2.16.840.1.113883.4.642.40.2.42.59` |
| `us-core-servicerequest` | `2.16.840.1.113883.4.642.40.2.42.63` | `2.16.840.1.113883.4.642.40.2.42.60` |
| `us-core-sex` | `2.16.840.1.113883.4.642.40.2.42.53` | `2.16.840.1.113883.4.642.40.2.42.61` |
| `us-core-simple-observation` | `2.16.840.1.113883.4.642.40.2.42.54` | `2.16.840.1.113883.4.642.40.2.42.62` |
| `us-core-smokingstatus` | `2.16.840.1.113883.4.642.40.2.42.55` | `2.16.840.1.113883.4.642.40.2.42.63` |
| `us-core-specimen` | `2.16.840.1.113883.4.642.40.2.42.56` | `2.16.840.1.113883.4.642.40.2.42.64` |
| `us-core-treatment-intervention-preference` | `2.16.840.1.113883.4.642.40.2.42.57` | `2.16.840.1.113883.4.642.40.2.42.65` |
| `us-core-tribal-affiliation` | `2.16.840.1.113883.4.642.40.2.42.58` | `2.16.840.1.113883.4.642.40.2.42.66` |
| `us-core-vital-signs` | `2.16.840.1.113883.4.642.40.2.42.60` | `2.16.840.1.113883.4.642.40.2.42.68` |
| `uscdi-requirement` | `2.16.840.1.113883.4.642.40.2.42.59` | `2.16.840.1.113883.4.642.40.2.42.67` |

## StructureDefinition: only in v8 (added since v7)

| id | OID |
|---|---|
| `us-core-adi-documentreference` | `2.16.840.1.113883.4.642.40.2.42.4` |
| `us-core-authentication-time` | `2.16.840.1.113883.4.642.40.2.42.6` |
| `us-core-individual-sex` | `2.16.840.1.113883.4.642.40.2.42.33` |
| `us-core-interpreter-needed` | `2.16.840.1.113883.4.642.40.2.42.34` |
| `us-core-observation-adi-documentation` | `2.16.840.1.113883.4.642.40.2.42.41` |

## SearchParameter: ids with DIFFERENT OID (34)

| id | v7 OID | v8 OID |
|---|---|---|
| `us-core-location-address` | `2.16.840.1.113883.4.642.40.2.40.55` | `2.16.840.1.113883.4.642.40.2.40.58` |
| `us-core-location-address-city` | `2.16.840.1.113883.4.642.40.2.40.56` | `2.16.840.1.113883.4.642.40.2.40.55` |
| `us-core-location-address-postalcode` | `2.16.840.1.113883.4.642.40.2.40.57` | `2.16.840.1.113883.4.642.40.2.40.56` |
| `us-core-location-address-state` | `2.16.840.1.113883.4.642.40.2.40.58` | `2.16.840.1.113883.4.642.40.2.40.57` |
| `us-core-patient-given` | `2.16.840.1.113883.4.642.40.2.40.81` | `2.16.840.1.113883.4.642.40.2.40.79` |
| `us-core-patient-id` | `2.16.840.1.113883.4.642.40.2.40.82` | `2.16.840.1.113883.4.642.40.2.40.80` |
| `us-core-patient-identifier` | `2.16.840.1.113883.4.642.40.2.40.83` | `2.16.840.1.113883.4.642.40.2.40.81` |
| `us-core-patient-name` | `2.16.840.1.113883.4.642.40.2.40.84` | `2.16.840.1.113883.4.642.40.2.40.82` |
| `us-core-practitioner-id` | `2.16.840.1.113883.4.642.40.2.40.85` | `2.16.840.1.113883.4.642.40.2.40.83` |
| `us-core-practitioner-identifier` | `2.16.840.1.113883.4.642.40.2.40.86` | `2.16.840.1.113883.4.642.40.2.40.84` |
| `us-core-practitioner-name` | `2.16.840.1.113883.4.642.40.2.40.87` | `2.16.840.1.113883.4.642.40.2.40.85` |
| `us-core-practitionerrole-practitioner` | `2.16.840.1.113883.4.642.40.2.40.88` | `2.16.840.1.113883.4.642.40.2.40.86` |
| `us-core-practitionerrole-specialty` | `2.16.840.1.113883.4.642.40.2.40.89` | `2.16.840.1.113883.4.642.40.2.40.87` |
| `us-core-procedure-code` | `2.16.840.1.113883.4.642.40.2.40.90` | `2.16.840.1.113883.4.642.40.2.40.88` |
| `us-core-procedure-date` | `2.16.840.1.113883.4.642.40.2.40.91` | `2.16.840.1.113883.4.642.40.2.40.89` |
| `us-core-procedure-patient` | `2.16.840.1.113883.4.642.40.2.40.92` | `2.16.840.1.113883.4.642.40.2.40.90` |
| `us-core-procedure-status` | `2.16.840.1.113883.4.642.40.2.40.93` | `2.16.840.1.113883.4.642.40.2.40.91` |
| `us-core-questionnaireresponse-authored` | `2.16.840.1.113883.4.642.40.2.40.94` | `2.16.840.1.113883.4.642.40.2.40.92` |
| `us-core-questionnaireresponse-id` | `2.16.840.1.113883.4.642.40.2.40.95` | `2.16.840.1.113883.4.642.40.2.40.93` |
| `us-core-questionnaireresponse-patient` | `2.16.840.1.113883.4.642.40.2.40.96` | `2.16.840.1.113883.4.642.40.2.40.94` |
| `us-core-questionnaireresponse-questionnaire` | `2.16.840.1.113883.4.642.40.2.40.97` | `2.16.840.1.113883.4.642.40.2.40.95` |
| `us-core-questionnaireresponse-status` | `2.16.840.1.113883.4.642.40.2.40.98` | `2.16.840.1.113883.4.642.40.2.40.96` |
| `us-core-race` | `2.16.840.1.113883.4.642.40.2.40.99` | `2.16.840.1.113883.4.642.40.2.40.97` |
| `us-core-relatedperson-id` | `2.16.840.1.113883.4.642.40.2.40.100` | `2.16.840.1.113883.4.642.40.2.40.98` |
| `us-core-relatedperson-name` | `2.16.840.1.113883.4.642.40.2.40.101` | `2.16.840.1.113883.4.642.40.2.40.99` |
| `us-core-relatedperson-patient` | `2.16.840.1.113883.4.642.40.2.40.102` | `2.16.840.1.113883.4.642.40.2.40.100` |
| `us-core-servicerequest-authored` | `2.16.840.1.113883.4.642.40.2.40.103` | `2.16.840.1.113883.4.642.40.2.40.101` |
| `us-core-servicerequest-category` | `2.16.840.1.113883.4.642.40.2.40.104` | `2.16.840.1.113883.4.642.40.2.40.102` |
| `us-core-servicerequest-code` | `2.16.840.1.113883.4.642.40.2.40.105` | `2.16.840.1.113883.4.642.40.2.40.103` |
| `us-core-servicerequest-id` | `2.16.840.1.113883.4.642.40.2.40.106` | `2.16.840.1.113883.4.642.40.2.40.104` |
| `us-core-servicerequest-patient` | `2.16.840.1.113883.4.642.40.2.40.107` | `2.16.840.1.113883.4.642.40.2.40.105` |
| `us-core-servicerequest-status` | `2.16.840.1.113883.4.642.40.2.40.108` | `2.16.840.1.113883.4.642.40.2.40.106` |
| `us-core-specimen-id` | `2.16.840.1.113883.4.642.40.2.40.109` | `2.16.840.1.113883.4.642.40.2.40.107` |
| `us-core-specimen-patient` | `2.16.840.1.113883.4.642.40.2.40.110` | `2.16.840.1.113883.4.642.40.2.40.108` |

## SearchParameter: only in v7 (dropped in v8)

| id | OID |
|---|---|
| `us-core-patient-gender` | `2.16.840.1.113883.4.642.40.2.40.79` |
| `us-core-patient-gender-identity` | `2.16.840.1.113883.4.642.40.2.40.80` |

## Library: only in v8 (added since v7)

| id | OID |
|---|---|
| `uscore-3.1.1-model-definition` | `2.16.840.1.113883.4.642.40.2.28.1` |
| `uscore-4.0.0-model-definition` | `2.16.840.1.113883.4.642.40.2.28.2` |
| `uscore-5.0.1-model-definition` | `2.16.840.1.113883.4.642.40.2.28.3` |
| `uscore-6.1.0-model-definition` | `2.16.840.1.113883.4.642.40.2.28.4` |
| `uscore-7.0.0-model-definition` | `2.16.840.1.113883.4.642.40.2.28.5` |
| `uscore-8.0.1-model-definition` | `2.16.840.1.113883.4.642.40.2.28.6` |

## Questionnaire: only in v8 (added since v7)

| id | OID |
|---|---|
| `AUDIT-C` | `2.16.840.1.113883.4.642.40.2.35.1` |
| `TAPS` | `2.16.840.1.113883.4.642.40.2.35.2` |
| `exercise-vital-sign` | `2.16.840.1.113883.4.642.40.2.35.3` |
| `hunger-vital-sign-example` | `2.16.840.1.113883.4.642.40.2.35.4` |
| `phq-9-example` | `2.16.840.1.113883.4.642.40.2.35.5` |
| `prapare-example` | `2.16.840.1.113883.4.642.40.2.35.6` |

---

## Resources whose OID is unchanged

### CodeSystem (5 unchanged)

| id | OID |
|---|---|
| `careplan-category` | `2.16.840.1.113883.4.642.40.2.16.1` |
| `condition-category` | `2.16.840.1.113883.4.642.40.2.16.2` |
| `us-core-category` | `2.16.840.1.113883.4.642.40.2.16.3` |
| `us-core-documentreference-category` | `2.16.840.1.113883.4.642.40.2.16.4` |
| `us-core-provenance-participant-type` | `2.16.840.1.113883.4.642.40.2.16.5` |

### OperationDefinition (1 unchanged)

| id | OID |
|---|---|
| `docref` | `2.16.840.1.113883.4.642.40.2.33.1` |

### SearchParameter (74 unchanged)

| id | OID |
|---|---|
| `us-core-allergyintolerance-clinical-status` | `2.16.840.1.113883.4.642.40.2.40.1` |
| `us-core-allergyintolerance-patient` | `2.16.840.1.113883.4.642.40.2.40.2` |
| `us-core-careplan-category` | `2.16.840.1.113883.4.642.40.2.40.3` |
| `us-core-careplan-date` | `2.16.840.1.113883.4.642.40.2.40.4` |
| `us-core-careplan-patient` | `2.16.840.1.113883.4.642.40.2.40.5` |
| `us-core-careplan-status` | `2.16.840.1.113883.4.642.40.2.40.6` |
| `us-core-careteam-patient` | `2.16.840.1.113883.4.642.40.2.40.7` |
| `us-core-careteam-role` | `2.16.840.1.113883.4.642.40.2.40.8` |
| `us-core-careteam-status` | `2.16.840.1.113883.4.642.40.2.40.9` |
| `us-core-condition-abatement-date` | `2.16.840.1.113883.4.642.40.2.40.10` |
| `us-core-condition-asserted-date` | `2.16.840.1.113883.4.642.40.2.40.11` |
| `us-core-condition-category` | `2.16.840.1.113883.4.642.40.2.40.12` |
| `us-core-condition-clinical-status` | `2.16.840.1.113883.4.642.40.2.40.13` |
| `us-core-condition-code` | `2.16.840.1.113883.4.642.40.2.40.14` |
| `us-core-condition-encounter` | `2.16.840.1.113883.4.642.40.2.40.15` |
| `us-core-condition-lastupdated` | `2.16.840.1.113883.4.642.40.2.40.16` |
| `us-core-condition-onset-date` | `2.16.840.1.113883.4.642.40.2.40.17` |
| `us-core-condition-patient` | `2.16.840.1.113883.4.642.40.2.40.18` |
| `us-core-condition-recorded-date` | `2.16.840.1.113883.4.642.40.2.40.19` |
| `us-core-coverage-patient` | `2.16.840.1.113883.4.642.40.2.40.20` |
| `us-core-device-patient` | `2.16.840.1.113883.4.642.40.2.40.21` |
| `us-core-device-status` | `2.16.840.1.113883.4.642.40.2.40.22` |
| `us-core-device-type` | `2.16.840.1.113883.4.642.40.2.40.23` |
| `us-core-diagnosticreport-category` | `2.16.840.1.113883.4.642.40.2.40.24` |
| `us-core-diagnosticreport-code` | `2.16.840.1.113883.4.642.40.2.40.25` |
| `us-core-diagnosticreport-date` | `2.16.840.1.113883.4.642.40.2.40.26` |
| `us-core-diagnosticreport-lastupdated` | `2.16.840.1.113883.4.642.40.2.40.27` |
| `us-core-diagnosticreport-patient` | `2.16.840.1.113883.4.642.40.2.40.28` |
| `us-core-diagnosticreport-status` | `2.16.840.1.113883.4.642.40.2.40.29` |
| `us-core-documentreference-category` | `2.16.840.1.113883.4.642.40.2.40.30` |
| `us-core-documentreference-date` | `2.16.840.1.113883.4.642.40.2.40.31` |
| `us-core-documentreference-id` | `2.16.840.1.113883.4.642.40.2.40.32` |
| `us-core-documentreference-patient` | `2.16.840.1.113883.4.642.40.2.40.33` |
| `us-core-documentreference-period` | `2.16.840.1.113883.4.642.40.2.40.34` |
| `us-core-documentreference-status` | `2.16.840.1.113883.4.642.40.2.40.35` |
| `us-core-documentreference-type` | `2.16.840.1.113883.4.642.40.2.40.36` |
| `us-core-encounter-class` | `2.16.840.1.113883.4.642.40.2.40.37` |
| `us-core-encounter-date` | `2.16.840.1.113883.4.642.40.2.40.38` |
| `us-core-encounter-discharge-disposition` | `2.16.840.1.113883.4.642.40.2.40.39` |
| `us-core-encounter-id` | `2.16.840.1.113883.4.642.40.2.40.40` |
| `us-core-encounter-identifier` | `2.16.840.1.113883.4.642.40.2.40.41` |
| `us-core-encounter-lastupdated` | `2.16.840.1.113883.4.642.40.2.40.42` |
| `us-core-encounter-location` | `2.16.840.1.113883.4.642.40.2.40.43` |
| `us-core-encounter-patient` | `2.16.840.1.113883.4.642.40.2.40.44` |
| `us-core-encounter-status` | `2.16.840.1.113883.4.642.40.2.40.45` |
| `us-core-encounter-type` | `2.16.840.1.113883.4.642.40.2.40.46` |
| `us-core-ethnicity` | `2.16.840.1.113883.4.642.40.2.40.47` |
| `us-core-goal-description` | `2.16.840.1.113883.4.642.40.2.40.48` |
| `us-core-goal-lifecycle-status` | `2.16.840.1.113883.4.642.40.2.40.49` |
| `us-core-goal-patient` | `2.16.840.1.113883.4.642.40.2.40.50` |
| `us-core-goal-target-date` | `2.16.840.1.113883.4.642.40.2.40.51` |
| `us-core-immunization-date` | `2.16.840.1.113883.4.642.40.2.40.52` |
| `us-core-immunization-patient` | `2.16.840.1.113883.4.642.40.2.40.53` |
| `us-core-immunization-status` | `2.16.840.1.113883.4.642.40.2.40.54` |
| `us-core-location-name` | `2.16.840.1.113883.4.642.40.2.40.59` |
| `us-core-medicationdispense-patient` | `2.16.840.1.113883.4.642.40.2.40.60` |
| `us-core-medicationdispense-status` | `2.16.840.1.113883.4.642.40.2.40.61` |
| `us-core-medicationdispense-type` | `2.16.840.1.113883.4.642.40.2.40.62` |
| `us-core-medicationrequest-authoredon` | `2.16.840.1.113883.4.642.40.2.40.63` |
| `us-core-medicationrequest-encounter` | `2.16.840.1.113883.4.642.40.2.40.64` |
| `us-core-medicationrequest-intent` | `2.16.840.1.113883.4.642.40.2.40.65` |
| `us-core-medicationrequest-patient` | `2.16.840.1.113883.4.642.40.2.40.66` |
| `us-core-medicationrequest-status` | `2.16.840.1.113883.4.642.40.2.40.67` |
| `us-core-observation-category` | `2.16.840.1.113883.4.642.40.2.40.68` |
| `us-core-observation-code` | `2.16.840.1.113883.4.642.40.2.40.69` |
| `us-core-observation-date` | `2.16.840.1.113883.4.642.40.2.40.70` |
| `us-core-observation-lastupdated` | `2.16.840.1.113883.4.642.40.2.40.71` |
| `us-core-observation-patient` | `2.16.840.1.113883.4.642.40.2.40.72` |
| `us-core-observation-status` | `2.16.840.1.113883.4.642.40.2.40.73` |
| `us-core-organization-address` | `2.16.840.1.113883.4.642.40.2.40.74` |
| `us-core-organization-name` | `2.16.840.1.113883.4.642.40.2.40.75` |
| `us-core-patient-birthdate` | `2.16.840.1.113883.4.642.40.2.40.76` |
| `us-core-patient-death-date` | `2.16.840.1.113883.4.642.40.2.40.77` |
| `us-core-patient-family` | `2.16.840.1.113883.4.642.40.2.40.78` |

### CapabilityStatement (2 unchanged)

| id | OID |
|---|---|
| `us-core-client` | `2.16.840.1.113883.4.642.40.2.13.1` |
| `us-core-server` | `2.16.840.1.113883.4.642.40.2.13.2` |

---

## Caveat on the constructed v7 file

- CodeSystem, ValueSet, StructureDefinition OIDs are **authoritative** — extracted from each resource's `identifier` element in the v7.0.0 package.
- CapabilityStatement, OperationDefinition, SearchParameter sections were **inferred by alphabetical sequential numbering** in their respective arcs (the v7 package does not emit OIDs on those types). The 74 / 108 SearchParameter matches with v8 are what alphabetical assignment predicts; the 34 differences reflect where the 2 dropped SearchParameters shift the rest of the list.
- Library and Questionnaire did not exist as resources in v7.0.0; they are new in v8.
