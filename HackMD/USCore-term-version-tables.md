# US Core CodeSystem Version Comparison (6.1.0 / 8.0.1 / 9.0.0)

Comparison of selected US Core CodeSystems across versions 6.1.0, 8.0.1, and 9.0.0.

**Legend:** ✓ present · ➕ added · ⛔ removed/retired · ⚠️ deprecated (concept-level `status` property)

## 1. condition-category

Canonical: `http://hl7.org/fhir/us/core/CodeSystem/condition-category`

| code | 6.1.0 | 8.0.1 | 9.0.0 | notes |
|---|---|---|---|---|
| problem | ⚠️ | ⚠️ | ⚠️ | Present + carries `status=deprecated` property in all three versions. 8.0.1 added a deprecation note to the definition pointing to THO `condition-category#problem-list-item`. |
| health-concern | ✓ | ✓ | ✓ | Same in all three (definition text trimmed in 8.0.1). |

## 2. us-core-category

Canonical: `http://hl7.org/fhir/us/core/CodeSystem/us-core-category`

| code | 6.1.0 | 8.0.1 | 9.0.0 | notes |
|---|---|---|---|---|
| sdoh | ✓ | ✓ | ✓ | |
| functional-status | ✓ | ✓ | ✓ | |
| disability-status | ✓ | ✓ | ✓ | |
| cognitive-status | ✓ | ✓ | ✓ | |
| treatment-intervention-preference | | ➕ | ✓ | Added in 8.0.1. |
| care-experience-preference | | ➕ | ✓ | Added in 8.0.1. |
| observation-adi-documentation | | ➕ | ✓ | Added in 8.0.1. |
| PMO | | | ➕ | Added in 9.0.0 (Portable Medical Order). |

## 3. us-core-documentreference-category

Canonical: `http://hl7.org/fhir/us/core/CodeSystem/us-core-documentreference-category`

| code | 6.1.0 | 8.0.1 | 9.0.0 | notes |
|---|---|---|---|---|
| clinical-note | ✓ | ✓ | ✓ | Same in all three versions. |

## 4. us-core-provenance-participant-type

Canonical: `http://hl7.org/fhir/us/core/CodeSystem/us-core-provenance-participant-type`

| code | 6.1.0 | 8.0.1 | 9.0.0 | notes |
|---|---|---|---|---|
| transmitter | ✓ | ✓ | ⛔ | Entire CodeSystem removed from US Core 9.0.0. |
