# Profile Comparison: Four Flag profiles for USCDIv7 prior art

## Profiles

| ID | Title | Canonical | Version | FHIR | Status |
|---|---|---|---|---|---|
| **A** | Flag - Alert (IPS) | `http://hl7.org/fhir/uv/ips/StructureDefinition/Flag-alert-uv-ips` | 2.0.0 | R4 | active |
| **B** | NHS England Reasonable Adjustment Flag (Adjustment) | `https://fhir.nhs.uk/England/StructureDefinition/England-Flag-PatientFlag-Adjustment` | 0.2.0 (2024-09-27) | R4 | draft |
| **C** | QICore Flag | `http://hl7.org/fhir/us/qicore/StructureDefinition/qicore-flag` | 8.0.0-ballot | R4 | active |
| **D** | Flag: Patient (EU core) | `http://hl7.eu/fhir/base/StructureDefinition/flag-patient-eu-core` | 2.0.0 | R4 | active |

---

## Method and conventions

- **Inclusion rule** — an element is listed if, in *any* profile's StructureDefinition.differential, it is `mustSupport=true`, has `min > 0`, or carries an obligation with a valueCode containing `SHALL` or `SHOULD`.
- **QI-Core key elements** — QI-Core does not use `mustSupport`. Every constrained element in its differential carries the `qicore-keyelement` extension (`valueBoolean=true`). QI-Core's IG documents this as its deliberate replacement for mustSupport for quality-measure and CDS profiles. For this comparison, `keyElement=true` is treated as equivalent to mustSupport and rendered as **✅ (key)** in the MS column.
- **EU Core** — does not use `mustSupport`, `min > 0`, or obligation extensions anywhere in its differential. Under the strict inclusion rule it contributes zero rows on its own. Its data still appears in rows another profile contributed, to surface type narrowings, slice definitions, and the "alert" relabellings.
- **Inherited values** — when `min` or other attributes come from the base FHIR Flag snapshot and are not restated in the profile differential, the cell is annotated *(inherited)*.
- **Profile B (NHS)** data is taken from the rendered snapshot of `England-Flag-PatientFlag-Adjustment` on Simplifier; the raw JSON SD lives in package `fhir.r4.nhsengland.programme` on a host outside the sandbox network allowlist.
- **Type cell** — populated only when the profile narrows the type, restricts target profiles, or applies a profile to a `CodeableConcept`. Otherwise left blank.
- **Comments cell** — profile-specific deltas only: `short` changes, binding + strength, fixed values, slicing, obligations, and any profile-specific invariants. Base-resource invariants (`ele-1`, `ext-1`, `dom-2..6`, `per-1`, `ref-1`) are omitted unless the profile adds new ones.
- **Symbols** — ✅ true · ❌ false · — not constrained / n/a.

---

## Element-by-element comparison

> **Reading note.** This table has 26 columns by design. View in a wide viewport or open the raw markdown; most Markdown viewers allow horizontal scrolling on tables.

