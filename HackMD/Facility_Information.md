
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

## Facility Telecom: No Changes to Profile


<!-- image of summary of changes-->
*No narrative summary of changes for Health Insurance Data Elements in the ASTP/ONC Standards Bulletin 2026-1.*

<!-- **:new: Definition :point_down:** -->

![image](https://hackmd.io/_uploads/HJY1Dj08-x.png)

### Summary of USCDI Comments:

*This content was developed with the assistance of Claude.*

| Position | Organizations | Reasons |
|---|---|---|
| **OPPOSE** | *(no outright opposition)* | — |
| **OPPOSE / REDESIGN** | LisaRNelsonRI (standards consultant) | Generalize to single Telecom element across all data classes |
| **MIXED / OPPOSE** | *(no mixed positions)* | — |
| **SUPPORT / with CHANGES** | Emory Healthcare (academic medical center), Epic (EHR vendor), EHR Association (vendor trade association), FAH (hospital trade association), Oracle Health (EHR vendor) | Specify default contact type or split phone/email; clarify scope (scheduling/clinical/admin); define context within USCDI not just FHIR IGs; facility-level should be default in shift-based care |
| **SUPPORT** | Regenstrief Institute (research/informatics) | ITU-T E.123/E.164 standards; consistent with Care Team Member Telecom |

For a complete summary of the comments, see the Appendix below:

<!-- markdown table summary of proposal use adobe to convert to excel and then script to markdown or just copy/paste -->

## US Core Proposed Design

### Summary

DATA ELEMENT|<br/>Standards listed are required.<br/>If more than one is listed,<br/> at least one is required unless<br/>otherwise noted.<br/>Standards versions represent the most recent <br/>available at time of publication.</center>|US Core V10 Proposal
---|---|---
| **Facility Telecom**<br>Phone or email contact information for a physical place of available services or resources. | •        ITU-T E.123, Series E: Overall Network Operation, Telephone Service, Service Operation and Human Factors, International operation - General provisions concerning users: Notation for national and international telephone numbers, email addresses and web addresses (incorporated by reference in § 170.299); and<br>•        ITU-T E.164, Series E: Overall Network Operation, Telephone Service, Service Operation and Human Factors, International operation - Numbering plan of the international telephone service: The international public telecommunication numbering plan | **No Change**: `Location.telecom` is already a US Core *Must Support* element|

<!-- ➕ In USCDI+ -->

### CCDA Design Notes

### Issues

### Proposal

1.  No Changes to US Core Location Profile nor additional guidance needed.

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

### Facility Information data class — Comment Position Summary (Facility Telecom)


**Comments grouped by position:**

**Strongly supportive**
- **Regenstrief Institute** [research/informatics institute] — Supports inclusion. Uses ITU-T E.123/E.164 standards, consistent with the existing Care Team Member Telecom element. Supports care coordination. No concerns. Aligned with SHIELD priorities — facility contact information supports laboratory and public health reporting.

**Supportive with refinements**
- **Emory Healthcare** [academic medical center] — Supports inclusion to improve availability of contact details. Encourages ONC to consider **separating phone and email contact points** at the facility level rather than treating them as a single combined element.
- **Epic** [EHR vendor] — Recommends the final v7 specify which contacts to use by default. Notes the same healthcare facility might use multiple phone numbers or email addresses depending on context: phone or email used to field patient inquiries; phone or email used to coordinate referrals or transitions of care; phone used for after-hours or urgent clinical contact. Any of these are reasonable to include, but the final v7 should specify which to use by default for consistent industry interpretation. Alternatively, USCDI could include multiple telecom types as distinct data elements or adopt a flexible approach allowing multiple telecom contacts to be exchanged.
- **EHR Association** [vendor trade association] — Generally supportive of including Facility Telecom as a USCDI data element. Recommends ONC clarify the intended use and scope of the element — specifically, **which types of contact information are expected** (e.g., scheduling, clinical, administrative) and how this aligns with existing capabilities in FHIR US Core.
- **Federation of American Hospitals / FAH** [hospital trade association] — Supports inclusion of Facility Telecom and recommends clarifying that **facility-level contact information should serve as the default for interoperability**. Argues individual clinician contact information is often unreliable in shift-based care environments, whereas facility-level contact points better support safe and effective coordination.
- **Oracle Health** [EHR vendor] — Supports inclusion of the proposed Facility Telecom data element. However, remains concerned that the required context for Facility Information is not clearly defined in USCDI itself — context **must be inferred from the HL7 FHIR US Core or HL7 CDA C-CDA implementation guides**, which are not consistently used when USCDI is used outside of interoperability initiatives. Recommends clarifying these contextual requirements directly within USCDI to ensure consistent interpretation and implementation. Same general argument Oracle makes throughout the letter — USCDI should communicate scope through its own definitions rather than relying on downstream IGs.

**Oppose / redesign**
- **Lisa Nelson / LisaRNelsonRI** [individual standards consultant] — Two related comments framing this as **data element bloat**. Argues USCDI could be streamlined by avoiding the creation of repetitive data elements that are really the same data element used over and over in different contexts. Recommends creating a **generalized Telecom Information data element in the Healthcare Information Attributes data class** that would replace Facility Telecom (Facility Information class), Care Team Member Telecom (Care Team Member class), Email Address / Phone Number / Phone Number Type (Patient class), and any future telecom elements needed for Health Insurance Payers/Plans, Encounter Locations, and other classes. Also recommends opening the value set of telecom systems beyond phone, fax, email, pager, URL, SMS, and other — to include **Direct addresses** (more specific than email) and **FHIR endpoints** that providers and patients may want to publicize as available telecom options. Frames the new Healthcare Information Attributes data class as the structural opportunity to consolidate repetitious data elements and make USCDI "more unitary and foundational."

**Other Facility Information class commentary (not Facility Telecom):**
- **CMS-CCSQ** [federal agency / payer] — On the existing **Facility Identifier** element: recommends ONC further clarify the description by including examples such as the **National Healthcare Safety Network (NHSN) Organization Identifier (OrgID)**. Capturing this data is important for tracking patient safety outcomes associated with specific facilities and addresses, and enables facilities within a given tax ID to be distinguishable from one another.
- **CDC (DSMH Working Group)** [federal agency / public health] — On the existing **Facility Managing Organization Identifier** element: documents the use case for the **National Ambulatory Medical Care Survey (NAMCS)** Health Center Component, which samples all care delivery sites under a sampled health center. Argues the Facility Managing Organization Identifier would help link data correctly to specific facilities, decrease risk of data loss and duplication, and reduce reporting burden through DHCS data modernization. Critical for **TEFCA framework / QHIN** patient and organizational matching across the complex healthcare ecosystem. The element is in C-CDA 4.0 at xpath `/ClinicalDocument/documentationOf/serviceEvent/performer/assignedEntity/id`.
- **AMIA** [physician informatics professional society] — On the existing **Facility Address** element: cites ANI's input that specific considerations are needed for **mobile units and Emergency Medical Services (EMS)**, which often operate without a fixed physical address. Excluding EMS from facility-based exchange frameworks risks omitting critical data related to care provided at the initial point of patient contact. Three recommendations: (1) clarify address representation for non-traditional care settings; (2) define address types required for USCDI exchange across patient encounters, provider directories, and regulatory/public health reporting; (3) introduce a standardized data element for address type to indicate the purpose of each address (mailing, etc.).

**Summary of Comments:** Facility Telecom is the most cleanly supported v7 addition reviewed so far measured by total volume of opposition — there is none. Even the redesign request from Lisa Nelson [individual standards consultant] is constructive: she'd consolidate Facility Telecom into a generalized Telecom Information element rather than oppose its inclusion. The supporting voices converge on a single shared concern: **the element underspecifies which contact context the telecom value represents.** Epic [EHR vendor] frames this most concretely — the same facility maintains different phone numbers and email addresses for patient inquiries, referral coordination, and urgent clinical contact, and without a default specified in USCDI, implementers will choose differently. Emory Healthcare [academic medical center] takes the simplest version of the same concern — at minimum, separate phone from email. The EHR Association [vendor trade association] generalizes the question to scheduling/clinical/administrative contact types and asks for FHIR US Core alignment. FAH [hospital trade association] adds a clinically grounded reason for the element being valuable in the first place: in shift-based care environments, individual clinician contact information is unreliable, so facility-level contacts are the only durable coordination point. Oracle Health [EHR vendor] makes its broader USCDI structural argument here — context for Facility Information today must be inferred from FHIR US Core or C-CDA implementation guides, which are inconsistently applied outside interoperability initiatives, so USCDI should define context internally. Regenstrief [research/informatics institute] is the only voice supporting without qualifications, citing ITU-T E.123/E.164 standards alignment and consistency with the existing Care Team Member Telecom element. **Lisa Nelson's redesign argument** — collapse Facility Telecom, Care Team Member Telecom, Patient Email/Phone, and future telecom elements into a single generalized Telecom Information element in the new Healthcare Information Attributes data class — is the most structurally significant proposal in the entire v7 comment record on this class. If adopted, it would directly address the EHR Association's value-set concern, Oracle's context concern, and Epic's default-specification concern by replacing class-specific telecom elements with a single context-aware element across all data classes. Nelson also flags that the current telecom value set (phone, fax, email, pager, URL, SMS, other) is too narrow and should explicitly accommodate **Direct addresses** (HL7 Direct messaging, more specific than generic email) and **FHIR endpoints** (publishable provider/patient API endpoints) — both of which are growing in production use and have no current USCDI representation. The tangential Facility Information class commentary on Facility Identifier (CMS-CCSQ), Facility Managing Organization Identifier (CDC), and Facility Address (AMIA/ANI) signals broader stakeholder interest in the data class that ONC may want to address holistically rather than element-by-element — particularly the EMS/mobile-unit gap AMIA highlights and the NHSN OrgID example CMS-CCSQ requests.

**Notably absent:** AHA, AHIP, AMA, AAAAI, AQIPS, NCQA, WEDI, HL7 (especially notable given the FHIR US Core alignment question), MEDITECH, Wolters Kluwer, Allina Health, UI Health, Providence Health, TMA (notably did *not* list Facility Telecom among their 15 "defer until vocabulary" elements), FDA, APHL, CSTE, SHIELD, AHIMA, ACLA, Vizient, CARIN Alliance, PACIO, SNOMED International, NCPDP, Altarum Institute, Vega Health, and Emory Healthcare's parallel academic medical centers are all silent on Facility Telecom. The absence of AHA is the most striking given that hospital-side coordination workflows are the primary use case FAH cites — only one of the two major hospital trade associations engaged. The absence of NCPDP is notable for the Direct address question Lisa Nelson raises, since NCPDP SCRIPT and similar pharmacy ePrescribing workflows depend heavily on Direct messaging. Patient advocacy and consumer groups are entirely absent despite facility contact information being a frequent patient-experience friction point.


