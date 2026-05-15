# Profile Comparison: Three DeviceRequest profiles

## Profiles

| ID | Title | Canonical | Version | FHIR | Status | Date |
|---|---|---|---|---|---|---|
| **A** | PCT GFE DeviceRequest (Da Vinci PCT) | `http://hl7.org/fhir/us/davinci-pct/StructureDefinition/davinci-pct-devicerequest` | 2.0.1 | R4 | draft | 2026-03-20 |
| **B** | PAO Device Request (DME Orders) | `http://hl7.org/fhir/us/dme-orders/StructureDefinition/PAOX-devicerequest` | 0.2.2 | R4 | active | 2023-06-25 |
| **C** | QICore DeviceRequest | `http://hl7.org/fhir/us/qicore/StructureDefinition/qicore-devicerequest` | 8.0.0-ballot | R4 | active | 2019-07-11 |

---

## Method and conventions

- **Inclusion rule** — an element is listed if it appears in any profile's `differential` carrying `mustSupport=true`, `min > 0`, or an obligation valueCode containing `SHALL` / `SHOULD`. The root `DeviceRequest` element is also included because QI-Core adds a profile-specific invariant there (`drq-3`); strictly the root does not pass the rule on its own but the invariant changes profile semantics meaningfully.
- **QI-Core key elements** — QI-Core does not use FHIR `mustSupport`. Every constrained element in its differential carries the `qicore-keyelement` extension (`valueBoolean=true`). QI-Core's IG documents this as its deliberate replacement for `mustSupport` for quality-measure and CDS authors. In the **MS** column below, `keyElement=true` is treated as MS-equivalent and rendered as ✅.
- **Pattern and fixed values are not MS** — PCT pattern-codes `status=active` and `intent=proposal`, and DME fixes `intent=order`. These constrain instances but are not in themselves `mustSupport`, `min>0`, or obligations. The rows still appear because *some other* profile triggers inclusion; the constraint is captured in the relevant Comments cell.
- **Inherited values** — when `min`, `max`, modifier flag, or type come from the base FHIR DeviceRequest snapshot and are not restated in the differential, the cell is annotated *(inherited)*.
- **Type cell** — populated only when the profile narrows the type or rebinds a `Reference` target. Otherwise blank.
- **Comments cell** — profile-specific deltas only: short relabels, binding + strength, slicing, conditions, profile-specific invariants. Base-resource invariants (`ele-1`, `dom-1..6`, `ref-1`) are omitted.
- **Symbols** — ✅ true · ❌ false · — not constrained / n/a.

> **Reading note.** This table has 20 columns. View in a wide viewport or open the raw markdown.

---

## Element-by-element comparison

