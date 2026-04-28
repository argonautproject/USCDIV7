
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

## Orders: New Profiles Needed


<!-- image of summary of changes-->

![image](https://hackmd.io/_uploads/HkKiY1lPbe.png)
![image](https://hackmd.io/_uploads/rJeR3F1ePbx.png)
![image](https://hackmd.io/_uploads/SJx5KkxDWe.png)

<!-- **:new: Definition :point_down:** -->

![image](https://hackmd.io/_uploads/ry8J9kgvbl.png)


### Summary of USCDI Comments:

*This content was developed with the assistance of Claude.*

| Position | Organizations | Reasons |
|---|---|---|
| **OPPOSE** | *(no outright opposition)* | — |
| **OPPOSE / REDESIGN** | TMA (state physician society) | Defer all three until vocabularies specified |
| **MIXED / OPPOSE** | Epic (EHR vendor), EHR Association (vendor trade association), Oracle Health (EHR vendor) | Epic: limit Med Device Order to implantable devices. EHR Assoc: not all EHRs (esp. ambulatory) support structured Nutrition Orders. Oracle: limit Referral Order to medical specialists only |
| **SUPPORT / with CHANGES** | NASPGHAN/CPNP (pediatric specialty societies), Academy of Nutrition and Dietetics (clinical specialty society), HL7 (SDO), SNOMED International (SDO), NCPDP (pharmacy SDO), NCQA (quality measurement), EHR Association (vendor trade association), WEDI (admin trade association), Regenstrief Institute (research/informatics), Altarum Institute (research org) | Vocabulary additions: SNOMED CT + LOINC + IDDSI for Nutrition; SNOMED + HCPCS for Med Device; SNOMED CT required for Referral. NASPGHAN/CPNP: enumerate parenteral nutrition. NCPDP: UDI + NDC for digital therapeutics. WEDI: distinguish referral/consult/transition. Altarum: NutritionOrder less mature than MedicationRequest |
| **SUPPORT** | CMS-CCSQ (federal/payer), Oracle Health (EHR vendor) — Med Device & Nutrition, Wolters Kluwer (clinical content vendor) | Mature, FHIR-aligned, vendor-implemented; reflects real-world workflows |

For a complete summary of the comments, see the Appendix below:

<!-- markdown table summary of proposal use adobe to convert to excel and then script to markdown or just copy/paste -->

## US Core Proposed Design

### Summary

DATA ELEMENT|<br/>Standards listed are required.<br/>If more than one is listed,<br/> at least one is required unless<br/>otherwise noted.<br/>Standards versions represent the most recent <br/>available at time of publication.</center>|US Core V10 Proposal
---|---|---
| **Medical Device Order ➕**<br>Provider-authored request for medical devices.<br>Examples include but are not limited to therapeutic footwear, insulin infusion pump, and continuous positive airway pressure (CPAP) machine. |  | 🆕 US Core DeviceRequest Profile (See Proposal)
| **Nutrition Order ➕**<br>Provider-authored request for therapeutic diet, nutrition support, and nutrition to promote and maintain health.<br>Examples include but are not limited to cardiac diet, Mediterranean diet, whole food diet, clear liquid diet, enteral nutrition, and nutritional<br>supplement. |  |🆕 US Core NutritionOrder Profile (See Proposal)
| **Referral Order**<br>Provider-authored request to another provider, specialist, or organization for care services.<br>Examples include but are not limited to referral<br>orders to a wound care specialist and to a podiatrist. |  | Update guidance in US Core ServiceRequest Profile

➕ In USCDI+

### CCDA Design Notes

### Issues :thinking_face: 

1. DeviceRequest is FMM=1, NutritionOrder is FMM =2 in FHIR R4  (both part of FHIR R6)
2. Implementer Support?
3. Terminology???

### Proposal
1.  🆕 US Core DeviceRequest Profile
     - Mandatory and Must Support elements: Must Support elements: `status, intent (m),code[x] (m), subject (m), authoredOn, requester`  (m = mandatory in base)
     - Search Parameters: patient, status, authored, code
1.  🆕 US Core NutritionOrder Profile
     - Mandatory and Must Support elements: Must Support elements: `status (m), intent (m), patient (m), dateTime (m), orderer, oralDiet.type`  (m = mandatory in base)
     - Search Parameters: patient, status, datetime, type
1.  Update guidance in US Core ServiceRequest Profile
   - Category codes for referrals
   - Additional bindings referrals

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

#### DeviceRequest
- [QI Core](https://packages2.fhir.org/xig/resource/hl7.fhir.us.qicore%7Ccurrent/StructureDefinition/qicore-devicerequest)
- [DME](https://packages2.fhir.org/xig/resource/hl7.fhir.us.dme-orders%7Ccurrent/StructureDefinition/PAOX-devicerequest)
- [PCT](http://hl7.org/fhir/us/davinci-pct/STU2/StructureDefinition-davinci-pct-devicerequest.html)

#### NutritionOrder
- [PACIO]([pfe-nutrition-order](https://packages2.fhir.org/xig/resource/hl7.fhir.us.pacio-pfe%7Ccurrent/StructureDefinition/pfe-nutrition-order))
- [QI Core](https://packages2.fhir.org/xig/resource/hl7.fhir.us.qicore%7Ccurrent/StructureDefinition/qicore-nutritionorder)
- [MCC](https://packages2.fhir.org/xig/resource/hl7.fhir.us.mcc%7Ccurrent/StructureDefinition/MCCNutritionOrder)



<!-- appended-from: orders-draft.md -->

### Orders data class — Comment Position Summary (Medical Device Order, Nutrition Order, Referral Order)

**Class additions:** Draft USCDI v7 adds three new data elements to the existing Orders data class. **Medical Device Order** — provider request for a medical device (examples: therapeutic footwear, insulin pump, CPAP). **Nutrition Order** — request for therapeutic diet or nutrition support; represented in HL7 FHIR via the NutritionOrder resource. **Referral Order** — structured request for care services from another provider, specialist, or service.

| Position | Organizations | Reasons |
|---|---|---|
| **OPPOSE** | *(no outright opposition)* | — |
| **OPPOSE / REDESIGN** | TMA (state physician society) | Defer all three until vocabularies specified |
| **MIXED / OPPOSE** | Epic (EHR vendor), EHR Association (vendor trade association), Oracle Health (EHR vendor) | Epic: limit Med Device Order to implantable devices. EHR Assoc: not all EHRs (esp. ambulatory) support structured Nutrition Orders. Oracle: limit Referral Order to medical specialists only |
| **SUPPORT / with CHANGES** | NASPGHAN/CPNP (pediatric specialty societies), Academy of Nutrition and Dietetics (clinical specialty society), HL7 (SDO), SNOMED International (SDO), NCPDP (pharmacy SDO), NCQA (quality measurement), EHR Association (vendor trade association), WEDI (admin trade association), Regenstrief Institute (research/informatics), Altarum Institute (research org) | Vocabulary additions: SNOMED CT + LOINC + IDDSI for Nutrition; SNOMED + HCPCS for Med Device; SNOMED CT required for Referral. NASPGHAN/CPNP: enumerate parenteral nutrition. NCPDP: UDI + NDC for digital therapeutics. WEDI: distinguish referral/consult/transition. Altarum: NutritionOrder less mature than MedicationRequest |
| **SUPPORT** | CMS-CCSQ (federal/payer), Oracle Health (EHR vendor) — Med Device & Nutrition, Wolters Kluwer (clinical content vendor) | Mature, FHIR-aligned, vendor-implemented; reflects real-world workflows |

**Comments grouped by position:**

**Strongly supportive**
- **CMS-CCSQ** [federal agency / payer] — Applauds inclusion of Nutrition Order in USCDI v7. (No separate CMS-CCSQ comments captured for Medical Device Order or Referral Order.)
- **Oracle Health** [EHR vendor] — Generally supports inclusion of Medical Device Order, particularly supports ONC's choice not to reference a vocabulary standard since DME orders are typically descriptive in the absence of a national vocabulary standard. Notes this is "yet another example of the scope of USCDI not being applicable to all EHRs or other HIT" (Oracle's broader argument for USCDI subset certification). Generally supports Nutrition Order with the same scope-applicability caveat.
- **Wolters Kluwer** [clinical content vendor] — Cites Nutrition Order, Medical Device Order, and Medication Administration among the v7 additions that "reflect real-world clinical workflows and provide deeper granularity needed for care planning, treatment management, and evidence-based practice." Frames the nutrition additions as advancing the Make America Healthy Again priorities related to chronic disease prevention and lifestyle-driven health outcomes.

**Supportive with refinements**
- **NASPGHAN (North American Society for Pediatric Gastroenterology, Hepatology and Nutrition) and CPNP (Council of Pediatric Nutrition Professionals)** [pediatric specialty professional societies] — Strongly support Nutrition Order inclusion as a required data class. Specifically urge ONC to **explicitly enumerate parenteral nutrition (PN) orders** within the scope. NASPGHAN represents 3,000+ pediatric subspecialist physicians; CPNP represents ~350 pediatric nutrition professionals. Argument: nutrition orders (oral, enteral, parenteral) are therapeutic interventions with significant safety implications, and interoperability failures during care transitions are a well-documented source of patient harm. Cites a national survey of pediatric clinicians showing only 54% reported standardized workflows for documenting food allergies/intolerances; 73% reported awareness of nutrition-related safety events at their institutions, including adverse reactions linked to incomplete or inaccessible documentation.
- **Academy of Nutrition and Dietetics (AND)** [clinical specialty professional society] — Strongly supports Nutrition Order and Nutrition Assessment inclusion as a "monumental step" ensuring nutritional care is fully integrated into the digital healthcare ecosystem. Documents current exchange maturity: Nutrition Order is actively exchanged using HL7 FHIR NutritionOrder; tested through PACIO Connectathons; included in the PACIO Implementation Guide; major EHR vendors (Epic, Oracle Health) have already implemented FHIR endpoints. Notes cross-specialty utility — RDNs, Speech-Language Pathologists (dysphagia/texture-modified diets), Occupational Therapists (feeding ability), and providers/nurses (therapeutic diets). Recommended terminology additions: SNOMED CT Dietary Regime (182922004) and sub-concepts, Enteral Feeding (229912004), Mixed Breast Milk and Bottle Feeding (35011000087100), Breast Milk Feeding (1297276008), Bottle Feeding of Patient (40043006), and **International Dysphagia Diet Standardization Initiative (IDDSI)** terminology.
- **HL7** [SDO] — Strongly supports Nutrition Order. Frames inclusion as "a critical step toward the 'Make America Healthy Again' initiative." Documents technical maturity in three dimensions: (1) FHIR alignment — represented by HL7 FHIR NutritionOrder resource following the standard request pattern used for medications and procedures; (2) proven exchange — successfully tested through PACIO Project and HL7 Connectathons in transitions of care (hospital to long-term care); (3) vendor readiness — major EHRs (Epic, Oracle Health, etc.) have already implemented FHIR R4 endpoints for the resource. Cross-specialty use: Speech-Language Pathologists for dysphagia/texture modifications and practitioners managing therapeutic diets (renal, diabetic, etc.). HL7's broader letter also flags Encounter vs. Appointment, Device Type vs. UDI, and **Procedures vs. Orders** scope boundaries as needing clarification.
- **SNOMED International** [SDO — terminology] — Two element-specific recommendations:
  - **Nutrition Order**: Recommends ONC designate SNOMED CT U.S. Edition as recommended or required vocabulary. SNOMED CT includes clinically validated concepts: 373783004 |Diet (substance)|, 182922004 |Dietary regime (regime/therapy)|, 160670007 |Cardiac diet (finding)|, 444971000124105 |Liquid diet (finding)|. FHIR NutritionOrder already supports SNOMED CT for oral diet type, supplement type, and enteral formula type coding. Notes SNOMED International's long-term collaboration agreement with the Academy of Nutrition and Dietetics to include NCPT (Nutrition Care Process Terminology) into SNOMED CT.
  - **Referral Order**: **Elevate SNOMED CT designation from "applicable" to "required."** SNOMED CT procedure hierarchy provides comprehensive standardized vocabulary including 307837007 |Referral to person (procedure)| and 306206005 |Referral to service (procedure)| and descendants. NCQA HEDIS quality measures already incorporate SNOMED CT-coded referral value sets, demonstrating validated real-world adoption at scale. Argues reliance on local or proprietary referral codes still prevalent in EHRs creates barriers to 21st Century Cures Act and TEFCA care coordination interoperability. Required designation, consistent with CMS QPP technical specifications, would drive convergence and eliminate costly mapping.
- **NCPDP (National Council for Prescription Drug Programs)** [pharmacy SDO] — Two recommendations:
  - **Medical Device Order**: add UDI and NDC to applicable vocabulary standards. Frames as enabling exchange of digital therapeutics, especially **prescription digital therapeutics**.
  - **Referral Order**: supports use of SNOMED, HCPCS, and CPT (used in the most recently named NCPDP SCRIPT Standard) and recommends **HCPCS and CPT be added** to applicable vocabulary standards.
- **NCQA** [quality measurement org] — Strongly supports both Medical Device Orders and Referral Orders (uses plural in their letter — likely typographical) among the v7 additions with "limited implementation burden given the large overlap with other exchange requirements." Specific recommendation: **add SNOMED and HCPCS terminology** to Medical Device Order applicable vocabulary standards. Rationale: NCQA is developing several new measures that include device orders, with SNOMED and HCPCS terminology in use and aligned to FHIR.
- **EHR Association** [vendor trade association] — Supports addition of Referral Order and Medical Device Order with scope-clarification asks:
  - **Medical Device Order**: requests clarification on scope across device categories. Implantable device ordering (e.g., pacemaker) involves multi-step process — referral, implantation, post-procedure documentation, device registry entry. CPAP ordering follows simpler DME workflow. These differences materially affect EHR capture and exchange. Recommends ONC provide explicit guidance on application to implantable vs. non-implantable devices.
  - **Referral Order**: supports inclusion. Provider-authored requests for care services are broadly documented in EHR systems, but Referral Order scope spans a wide spectrum — medical specialty referrals, social and community services, home health — each with distinct workflows and data structures. Not all EHRs support all referral types. Recommends ONC clearly delineate scope, specifying whether it applies solely to medical specialty referrals or also includes social services and community-based referrals.
- **WEDI** [administrative/transactions trade association] — Cites Referral Order and Referral Note among v7 additions that "could materially reduce administrative burden and improve interoperability." Recommendations: clarify how Referral Order/Note connect to Appointment, Encounter, and the receiving organization; provide guidance and examples distinguishing "referral request" vs. "consult request" vs. "transition of care" communications to reduce inconsistent implementations; encourage alignment with API-based coordination workflows so referral content can be used downstream — "referrals are a major friction point across providers and payers."
- **Regenstrief Institute** [research/informatics institute] — Element-by-element table positions:
  - **Medical Device Order**: Support. No vocabulary specified. Examples: therapeutic footwear, insulin pump, CPAP. Recommendation: consider referencing SNOMED CT or HCPCS for device order identification.
  - **Nutrition Order**: Support with caveat. No vocabulary specified in draft. Vocabulary readiness for Nutrition Assessment is strong (21 nutrition-related LOINCs in v2.82, anchored by 75303-8 Nutrition assessment Narrative, 75293-1 Physical findings, 75282-4 Nutrition assessment panel, plus the standardized MNA-SF panel 107107-5). Recommends ONC clarify expected vocabulary for Nutrition Order, potentially referencing **LOINC for order identification and SNOMED CT for diet type concepts**, consistent with the FHIR NutritionOrder resource structure.
  - **Referral Order**: Support. Structured referral request to another provider/specialist. No vocabulary specified. Pairs well with new Referral Note in Clinical Notes — "the order + note pairing is well-designed for referral workflows." Aligned with care coordination.
- **Altarum Institute** [health-services research org] — On Nutrition Order, raises an implementation maturity consideration: while the element addresses important clinical and public health needs, **the FHIR NutritionOrder resource is less widely implemented in production systems** than more commonly exchanged order patterns (medication orders captured via MedicationRequest). For many implementers, medication ordering provides a familiar baseline for what a "minimum viable" order should include (who ordered it, what is being ordered, timing/schedule, status, patient-specific instructions). Recommends ASTP/ONC add brief usage guidance clarifying intended scope (enteral/parenteral nutrition vs. diet orders), the minimum set of fields expected for exchange, and how Nutrition Order relates to or differs from other order types in USCDI (particularly medication orders), so organizations can implement consistently across acute and post-acute care transitions.

**Mixed / oppose**
- **Epic** [EHR vendor] — Recognizes the value of Medical Device Order and the clinical need for consistent exchange across organizations. Recommends ONC clarify intended scope before finalization and specify a required vocabulary standard. Argues complexity of implementation varies significantly by device type: medical device orders for **implantable devices** represent a well-understood concept with consistent documentation practices across the industry; orders for **other durable medical equipment** are documented in more varied ways across organizations and EHR implementations, and the vocabulary standards and workflows necessary for consistent exchange are not uniform. Recommends ONC acknowledge this variation and **limit the scope of this element to implantable devices with mature documentation practices**. Epic does not separately address Nutrition Order or Referral Order.
- **EHR Association** [vendor trade association] (Nutrition Order — mixed, while supporting Med Device Order and Referral Order) — Requests clarification on scope and applicability of Nutrition Order across EHR types. Nutrition orders vary widely from clinical dietary prescriptions in inpatient settings to nutritional supplement recommendations in ambulatory care. **Not all EHR systems — particularly those serving ambulatory-only practices — are designed to capture structured nutrition orders.** Cited examples span a broad complexity range, from total parenteral nutrition (TPN) and enteral nutrition to general dietary recommendations. Recommends ONC clarify the **minimum scope** and specify which care settings are expected to support it; requirements should reflect each setting's clinical and workflow context and should not impose structured documentation requirements on EHRs that do not routinely support nutrition ordering workflows.
- **Oracle Health** [EHR vendor] (Referral Order — mixed) — Supports inclusion but has concerns about scope. **Recommends ONC limit the scope of Referral Order to exclusively medical specialist referrals, not to social and community services.** Frames as another example of USCDI overreach into workflows not all EHRs are designed to support. (Oracle separately supports Medical Device Order and Nutrition Order, so their position is element-specific.)

**Oppose / redesign**
- **TMA (Texas Medical Association)** [state physician professional society] — Lists **Medical Device Order** ("Medication Device Order" — apparent typo in TMA's letter), **Nutrition Order**, and **Referral Order** among 15 elements ONC should not adopt until each has a correlating vocabulary standard.

**Summary of Comments:** The Orders data class additions show three distinct support profiles — one element with broad clean support, one with subject-matter-society backing plus structural caveats, and one with scope-boundary debate. **Nutrition Order** is the most supported v7 addition reviewed so far measured by depth of subject-matter engagement. The pediatric-nutrition specialty societies (NASPGHAN, CPNP) [clinical specialty professional societies], the registered-dietitian professional society (Academy of Nutrition and Dietetics), HL7 [SDO], and Regenstrief [research/informatics institute] all specifically endorse the element with vocabulary recommendations that converge on the same answer: **LOINC for order identification + SNOMED CT for diet type concepts** (with IDDSI dysphagia terminology added per AND). HL7 frames the element as technically mature with proven exchange (PACIO Connectathons, Epic and Oracle Health FHIR R4 endpoints). The only structural critique on Nutrition Order comes from the EHR Association [vendor trade association], who argue ambulatory-only EHRs may not be designed to capture structured nutrition orders — which Altarum [research org] echoes by noting the FHIR NutritionOrder resource is less widely deployed than MedicationRequest. Both ask ONC to scope by care setting, not abandon the element. **Medical Device Order** has the most vocabulary debate and the most explicit scope-redesign request. Three SDOs/quality orgs propose three valid vocabulary stacks — NCPDP [pharmacy SDO] proposes UDI + NDC for digital therapeutics, NCQA [quality measurement] proposes SNOMED + HCPCS for HEDIS measure alignment, Regenstrief [research/informatics] proposes SNOMED CT or HCPCS — but Epic [EHR vendor] takes the strongest scope position: **limit to implantable devices** where documentation is mature. Oracle Health [EHR vendor] takes the opposite position, *supporting* the element precisely because no vocabulary is mandated, since DME orders are typically descriptive. The EHR Association [vendor trade association] occupies the middle, asking ONC to differentiate guidance for implantable vs. DME without picking one or the other. **Referral Order** has near-universal support but a single contested scope question: **does it cover only medical specialty referrals or also social services and community-based referrals?** Oracle Health [EHR vendor] takes the strongest position — limit to specialty referrals. The EHR Association asks ONC to delineate scope without picking. WEDI [administrative trade association] wants explicit examples distinguishing referral request, consult request, and transition of care — the same scope-disambiguation request from a different angle. SNOMED International's [SDO] specific ask to **elevate SNOMED CT from applicable to required** for Referral Order (with concrete codes 307837007 and 306206005, and CMS QPP alignment) is the most concrete vocabulary recommendation across all three Orders elements and would directly address the "local code drift" risk WEDI and others raise. **Across all three elements, the most striking structural critique** comes from HL7 [SDO]: their letter flags **Procedures vs. Orders** as a scope-boundary that USCDI v7 needs to clarify alongside Encounter vs. Appointment and Device Type vs. UDI. None of the Orders-specific comments engage that question directly, suggesting this remains an open issue that ONC will need to resolve in implementation guidance.

**Notably absent:** AHA, FAH, AHIP, AMIA, ANI, AMA, AQIPS, MEDITECH, Allina Health, Emory Healthcare, UI Health, Providence Health, FDA (notable for Medical Device Order given UDI and digital therapeutics), CDC, APHL, CSTE, AHIMA, ACLA, SHIELD, Vizient, Vega Health, CARIN Alliance, and AAAAI are all silent or only tangentially engaged on the Orders class additions despite filing v7 letters. AHIP's silence is conspicuous given that referrals and DME orders are central to prior-authorization workflows targeted by the CMS-0057-F Final Rule that takes effect January 2027. The absence of FDA on Medical Device Order is striking given UDI is a core FDA medical device regulation — NCPDP raises the UDI question without an FDA voice in the record. Speech-language pathology and occupational therapy professional societies (ASHA, AOTA) are absent despite both being explicitly invoked by HL7 and AND as cross-specialty users of Nutrition Order. The home health and DME supplier trade associations (NAHC, AAHomecare) are absent despite the element directly affecting their workflows.

