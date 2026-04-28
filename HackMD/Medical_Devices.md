
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

## Medical Device: No Changes to Profile


<!-- image of summary of changes-->
*No narrative summary of changes for Health Insurance Data Elements in the ASTP/ONC Standards Bulletin 2026-1.*

<!-- **:new: Definition :point_down:** -->

![image](https://hackmd.io/_uploads/B1MoqiRIZe.png)

### Summary of USCDI Comments:

*This content was developed with the assistance of Claude.*

Device Type is one of the most cleanly supported v7 additions, with **broad consensus that the element belongs in USCDI** and **convergence around SNOMED CT as the vocabulary**.

| Position | Organizations | Reasons |
|---|---|---|
| **OPPOSE** | *(no outright opposition)* | — |
| **OPPOSE / REDESIGN** | *(none)* — TMA notably did NOT include Device Type in their defer-until-vocabulary list | — |
| **MIXED / OPPOSE** | ACLA (clinical lab trade association) | Burdensome; not used in clinical decisions; LIS gaps |
| **SUPPORT / with CHANGES** | AHA (hospital trade association), FAH (hospital trade association), Emory Healthcare (academic medical center), SHIELD (lab data standards coalition), APHL (public health labs), HL7 (SDO), SNOMED International (SDO), NCQA (quality measurement), Regenstrief Institute (research/informatics) | Clarify Device Type vs. UDI; exclude calibrators/controls/consumables; SNOMED CT to required; add HCPCS for HEDIS |
| **SUPPORT** | CMS-CCSQ (federal/payer), Oracle Health (EHR vendor) | Mature; aligns with existing workflows |

For a complete summary of the comments, see the Appendix below:

<!-- markdown table summary of proposal use adobe to convert to excel and then script to markdown or just copy/paste -->

## US Core Proposed Design

### Summary

DATA ELEMENT|<br/>Standards listed are required.<br/>If more than one is listed,<br/> at least one is required unless<br/>otherwise noted.<br/>Standards versions represent the most recent <br/>available at time of publication.</center>|US Core V10 Proposal
---|---|---
| **Device Type ➕**<br>Kind of instrument, machine, appliance, implant, software, and similar medical device. | • SNOMED Clinical Terms (SNOMED CT) U.S. Edition, September 2025 Release |  **No Change**: `Device.type` is already a US Core *Must Support* element|

➕ In USCDI+

### CCDA Design Notes

### Issues

### Proposal

1.  No Changes to US Core Device Profile nor additional guidance needed.

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

### Medical Devices data class — Comment Position Summary (Device Type)

**Comments grouped by position:**

**Strongly supportive**
- **CMS-CCSQ** [federal agency / payer] — Applauds inclusion of Device Type in USCDI v7.
- **Oracle Health** [EHR vendor] — Supports inclusion of the proposed Device Type data element. Brief, unqualified support.

**Supportive with refinements**
- **American Hospital Association / AHA** [hospital trade association] — Lists Device Type as one of the elements that "align with clinical workflows and are supported by certified health IT." Notes the element captures kind of instrument, machine, appliance, implant, software, or similar medical device using SNOMED. Supports the advancement because it **supports existing workflows** and could inform **hospital quality improvement activities** related to device use and other internal analyses.
- **Federation of American Hospitals / FAH** [hospital trade association] — Notes Device Type is **already represented in exchange specifications required in the ONC Health IT Certification Program and is largely supported by certified health IT**. Supports inclusion. Frames it among elements that reflect data already routinely captured in clinical practice and would facilitate interoperability gains consistent with current operational workflow without introducing data variability.
- **Emory Healthcare** [academic medical center] — Appreciates the need to and utility of specifying device types but has concerns about **device ambiguity** for items that span categories. Specifically: **an intrauterine device is considered both a medical device and a medication**. Seeks clarity from ONC on how devices like those might be best documented.
- **SHIELD (Riki Merrick)** [lab/diagnostic data standards coalition] — Supports inclusion but recommends two scope clarifications. First, narrow the SNOMED CT scope to **descendants of 272181003 |Clinical equipment and/or device (physical object)|** rather than the entire SNOMED CT physical object hierarchy. Second, **initially focus on instruments and test kits/reagents — not controls, calibrators, or other consumables**. Recommends adding a Usage Note: *"This element supports categorization of medical devices, while the UDI element identifies the specific medical device used for that patient, procedure, performed lab tests."* Welcomes clarification on how Device Type is intended to be used in conjunction with the existing Unique Device Identifier element.
- **APHL (Association of Public Health Laboratories)** [public health labs trade association] — Suggests ONC clarify that **Device Type does not cover calibrators, controls, or consumables**. Recommends ONC update the usage notes with the same Usage Note language SHIELD proposes. APHL also files a parallel comment on the existing **Unique Device Identifier (UDI)** element with an updated usage note: *"This element can support the identification of the type of medical device, or the specific medical device used in a patient encounter. The device type is used for higher-level categorization of medical devices. When including the production identifier(s), this element identifies the specific medical device used for that patient, procedure, and/or performed lab tests."*
- **HL7** [SDO] — Recommends clarifying that the Device Type element **does not cover calibrators, controls, or consumables**. Recommends adding the same Usage Note that SHIELD and APHL propose. HL7 also flags the broader scope-boundary issue in the cover bullets: USCDI v7 needs to clarify the relationship between **Device Type vs. Unique Device Identification (UDI)** alongside Encounter vs. Appointment, Procedures vs. Orders, and Events vs. Outcomes. HL7 also recommends adding to the existing UDI element's usage note: *"Using the device identifier of the UDI data element supports the identification of the kind of medical device for that manufacturer. When including the production identifier(s) along with the device identifier of the UDI data element, it refers to the specific medical device used for that patient, procedure and performed lab tests. In contrast, the device type data element is used for the higher level categorization of medical devices."*
- **SNOMED International** [SDO — terminology] — Supports the designation of SNOMED CT as an applicable vocabulary standard for Device Type and **recommends elevation to required status**. SNOMED CT physical object hierarchy provides a clinically validated, regularly updated taxonomy of medical devices spanning implantable, non-implantable, therapeutic, and diagnostic categories. Critically, the **NLM's AccessGUDID database maps FDA UDI to device characteristics and includes SNOMED CT mappings** — establishing SNOMED CT as the terminology bridge between FDA regulatory device identifiers and clinical documentation systems. This linkage directly supports the interoperability goals of the 21st Century Cures Act's information blocking provisions. Notes that **HCPCS Level II codes, while appropriate for billing and reimbursement contexts, lack the hierarchical structure necessary for computable clinical queries and decision support**. SNOMED CT supports semantic subsumption, enabling queries such as "identify all patients with an implanted cardiovascular device." Required designation, consistent with the adjacent Medical Device Order designation, would prevent parallel incompatible coding systems from emerging as Device Type data is exchanged across TEFCA. Cites NCQA's concurrent adoption of SNOMED CT for device-related quality measures as further validation.
- **NCQA** [quality measurement org] — Strongly supports Device Type among the v7 elements with "limited implementation burden given the large overlap with other exchange requirements." Specific recommendation: **add HCPCS terminology to the applicable vocabulary standard** (alongside SNOMED). Rationale: NCQA HEDIS measures use SNOMED and HCPCS in value sets to define specific device types, such as **wheelchairs or continuous glucose monitors**.
- **Regenstrief Institute** [research/informatics institute] — Supports the addition of Device Type (SNOMED CT) **alongside the existing Unique Device Identifier (UDI)** as appropriate. Recommends ONC provide guidance on how Device Type relates to the **FDA's Global Medical Device Nomenclature (GMDN)** and the **Product Classification database**, to support consistent categorization across clinical and regulatory contexts.

**Mixed / oppose**
- **American Clinical Laboratory Association / ACLA** [clinical laboratory trade association] — The most operationally cautionary voice. Several specific concerns:
  - **Burdensome**: there could be different device types for the same test across the collection and testing processing.
  - **Limited clinical use**: "Providers do not currently factor UDI information into the clinical decision-making process as it is not a critical piece of information for treatment decisions. The required inclusion of non-pertinent information to a test result can slow down the decision process and adds costs to interoperability support and implementations."
  - **LIS support gaps**: "Existing LIS platforms may not broadly support the inclusion of UDI information with a test result. Updating these LIS systems can be expensive and time consuming while having limited impact on patient treatment decisions."
  - **Message size**: can impact the size of the result message.
  - **Data quality concern**: ACLA "is concerned that the inclusion of UDI in USCDI version 8 will not lead to broad adoption with high-quality data."
  - **Roadmap recommendation**: suggests ASTP work with **FDA, CMS/CLIA, public health agencies, laboratories, and instrument manufacturers to establish a practical roadmap**.

**Other Medical Devices class commentary (not Device Type itself):**
- **Unique Device Identifier (UDI)** (existing element): **APHL** and **HL7** both file separate comments on the existing UDI element with updated usage notes that disambiguate UDI's role from Device Type's. Both proposals frame UDI as identifying *the specific medical device used* (instance-level), while Device Type categorizes *the kind of medical device* (type-level).
- **Test Kit Unique Identifier** (proposed addition by CSTE): **CSTE** [state epidemiologists] recommends ONC add Test Kit Unique Identifier among other granular laboratory data elements (testing/performing laboratory CLIA identifier, ordering provider name, accession number, dates, abnormal flag, test result value with units/reference range/interpretation). Notes test kit identifier is critical for case adjudication and ELR linkage.
- **Medical Device Order vocabulary** (covered separately under Orders class): NCPDP recommended UDI + NDC for digital therapeutics; NCQA recommended SNOMED + HCPCS — both are vocabulary recommendations that touch the Medical Devices class boundary.

**Summary of Comments:** Device Type is one of the most cleanly supported v7 additions, with **broad consensus that the element belongs in USCDI** and **convergence around SNOMED CT as the vocabulary**. The opposition list is essentially empty — TMA notably did NOT include Device Type in their 15-element defer-until-vocabulary list, suggesting even TMA agrees the SNOMED CT vocabulary specification in the draft is adequate. The single most coordinated structural critique comes from three lab-side voices — **SHIELD** [lab data standards coalition], **APHL** [public health labs trade association], and **HL7** [SDO] — all independently asking ONC to **clarify that Device Type does not cover calibrators, controls, or consumables** and to add a Usage Note distinguishing Device Type (categorical) from UDI (instance-level). All three propose nearly identical Usage Note language: "This element supports categorization of medical devices, while the UDI element identifies the specific medical device used for that patient, procedure, performed lab tests." This is the cleanest cross-letter coordination on Usage Note language seen anywhere in the v7 record, and reflects long-running collaboration among the SHIELD/APHL/HL7 community on lab data standards. **SHIELD additionally narrows the SNOMED CT scope** to descendants of 272181003 |Clinical equipment and/or device (physical object)| rather than the entire physical object hierarchy — a precise scope refinement that would prevent Device Type from being populated with non-clinical physical objects. **SNOMED International** [SDO] takes the strongest pro-vocabulary position: elevate SNOMED CT from "applicable" to "required," anchored on the **NLM AccessGUDID mapping that already bridges FDA UDI to SNOMED CT** — a federally maintained crosswalk that makes SNOMED CT the natural terminology bridge between FDA regulatory identifiers and clinical documentation. SNOMED Intl's argument that HCPCS Level II lacks the hierarchical structure for computable subsumption queries (e.g., "identify all patients with an implanted cardiovascular device") is the most concrete clinical-decision-support justification for SNOMED CT-required status. **NCQA** [quality measurement org] takes the parallel position from the quality-measurement angle: HEDIS uses both SNOMED and HCPCS for device value sets (wheelchairs, continuous glucose monitors), so HCPCS should be added as applicable vocabulary alongside SNOMED. The two recommendations are reconcilable — SNOMED CT for clinical EHR implementations (SNOMED Intl's framing) plus HCPCS for billing and quality measurement (NCQA's framing), with **AccessGUDID and the FDA UDI database providing the cross-walk infrastructure** Regenstrief flags. **Emory Healthcare's** [academic medical center] IUD example — that an intrauterine device is both a medical device and a medication — is the sharpest individual edge case in the Device Type commentary and surfaces a real cross-class scope question (is the IUD captured in Medical Devices, Medications, or both?) that ONC will need to address in implementation guidance. **ACLA's** [clinical laboratory trade association] operational critique is the only substantive challenge to inclusion: the lab-side workflow cost of capturing Device Type for every test, the limited use of UDI/Device Type information in clinical decision-making, and the LIS-system burden of supporting these elements. ACLA's concern that "inclusion of UDI in USCDI version 8 will not lead to broad adoption with high-quality data" is consistent with their parallel concern on Specimen Collection Method — both reflect ACLA's view that USCDI elements should match information actually flowing through lab-side systems rather than ideal data captures. ACLA's proposed solution — that ASTP work with **FDA, CMS/CLIA, public health agencies, laboratories, and instrument manufacturers to establish a practical roadmap** — is the most policy-specific recommendation in any v7 element commentary and effectively asks ONC to convene a cross-agency working group rather than mandate Device Type unilaterally. **The shared takeaway across all comments** is that Device Type benefits enormously from **already having a vocabulary specified** (SNOMED CT) — the only v7 element with this property among the more contested additions — and the discussion accordingly focuses on **scope refinement (excluding calibrators/controls/consumables, narrowing the SNOMED CT subhierarchy, distinguishing Device Type from UDI)** rather than vocabulary debate. ONC's adoption path here looks well-defined: incorporate the shared SHIELD/APHL/HL7 Usage Note, narrow the SNOMED CT scope per SHIELD's recommendation, add HCPCS as applicable per NCQA, and provide cross-reference guidance to FDA AccessGUDID / GMDN / Product Classification per Regenstrief.

**Notably absent:** AHIP, AMIA, ANI, AMA, AAAAI, AQIPS, MEDITECH (notable — engaged on most other v7 elements but silent on Device Type despite its EHR-implementation implications), Allina Health, Providence Health, UI Health, **FDA** (the single most striking absence — FDA is the regulatory authority for medical devices and UDI under the 2007 FDA Amendments Act, and AccessGUDID is FDA-maintained), AHIMA, CDC, CSTE (engaged on Test Kit Unique Identifier but not Device Type itself), AAAAI, CARIN Alliance, PACIO, NCPDP (engaged on Medical Device Order but not Device Type), Wolters Kluwer, Vega Health, Vizient, WEDI, Epic (notable — addressed Medical Device Order extensively but no separate Device Type comment, suggesting implicit support), AMIA, and patient advocacy groups are silent on Device Type despite filing v7 letters or being active in the v7 process. **FDA's complete absence is the single most consequential gap** given that Device Type, UDI, AccessGUDID, GMDN, and the Product Classification database are all FDA-maintained or FDA-regulated infrastructure. SNOMED International, Regenstrief, and others reference FDA databases extensively, but FDA has no voice in the record advising ONC on the regulatory bridge between SNOMED CT clinical documentation and FDA's device classification system. The absence of medical device manufacturer trade associations (AdvaMed, MDMA) is also striking given they are the upstream source of UDI data and would be primary affected parties of Device Type implementation choices. Patient advocacy groups are absent despite Device Type implications for patient-facing concerns like device recalls and adverse event reporting.