| Element path | Description (base FHIR R4) | A MS | A Mand | A Mod | A Card | A Type | A Comments | B MS | B Mand | B Mod | B Card | B Type | B Comments | C MS | C Mand | C Mod | C Card | C Type | C Comments |
|---|---|:-:|:-:|:-:|:-:|---|---|:-:|:-:|:-:|:-:|---|---|:-:|:-:|:-:|:-:|---|---|
| `DeviceRequest` (root) | **Short:** Medical device request. **Definition:** Represents a request for a patient to employ a medical device. The device may be an implantable device, or an external assistive device, such as a walker. | — | — | ❌ | (inherited) | — | Not constrained at the root. | — | — | ❌ | (inherited) | — | Root listed in differential with no constraints. | — | — | ❌ | (inherited) | — | Adds profile-specific invariant **`drq-3`** (error severity): "to indicate what device, either at least one coding in the code or a codeOptions extension shall be provided". Expression: `(code is Reference).not() implies code.extension('http://hl7.org/fhir/StructureDefinition/codeOptions').exists() xor code.coding.exists()`. |
| `DeviceRequest.modifierExtension:doNotPerform` | **Short:** Extension. **Definition:** An Extension. (Slice on `modifierExtension` for the R5 backport `extension-DeviceRequest.doNotPerform`.) | — | — | — | n/a | — | n/a | — | — | — | n/a | — | n/a | ✅ | ❌ | ✅ | 0..1 | `Extension(http://hl7.org/fhir/5.0/StructureDefinition/extension-DeviceRequest.doNotPerform)` | Slice name `doNotPerform`. Short relabelled `(QI) Extension`. **isModifierReason:** "The do not perform element changes the meaning of the request from a positive to a negative statement". R5-style do-not-perform semantics back-ported into R4. |
| `DeviceRequest.identifier` | **Short:** External Request identifier. **Definition:** Identifiers assigned to this order by the orderer or by the receiver. | — | — | ❌ | (inherited) | — | Not constrained. | — | — | ❌ | (inherited) | — | Not constrained. | ✅ | ❌ | ❌ | 0..* | — | Short relabelled `(QI) External Request identifier`. No other constraint. |
| `DeviceRequest.status` | **Short:** draft \| active \| on-hold \| revoked \| completed \| entered-in-error \| unknown. **Definition:** The status of the request. | — | ✅ *(inherited)* | ✅ | 1..1 | — | **`patternCode: active`** — every conforming GFE DeviceRequest is constrained to status `active`. Binding `request-status\|4.0.1` (required, inherited). | — | ✅ *(inherited)* | ✅ | 1..1 | — | Not constrained beyond base. Binding inherited (required). | ✅ | ✅ *(inherited)* | ✅ | 1..1 | — | Short relabelled `(QI) draft | active | on-hold | revoked | completed | entered-in-error | unknown`. Binding inherited. No fixed/pattern. |
| `DeviceRequest.intent` | **Short:** proposal \| plan \| directive \| order \| original-order \| reflex-order \| filler-order \| instance-order \| option. **Definition:** Whether the request is a proposal, plan, an original order or a reflex order. | — | ✅ *(inherited)* | ✅ | 1..1 | — | **`patternCode: proposal`** — every PCT GFE DeviceRequest is a proposal (consistent with GFE workflow: the request is not yet an order). Binding `request-intent\|4.0.1` (required, inherited). | — | ✅ *(inherited)* | ✅ | 1..1 | — | **`fixedCode: order`** — every PAO DeviceRequest is an order. Binding inherited (required). | ✅ | ✅ *(inherited)* | ✅ | 1..1 | — | Short relabelled `(QI) proposal | plan | directive | order | original-order | reflex-order | filler-order | instance-order | option`. Binding inherited. No fixed/pattern. |
| `DeviceRequest.code[x]` | **Short:** Device requested. **Definition:** The details of the device to be used. | ✅ | ✅ *(inherited)* | ❌ | 1..1 | — | No type narrowing. Binding inherited at example strength against `device-kind`. | — | ✅ *(inherited)* | ❌ | 1..1 | — | Not constrained beyond base. Type and binding inherited. | ✅ | ✅ *(inherited)* | ❌ | 1..1 | `Reference(qicore-device) \| CodeableConcept` | Reference target narrowed and re-profiled to `qicore-device`. Short relabelled `(QI) Device requested`. Binding **tightened** from *example* to **preferred** against `http://hl7.org/fhir/ValueSet/device-kind`. Element has **condition `drq-3`** (must satisfy the root invariant — either a coding or a codeOptions extension). |
| `DeviceRequest.codeCodeableConcept.extension:codeOptions` | **Short:** Url of a value set of candidate devices. **Definition:** A logical reference (e.g. a reference to ValueSet.url) to a value set/version that identifies a set of possible coded values representing the device. (Slice for the R5 `codeOptions` extension.) | — | — | — | n/a | — | n/a | — | — | — | n/a | — | n/a | ✅ | ❌ | ❌ | 0..1 | `Extension(http://hl7.org/fhir/StructureDefinition/codeOptions\|8.0.0-ballot)` | Slice name `codeOptions`. Short relabelled `(QI) Url of a value set of candidate devices`. Provides a R5-style way to point to a *value set* of candidate devices when no single coding is known yet. **Condition `drq-3`** — either this extension or `code.coding` must be present. |
| `DeviceRequest.subject` | **Short:** Focus of request. **Definition:** The patient who will use the device. | — | ✅ *(inherited)* | ❌ | 1..1 | `Reference(us-core-patient\|7.0.0)` | Target list **narrowed to Patient only** and re-profiled to US Core Patient v7.0.0 (version-pinned). Base R4 allows `Patient \| Group \| Location \| Device`. | — | ✅ | ❌ | 1..1 | `Reference(Patient \| Group \| Location \| Device)` | Same target list as base R4. No type narrowing, no profile re-binding. | ✅ | ✅ *(inherited)* | ❌ | 1..1 | `Reference(qicore-patient)` | Target list **narrowed to Patient only** and re-profiled to QI-Core Patient. Short relabelled `(QI) Focus of request`. |
| `DeviceRequest.encounter` | **Short:** Encounter motivating request. **Definition:** An encounter that provides additional context in which this request is made. | — | — | ❌ | (inherited 0..1) | — | Not constrained. | ✅ | ❌ | ❌ | 0..1 | `Reference(us-core-encounter)` | Reference target **narrowed and re-profiled** to US Core Encounter. The only must-support element in the DME profile. | — | — | ❌ | (inherited 0..1) | — | Not constrained. |
| `DeviceRequest.authoredOn` | **Short:** When recorded. **Definition:** When the request transitioned to being actionable. | — | — | ❌ | (inherited 0..1) | — | Not constrained. | — | — | ❌ | (inherited 0..1) | — | Not constrained. | ✅ | ❌ | ❌ | 0..1 | — | Short relabelled `(QI) When recorded`. No other constraint. |

