# US Core Flag — element-level summary

## Profile

| Attribute | Value |
|---|---|
| **Title** | US Core Flag |
| **Name** | `USCoreFlag` |
| **Canonical** | `http://hl7.org/fhir/us/core/StructureDefinition/us-core-flag` |
| **Version** | 8.0.0-ballot |
| **FHIR release** | R4 |
| **Status** | active |
| **Base resource** | `Flag` (constraint) |
| **Description** | Profile of Flag for decision support / quality metrics. Defines the core set of elements and extensions for quality rule and measure authors. |

## Method

- An element is listed if it appears in the profile's `differential` carrying `mustSupport=true`, `min > 0`, or an obligation valueCode containing `SHALL` / `SHOULD`.
- Inherited `min` from the base FHIR Flag snapshot is shown as *(inherited)*.
- The **Comments** cell carries the base FHIR `short` and `definition` for the element, then any profile-specific deltas — relabelled `short` text, binding + strength changes, type narrowings. Base-resource invariants (`ele-1`, `ref-1`, etc.) are omitted.

## Element-level constraints

| Element path | MS | Mand (min≥1) | Mod | Card | Type | Comments |
|---|:-:|:-:|:-:|:-:|---|---|
| `Flag.status` | ✅ | ✅ *(inherited)* | ✅ | 1..1 | — | **Short:** active \| inactive \| entered-in-error. **Definition:** Supports basic workflow. Short relabelled `(US) active | inactive | entered-in-error`. Binding `flag-status\|4.0.1` (required, inherited). No fixed value. |
| `Flag.category` | ✅ | ❌ | ❌ | 0..* | — | **Short:** Clinical, administrative, etc. **Definition:** Filtering category for the flag; used for display/UI scoping. Short relabelled `(US) Clinical, administrative, etc.`. Binding strength **tightened** from *example* (base) to **preferred** against the same FHIR base value set `http://hl7.org/fhir/ValueSet/flag-category`. |
| `Flag.code` | ✅ | ✅ *(inherited)* | ❌ | 1..1 | — | **Short:** Coded or textual message to display to user. **Definition:** The coded value or textual component of the flag to display. Short relabelled `(US) Coded or textual message to display to user`. **Binding:** `http://cts.nlm.nih.gov/fhir/ValueSet/2.16.840.1.113762.1.4.1234.567` (DEC Disability Accommodations Examples) — strength **preferred**. **Source:** Disability Equity Collaborative (DEC), *Appendix 0.8 – Disability Accommodations Examples* — https://www.disabilityequitycollaborative.org/wp-content/uploads/2026/04/Appendix-0.8-Disability-Accommodations-Examples.pdf. *Note: the VSAC canonical above is a placeholder OID for layout/illustrative purposes only; no real VSAC value set has been authored or registered.* |
| `Flag.code.text` | ✅ | ❌ | ❌ | 0..1 | — | **Short:** Plain text representation of the concept. **Definition:** A human-language representation of the concept as seen/selected/uttered by the user who entered the data, and/or which represents the intended meaning of the user. **Profile use:** supports free-text accommodation descriptions — bespoke or one-off adjustments that do not fit a coded concept from the DEC value set. Implementers SHOULD populate `text` whenever the accommodation cannot be fully expressed by a `coding`, and MAY populate it alongside a `coding` to preserve the original wording captured at the point of recording. |
| `Flag.subject` | ✅ | ✅ *(inherited)* | ❌ | 1..1 | `Reference(us-core-patient \| us-core-location \| Group \| us-core-organization \| us-core-practitioner)` | **Short:** Who/What is flag about? **Definition:** The patient, location, group, organisation, practitioner, etc. this flag is associated with. Short relabelled `(US) Who/What is flag about?`. Target list **narrowed**: drops Medication, Procedure, and PlanDefinition from the FHIR base list; the surviving four FHIR targets are re-bound to their US Core profiles (Group remains unprofiled). |

## Summary

US Core Flag is a deliberately thin profile. What it does:

1. **Marks four elements as `mustSupport`** (`Flag.status`, `Flag.category`, `Flag.code`, `Flag.subject`), signalling to implementers which elements they should expect to populate and consume.
2. **Tightens terminology binding strength** on `Flag.category` from *example* (base FHIR) to **preferred** against the same FHIR base value set, without changing the value set itself.
3. **Anchors `Flag.code` to a placeholder VSAC canonical** — `http://cts.nlm.nih.gov/fhir/ValueSet/2.16.840.1.113762.1.4.1234.567` (*DEC Disability Accommodations Examples*) — at **preferred** binding strength, with codes sourced from the Disability Equity Collaborative *Appendix 0.8 – Disability Accommodations Examples*. The VSAC OID is a sham placeholder for illustrative purposes; no real VSAC value set has been authored or registered.
4. **Marks `Flag.code.text` as `mustSupport`** to support free-text accommodations — bespoke or one-off adjustments that do not map to a coded DEC concept. The base `0..1` cardinality is preserved.
5. **Narrows `Flag.subject` target profiles** to five resources (Patient, Location, Group, Organization, Practitioner) and re-binds four of them to US Core profiles. Medication, Procedure, and PlanDefinition are dropped.
6. **Relabels `short` text** with a `(US) ` prefix on every constrained element, so US Core overrides are recognisable in rendered profile trees.

The profile is best read as a typed scaffold for decision support and quality-measure authoring against the DEC accommodation codes, rather than a clinical content profile in its own right.

## Source

- StructureDefinition file (as supplied).
- US Core IG: `https://hl7.org/fhir/us/core/`.
- Disability Equity Collaborative (DEC), *Appendix 0.8 – Disability Accommodations Examples*: https://www.disabilityequitycollaborative.org/wp-content/uploads/2026/04/Appendix-0.8-Disability-Accommodations-Examples.pdf
