
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

## Health Insurance Information: No Changes to Profile


<!-- image of summary of changes-->
*No narrative summary of changes for Health Insurance Data Elements in the ASTP/ONC Standards Bulletin 2026-1.*

<!-- **:new: Definition :point_down:** -->

![image](https://hackmd.io/_uploads/HJihwc0Ibe.png)

### Summary of USCDI Comments:

*This content was developed with the assistance of Claude.*

| Position | Organizations | Reasons |
|---|---|---|
| **OPPOSE** | AHIP (insurance trade association) | Patient privacy / re-identification risk once data is shared via API to non-HIPAA third-party apps; no national plan identifier standard exists (HPID rescinded; NAIC, HIOS not universal); Coverage Period from non-source-of-truth providers risks outdated/confusing information |
| **OPPOSE / REDESIGN** | TMA (state physician society) | Defer all four elements until correlating vocabulary standards are specified |
| **MIXED / OPPOSE** | WEDI (admin/transactions trade association), MEDITECH (EHR vendor) | WEDI: confusion likely between USCDI data and administrative transactions (eligibility/benefits) which are more accurate; risks free text/local codes; need "as of" date and source attribution guidance; clarify these support — not replace — administrative functions. MEDITECH: Coverage Period requires new build (only expiration date is captured today); Payer needs clarification on which EHR field to reference; Plan and Plan Identifier already supported |
| **SUPPORT / with CHANGES** | AHA (hospital trade association), FAH (hospital trade association), Epic (EHR vendor), Regenstrief Institute (research/informatics), csnewman (individual) | AHA: provide examples of plan identifiers; explain need vs. rescinded 2012 HPID requirements; provide examples for Payer and Plan to prevent variability. FAH: clarify plan identifiers via examples; identify relationship between plan-by-type and member identifiers. Epic: clarify Payer and Plan refer specifically to *names* (not all the sub-attributes, which are covered by separate Identifier elements). Regenstrief: vocabulary gap — reference NPPES, CARIN Alliance payer identifiers, or HIOS plan identifiers (ACA marketplace). csnewman: disambiguate near-identical descriptions of existing Health Insurance Group Identifier and new Plan Identifier |
| **SUPPORT** | CMS-CCSQ (federal agency / payer), CDC (federal agency / public health), UI Health (academic medical center), Oracle Health (EHR vendor), NCQA (quality measurement org) | CMS-CCSQ: applauds inclusion of all four. CDC: critical for birth-certificate "principal source of payment" reporting and NHCS maternal-outcomes analysis by health insurance and housing assistance status. UI Health: most critical component of v7 — directly aligns with CMS-0057-F Prior Authorization API mandate (Jan 1, 2027). Oracle Health: supports all four. NCQA: strongly supports as high-value adds with limited burden |

For a complete summary of the comments, see the Appendix below:

<!-- markdown table summary of proposal use adobe to convert to excel and then script to markdown or just copy/paste -->

## US Core Proposed Design

### Summary

DATA ELEMENT|<br/>Standards listed are required.<br/>If more than one is listed,<br/> at least one is required unless<br/>otherwise noted.<br/>Standards versions represent the most recent <br/>available at time of publication.</center>|US Core V10 Proposal
---|---|---
**Health Insurance Coverage Period ➕**<br />The time frame in which the policy is in force.||**No Change**: `Coverage.period` is already a US Core *Must Support* element|
| **Health Insurance Payer**<br>Issuer of the policy. | | **No Change**: `Coverage.payor` is already a  US Core *Must Support* element|
| **Health Insurance Plan ➕**<br>Health insurance offering or package. |  | **No Change**:`Coverage.class:plan` is already a  US Core *Must Support* element|
| **Health Insurance Plan Identifier ➕**<br>Sequence of characters used to uniquely refer to an insurance plan. |  |**No Change**: `Coverage.class:plan.value` and `Coverage.class:plan.name` already are US Core *Must Support* elements|

➕ In USCDI+

### CCDA Design Notes

### Issues

### Proposal

1.  No Changes to US Core Coverage Profile nor additional guidance needed.

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

### Comment Position Summary

**Comments grouped by position:**

**Strongly supportive**
- **CMS-CCSQ** [federal agency / payer] — Filed four parallel "applauds inclusion" comments, one for each element (Coverage Period, Payer, Plan, Plan Identifier).
- **CDC (DSMH Working Group)** [federal agency / public health] — Filed coordinated comments on all four. Frames the use case around the U.S. Standard Certificate of Live Birth and Facility Worksheet for the Live Birth Certificate, both of which require identification of the **principal source of payment for the delivery** at the time of delivery (private insurance, Medicaid or comparable state program, self-pay, other source). Cites NHCS demonstration projects showing utility of including health insurance in maternal outcomes analyses by housing assistance status. For Payer Name specifically, notes the data lives at C-CDA 4.0 Payers Section template `2.16.840.1.113883.10.20.34.2.4`/`2.16.840.1.113883.10.20.22.4.129` and that all EHR encounters in NHCS production already include payer name information.
- **UI Health (University of Illinois Health)** [academic medical center] — Strong Support. Frames Health Insurance Information as "the most critical component of the v7 proposal." Direct alignment with the CMS-0057-F Final Rule requirements that take effect January 1, 2027. Argument: to meet the 2027 mandate for automated, electronic Prior Authorization APIs, healthcare systems must be able to programmatically identify plan-specific requirements. Standardizing these elements reduces the administrative friction caused by manual payer portal navigation. "Without a standardized Plan Identifier, the move toward real-time authorization remains an aspirational goal rather than an operational reality."
- **Oracle Health** [EHR vendor] — "We support the inclusion of the proposed Health Insurance Coverage Period, Health Insurance Payer, Health Insurance Plan, and Health Insurance Plan Identifier data elements." No qualifications.
- **NCQA** [quality measurement org] — Lists Health Insurance Information elements among the v7 additions NCQA "strongly supports" as high-value adds with limited implementation burden given large overlap with other exchange requirements.

**Supportive with refinements**
- **American Hospital Association / AHA** [hospital trade association] — Agrees standardized exchange of payer and plan data can minimize administrative burden and improve care coordination across care settings. Asks ONC to provide clarifying details: (1) examples of plan identifiers to minimize variation and prevent free-text or local codes; (2) clarifying information on why the element is needed *now* and **how this proposal differs from the rescinded 2012 health plan identifier (HPID) requirements** that were withdrawn after stakeholder concerns about provider burden, implementation costs, and inefficiencies; (3) examples for Payer and Plan, since their current descriptions don't include any. AHA's HPID reference is the most pointed historical critique — implicitly asking ONC to demonstrate this isn't HPID 2.0.
- **Federation of American Hospitals / FAH** [hospital trade association] — Supports inclusion of all four elements; already widely captured and supported in certified health IT. Standardized exchange of payer and plan information can reduce administrative burden, improve coordination, and help providers identify changes to coverage more expeditiously. Urges clarification of plan identifiers through examples and through identifying the relationship between plan (by specific type of plan) and member identifiers.
- **Epic** [EHR vendor] — Recommends ONC clarify the definitions of Health Insurance Payer and Health Insurance Plan to specify that each refers to a **name**. As currently written, both definitions are broad enough to encompass sub-attributes such as identifiers, contact information, and plan terms — which are already addressed by Health Insurance Payer Identifier and Health Insurance Plan Identifier data elements elsewhere in the draft. Without this clarification, the same conceptual content could be exchanged through multiple elements inconsistently.
- **Regenstrief Institute** [research/informatics institute] — Supports with caveat across all four elements. Important for administrative interoperability and prior authorization workflows (particularly in alignment with CMS-0057-F), but most elements lack specified vocabulary standards — only Health Insurance Coverage Type references Source of Payment Typology (SOPT) v9.2. Recommends ONC reference existing payer and plan identifier systems: **CMS National Plan and Provider Enumeration System (NPPES)** identifiers; the **CARIN Alliance's payer identifier work**; and **HIOS (Health Insurance Oversight System)** plan identifiers used in ACA marketplace contexts. Notes plan names are not standardized across payers, so guidance on minimum expected structure (plan name + type at minimum) is needed.
- **csnewman** [unaffiliated individual] — Flags that the descriptions of the existing Health Insurance Group Identifier ("Sequence of characters used to uniquely refer to a specific health insurance plan") and the new Health Insurance Plan Identifier ("Sequence of characters used to uniquely refer to an insurance plan") are nearly identical and should be disambiguated.

**Mixed / oppose**
- **WEDI** [administrative/transactions trade association — formal HHS Secretary advisor] — Substantial concerns specifically about Health Insurance Information elements: they may cause **confusion between data collected and shared through USCDI vs. administrative transactions, which are likely more accurate**. Confusion about Health Insurance Payer, Plan, and Plan Identifier will likely lead to use of free text or local codes, providing limited interoperability benefit. Additionally, guidance is needed on how "as of" dates and source attribution should be conveyed, and clarification is needed on which data elements can support workflows but not *replace* administrative functions (eligibility and benefits verification). These data elements are integral to administrative simplification "but risk real-world usability if used inconsistently."
- **MEDITECH** [EHR vendor] — Partial support, partial concern, element by element:
  - **Coverage Period** — the insurance policy expiration date is standardly captured today, but **not a coverage period start date**. New development work would be required.
  - **Payer** — further clarification needed; health insurance and payer information are captured in more than one area of an EHR; unclear from current proposed definition which fields would need to be referenced.
  - **Plan and Plan Identifier** — already supported, no concerns.

**Oppose / redesign**
- **TMA (Texas Medical Association)** [state physician professional society] — Lists all four Health Insurance Information elements (Coverage Period, Payer, Plan, Plan Identifier) among 15 elements ONC should not adopt until each has a correlating vocabulary standard.

**Oppose**
- **AHIP (America's Health Insurance Plans)** [insurance trade association] — The most extensive and only outright opposition. Recommends ONC **not add** Health Insurance Payer, Health Insurance Plan, Health Insurance Plan Identifier, or Health Insurance Coverage Period, and recommends *removing* the existing Payer Identifier. Four arguments:
  - **Privacy and security**: Once shared via the Patient Access API to third-party applications under the ONC Cures Act Rule and CMS Interoperability and Patient Access Rule, data falls outside HIPAA protection. There is no data segmentation opportunity — all USCDI elements are required to be shared with selected third-party applications. AHIP recommends ONC remove Member Identifier, Subscriber Identifier, Relationship to Subscriber, and Group Identifier on these grounds.
  - **Re-identification risk**: Detailed benefit information could be used to identify someone in a different data set, make associations across data sets, or re-identify a de-identified data set.
  - **No national standard exists**: CMS never finalized health plan enumeration; NAIC identifiers are not universal across all plans; HIOS identifiers exist for Marketplace plans but are not universal. AHIP argues USCDI shouldn't include elements that have no associated value set or national standard. Recommends ONC not add Health Insurance Payer, Plan, and Plan Identifier and remove the Health Insurance Payer Identifier element.
  - **Source-of-truth and currency concerns for Coverage Period**: Coverage information could quickly become outdated. A person could change employers or have a qualifying life event that switches plans. The Cures Act Final Rule requires providers to share USCDI with patients and other providers, "risking outdated or inaccurate information on a person's coverage being passed through the system. Once this data is in a person's record, there will not be an easy way to determine if it is accurate or its provenance."
  - AHIP's broader policy ask: ONC and CMS should reconsider the automatic link between USCDI and the Patient Access API; each data element should be weighed separately for EHR standardization vs. third-party API exposure.

**Summary of Comments:** Health Insurance Information is the most ideologically polarized class in Draft USCDI v7. **Strong support** comes from federal agencies (CMS-CCSQ, CDC), academic medical centers and providers concerned about CMS-0057-F prior-authorization compliance (UI Health), and quality and informatics organizations (NCQA, Oracle Health). **Strong opposition** comes from a single but well-positioned voice — AHIP [insurance trade association] — speaking on behalf of plans covering 205 million Americans. The supporters frame these elements as **enabling infrastructure** for real-time prior authorization, claim-status exchange, and administrative-burden reduction; UI Health is the most pointed: the Plan Identifier is essential infrastructure for the January 2027 CMS Prior Authorization API mandate, "without [which] the move toward real-time authorization remains an aspirational goal rather than an operational reality." AHIP frames the same elements as **patient privacy and re-identification risk** because USCDI flows automatically into the third-party-app Patient Access API, where HIPAA does not extend; AHIP also surfaces a substantive technical concern shared by the supporters — that **no national plan identifier standard exists** (HPID was rescinded; HIOS and NAIC are partial). The hospital trade associations (AHA, FAH) [provider trade associations] take a middle path — supporting inclusion while pointedly asking ONC to explain how this differs from the failed 2012 HPID effort. The administrative-transactions community (WEDI) [admin trade association] flags the most operationally specific concern: USCDI exchange of payer and plan data risks **conflict with the X12 271 eligibility/benefits transactions and 837 claims**, which are the federally regulated source-of-truth for this information; without "as of" date and source attribution guidance, USCDI Health Insurance Information will degrade to free text and local codes. The vendor community is split: Oracle Health supports all four with no qualifications; Epic asks for naming clarification (Payer and Plan = names only, not all sub-attributes); MEDITECH supports Plan and Plan Identifier as already implemented but flags Coverage Period as requiring new build (only expiration date is captured today). Vocabulary specification is the most universal request among supporters — Regenstrief Institute [research/informatics] proposes the most concrete answer: NPPES for payer identifiers, the CARIN Alliance's payer identifier work, and HIOS for ACA Marketplace plan identifiers. Only Health Insurance Coverage Type currently references a real vocabulary (SOPT v9.2). The single redesign concern from csnewman [individual] — that the new Plan Identifier and existing Group Identifier descriptions are nearly identical — is structurally minor but could be addressed in a usage note.

**Notably absent:** AMA, AMIA, ANI, AQIPS, AHIMA, EHR Association, Allina Health, Emory Healthcare, Wolters Kluwer, Vizient, ACLA, Altarum Institute, FDA, APHL, CSTE, SHIELD, Vega Health, and CARIN Alliance itself are all silent on the Health Insurance Information class despite filing v7 letters. The absence of CARIN Alliance is particularly striking — Regenstrief explicitly cites CARIN's payer identifier work as a vocabulary recommendation, and CARIN's mission is consumer-directed health data exchange, but CARIN's own letter (cid 14830) addresses different topics (CPCDS / Explanation of Benefit class). The absence of CSTE and APHL is notable given their detailed engagement on every public-health-adjacent element elsewhere — they appear to view payer information as outside public-health surveillance scope. Patient advocacy and consumer groups are entirely absent despite AHIP's privacy framing, which would otherwise invite consumer-side counterargument.


