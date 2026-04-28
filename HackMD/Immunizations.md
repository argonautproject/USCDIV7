
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

## Immunization: No Changes to Profile


<!-- image of summary of changes-->
*No narrative summary of changes for Health Insurance Data Elements in the ASTP/ONC Standards Bulletin 2026-1.*

<!-- **:new: Definition :point_down:** -->

![image](https://hackmd.io/_uploads/ByJ4YiRUZe.png)

### Summary of USCDI Comments:

*This content was developed with the assistance of Claude.*

| Position | Organizations | Reasons |
|---|---|---|
| **OPPOSE** | *(no outright opposition)* | — |
| **OPPOSE / REDESIGN** | TMA (state physician society), LisaRNelsonRI (standards consultant) | TMA: defer until vocabulary specified. Nelson: generalize Record Source to Healthcare Information Attributes |
| **MIXED / OPPOSE** | Epic (EHR vendor), Oracle Health (EHR vendor) | Epic: Status overlaps with Reason Not Performed; Record Source ambiguous. Oracle: original CDC ask was Boolean primarySource, not entity ID |
| **SUPPORT / with CHANGES** | ANI (nursing informatics), Altarum Institute (research org), AIRA (immunization registry trade association), CSTE (state epidemiologists), Regenstrief Institute (research/informatics), HL7 (SDO), csnewman (individual) | Specify FHIR value sets; rename "Immunizations" element; harmonize with HL7 v2 VXU + FHIR reportOrigin |
| **SUPPORT** | Emory Healthcare (academic medical center), Wolters Kluwer (clinical content vendor), Oracle Health (EHR vendor) — Status only | Mature; supports IIS data quality; multi-setting care coordination |

For a complete summary of the comments, see the Appendix below:

<!-- markdown table summary of proposal use adobe to convert to excel and then script to markdown or just copy/paste -->

## US Core Proposed Design

### Summary

DATA ELEMENT|<br/>Standards listed are required.<br/>If more than one is listed,<br/> at least one is required unless<br/>otherwise noted.<br/>Standards versions represent the most recent <br/>available at time of publication.</center>|US Core V10 Proposal
---|---|---
| **Immunization Status ➕**<br>State of an immunization event. |  |  **No Change**: `Immunization.status` is already a US Core *Must Support* element|
| **Immunization Record Source ➕**<br>Immunization event information source.<br>Examples include but are not limited to facility administering the immunization and an external record. |   |**No Change**:`Immunization.location` is already a US Core *Must Support* element|

➕ In USCDI+

### CCDA Design Notes

### Issues

### Proposal

1.  No Changes to US Core Immunization Profile nor additional guidance needed.

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


<!-- appended-from: immunizations-draft.md -->

### Immunizations data class — Comment Position Summary (Immunization Status + Immunization Record Source)

**Class additions in v7:**
- **Immunization Status** (new) — state of an immunization event (e.g., completed, entered-in-error, not-done).
- **Immunization Record Source** (new) — source of immunization event information. Examples include facility administering the immunization and an external record.

**Several commenters also propose adding** Vaccination Administration Date, Vaccination Event Record Type, and renaming the existing Immunizations element to "Vaccine Administered Code" or "Vaccine Type" — these are summarized after the v7 additions.

| Position | Organizations | Reasons |
|---|---|---|
| **OPPOSE** | *(no outright opposition)* | — |
| **OPPOSE / REDESIGN** | TMA (state physician society), LisaRNelsonRI (standards consultant) | TMA: defer until vocabulary specified. Nelson: generalize Record Source to Healthcare Information Attributes |
| **MIXED / OPPOSE** | Epic (EHR vendor), Oracle Health (EHR vendor) | Epic: Status overlaps with Reason Not Performed; Record Source ambiguous. Oracle: original CDC ask was Boolean primarySource, not entity ID |
| **SUPPORT / with CHANGES** | ANI (nursing informatics), Altarum Institute (research org), AIRA (immunization registry trade association), CSTE (state epidemiologists), Regenstrief Institute (research/informatics), HL7 (SDO), csnewman (individual) | Specify FHIR value sets; rename "Immunizations" element; harmonize with HL7 v2 VXU + FHIR reportOrigin |
| **SUPPORT** | Emory Healthcare (academic medical center), Wolters Kluwer (clinical content vendor), Oracle Health (EHR vendor) — Status only | Mature; supports IIS data quality; multi-setting care coordination |

**Comments grouped by position:**

**Strongly supportive**
- **Emory Healthcare** [academic medical center] — Strongly supports inclusion of Immunization Record Source. Supports detailed and specific provenance of data. (No separate comment on Immunization Status captured.)
- **Wolters Kluwer** [clinical content vendor] — Urges ONC to include Immunization Status alongside Vaccination Administration Date in a future version of USCDI. Frames as parallel to Adverse Events timing — status and timing of vaccines critical for analytics, decision support, and surveillance.
- **Oracle Health** [EHR vendor] — Supports inclusion of both Immunization Status and Immunization Record Source. Has concerns specifically with Record Source scoping (see mixed/oppose below).

**Supportive with refinements**
- **Alliance for Nursing Informatics / ANI** [nursing informatics professional society] — Strongly supports both elements. Argues immunization administration is "a foundational nursing function across virtually every care setting." Immunization Status enables point-of-care clinical decision support for nurses administering vaccines, surfacing whether status is current, overdue, or contraindicated; critical to preventing both duplicate vaccinations and missed immunization opportunities. Immunization Record Source is "equally important" — knowing whether a record originates from patient self-report, a state immunization information system (IIS), an imported EHR record, or a directly administered dose enables nurses to apply appropriate clinical judgment about data reliability. Particularly significant for patients who receive immunizations across multiple settings (primary care, retail pharmacy, occupational health, school health).
- **Altarum Institute** [health-services research org] — Recommends ASTP/ONC provide explicit value set guidance for both elements. **For Status**: align with FHIR Immunization resource status value set (`completed`, `entered-in-error`, `not-done`). **For Record Source**: specify at minimum **provider-reported (new administration), historical (from external record), and patient-reported**. This distinction is critical for IIS deduplication logic and coverage rate estimation and should be harmonized with the **HL7 v2 immunization messaging standard (VXU) field OBX-5 for information source** and the **FHIR Immunization.reportOrigin** element.
- **AIRA (American Immunization Registry Association) / mbkurilo@immregistries.org** [immunization registry trade association] — Concerned about confusing reuse of "Immunization(s)" for both the data class and the data element. Data Class name is appropriate; **Data Element should be renamed from "Immunization" to "Vaccine Type"** to be more descriptive — the value set describes different vaccines. Notes "further comments are provided in the attached" (attachment was not captured during scraping). AIRA's recommendations are referenced by CSTE.
- **CSTE (Council of State and Territorial Epidemiologists)** [state public health surveillance] — Supports inclusion of Immunization Record Source / Vaccination Event Record Type and **supports AIRA's comment on clarifying the definition and data element name**. Frames immunization data exchange as critical for IIS deduplication, vaccine matching, and inventory decrementing for public health.
- **Regenstrief Institute** [research/informatics institute] — Supports both elements. **Immunization Status**: no vocabulary specified in draft; FHIR uses a required value set (completed | entered-in-error | not-done); recommend referencing the FHIR Immunization Status value set for consistency. **Immunization Record Source**: no vocabulary specified; aligns with IIS data quality needs; consider referencing **NCI Thesaurus or HL7 information source value sets**. Both aligned with public health priorities — critical for IIS reporting and IIS data provenance.
- **HL7** [SDO] — Lists Immunization Status among the v7 elements highlighted as needing clearer definitions, usage notes, and code system examples. Also flags broader theme: USCDI guidance is too high-level, leading to inconsistencies as entities are left to interpret each element.
- **csnewman** [unaffiliated individual] — Examples (or better yet defined values) should be given for Immunization Status — presumably at least "complete" and "not performed" should be called out, assuming the scope of "record of a vaccine administration" includes refusals of vaccines. Separately notes the description of lot number ("specific quantity of manufactured material of a batch of vaccine product") is odd in its use of "quantity" and may cause confusion regarding the amount of vaccine administered — proposes "instance" instead of "quantity."

**Mixed / oppose**
- **Epic** [EHR vendor] — Two element-specific concerns:
  - **Immunization Status**: Recommends ONC clarify the definition and intended scope. Definition does not specify which status values are in scope. **If a "not performed" or equivalent status is included in the Immunization Status value set, that concept would be duplicative of Reason Not Performed**. ONC should reconcile these elements to avoid conflicting or redundant exchange expectations.
  - **Immunization Record Source**: Definition does not clearly distinguish whether the element represents **where an immunization was administered, where it was documented, or the source registry** — three unique concepts captured and exchanged differently. Ambiguity is further complicated where source documentation falls outside the clinical encounter — for example, an at-home nasal spray flu vaccine: is the record source the patient, the dispensing pharmacy, or the recommending provider? Recommends ONC clarify the element is scoped to immunizations administered within clinical care settings and consider whether existing Provenance data elements already address this sourcing information.
- **Oracle Health** [EHR vendor] — Supports inclusion but raises a substantive scope concern about Immunization Record Source. Looking at the original CDC submission, "their desire was simply for a binary indication of whether the record was based on historical data (e.g., second-hand knowledge of the vaccination) or administered directly by the provider communicating the information." A Boolean would most closely align with the **Immunization.primarySource** field on the FHIR R4 Immunization resource (currently labeled Must Support on the FHIR US Core IG Immunization profile). However, the proposed definition's examples ("facility administering the immunization and an external record") suggest an expectation that the element identify the specific entity that performed the administration — a different and more complex concept than a binary primarySource flag.

**Oppose / redesign**
- **Lisa Nelson / LisaRNelsonRI** [individual standards consultant] — Argues Immunization Record Source needs to be redefined to reflect accurate provenance principles. **A facility (location) is not a viable legal entity**; the organization that manages the facility is the actual source of information. Proposed redesign: rename to "Record Source" and move it to the Healthcare Information Attributes data class. Updated definition: "Event information source. Examples include but are not limited to the Organization responsible for the facility administering the immunization and an external record. An information source can be an organization or a personnel member of an organization, or a device that is operated by an organization, personnel of an organization, or the patient themselves, or a patient or someone related to a patient." Frames the new Healthcare Information Attributes data class as the structural opportunity to consolidate repetitious data elements rather than create class-specific elements.
- **TMA (Texas Medical Association)** [state physician professional society] — Lists both Immunization Status and Immunization Record Source among 15 elements ONC should not adopt until each has a correlating vocabulary standard.

**Other Immunizations class commentary (not the v7 additions):**

- **Vaccination Administration Date** (proposed addition — not in v7 draft): **CDC**, **CSTE**, **Altarum Institute**, **Wolters Kluwer**, and **minigrrl** all recommend ONC add this element. CDC argues it's distinctly different from Medication Administration due to (1) unique clinical practices, immunization informatics, and standards (CVX, etc.) for vaccine-related events; (2) operational aspects of ETLing vaccine administration data for clinical, regulatory, and public health needs; (3) priority of USCDI to address public health interoperability needs unique to vaccine data ecosystem. The element provides a critical temporal attribute that enhances identity resolution and deduplication — when individuals share similar identifiers (name, DOB), administration date serves as additional differentiator. Already routinely captured in certified EHRs and IIS, making it mature and implementable with low adoption burden. CDC recommends standardization using ISO 8601 (YYYY-MM-DD or YYYY-MM-DDThh:mm:ssZ). Altarum makes the disambiguation argument: although Performance Time in Healthcare Information Attributes could theoretically cover this case, it could also be interpreted to refer to when the order was placed or when the encounter occurred — a dedicated Vaccination Administration Date eliminates ambiguity and aligns with IIS specificity expectations. minigrrl protests the **demotion** of this element from a higher level alongside 20 other Case Reporting elements (21 certified EHR products exchange these elements via eCR today, which by USCDI's own maturity criteria should support promotion, not demotion).