| Element path | Description (base FHIR) | A MS | A Mand | A Mod | A Card | A Type | A Comments | B MS | B Mand | B Mod | B Card | B Type | B Comments | C MS | C Mand | C Mod | C Card | C Type | C Comments | D MS | D Mand | D Mod | D Card | D Type | D Comments |
|---|---|:-:|:-:|:-:|:-:|---|---|:-:|:-:|:-:|:-:|---|---|:-:|:-:|:-:|:-:|---|---|:-:|:-:|:-:|:-:|---|---|
| `Flag.contained` | **Short:** Contained, inline Resources. **Definition:** Resources with no independent existence apart from their container; cannot be identified independently. | — | — | ❌ | (inherited) | — | Not constrained. | ✅ | ❌ | ❌ | 0..* (sliced unordered, open, by `$this(Type)`) | — | Sliced to add a `provenance` slice (see next row). | — | — | ❌ | (inherited) | — | Not constrained. | — | — | ❌ | (inherited) | — | Not constrained. |
| `Flag.contained:provenance` | **Short:** Who, What, When for a set of resources. **Definition:** Provenance assertion describing entities/processes involved in producing or influencing this Flag. | — | — | — | n/a | — | n/a | ✅ | ❌ | ❌ | 0..1 | `EnglandProvenanceFlag` | Inline Provenance per Flag instance: practitioner, NHS SDS role code, organization, CREATE/DELETE activity. | — | — | — | n/a | — | n/a | — | — | — | n/a | — | n/a |
| `Flag.extension` *(slice for `flag-priority`)* | **Short:** An alarm code. **Definition:** A code identifying the priority of the alert (e.g. IHE PCD TF-2 Table B.8-4 "Alert Priority"). | ✅ | ❌ | ❌ | 0..1 | `Extension(flag-priority\|5.3.0-ballot-tc1)` | Slice name `flag-priority`. **Obligations:** *Creator* SHALL `populate-if-known`; *Consumer* SHALL `handle`, SHOULD `display`. | — | — | — | n/a | — | NHS profile does not slice this extension. (It adds a separate `extensionEnglandFlagNotes` slice for free-text adjustment notes.) | — | — | — | n/a | — | Not sliced. | ❌ | ❌ | ❌ | 0..1 | `Extension(flag-priority)` | Slice name `flagPriorityExt`. Same FHIR `flag-priority` extension referenced, but NOT marked must-support and no obligations applied. |
| `Flag.status` | **Short:** active \| inactive \| entered-in-error. **Definition:** Supports basic workflow. | ❌ | ✅ (inherited) | ✅ | 1..1 | — | **Fixed value:** `active`. Binding: `flag-status\|4.0.1` (**required**, inherited). | ✅ | ✅ (inherited) | ✅ | 1..1 | — | No fixed value — full lifecycle conformant. Binding: `flag-status` (**required**, inherited). | ✅ (key) | ✅ (inherited) | ✅ | 1..1 | — | Short relabelled `(QI) active | inactive | entered-in-error`. No other constraint; binding inherited. | ❌ | ✅ (inherited) | ✅ | 1..1 | — | Short relabelled `Alert status`. No other constraint; binding inherited. |
| `Flag.category` | **Short:** Clinical, administrative, etc. **Definition:** Filtering category for the flag; used for display/UI scoping. | ✅ | ❌ | ❌ | 0..* | `CodeableConcept(CodeableConcept-uv-ips)` | Binding: `flag-category\|4.0.1` (**example**, inherited). **Obligations:** *Creator* SHALL `populate-if-known`; *Consumer* SHALL `handle`, SHOULD `display`. | ✅ | ✅ (**min=2**) | ❌ | **2..*** (sliced unordered, open, by `$this(Pattern)`) | — | Profile forces *at least two* category instances via slicing — one `patientFlag` slice + one `programmeFlag` slice. Root binding `flag-category` (example); slice bindings carry the real conformance. | ✅ (key) | ❌ | ❌ | 0..* | — | Binding strength **tightened** to **preferred** against `flag-category`. Short relabelled `(QI) Clinical, administrative, etc.`. | ❌ | ❌ | ❌ | 0..* | — | Not constrained beyond base. |
| `Flag.category:patientFlag` | (slice of `Flag.category`) **Short:** Clinical, administrative, etc. **Definition:** The slice that classifies the Flag as a Patient Flag programme record. | — | — | — | n/a | — | n/a | ✅ | ❌ | ❌ | 0..1 | — | Binding: `EnglandFlagCategoryPatient` (**required**). | — | — | — | n/a | — | n/a | — | — | — | n/a | — | n/a |
| `Flag.category:programmeFlag` | (slice of `Flag.category`) **Short:** Clinical, administrative, etc. **Definition:** The slice that names which NHS England programme owns the flag. | — | — | — | n/a | — | n/a | ✅ | ❌ | ❌ | 0..1 | — | Binding: `EnglandFlagCategoryProgramme` (**required**). | — | — | — | n/a | — | n/a | — | — | — | n/a | — | n/a |
| `Flag.code` | **Short:** Coded or textual message to display to user. **Definition:** The coded value or textual component of the flag to display. | ✅ | ✅ | ❌ | 1..1 | `CodeableConcept(CodeableConcept-uv-ips)` | Binding: `flag-code\|4.0.1` (**example**, inherited). **Obligations:** *Creator* SHALL `populate-if-known`; *Consumer* SHALL `handle`, SHOULD `display`. | ✅ | ✅ (inherited) | ❌ | 1..1 | — | Binding: `EnglandFlagCodeProgramme` (**extensible**) — programme-defined RA codes. | ✅ (key) | ✅ (inherited) | ❌ | 1..1 | — | Binding strength **tightened** to **preferred** against `flag-code`. Short relabelled `(QI) Coded or textual message to display to user`. | ❌ | ✅ (inherited) | ❌ | 1..1 | — | Short relabelled `Coded or textual message to display to user.` (no change in meaning). Binding inherited. |
| `Flag.subject` | **Short:** Who/What is flag about? **Definition:** The patient, location, group, organization, practitioner, etc. this flag is associated with. | ✅ | ✅ | ❌ | 1..1 | `Reference(Patient \| Location \| Group \| Organization \| Practitioner \| PlanDefinition \| Medication \| Procedure)` | Target list = full FHIR base list. **Obligations:** *Creator* SHALL `populate-if-known`; *Consumer* SHALL `handle`, SHOULD `display`. | ✅ | ✅ | ❌ | 1..1 | `Reference(Group \| Location \| Medication \| Organization \| Patient \| PlanDefinition \| Practitioner \| Procedure)` | Target list = full FHIR base list (NOT narrowed to Patient). Patient-only constraint lives at the API layer (PDS/NHS Number), not in the profile. | ✅ (key) | ✅ (inherited) | ❌ | 1..1 | `Reference(qicore-patient \| qicore-location \| Group \| qicore-organization \| qicore-practitioner)` | Target list **narrowed**: drops Medication, Procedure, PlanDefinition; remaining FHIR targets re-bound to QI-Core profiles. Short relabelled `(QI) ...`. | ❌ | ✅ (inherited) | ❌ | 1..1 | `Reference(patient-eu-core)` | Target list **narrowed to Patient only** (EU Core Patient profile). Aligns with profile name "Flag: Patient (EU core)". |
| `Flag.subject.reference` | **Short:** Literal reference, relative, internal or absolute URL. **Definition:** A reference to a location at which the other resource is found. | ✅ | ✅ | ❌ | 1..1 | `string` | **Obligations:** *Creator* SHALL `populate-if-known`; *Consumer* SHALL `handle`. | — | — | — | (inherited) | — | Not constrained at this child level. | — | — | — | (inherited) | — | Not constrained. | — | — | — | (inherited) | — | Not constrained. |
| `Flag.period` | **Short:** Time period when flag is active. **Definition:** The period of time from the activation of the flag to inactivation; if active, end should be unspecified. | — | — | ❌ | (inherited) | — | Not constrained. | — | — | ❌ | (inherited) | — | Not constrained. | ✅ (key) | ❌ | ❌ | 0..1 | — | Marked as a QI-Core key element. Short relabelled `(QI) Time period when flag is active`. No other constraint. | ❌ | ❌ | ❌ | 0..1 | — | Short relabelled `Time period when the alert is active`. No other constraint. |

