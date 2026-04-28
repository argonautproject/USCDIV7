
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

## Procedures: No Changes to Profile


<!-- image of summary of changes-->
*No narrative summary of changes for Procedures Data Elements in the ASTP/ONC Standards Bulletin 2026-1.*

<!-- **:new: Definition :point_down:** -->

![image](https://hackmd.io/_uploads/B1MoqiRIZe.png)

### Summary of USCDI Comments:

*This content was developed with the assistance of Claude.*

Procedure Status has near-universal support and a clean vocabulary recommendation.

| Position | Organizations | Reasons |
|---|---|---|
| **OPPOSE** | *(no outright opposition)* | — |
| **OPPOSE / REDESIGN** | TMA (state physician society) | Defer until vocabulary specified |
| **MIXED / OPPOSE** | FAH (hospital trade association), ACLA (clinical lab trade association), APHL (public health labs), HL7 (SDO) | FAH: status fields rarely updated, default to "active." ACLA/APHL/HL7: clarify not for lab data |
| **SUPPORT / with CHANGES** | david_rocha (individual), Regenstrief Institute (research/informatics), AMA (physician society), CDC (federal/public health), csnewman (individual) | Specify FHIR EventStatus value set; SNOMED CT codes (394906002, 443938003, 416237000); CDC: only "provided/completed" |
| **SUPPORT** | CMS-CCSQ (federal/payer), Oracle Health (EHR vendor), HL7 (SDO) | Mature; supports longitudinal tracking |

For a complete summary of the comments, see the Appendix below:

<!-- markdown table summary of proposal use adobe to convert to excel and then script to markdown or just copy/paste -->

## US Core Proposed Design

### Summary

DATA ELEMENT|<br/>Standards listed are required.<br/>If more than one is listed,<br/> at least one is required unless<br/>otherwise noted.<br/>Standards versions represent the most recent <br/>available at time of publication.</center>|US Core V10 Proposal
---|---|---
| **Procedure Status ➕**<br>The status of planned or performed activity.<br>Examples include but are not limited to in-progress, completed, and not done. |  **No Change**: `Procedure.status` is already a US Core *Must Support* element|

➕ In USCDI+

### CCDA Design Notes

### Issues

### Proposal

1.  No Changes to US Core Procedure Profile nor additional guidance needed.

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


<!-- appended-from: procedures-draft.md -->

### Procedure Status (Procedures data class) — Comment Position Summary


**Comments grouped by position:**

**Strongly supportive**
- **CMS-CCSQ** [federal agency / payer] — Applauds inclusion of Procedure Status in USCDI v7. Brief, consistent with CMS-CCSQ's pattern across other v7 elements.
- **Oracle Health** [EHR vendor] — Supports inclusion of the proposed Procedure Status data element. Brief, unqualified support.
- **HL7** [SDO] — Lists Procedure Status among the v7 elements highlighted as needing clearer definitions, usage notes, and code system examples. Specifically supports Procedure Status with one boundary clarification (see mixed/oppose).

**Supportive with refinements**
- **david_rocha** [individual / standards commenter] — Provides specific SNOMED CT codes for the three example values: **394906002 |Procedure started (situation)|** and descendants for "procedure in progress"; **443938003 |Procedure carried out on subject (situation)|** and descendants for "procedure completed"; **416237000 |Procedure not done (situation)|** and descendants for "procedure not done." Argues SNOMED CT needs to be a required standard for Procedure Status to remain consistent with CMS Quality Payment Program (QPP) technical specifications.
- **Regenstrief Institute** [research/informatics institute] — Supports inclusion. Notes status of planned/performed activity (in-progress, completed, not-done) with no vocabulary specified in draft. Recommends referencing the **FHIR EventStatus value set**. Important for distinguishing planned vs. completed procedures. Aligned with public health priorities — procedure completion status needed for case reporting.
- **CDC (DSMH Working Group)** [federal agency / public health] — Supports inclusion. National Hospital Care Survey includes procedure information in restricted use and public use data files. **CDC notes a specific scope preference: "We would only want to receive 'provided' or 'completed' procedures."** Inclusion would improve accuracy of reporting procedure information in official federal statistics. Cites two demonstration projects: NHSR No. 201 ("Examination of Maternal Health Outcomes by Housing Assistance Status") and Vital and Health Statistics Series 2 No. 193 ("Identifying co-occurring disorders among patients with an opioid-involved hospital encounter using NHCS data"). Element is in C-CDA 4.0 at xpath under the Procedures Section template (templateId root 2.16.840.1.113883.10.20.22.2.7.1) statusCode element.
- **American Medical Association / AMA** [physician professional society] — Combined Procedures and Status Elements section addressing Procedure Status, Condition Status, and Immunization Status together. Supports expansion of status elements that improve interpretability and longitudinal tracking. Recommends ASTP/ONC provide **clear value set guidance and examples to ensure consistent use across systems and settings, especially where status may be inferred from workflow rather than explicitly documented**. AMA's framing aligns with FAH's workflow concern but takes the constructive position rather than the opposition position.
- **csnewman** [unaffiliated individual] — Flags an overlap concern: if the Healthcare Information Attributes data class applies to the Procedure data class, there appears to be overlap between **Indication** ("Sign, symptom, or medical condition that is the reason for a care activity") and **Reason for Referral** — and queries whether Reason for Referral is even needed in the Procedure data class given the new Referral Order data element.

**Mixed / oppose**
- **Federation of American Hospitals / FAH** [hospital trade association] — The strongest Procedure Status critique in the comment record. Argues that **in practice, procedure status fields are frequently not updated after initial entry and often default to "active" regardless of the actual state of the activity**. Exchanging status data that does not reliably reflect current clinical reality risks **misleading receiving providers and undermining confidence in the usefulness of interoperable data**. FAH does not formally oppose but flags this as a fundamental data-quality concern.
- **ACLA (American Clinical Laboratory Association)** [clinical laboratory trade association] — Notes laboratory results currently include Result Status, and would appreciate clarification that **Procedure and Procedure Status are not expected to be used for any laboratory data**.
- **APHL (Association of Public Health Laboratories)** [public health labs trade association] — Supports Procedure Status but wants to clarify that **Procedure and Procedure Status are not expected to be used for any laboratory data**. Identical scope concern to ACLA.
- **HL7** [SDO] — Supports the new Procedure Status data element but **requests clarity that Procedure and Procedure Status data elements are not expected to be used for any laboratory data**. Identical scope concern to ACLA and APHL.

**Oppose / redesign**
- **TMA (Texas Medical Association)** [state physician professional society] — Lists Procedure Status among 15 elements ONC should not adopt until each has a correlating vocabulary standard.

**Summary of Comments:** Procedure Status has near-universal support and a clean vocabulary recommendation. The element is broadly accepted as a valuable addition to the Procedures data class — no commenter outright opposes, and even TMA's [state physician society] defer-pending-vocabulary position is constructive rather than substantive. The vocabulary recommendation converges cleanly: **Regenstrief Institute** [research/informatics institute] points to the **FHIR EventStatus value set**, and **david_rocha** [individual] provides specific **SNOMED CT Situation hierarchy codes** (394906002 Procedure started, 443938003 Procedure carried out, 416237000 Procedure not done) with the rationale that SNOMED CT is required for CMS QPP technical specifications alignment. The two recommendations are reconcilable — FHIR EventStatus for the value-set structure, SNOMED CT codes for the specific concept identifiers. **The single most coordinated structural critique on Procedure Status** comes from three lab-side voices — **ACLA** [clinical laboratory trade association], **APHL** [public health labs trade association], and **HL7** [SDO] — all independently asking ONC to clarify that Procedure and Procedure Status elements **are not expected to be used for any laboratory data**. The lab side already has Laboratory Result Status (in USCDI v1+) for tracking specimen progression through the testing workflow, and the lab-side concern is that ambiguity about whether Procedure Status applies to lab orders or specimens would create dual-encoding inconsistencies between the Laboratory class and the Procedures class. This is a clean Usage Note request — ONC should explicitly state in the v7 final that Procedure Status is scoped to non-laboratory procedures. **FAH's** [hospital trade association] workflow critique — that procedure status fields are frequently not updated after initial entry and default to "active" regardless of actual state — is the most operationally specific challenge in the Procedure Status commentary. FAH's concern is that exchanging status data that doesn't reliably reflect current clinical reality could mislead receiving providers and undermine confidence in interoperable data overall. **AMA's** [physician professional society] more constructive framing addresses FAH's concern from the opposite angle: ONC should provide value-set guidance "especially where status may be inferred from workflow rather than explicitly documented." The combined FAH/AMA framing suggests ONC should add usage guidance about workflow-driven status updates — when status defaults are used, when manual updates are required, and how implementers should handle stale status values. **CDC's** [federal/public health] scope preference — only "provided" or "completed" procedures for NHCS purposes — is consistent with the FHIR EventStatus completion subset and points to a downstream filtering option for public-health consumers of Procedure Status data. **csnewman's** [individual] Procedures class overlap concern — that Indication (in the new Healthcare Information Attributes class) overlaps with Reason for Referral when both are applied to the Procedure data class — is the most pointed individual challenge to the Healthcare Information Attributes class as currently scoped, suggesting ONC has not fully reconciled which existing per-class elements should be deprecated when the new cross-cutting class elements are introduced. **The shared takeaway across all comments** is that ONC's tendency to specify value sets through narrative examples rather than referencing FHIR value sets directly creates ambiguity that implementers will resolve inconsistently. Without anchoring Procedure Status to the FHIR EventStatus value set explicitly, the v7 draft leaves the element semantically underspecified — a problem the lab-side scope clarification, the FAH workflow critique, and the AMA value-set guidance request all flag from different angles. ONC's adoption path here looks well-defined: anchor Procedure Status to FHIR EventStatus (with SNOMED CT codes for specific concepts), add a Usage Note clarifying scope excludes laboratory data, and provide implementation guidance addressing workflow-driven status updates and stale status values.

**Notably absent:** AHA, AHIP, AMIA, ANI, AAAAI, AQIPS, NCQA, WEDI, EHR Association (notably did not address Procedure Status despite addressing Reason Not Performed and Healthcare Information Attributes broadly), MEDITECH, Allina Health, Emory Healthcare, UI Health, Providence Health, FDA, AHIMA, SHIELD, CARIN Alliance, PACIO, **SNOMED International** (notable — they engaged on most other v7 elements with specific SNOMED CT code recommendations but only david_rocha provided SNOMED CT codes for Procedure Status), NCPDP, Wolters Kluwer, Vega Health, Vizient, and patient advocacy groups are silent on Procedure Status despite filing v7 letters. The complete absence of patient advocacy is consistent with a class focused on technical workflow rather than patient-facing concerns. SHIELD's silence on Procedure Status is notable given that procedure-vs-lab data scope is squarely in their domain — though APHL filed the lab-scope clarification on SHIELD's behalf, suggesting deliberate division of labor between the two organizations on lab-side issues. The absence of NCQA on Procedure Status is striking given quality measurement extensively uses procedure completion status for HEDIS measure logic. SNOMED International's absence is the single most consequential gap — they provided concrete SNOMED CT code recommendations for Specimen Collection Method, Device Type, Referral Order, and many other v7 elements, but Procedure Status received their SNOMED CT codes only via david_rocha's individual ISP submission rather than through the SNOMED International organizational letter.

---