- **Vaccination Event Record Type** (proposed addition — not in v7 draft): **CDC** recommends ONC add a **"Vaccine Administration Event Record Type"** element distinct from Immunization Record Source. This element would document whether a vaccination occurrence is a "new immunization record" or a "historical immunization record" — a different key from where the record came from. CDC argues this is essential for interoperability, helps reduce duplicate vaccination records, supports public health surveillance during mass immunization campaigns, and provides high-quality data for vaccine effectiveness and safety research. **CSTE** supports inclusion and supports AIRA's comments on clarifying definitions.

- **Rename existing "Immunizations" element**: **CDC** recommends renaming to **"Vaccine Administered Code"** to clarify the element captures a coded representation of the administered vaccine (CVX/NDC) rather than an immunization event. The rename does not modify the definition, datatype, or value set — but resolves the confusion within USCDI where "Immunizations" refers to both a data class and a data element. Aligns with the FHIR Immunization resource's `vaccineCode` element. **AIRA** independently recommends a similar but different rename: **"Vaccine Type"** — same disambiguation goal, different naming choice.

- **Vocabulary recommendation — NUVA**: **david_rocha** [individual] recommends ONC consider **NUVA** (a multilingual vaccine catalogue from Syadem) for representation of immunization data. NUVA decomposes vaccines into valences, links to diseases and international/national codifications (CIS/CIP, CVX, ATC, SNOMED CT), and enables harmonization across borders or systems, IIS interoperability, automatic enrichment of Digital Vaccination Records, and valence-driven interpretation in Vaccine Decision Support Systems (VADES).