---

## Use-case and narrative comparison

### Profile A — Flag - Alert (IPS)

A content profile inside the HL7 International Patient Summary specification. Designed for cross-border patient-summary exchange. The Flag instance carries one alert inside an IPS Bundle and is surfaced to a clinician reading the IPS at the point of care, often in unscheduled care contexts. Conformance is expressed precisely through `mustSupport` plus per-element Creator/Consumer obligation extensions with SHALL/SHOULD verbs, plus a fixed `status = active` that limits conforming instances to live alerts. Binding strengths on `Flag.category` and `Flag.code` are left at **example**, leaving terminology choice to the implementing jurisdiction.

### Profile B — NHS England Reasonable Adjustment Flag

A national service profile underpinning a statutory duty under the Equality Act 2010. The Adjustment profile sits inside a multi-resource "Reasonable Adjustment Record" alongside a parent `England-Flag-PatientFlag` marker and an optional `England-Condition-Flag` for the underlying disability. Conformance is expressed through `mustSupport`, **required** bindings on the two `Flag.category` slices, an **extensible** binding on `Flag.code`, a mandatory 2..* category cardinality, and a contained `EnglandProvenanceFlag` carrying who-recorded-it and CREATE/DELETE history. No obligation extensions; conformance behaviour is lifted to the API and the IG narrative ("Implementations SHALL provide capability to offer and consume basic CRUD interactions via HTTP"). Access gated by NHS Spine, smartcard, and RBAC. England-only, direct-care-only, mandated for use across all NHS care settings. Profile is in draft; the service is live and currently onboarding GP suppliers for write capability through April–June 2026.

### Profile C — QICore Flag

A US Realm profile designed for clinical decision support and quality-measure authors, not for a specific clinical use case. Its differential is intentionally thin: no `mustSupport` (QI-Core uses `qicore-keyelement` extension instead, signalling elements that quality-measure authors should expect to reference), no required bindings, no fixed values, no obligations. What QI-Core *does* change: it tightens `Flag.category` and `Flag.code` binding strength from **example** to **preferred** against the same FHIR base value sets, and narrows the `Flag.subject` target list — removing `Medication`, `Procedure`, and `PlanDefinition` and re-binding the surviving four targets (Patient, Location, Organization, Practitioner) to their QI-Core counterparts (Group stays unprofiled). The relabelling of `short` text with a `(QI)` prefix is a stylistic convention to mark QI-Core overrides in IG rendering. The profile is best read as a "well-typed scaffold" for quality measures rather than a clinical content profile.

### Profile D — Flag: Patient (EU core)

