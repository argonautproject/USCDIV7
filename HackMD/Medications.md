
<style>
#doc.markdown-body, .ui-infobar, .container-thiner {
    max-width: 1080px; /* Adjust this value to make wider, e.g., 1200px or 1550px */
}
.ui-content #doc.markdown-body, .ui-content .ui-infobar {
    max-width: 1550px; /* Set a wider max-width for content */
}
@media (min-width: 768px) {
    #doc.markdown-body, .ui-infobar {
        max-width: 750px; /* Optional: Adjust for smaller screens */
    }
}
@media (min-width: 1200px) {
    #doc.markdown-body, .ui-infobar {
        max-width: 1170px; /* Optional: Adjust for larger screens */
    }
}
</style>

## Medications: New Profile Needed
<!-- image of summary of changes-->
![image](https://hackmd.io/_uploads/HJw2a0kDZl.png)
*No narrative summary for the Medication Dispense Quantity Data Element in the ASTP/ONC Standards Bulletin 2026-1.*

<!-- **:new: Definition :point_down:** -->

![image](https://hackmd.io/_uploads/ryKmACyvbx.png)

### Summary of USCDI Comments:

*This content was developed with the assistance of Claude.*

| Position | Organizations | Reasons |
|---|---|---|
| **OPPOSE** | *(no outright opposition)* | — |
| **OPPOSE / REDESIGN** | TMA (state physician society) | Defer both elements until correlating vocabulary standards are specified |
| **MIXED / OPPOSE** | Epic (EHR vendor), EHR Association (vendor trade association), Oracle Health (EHR vendor), NCPDP (pharmacy SDO) | Epic, EHR Association, Oracle: split the Medications class into separate Prescription / Dispense / Administration data classes mirroring FHIR (MedicationRequest, MedicationDispense, MedicationAdministration) before finalizing — current draft conflates discrete concepts. Med Admin: limit scope to provider-administered events in clinical settings (primarily inpatient), exclude patient self-report. Dispense Quantity: separate "prescribed/intended quantity" from "actually-dispensed quantity" — distinct concepts, distinct value semantics. NCPDP: quantity dispensed vs. quantity to be dispensed are different concepts; if capturing actual-dispense amounts, requires a new dispense data class — a single prescription with refills has multiple dispense quantities |
| **SUPPORT / with CHANGES** | ANI (nursing informatics), AMIA (physician informatics), SNOMED International (SDO), HL7 (SDO), UI Health (academic medical center), Emory Healthcare (academic medical center), CDC (federal/public health), Regenstrief Institute (research/informatics), Wolters Kluwer (clinical content vendor), david_rocha (individual), csnewman (individual) | ANI: provide nursing MAR documentation guidance (PRN, dose modifications, route changes). AMIA: clarify Fill Status data source (patient/clinician/exchange/pharmacy?); reconcile with adherence. SNOMED Intl: designate SNOMED CT U.S. Edition for administration method/route/site (alongside NCPDP and NCI). HL7: clear definitions, usage notes, code system examples, support synonyms. UI Health: also define a Medication Reconciliation status attribute (e.g., "Validated," "Discrepancy Identified") to convey trust. Emory: differentiate retail/inpatient/ambulatory dispense; include UOM; opioid MEDD use case. CDC: ties Med Admin to NHSN harm measures (e.g., hypoglycemic event within 24 hours of diabetes med) and birth-certificate facility worksheet. Regenstrief: aligns with FHIR MedicationAdministration; complements existing Medication Dispense Status. Wolters Kluwer: also add Negation Rationale (Level 2) to the Medications class for accurate quality measure reporting. david_rocha: SNOMED CT pack size attributes (1142142004 Has pack size, 774163005 Has pack size unit) for Dispense Quantity. csnewman: clarify ambiguity between new Dispense Quantity and existing Dose / Dose Unit of Measure elements |
| **SUPPORT** | CMS-CCSQ (federal/payer), CSTE (state epidemiologists), CDC (federal/public health), Texas Department of Health-OIA (state public health), NCQA (quality measurement) | CMS-CCSQ: applauds Medication Administration inclusion. CSTE/TDH-OIA: medication data critical for eCR — STI, HIV, TB surveillance, antimicrobial resistance, and opioid overdose response. NCQA: strongly supports both elements as high-value adds with limited burden |

For a complete summary of the comments, see the Appendix below:

<!-- markdown table summary of proposal use adobe to convert to excel and then script to markdown or just copy/paste -->

## US Core Proposed Design

### Summary

DATA ELEMENT|<br/>Standards listed are required.<br/>If more than one is listed,<br/> at least one is required unless<br/>otherwise noted.<br/>Standards versions represent the most recent <br/>available at time of publication.</center>|US Core V10 Proposal
---|---|---
| **Medication Administration ➕**<br>Information about the event of a patient consuming or otherwise being given a medication.<br>Examples include but are not limited to swallowing a tablet, administering an injection, and a long running infusion. |  |🆕 US Core MedicationAdministration Profile (See Proposal)
| **Medication Dispense Quantity ➕**<br>The amount of medication dispensed or to be dispensed. |  |**No Change**: ` MedicationRequest.dispenseRequest.quantity` and `MedicationDispense.quantity` already are US Core *Must Support* elements|

➕ In USCDI+

### CCDA Design Notes

### Issues

### Proposal
1. 🆕 US Core MedicationAdministration Profile
   - Mandatory and Must Support elements: `status (m), statusReason, category, medication[x] (m), subject (m), effective[x] (m), performer, request, dosage`  (m = mandatory in base)
   - Terminology same as for MedicationRequest/Dispense
   - Search Parameters: patient, status, effective-time, medication, code
   - Edits to Medication List guidance page


1.  No Changes to US Core MedicationRequest Profile and US Core MedicationDispense Profile.
    - Possible updates to guidance because of new US Core MedicationAdministration Profile.

### Decisions

1.
2.
3.

### IG Updates

- [ ] USCDI Mapping Table
<!-- - [ ] Update US Core Profile
- [ ] Update Introduction
- [ ] Implementation Specific Guidance
- [ ] New Example(s) pending final review of decisions
- [ ] Update Example(s) pending final review of decisions -->

---

## Appendix

### Prior Art

- [pdmp-medicationadministration](https://packages2.fhir.org/xig/resource/hl7.fhir.us.pdmp%7Ccurrent/StructureDefinition/pdmp-medicationadministration)
- [Standardized Medication Profile - MedicationAdministration](	http://hl7.org/fhir/us/smp/StructureDefinition/smp-medicationadministration)
- [QI Core](https://packages2.fhir.org/xig/resource/hl7.fhir.us.qicore%7Ccurrent/StructureDefinition/qicore-medicationadministration)
- [US Public Health MedicationAdministration](https://packages2.fhir.org/xig/resource/hl7.fhir.us.ph-library%7Ccurrent/StructureDefinition/us-ph-medicationadministration)
- MCode
- 

<!-- appended-from: medications-draft.md -->

### Medications data class — Comment Position Summary (Medication Administration + Medication Dispense Quantity)

**Class additions:** Draft USCDI v7 adds two new data elements to the existing Medications data class: **Medication Administration** (information about the event of a patient consuming or otherwise being administered a medication; examples include route and method of administration) and **Medication Dispense Quantity** (the amount of medication dispensed or to be dispensed). Several commenters also propose elevating the Level 2 **Negation Rationale** element into the class.

| Position | Organizations | Reasons |
|---|---|---|
| **OPPOSE** | *(no outright opposition)* | — |
| **OPPOSE / REDESIGN** | TMA (state physician society) | Defer both elements until correlating vocabulary standards are specified |
| **MIXED / OPPOSE** | Epic (EHR vendor), EHR Association (vendor trade association), Oracle Health (EHR vendor), NCPDP (pharmacy SDO) | Epic, EHR Association, Oracle: split the Medications class into separate Prescription / Dispense / Administration data classes mirroring FHIR (MedicationRequest, MedicationDispense, MedicationAdministration) before finalizing — current draft conflates discrete concepts. Med Admin: limit scope to provider-administered events in clinical settings (primarily inpatient), exclude patient self-report. Dispense Quantity: separate "prescribed/intended quantity" from "actually-dispensed quantity" — distinct concepts, distinct value semantics. NCPDP: quantity dispensed vs. quantity to be dispensed are different concepts; if capturing actual-dispense amounts, requires a new dispense data class — a single prescription with refills has multiple dispense quantities |
| **SUPPORT / with CHANGES** | ANI (nursing informatics), AMIA (physician informatics), SNOMED International (SDO), HL7 (SDO), UI Health (academic medical center), Emory Healthcare (academic medical center), CDC (federal/public health), Regenstrief Institute (research/informatics), Wolters Kluwer (clinical content vendor), david_rocha (individual), csnewman (individual) | ANI: provide nursing MAR documentation guidance (PRN, dose modifications, route changes). AMIA: clarify Fill Status data source (patient/clinician/exchange/pharmacy?); reconcile with adherence. SNOMED Intl: designate SNOMED CT U.S. Edition for administration method/route/site (alongside NCPDP and NCI). HL7: clear definitions, usage notes, code system examples, support synonyms. UI Health: also define a Medication Reconciliation status attribute (e.g., "Validated," "Discrepancy Identified") to convey trust. Emory: differentiate retail/inpatient/ambulatory dispense; include UOM; opioid MEDD use case. CDC: ties Med Admin to NHSN harm measures (e.g., hypoglycemic event within 24 hours of diabetes med) and birth-certificate facility worksheet. Regenstrief: aligns with FHIR MedicationAdministration; complements existing Medication Dispense Status. Wolters Kluwer: also add Negation Rationale (Level 2) to the Medications class for accurate quality measure reporting. david_rocha: SNOMED CT pack size attributes (1142142004 Has pack size, 774163005 Has pack size unit) for Dispense Quantity. csnewman: clarify ambiguity between new Dispense Quantity and existing Dose / Dose Unit of Measure elements |
| **SUPPORT** | CMS-CCSQ (federal/payer), CSTE (state epidemiologists), CDC (federal/public health), Texas Department of Health-OIA (state public health), NCQA (quality measurement) | CMS-CCSQ: applauds Medication Administration inclusion. CSTE/TDH-OIA: medication data critical for eCR — STI, HIV, TB surveillance, antimicrobial resistance, and opioid overdose response. NCQA: strongly supports both elements as high-value adds with limited burden |

**Comments grouped by position:**

**Strongly supportive**
- **CMS-CCSQ** [federal agency / payer] — Applauds inclusion of Medication Administration in USCDI v7.
- **CSTE (Council of State and Territorial Epidemiologists)** [state public health surveillance] — Filed parallel comments on every new and existing medication-related sub-element (Medication Administration, Date Medication Administered, Medication Administered Code, Medication Administered Performer, Medication Administered Reason Reference, Medication Administration Dose, Medication Administration Dose Units, Medication Administration Route). Frames medication data as critical for exchange with public health and inclusion in eCR standards. Particularly important for STI programs, HIV and TB surveillance, public health response, antimicrobial-resistant pathogen surveillance, and opioid overdose/death reduction programs.
- **Texas Department of Health (jessilott)** [state public health agency] — Supports inclusion of Medication Administration as it strengthens completeness of medication histories and enhances interoperability across health information systems.
- **NCQA** [quality measurement org] — Lists Medication Administration and Medication Dispense Quantity among the v7 additions NCQA "strongly supports" as high-value adds with limited implementation burden given large overlap with other exchange requirements.
- **CDC (DSMH Working Group)** [federal agency / public health] — Two coordinated comments on Medication Administration. (1) Documents that a medication was actually given to a patient; without standardized exchange, accurate determination of medication use is limited, affecting identification of medication-related harm or treatment success. CDC quality measures including NHSN measures rely on confirmed medication administration to evaluate harm-related events such as whether a hypoglycemic event occurred within 24 hours of receiving a diabetes medication. (2) Ties the element to the live-birth-certificate facility worksheet, which captures medication administration during labor and delivery (e.g., antibacterial medication given systemically between onset of labor and delivery). Inclusion would improve electronic exchange between hospital EHRs and birth registration systems.

**Supportive with refinements**
- **Alliance for Nursing Informatics / ANI** [nursing informatics professional society] — Strongly supports both Route of Administration (existing) and Medication Dispense Quantity (new), and regards both as essential elements of comprehensive, safe medication documentation. Argues nurses are primary administrators of medications in inpatient and many ambulatory settings, responsible for verifying and documenting correct route for every administration; the absence in prior USCDI versions represented a meaningful gap. Together these elements reduce risk at care transitions where incomplete medication data is a leading contributor to preventable adverse drug events. Recommends implementation guidance addressing nursing-specific MAR documentation nuances: PRN administration, dose modifications, and route changes.
- **AMIA** [physician informatics professional society] — Discussion of Medication Administration and Medications Dispensed flags clarification need for the existing Fill Status element: who generates this information — patient, clinician, exchange, or pharmacy? Notes medication reconciliation is a "notorious problem" and adherence documentation is corollary; fill history may be available from some pharmacies as adherence proxy, but whether the patient is actually taking the medication is largely based on patient self-reporting. Also flags risk of patients not returning for the second part of a dispensed medication, and the disconnect in outpatient settings between pharmacy filling and patient receipt.
- **SNOMED International** [SDO — terminology] — Commends ONC for continued designation of SNOMED CT U.S. Edition for Route of Administration alongside NCI Thesaurus and FDA SPL Terminology. For the new Medication Administration element, recommends ONC explicitly name SNOMED CT U.S. Edition for administration method, route, and site concepts (in addition to NCPDP and NCI). SNOMED CT 18629005 |Administration of drug or medicament (procedure)| and related concepts support structured documentation of the full administration event, ensuring interoperability with clinical documentation systems already using SNOMED CT and supporting FHIR-based MedicationAdministration implementation.
- **HL7** [SDO] — Lists Medication Administration and Medication Dispense Quantity among elements requiring clearer definitions, usage notes, and code system examples. Notes the broader USCDI guidance is too high-level, leading to industry inconsistencies as entities are left to interpret meaning of each element. Recommends ONC support synonyms for USCDI elements (some domains are accustomed to "their" names, making it hard to identify when a concept is already supported).
- **UI Health (University of Illinois Health)** [academic medical center] — "Support with Gap Identification" for both Medication Administration and Medication Dispense Quantity. Supports addition for clinical review purposes, but argues that for these to be effective in a high-reliability setting, ASTP must define a "Medication Reconciliation" status or attribute. Standardizing the outcome of a Med Rec event (e.g., "Validated," "Discrepancy Identified") ensures the next provider in the care continuum knows the list is accurate. "Without this, we are exchanging more data without exchanging the 'trust' that the medication list has been verified."
- **Emory Healthcare** [academic medical center] — On Medication Dispense Quantity: requests additional clarity beyond the proposed definition, since dispensing varies across care areas (inpatient, ambulatory, retail dispense). Asks whether the element refers to retail dispense — if so, it is a standard field in ambulatory prescriptions, but dispense quantity is at times a calculated value. Recommends defining the element as "the actual count of units dispensed with unit of measure included." Notes this would support calculation of total dose, especially useful in opioid prescribing and Morphine Equivalent Daily Dose (MEDD) calculation.
- **Regenstrief Institute** [research/informatics institute] — Supports both elements. Medication Administration: aligns with FHIR MedicationAdministration resource; important for medication reconciliation and case data exchange in public health (PH). Medication Dispense Quantity: straightforward quantitative element with numeric + UCUM units; complements existing Medication Dispense Status. Both support public health case data exchange.
- **Wolters Kluwer** [clinical content vendor] — Supports Medication Administration as part of broader expansion of clinical care documentation. Separately advocates promoting Negation Rationale from Level 2 to the Medications class — promotes more accurate quality measure reporting and overall improvement in quality of care by informing the care team about deviations from standard treatments.
- **david_rocha** [individual / standards commenter] — Recommends SNOMED CT pack size attributes for Medication Dispense Quantity: SCTID 1142142004 |Has pack size (attribute)| for amount/quantity present in package, and SCTID 774163005 |Has pack size unit (attribute)| for the units. These provide structured representation alternatives to free-form numeric capture.
- **csnewman** [unaffiliated individual] — Two comments. (1) The lifecycle of ordering, dispensing, and administering medications is complex and not easily conveyed in a single data class — recommends expanding the existing Medication data class into distinct data classes for orders, dispense, and administrations (echoes Epic's, EHR Association's, and Oracle's structural recommendation). (2) Distinction between the new Medication Dispense Quantity and existing Dose / Dose Unit of Measure elements is unclear — please clarify.

**Mixed / oppose**
- **Epic** [EHR vendor] — Two element-specific positions plus a structural recommendation:
  - **Medication Administration**: Recommends ONC clarify the definition and intended scope. As proposed, "information about the event of a patient consuming or otherwise being administered a medication" encompasses multiple pieces of data (route, site, dose, date/time, provider) rather than specifying discrete information. Will lead to inconsistent implementation. Also recommends ONC separately evaluate maturity and applicability across care settings — most mature in inpatient, far less consistently captured in ambulatory and other settings; standards and workflows for reliable ambulatory exchange are not uniformly in place. If USCDI offered flexibility to adopt elements for targeted care settings only, inpatient adoption seems appropriate.
  - **Medication Dispense Quantity**: Supports addition but recommends clarifying definition before finalization. Current language conflates two distinct concepts: quantity *to be dispensed* (single value associated with a prescription — the prescribed quantity) versus quantity *actually dispensed* (no one-to-one relationship with prescription — multiple dispense events over time, including refills, partial fills due to inventory, and patient-requested partial fills). These serve different clinical and operational purposes and should be defined and referenced separately.
  - **Structural recommendation**: US Core Implementation Guide and CDA standards already separate prescription and dispense information using MedicationRequest and MedicationDispense. Recommends ONC align USCDI by splitting the Medications data class into two distinct classes — one for Medication Prescriptions and one for Medication Dispenses — and grouping Dispense Status and Dispense Quantity together under the new Medication Dispenses class.
- **EHR Association** [vendor trade association] — Mirrors Epic's positions:
  - **Medication Administration**: Concerns that the element conflates clinically documented administration events (e.g., a nurse administering medication in an inpatient setting) with patient-reported or outpatient medication use. In non-inpatient settings, "administration" is difficult to verify; while EHRs document prescription or dispensing, confirmation of administration often relies on patient self-report. Detailed MAR data including timing, dosing events, and route is highly complex and may introduce risk of misrepresentation if exchanged without sufficient context. Recommends ONC clarify that the element applies specifically to provider-administered medications in clinical settings, explicitly excludes patient-reported adherence, and acknowledge that this information is primarily relevant to inpatient settings — not all EHRs serve as the system of record. ONC should distinguish between MedicationRequest (prescription) and MedicationAdministration (confirmed administration); scope should be limited to confirmed administration events.
  - **Medication Dispense Quantity**: Supports adding the information but flags the same prescribed-vs-actually-dispensed conflation Epic raises. These represent fundamentally different concepts — intent (FHIR MedicationRequest) vs. event (FHIR MedicationDispense). Recommends scoping the element to the confirmed dispense event quantity to avoid conflation with prescribing intent.
- **Oracle Health** [EHR vendor] — Generally supports Medication Administration but raises concerns. (1) Suggests focusing on administrations by a clinician — beyond the scope of Medication Adherence, EHRs do not capture patient recordings of self-administrations, and clinicians don't currently include this level of detail. (2) Notes definition references "information about the event" while examples focus on route and method, the submission includes dose, and the Medications class already includes Route of Administration — adds ambiguity about what data is relevant to Prescription vs. Dispense vs. Administration. **Strongly recommends** the Medications data class be split into individual classes for (1) Medication Request, (2) Medication Dispense, and (3) Medication Administration, identifying for each class the relevant data elements. Acknowledges some elements would appear in multiple classes; argues this substantially reduces complexity. Frames as another example of using FHIR concepts to define USCDI.
- **NCPDP (National Council for Prescription Drug Programs)** [pharmacy SDO] — Recommends ONC clarify intent for Medication Dispense Quantity. The quantity dispensed and the quantity to be dispensed are two different concepts that should be referenced separately. The amount of medication *to be* dispensed (alternately phrased as "prescribed dispense quantity") is a single value associated with each prescription and is appropriate for the Medications data class. The amount of medication actually dispensed does not have a one-to-one association with a prescription because a prescription with multiple refills will have multiple amounts to be dispensed. If ONC wishes to capture actual amount dispensed, that should be captured through a new data class for dispense information. Separately, NCPDP appreciates ONC updating Medications Dispensed to "Medication Dispense Status" and recommends updating the ePrescribing NCPDP SCRIPT Standard reference to use the most recently named version, plus adding NCPDP Telecommunication Standard Version D.0© and Version F6© to "Applicable Standard(s)."

**Oppose / redesign**
- **TMA (Texas Medical Association)** [state physician professional society] — Lists both Medication Administration and Medication Dispense Quantity among 15 elements ONC should not adopt until each has a correlating vocabulary standard.

**Summary of Comments:** The Medications class additions face the most coordinated structural-redesign critique in Draft USCDI v7. Three EHR voices — Epic [EHR vendor], the EHR Association [vendor trade association], and Oracle Health [EHR vendor] — converge on the same recommendation independently, joined by NCPDP [pharmacy SDO] and the individual commenter csnewman: **split the Medications data class into separate classes mirroring FHIR's resource model** (MedicationRequest, MedicationDispense, MedicationAdministration). The argument is grounded in the FHIR R4 architecture already implemented by certified health IT — these resources exist as separate concepts because prescribing intent, fulfillment events, and administration events have distinct cardinality, distinct authoring parties, and distinct downstream use. The most operationally specific version of the critique comes from NCPDP and is echoed by Epic, EHR Association, and Oracle Health: **Medication Dispense Quantity conflates prescribed dispense quantity (one per prescription) with actual dispense quantity (one or more per dispense event)**. A prescription with refills has one prescribed quantity but multiple dispense events over time; partial fills due to inventory or patient request fragment this further. Without scoping the element to one or the other, exchanged values will mean different things in different transactions. The same conflation pattern affects **Medication Administration**: Epic, EHR Association, and Oracle Health all flag that the proposal blends provider-administered events (mature in inpatient settings) with patient self-report (variable across ambulatory contexts and largely unverifiable). The supporting voices are more diffuse but converge on a different structural concern. ANI [nursing informatics], UI Health [academic medical center], and AMIA [physician informatics] all point out that **medication reconciliation** is the use case these elements ultimately serve, and that without reconciliation status (UI Health's "Validated/Discrepancy Identified") and adherence semantics (AMIA's question about Fill Status authorship), exchanging medication events generates volume without trust. The vocabulary cluster is unusually concrete: **SNOMED International** [SDO] proposes specific SCTIDs (18629005 for administration of drug, plus method/route/site concepts) for Medication Administration; **david_rocha** [individual] proposes specific pack-size SCTIDs (1142142004 and 774163005) for Dispense Quantity; **NCPDP** [pharmacy SDO] proposes adding NCPDP Telecommunication Standard D.0 and F6 alongside SCRIPT. Public-health voices — **CSTE** [state epidemiologists, eight separate comments], **CDC** [federal/public health], **TDH** [state public health], **CMS-CCSQ** [federal/payer] — back inclusion strongly, framing medication exchange as foundational for eCR, NHSN harm measurement, antimicrobial resistance and opioid surveillance, and the live-birth-certificate facility worksheet. **Wolters Kluwer's** [clinical content vendor] separate ask to elevate Negation Rationale (Level 2) into the Medications class for quality-measure reporting is a logical complement — distinguishing why a medication wasn't administered is the same conceptual move as documenting that it was.

**Notably absent:** AHA, FAH, AHIP, AHIMA, AQIPS, MEDITECH, Allina Health, Providence Health, ANI's parallel medication-administration peer organization (e.g., AONL), pharmacy chains and PBMs, FDA, AHRQ, APHL, SHIELD, ACLA, AHIP, CARIN Alliance, Vega Health, and Vizient are all silent on the Medications class additions despite filing v7 letters. AHIP's silence is conspicuous given the prior-authorization implications of medication data flowing into the patient-access API. The hospital trade associations (AHA, FAH) are silent on Medications despite their detailed engagement on Adverse Events and Reason Not Performed — possibly indicating these workflows are seen as already-mature and not contested. The absence of pharmacy chain trade associations and the major PBMs is the most operationally significant gap given that NCPDP's redesign concerns about dispense quantity directly affect retail pharmacy data flows.