**Summary of Comments:** The Immunizations class additions are broadly supported but generate the most coordinated rename/restructure requests in the v7 comment record. **Immunization Status** is supported with one substantive technical concern: Epic [EHR vendor] argues that if "not performed" is included in the Status value set, that concept duplicates the new Reason Not Performed element in the Healthcare Information Attributes class — ONC needs to reconcile these elements. The vocabulary recommendation for Immunization Status converges cleanly: Altarum Institute [research org], Regenstrief Institute [research/informatics institute], and HL7's [SDO] general scope-clarification themes all point to the **FHIR Immunization status value set (completed, entered-in-error, not-done)** as the obvious answer. **Immunization Record Source** is the more contested element with three distinct critiques converging on the same underlying problem — what does "source" mean? Epic [EHR vendor] frames it as an ambiguity between *where administered*, *where documented*, and *source registry*. Oracle Health [EHR vendor] points to a more fundamental mismatch: the original CDC submission was for a Boolean Primary Source flag aligned with FHIR Immunization.primarySource, but the proposed definition's examples expect identification of specific entities — a substantively different concept. LisaRNelsonRI [individual standards consultant] makes the most pointed redesign argument: a facility (location) cannot be a valid provenance source — only an organization, person, or device-in-context can — so the element should be generalized and moved to Healthcare Information Attributes as a "Record Source" attribute reusable across data classes. The **value set for Immunization Record Source** has the cleanest answer in the comment record: Altarum recommends **provider-reported, historical, and patient-reported** at minimum, harmonized with HL7 v2 VXU OBX-5 and FHIR Immunization.reportOrigin. **The most consequential broader pattern in the Immunizations class commentary is the coordinated push to add Vaccination Administration Date and Vaccination Event Record Type alongside the v7 additions.** CDC [federal/public health], CSTE [state epidemiologists], Altarum Institute [research org], Wolters Kluwer [clinical content vendor], and minigrrl [individual] all argue the v7 draft is incomplete without these two additional elements — particularly Vaccination Administration Date, which is currently routinely captured in certified EHRs and IIS, mature and implementable, but not surfaced as a USCDI element. CDC's argument that **administration date enables patient-matching deduplication** when individuals share name/DOB identifiers is the most operationally specific case for inclusion, and Altarum's argument that **Performance Time is too ambiguous** (could mean order placement, encounter time, or administration time) is the most technically specific. **The rename argument is also cleanly coordinated**: CDC proposes "Vaccine Administered Code"; AIRA [immunization registry trade association] proposes "Vaccine Type." Both target the same underlying problem — the existing element name "Immunizations" is identical to the data class name and ambiguous as to whether it represents the event or the coded vaccine type — so they propose different but reconcilable names. ANI's [nursing informatics professional society] framing of immunization administration as "a foundational nursing function" with care-coordination implications across primary care, retail pharmacy, occupational health, and school health settings is the strongest clinical-workflow justification for the v7 additions and aligns with Wolters Kluwer's [clinical content vendor] support.

**Notably absent:** AHA, FAH, AHIP, AMIA, AMA, AAAAI, AQIPS, NCQA, WEDI, EHR Association, MEDITECH, Allina Health, UI Health, Providence Health, FDA (especially notable given FDA's role in vaccine safety surveillance via VAERS), AHIMA, ACLA, SHIELD, APHL (notable absence given immunization-related public-health reporting parallels lab reporting), CARIN Alliance, PACIO, SNOMED International (notable — they engaged on most other v7 elements with specific code recommendations but not these), NCPDP, Vega Health, and Vizient are silent on the Immunization elements despite filing v7 letters. The absence of FDA on Immunization Record Source is the single most striking gap given that VAERS adverse event reporting depends on accurate identification of administering providers and source provenance. The complete absence of pediatric professional societies (AAP) is also notable given pediatric immunization schedules are the most workflow-intensive use case for these elements. Patient advocacy and consumer groups are absent despite consumer-facing immunization records being a frequent patient-experience domain.