A European base profile for *patient-related* alerts. The most clearly differentiated structural choice is that `Flag.subject` is narrowed to a single target — the EU Core Patient profile — making this a *patient-only* Flag at the profile layer (unlike NHS, which leaves the broad target list in place and narrows only at the API). The profile also slices `Flag.extension` to declare three named slices for downstream use: `flagDetailExt` (referencing the FHIR `flag-detail` extension), `flagPriorityExt` (referencing the same `flag-priority` extension that IPS makes mustSupport), and `note` (referencing the FHIR `note` extension, with `value[x].text` exposed for narrative). None of these slices is marked must-support; the profile leaves it to derived national profiles to require them. EU Core consistently relabels Flag-vocabulary as "alert" in `short` descriptions, signalling that EU national base profiles should treat the resource as an alert carrier. No obligation extensions, no `mustSupport`, no `min > 0`, no required bindings.

### Cross-profile observations

**Conformance philosophy is the main axis of difference.**

- IPS uses obligation extensions with Creator/Consumer SHALL/SHOULD verbs.
- NHS uses `mustSupport` + required bindings + slice cardinality + contained Provenance for audit.
- QI-Core uses `qicore-keyelement` + binding-strength tightening + target-profile re-binding, deferring mustSupport to derived profiles.
- EU Core uses type narrowing + extension slicing as a *base profile* that downstream national profiles are expected to constrain further.

**Subject scoping diverges sharply.**

- IPS keeps all eight base targets (cross-border IPS may flag locations, medications, etc.).
- NHS keeps all eight base targets at profile level (patient-only is enforced only at the API layer — worth noting as a profile-vs-runtime gap).
- QI-Core narrows to five targets (drops Medication, Procedure, PlanDefinition) and re-binds four of them to QI-Core profiles.
- EU Core narrows to one (Patient only), the most aggressive narrowing in the set.

**Terminology binding strength escalates left-to-right across the profiles.**

- IPS: `Flag.category` and `Flag.code` at **example** strength.
- EU Core: same, inherited.
- QI-Core: both tightened to **preferred** against the same FHIR base value sets.
- NHS: `Flag.category` slices at **required** against NHS-specific value sets; `Flag.code` at **extensible** against `EnglandFlagCodeProgramme`.

**Status handling.**

- IPS pins `status = active` (only live alerts conform).
- NHS, QI-Core, and EU Core all leave the full lifecycle intact (`active`, `inactive`, `entered-in-error`).

**Priority / alarm code.**

- IPS makes the `flag-priority` extension `mustSupport` with full Creator/Consumer obligations.
- EU Core declares the same extension as a slice but does not mark it must-support.
- NHS and QI-Core do not reference this extension at all.

**Authorship.**

- IPS, QI-Core, and EU Core all leave `Flag.author` essentially at base.
- NHS does not constrain `Flag.author` either — instead it captures authorship through a **contained `Provenance`** (`EnglandProvenanceFlag`) bound into a `Flag.contained:provenance` slice. This is a structurally distinct pattern that none of the other three profiles use.

**Implications for USCDIv7 prior art.**

1. If USCDIv7 wants per-element conformance verbs (SHALL `populate-if-known`, SHOULD `display`), IPS is the closest exemplar.
2. If USCDIv7 wants binding tightening without forcing terminology, QI-Core's preferred-strength approach is the lightest precedent.
3. If USCDIv7 wants statutory-grade conformance with required slice bindings and audit trails, NHS RAF is the heaviest precedent.
4. If USCDIv7 wants a *patient-only* Flag profile, EU Core has set that pattern at the profile layer; NHS has chosen not to.
5. None of the four profiles uses `Flag.author` as the authorship anchor — three leave it untouched, and NHS replaces it with contained Provenance. Worth flagging if USCDIv7 wants explicit recording-clinician capture.

---

## Sources

- **Profile A:** `StructureDefinition-Flag-alert-uv-ips.json`, as supplied.
- **Profile B:** Rendered snapshot of `England-Flag-PatientFlag-Adjustment` v0.2.0 (2024-09-27) on Simplifier in the Patient Flag IG — Alpha (`https://simplifier.net/guide/PatientFlag`), now superseded by the Beta IG (`https://simplifier.net/guide/patient-flag-implementation-guide-beta`). Raw JSON SD in `fhir.r4.nhsengland.programme`; package host outside the sandbox network allowlist. Service narrative from the NHS England Digital service page PDF (last edited 10 February 2026).
- **Profile C:** `StructureDefinition-qi-core-flag.json`, as supplied. QI-Core IG: `https://build.fhir.org/ig/HL7/fhir-qi-core/`.
- **Profile D:** `StructureDefinition-flag-patient-eu-core.json`, as supplied. EU Core IG: `https://build.fhir.org/ig/hl7-eu/base/`.