---

## Use-case and narrative comparison

### Profile A — PCT GFE DeviceRequest (Da Vinci Patient Cost Transparency)

A content profile for Da Vinci's **Patient Cost Transparency** Implementation Guide, which operationalises the US No Surprises Act's *Good Faith Estimate* (GFE) workflow. A DeviceRequest in PCT is not actually a clinical device order — it is the data structure used to communicate *what device* a payer is being asked to price for an upfront cost estimate. That framing drives the profile's two distinctive constraints: `status` is pattern-coded `active` (the GFE request is in flight) and `intent` is pattern-coded `proposal` (it is not yet an order; it is a proposal for which a price is being estimated). The profile narrows `subject` to a version-pinned `us-core-patient|7.0.0`, anchoring the patient identification to US Core 7.0.0 specifically. `code[x]` is must-support but otherwise unchanged — the profile does not narrow the type or change the binding, leaving payers free to receive either a `CodeableConcept` or a `Reference(Device)`. Conformance is expressed with `mustSupport` plus pattern values; no obligations, no required bindings, no profile-specific invariants.

### Profile B — PAO Device Request (DME Orders)

A content profile for the **DME Orders / Prior Authorization Order eXchange (PAOX)** Implementation Guide. The use case is durable-medical-equipment ordering: a clinician orders DME, and the order needs to flow through prior-authorization workflows with the relevant payer or DME supplier. The profile is intentionally minimal: only `encounter` is must-support, narrowed to `us-core-encounter` so that the order is always anchored to a US Core encounter context. `intent` is **fixed** (not patterned) to `order` — the only conforming value — reflecting that PAOX is for actual orders, not proposals or plans. There is no narrowing of `subject` or `code[x]`, no required terminology binding, no profile-specific invariants. The conformance burden is carried by the wider IG narrative and the API contract rather than the SD.

### Profile C — QICore DeviceRequest

A US Realm scaffold profile designed for **quality-measure and clinical-decision-support authors** rather than a specific clinical use case. Eight elements are marked with `qicore-keyelement=true` (QI-Core's mustSupport-replacement convention): `modifierExtension:doNotPerform`, `identifier`, `status`, `intent`, `code[x]`, `codeOptions` slice, `subject`, and `authoredOn`. The profile back-ports two R5 features into R4 — the `do-not-perform` modifier extension and the `codeOptions` extension on `CodeableConcept` (for pointing at a value set of candidate devices instead of a single coding). A new profile-specific invariant **`drq-3`** enforces that either `code.coding` or the `codeOptions` extension must be present so a measure author can always determine what device is being requested. `code[x]`'s `Reference` target is narrowed and re-profiled to `qicore-device`; `subject` is narrowed to Patient only and re-profiled to `qicore-patient`. Binding strength on `code[x]` is tightened from *example* to **preferred** against the same FHIR base value set. No obligations, no required bindings, no `mustSupport`.

### Cross-profile observations

**The three profiles serve sharply different downstream consumers.**

- PCT: payers evaluating a Good Faith Estimate for a proposed device.
- DME: prior-authorisation processors evaluating a DME order.
- QI-Core: quality-measure and CDS engines evaluating compliance.

**`intent` is the cleanest signal of the use-case difference.** PCT patterns it to `proposal`, DME fixes it to `order`, QI-Core leaves the full value set open. A receiving system can use this single element to identify which workflow the message belongs to.

**Conformance philosophies diverge.**

- PCT uses `mustSupport` plus pattern values to constrain workflow state without invalidating broader DeviceRequest instances.
- DME uses one `mustSupport` plus one fixed value, leaning on the IG and API to carry the rest.
- QI-Core uses `qicore-keyelement` plus binding-strength tightening plus a new profile-specific invariant. It does not use `mustSupport` at all.

**Subject scoping diverges.** Base R4 allows `Patient | Group | Location | Device` for `DeviceRequest.subject`. PCT narrows to Patient (version-pinned US Core 7.0.0). QI-Core narrows to Patient (QI-Core Patient). DME keeps all four base R4 targets. PCT's version-pinning is the most aggressive cross-package coupling in the set — it forces consumers onto exactly US Core 7.0.0 and breaks if US Core advances.

**`code[x]` is where QI-Core does the heaviest lifting.** Beyond keyElement and preferred binding, QI-Core adds:
- A re-profiled `Reference(qicore-device)` target.
- A `codeOptions` slice on the `CodeableConcept` variant that back-ports an R5 feature into R4.
- A profile-specific invariant `drq-3` that bridges the two so a measure can be written against either form.

PCT and DME, by contrast, leave `code[x]` essentially as-is. A measure author writing against PCT or DME cannot rely on the same structural guarantees they would get from QI-Core.

**Do-not-perform semantics.** Only QI-Core back-ports the R5 `DeviceRequest.doNotPerform` modifier extension into R4. PCT and DME have no way to express a "do not perform this device request" instruction inside their conformance profiles — implementers would have to add the extension out-of-band and it would not be must-support.

**Encounter linkage.** Only DME makes encounter must-support and narrows it to US Core Encounter. For PCT and QI-Core, encounter is free-form 0..1 against the base R4 Encounter resource. If a use case needs to anchor a DeviceRequest to an encounter, DME is the only profile in the set that enforces it at the SD layer.

**No profile uses obligation extensions.** None of the three uses the `obligation` extension pattern with SHALL/SHOULD verbs — a pattern more common in IPS and HL7 international profiles. All three rely on `mustSupport` or `keyElement` plus narrative IG text.

---

## Sources

- **Profile A:** `StructureDefinition-davinci-pct-devicerequest.json` (v2.0.1, 2026-03-20). PCT IG: `https://hl7.org/fhir/us/davinci-pct/`.
- **Profile B:** `StructureDefinition-PAOX-devicerequest.json` (v0.2.2, 2023-06-25). DME Orders IG: `https://build.fhir.org/ig/HL7/dme-orders/`.
- **Profile C:** `StructureDefinition-qicore-devicerequest.json` (v8.0.0-ballot, 2019-07-11). QI-Core IG: `https://build.fhir.org/ig/HL7/fhir-qi-core/`.
