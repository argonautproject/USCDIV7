
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

## Patient Demographics: Changes TBD


<!-- image of summary of changes-->
![image](https://hackmd.io/_uploads/HJjA4glPbx.png)
*No narrative summary for the
Patient Identifer Data Element in the ASTP/ONC Standards Bulletin 2026-1.*

<!-- **:new: Definition :point_down:** -->

![image](https://hackmd.io/_uploads/rkNOHgevbl.png)

### Summary of USCDI Comments:

*This content was developed with the assistance of Claude.*

#### Accommodation

| Position | Organizations | Reasons |
|---|---|---|
| **OPPOSE** | *(no outright opposition)* | — |
| **OPPOSE / REDESIGN** | Oracle Health (EHR vendor) | No clearly defined standard for accommodations exists, but a Disability Status profile does (eCase Reporting); either pivot to Disability Status using the existing eCase Reporting profile, or withdraw and collaborate with HL7 to establish an agreed Accommodation profile |
| **MIXED / OPPOSE** | Allina Health (provider/health system), EHR Association (vendor trade association) | Allina: definition too broad — could encompass clinical, language, disability, therapeutic, financial, or community-based supports; need scope clarification. EHR Association: ambiguity between capturing disability status vs. specific accommodations provided; no established finite value set; clarify intent and provide reference vocabulary |
| **SUPPORT / with CHANGES** | SNOMED International (SDO), PACIO Project (post-acute care interop community), MEDITECH (EHR vendor) | SNOMED: designate SNOMED CT U.S. Edition; consider complementary SNOMED CT (clinical concepts) + LOINC (observation/questionnaire structure) dual designation. PACIO: expand definition to include "companions" (legal caregivers, representatives) covered by ADA Title II §35.160(a) and §36.303. MEDITECH: encourage adoption — currently captured through non-standardized special-patient indicators; standardization is welcome |
| **SUPPORT** | AHA (hospital trade association), FAH (hospital trade association), CMS-CCSQ (federal agency / payer), NCQA (quality measurement), Wolters Kluwer (clinical content vendor), Regenstrief Institute (research/informatics) | AHA: already leveraged in clinical workflows and supported by certified HIT; standardization ensures awareness across care settings. FAH: already routinely captured. CMS-CCSQ: applauds inclusion. NCQA: strongly supports as high-value addition with limited burden. Wolters Kluwer: enriches care coordination, transitions, equitable care delivery. Regenstrief: important for person-centered care and ADA compliance |

#### Patient Identifier and Deceased Indicator

| Position | Organizations | Reasons |
|---|---|---|
| **OPPOSE** | *(no outright opposition to either element)* | — |
| **OPPOSE / REDESIGN** | TMA (state physician society) | Defer both until vocabularies specified |
| **MIXED / OPPOSE** | *(no mixed positions)* | — |
| **SUPPORT / with CHANGES** | AHA (hospital trade association), FAH (hospital trade association), WEDI (admin trade association), CSTE (state epidemiologists), APHL (public health labs), CDC (federal/public health), TDH-OIA (state public health), Regenstrief Institute (research/informatics), Altarum Institute (research org), EHR Association (vendor trade association), Epic (EHR vendor), david_rocha (individual) | Patient Identifier: clarify identifier types (MRN/regional/enterprise); add Type and Assigning Authority elements. Deceased Indicator: usage notes acknowledging timeliness limits; align with Medicolegal Death Investigation FHIR IG; coordinate with vital records systems |
| **SUPPORT** | Oracle Health (EHR vendor), MEDITECH (EHR vendor), CMS-CCSQ (federal/payer), Wolters Kluwer (clinical content vendor) | Mature, widely supported, supports patient matching and data quality |

For a complete summary of the comments, see the Appendix below:

<!-- markdown table summary of proposal use adobe to convert to excel and then script to markdown or just copy/paste -->

## US Core Proposed Design

### Summary

DATA ELEMENT|<br/>Standards listed are required.<br/>If more than one is listed,<br/> at least one is required unless<br/>otherwise noted.<br/>Standards versions represent the most recent <br/>available at time of publication.</center>|US Core V10 Proposal
---|---|---
| **Accommodation ➕**<br>Modifications, tools, technologies, and other supports necessary to access care. | • SNOMED Clinical Terms (SNOMED CT) U.S. Edition, September 2025 Release | See proposal below |
| **Deceased Indicator ➕**<br>Indicates if the person is deceased or not. |  |**No Change**: `Patient.deceased[x]` already is a US Core *Additional USCDI* element |
| **Patient Identifier**<br>Sequence of characters assigned by an organization to uniquely refer to a patient.<br>Examples include but are not limited to Medical Record Number. |  |**No Change**: `Patient.identifier` already is a US Core *Must Support* element|

➕ In USCDI+

### CCDA Design Notes

### Issues

- Terminology

### Proposal

1.  Options
    - Add the standard [Patient Disability Extension](http://hl7.org/fhir/StructureDefinition/patient-disabilityextension) to US Core Patient (aligns with prior design)
    - Add New US Core Note Profile ( see the [NHS England Reasonable Adjustment Flag](https://digital.nhs.uk/services/reasonable-adjustment-flag))
    - Add New US Core Observation Profile

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

### Accommodation (Patient Demographics/Information data class) — Comment Position Summary


**Comments grouped by position:**

**Strongly supportive**
- **CMS-CCSQ** [federal agency / payer] — Applauds inclusion in USCDI v7.
- **American Hospital Association / AHA** [hospital trade association] — Supports adoption. Standardization can ensure awareness of patient-specific access needs across care delivery settings; element is already leveraged in clinical workflows and supported by certified health IT. AHA places Accommodation alongside Device Type and Deceased Indicator as the v7 elements that "align with clinical workflows and are supported by certified health IT" — the cleanest support tier in their letter.
- **Federation of American Hospitals / FAH** [hospital trade association] — Supports inclusion. Reflects data already routinely captured in clinical practice; inclusion would facilitate interoperability gains consistent with current operational workflow without introducing data variability that could undermine interoperability goals. FAH groups Accommodation with Device Type and Deceased Indicator as the v7 additions clearly suited for inclusion.
- **NCQA** [quality measurement org] — Strongly supports as a high-value addition with limited implementation burden given large overlap with other exchange requirements.
- **Wolters Kluwer** [clinical content vendor] — Cites Accommodation alongside Appointment, Healthcare Agent, and Deceased Indicator as elements that "enrich the context required for efficient, safe, and equitable care delivery." These contextual elements are foundational for modern care management, value-based care programs, and whole-person care initiatives.
- **Regenstrief Institute** [research/informatics institute] — Supports inclusion. Notes SNOMED CT (Sept 2025) is specified. Important for disability access and health equity, person-centered care, and ADA compliance. Aligned with SHIELD and public health priorities.

**Supportive with refinements**
- **SNOMED International** [SDO — terminology] — Recommends ONC designate SNOMED CT U.S. Edition as an applicable vocabulary standard. Argues SNOMED CT physical object and clinical finding hierarchies include a validated range of concepts relevant to accommodation documentation: assistive devices (hearing aids, mobility aids, communication devices), disability-related modifications, and care access requirements. Frames designation as supporting health equity objectives and aligning with federal accommodation requirements under Section 504 of the Rehabilitation Act and the Americans with Disabilities Act. Further recommends a complementary dual designation: **SNOMED CT** for clinical concept coding of specific accommodations and **LOINC** for observation and questionnaire structure — consistent with the established complementary roles these standards play across multiple USCDI data classes and aligned with HL7 FHIR US Core (LOINC for observation types, SNOMED CT for clinical values). Dual designation would ensure Accommodations data can be represented in both structured clinical documentation and patient-facing questionnaire formats, supporting CMS Interoperability and Patient Access Final Rule patient-access requirements.
- **PACIO Project** [post-acute care interoperability community] — Recommends updating the data element description to include legal caregivers or representatives of the patient — "companions" in federal regulatory language — who are also covered by law to receive accommodations. Proposed revised definition: "Modifications, tools, technologies, and other supports necessary to access care **by the patient and their companions**." Cites a 2024 Journal on Quality and Patient Safety study showing healthcare organizations are already collecting accommodation data, but in non-standardized ways. Grounds the recommendation in specific federal regulations:
  - **ADA Title II (28 C.F.R. § 35.160(a))**: public entities must take steps to ensure communications with companions with disabilities are as effective as communications with others; "companion" includes family members, friends, or associates including legal guardians, conservators, and healthcare proxy holders.
  - **ADA § 36.303(c)**: public accommodations must furnish auxiliary aids and services for effective communication with companions who are individuals with disabilities.
  - **Section 504 of the Rehabilitation Act and Title 28 § 36.303**: broader accommodation requirements applicable to caregivers/parents.
  - **DOJ guidance** specifically calling out covered entities' obligation to provide effective communication for companions with communication disabilities.

  PACIO is also separately advancing a complementary proposal to add a Disability Status data element under Patient Demographics/Information (alongside renaming the existing Disability Status under Health Status Assessments to "Disability Assessment") — disambiguating self-reported demographic status from clinician-collected health assessment data.
- **MEDITECH** [EHR vendor] — Encourages adoption. Notes patient accommodations are currently captured through non-standardized queries that indicate special patient indicators; encourages adoption of data elements that can be captured through standard fields. MEDITECH's framing positions current EHR practice as the problem the element solves.

**Mixed / oppose**
- **Allina Health** [provider / health system] — Supports efforts to improve capture of patient needs that impact access to care, but argues the current definition of "Accommodation" is too broad and lacks sufficient specificity for consistent implementation. The term could encompass: clinical accommodations (medical/surgical or obstetric needs), language services, disability-related accommodations, therapeutic supports, financial assistance, or community-based services. Without clearer boundaries, it's difficult to determine what's in scope for capture as a discrete data element. Recommends ASTP further define intended scope and use cases, clarify whether specific categories of accommodations are expected to be captured, and provide guidance on standardization and operationalization within workflows.
- **EHR Association** [vendor trade association] — Requests clarification on definition and codification. As currently defined, the element appears to describe a patient's *disability status or functional limitation* (e.g., limited mobility) rather than the *specific accommodations provided* (e.g., wheelchair-accessible exam room). There is no established, finite value set for accommodations, and it's unclear whether EHRs are expected to capture disability status, accommodation type, or both. Recommends ONC clarify the intent and provide a defined value set or reference vocabulary to support consistent implementation.

**Oppose / redesign**
- **Oracle Health** [EHR vendor] — Recommends ONC either pivot the element or withdraw the proposal. Notes the submission references the FHIR US eCR Disability Status specification (`http://hl7.org/fhir/us/ecr/2021Jan/StructureDefinition-disability-status.html`), which is currently used in eCase Reporting — but that profile's value set indicates the disability, not the modifications, tools, technologies, and other supports necessary to access care. The submission claims no other applicable standards exist, while the proposed data element generally references SNOMED. Oracle's position: there is no clearly defined standard for accommodations, but there *is* one for Disability Status. Two options: (1) change the perspective to including a Disability Status, following the profile used for eCase Reporting; or (2) withdraw the proposal and collaborate with HL7 to establish an agreed-to profile definition for Accommodation.

**Summary of Comments:** Accommodation is the most cleanly supported v7 addition reviewed so far — six commenters offer clean support and three support with constructive refinements, with only Oracle Health [EHR vendor] taking a redesign-or-withdraw position. The supporting voices converge on three reinforcing points: (1) the data is already routinely captured in clinical workflows (AHA, FAH, MEDITECH), (2) the use case is grounded in concrete federal accommodation law — ADA, Section 504 of the Rehabilitation Act, and CMS Interoperability and Patient Access Final Rule (SNOMED International, Wolters Kluwer, Regenstrief), and (3) the element is high-value for health equity, person-centered care, and value-based care models with limited implementation burden (NCQA, Wolters Kluwer, Regenstrief). The refinement requests cluster around two related concerns. **Vocabulary** is the most concrete: SNOMED International [SDO] proposes a specific dual designation — SNOMED CT U.S. Edition for clinical concepts plus LOINC for observation/questionnaire structure, mirroring HL7 FHIR US Core conventions — which would directly address the EHR Association's [vendor trade association] complaint about the missing finite value set. **Scope clarification** is the second: Allina Health [provider/health system] and the EHR Association both flag that the current definition is broad enough to encompass everything from sign language interpreters to financial assistance, and that the element conflates disability status (a patient characteristic) with accommodations provided (an organizational response). Oracle Health takes the strongest version of this position — the submission's referenced standard (the FHIR US eCR Disability Status profile) actually models disability, not accommodations, suggesting either (a) pivot the element to Disability Status, or (b) withdraw and develop the profile through HL7. PACIO Project's [post-acute care interop community] companion-inclusion recommendation is the most policy-grounded refinement: ADA Title II and Section 504 explicitly extend accommodation rights to family members, legal guardians, and healthcare proxy holders, and the current definition fails to capture this. PACIO's parallel effort to add a Disability Status element to Patient Demographics/Information (alongside renaming the existing Disability Status under Health Status Assessments to "Disability Assessment") would, if adopted alongside Accommodation, resolve the disability-status-vs.-accommodations-provided ambiguity that EHR Association and Oracle Health raise — making PACIO's two proposals structurally complementary.

**Notably absent:** Epic, ANI, AMIA, AMA, AHIP, AQIPS, TMA (notably did *not* list Accommodation among their 15 "defer-until-vocabulary" elements), CDC, APHL, CSTE, FDA, AHIMA, UI Health, Emory Healthcare, Altarum Institute, SHIELD, HL7, ACLA, Vizient, WEDI, CARIN Alliance, and Vega Health are all silent on Accommodation despite filing v7 letters. Epic's silence is the most striking omission — Epic took strong positions on most other Patient Demographics elements but offered no comment here, possibly indicating Epic considers the element mature and uncontroversial. ANI's silence is also notable given Accommodation is squarely a nursing-led documentation domain with health-equity implications that ANI engaged with extensively elsewhere. The absence of disability-rights advocacy organizations is conspicuous given the element's explicit grounding in ADA and Section 504 — PACIO is the only voice carrying that perspective, and they're an interoperability community, not a disability advocacy group.

### Patient Demographics/Information data class — Comment Position Summary (Patient Identifier + Deceased Indicator)

**Comments grouped by position:**

**Strongly supportive**
- **CMS-CCSQ** [federal agency / payer] — Applauds inclusion of Deceased Indicator in USCDI v7. (No separate CMS-CCSQ comment captured for Patient Identifier.)
- **Oracle Health** [EHR vendor] — Supports the inclusion of both proposed Deceased Indicator and Patient Identifier data elements. Brief, unqualified.
- **MEDITECH** [EHR vendor] — On Patient Identifier: each patient standardly has a unique identifier within the HCIS; most patients have multiple medical record numbers. On Deceased Indicator: adoption would require development work — currently notes patients' expiration but it's not standardly interoperable with the deceased indicator received from other developers through inbound data. MEDITECH's position is supportive but flags the operational reality that EHRs implement this concept inconsistently today.
- **Wolters Kluwer** [clinical content vendor] — Cites Deceased Indicator alongside Appointment, Healthcare Agent, and Accommodation as elements that "enrich the context required for efficient, safe, and equitable care delivery." Notes deceased status is "of particular importance as a discrete data element that will improve official federal statistics, as well as support local provider organizations in eliminating undesired communications to grieving families." Stronger framing for Deceased Indicator than the broader cluster.

**Supportive with refinements**

*Patient Identifier:*
- **American Hospital Association / AHA** [hospital trade association] — Recognizes the importance of unique patient identifiers in supporting patient matching activities and ensuring patient safety, and "in concept, we support the establishment of unique patient identifier standards." However, urges ONC to **specify the types of patient identifiers that would be included**. ONC's guidance should address whether MRNs and/or other identifiers like regional identifiers would be required. Lists Patient Identifier among elements requiring "clarifying guidance and vocabulary standards prior to adoption."
- **Federation of American Hospitals / FAH** [hospital trade association] — Recognizes that the use of unique patient identifiers would support more accurate patient matching across disparate health information systems. Supports inclusion but **requests clarification on expected identifier types** — specifically whether the element is intended to require a medical record number or support alternative identifiers (e.g., enterprise or regional identifiers) to ensure reliable and consistent patient identification across systems.
- **WEDI** [administrative/transactions trade association] — Cites Patient Identifier among the v7 additions that "could materially reduce administrative burden and improve interoperability." Recommendation: clarify the types of patient identifiers being considered and how they should be represented to prevent confusion with other identifiers and inappropriate reuse outside intended contexts. "Patient matching remains a pervasive operational issue."
- **CSTE (Council of State and Territorial Epidemiologists)** [state public health surveillance] — Supports inclusion of Patient Identifier in USCDI v7 and recommends ONC also include **two additional data elements**: (1) **Type of Patient Identifier** (medical record number, Medicare number, social security number, laboratory patient identifier); (2) **Patient Identifier Assigning Authority** (which organization assigned the identifier — health care organization, governmental agency, etc.). Four use cases: (i) person matching and deduplication — STLT public health agencies currently spend countless hours manually deduplicating partially matched patient records even with best algorithms; (ii) public health follow-up during case investigation; (iii) automated/semi-automated query of HIE or clinical repository (relevant to TEFCA); (iv) bidirectional data exchange routing data to correct medical record. Filed parallel comments on existing **Medicare Patient Identifier** noting it's one type that could be subsumed under a Patient Identifier + Type + Assigning Authority structure.
- **APHL (Association of Public Health Laboratories)** [public health labs trade association] — Supports the addition of Patient Identifier Type as "very important data element for public health" but notes the system that created the identifier — what HL7 calls the **assigning authority** — must also be included to be useful across organizations. APHL recommends including assigning authority with this and any other identifier element (in all HL7 products this is part of the various supported data types for identifiers). Proposes updated definition: "Sequence of characters assigned by an organization to uniquely refer to a patient over time, **including a means to identify the organization or system that assigned it**."
- **CDC (DSMH Working Group)** [federal agency / public health] — Supports inclusion. Documents the use case for NHCS and NAMCS: both conduct data linkages to other federal datasets (National Death Index, HUD, etc.) and publish them as restricted use data files. The element will "increase the ability to track unique patients, improving accuracy and quality in these produced datasets." Notes Patient Identifier Type is encompassed in the patient ID structure in C-CDA 4.0; ID has issuing authority and type associated with it (HL7 II: InstanceIdentifier V3 Data Type). The majority of EHR files submitted for NAMCS and NHCS have name/DOB/address but **lack medical record number (MRN) and Health Insurance Claims Number (HIC)** — NHCS would like to expand identifiers to include patient control number (PCN).
- **Texas Department of Health (TDH-OIA / jessilott)** [state public health agency] — Supports the inclusion of Patient Identifier. Recommends ASTP/ONC consider explicitly including the identifier's **"type" and "source/assigning authority"** as part of this data element. These attributes are critical for distinguishing among multiple identifiers, ensuring correct interpretation, and supporting consistent interoperability across systems.
- **Regenstrief Institute** [research/informatics institute] — Supports inclusion. Notes no vocabulary specified (identifier string). Supports patient matching and record linkage. Recommends guidance on identifier type coding (e.g., **HL7 v2 identifier type codes**). Aligned with public health priorities — patient matching critical for PH.

*Deceased Indicator:*
- **Altarum Institute** [health-services research org] — Supports inclusion. Element is utilized by both healthcare and public health institutions: in healthcare software, used to deprecate patient records for system efficiency and to prevent awkward situations like appointment reminders for deceased individuals; in both contexts, used for research. Implementation note: **within vital records and FHIR-based mortality exchange, when a date of death is available, systems typically convey it using Date of Death without a Deceased Indicator present**. Altarum recommends ONC note in USCDI guidance that the Deceased Indicator should primarily be used to indicate that **death is known even if the exact date is not yet available or is not being exchanged**. Particularly important for **perinatal and newborn contexts** (birth reporting and birth defect surveillance), where documenting whether an infant is deceased can materially affect downstream reporting workflows, case ascertainment, and interpretation of outcomes — even when the exact date of death may not be present.
- **EHR Association** [vendor trade association] — Supports the inclusion of Deceased Indicator and recognizes its clinical and administrative importance for patient safety and care coordination. **Notes a practical challenge related to data currency**: EHR systems are not always notified in a timely or reliable manner when a patient passes away outside of the healthcare system (e.g., at home or in a non-affiliated facility). As a result, this field may not consistently reflect the most current or accurate status across implementations. Recommends ONC acknowledge in usage notes that the Deceased Indicator may not always represent real-time or fully accurate information, and that implementers should not rely on this field as a definitive record of patient death without appropriate verification processes.
- **Epic** [EHR vendor] — Supports inclusion. Today, Epic software captures and exchanges both a patient's deceased status and date and time of death when documented in clinical workflows. Notes USCDI inclusion alone will not fully address the broader challenge of ensuring deceased status reaches EHR systems reliably — **mortality information often originates outside clinical encounters through vital records systems and similar sources**. Urges ONC to coordinate with relevant federal and state government agencies, including public health authorities and state-level vital records offices, to promote more comprehensive and timely exchange of mortality information.
- **david_rocha** [individual / standards commenter] — Recommends Deceased Indicator align with the **Medicolegal Death Investigation FHIR IG**. CMS and ONC need to promote event-driven exchange for this data element across payers, providers, and delegated entities using standards-based APIs.
- **CDC (DSMH Working Group)** [federal agency / public health] — Supports inclusion. NHCS includes discharge status as a data element with "deceased" as one of the reported levels. Inclusion would improve accuracy of reporting discharge statuses in official federal statistics produced by NHCS data. Demonstration projects: NHSR No. 187 ("Mortality Following Nonfatal Opioid Overdose Visits to the Emergency Department") and NHSR No. 167 ("Inpatient Hospitalization and Risk of Mortality Among Patients Diagnosed With Pneumonia"). The element is in C-CDA 4.0 at xpath `ClinicalDocument/recordTarget/patientRole/patient/sdtc:deceasedInd`. The majority of EHR encounters submitted to NHCS include discharge status code information.
- **AHA** [hospital trade association] — Lists Deceased Indicator among elements that "align with clinical workflows and are supported by certified health IT." ONC's reliable exchange of information on deceased status would support patient matching processes and may mitigate undue stress to family members caused by outreach for a deceased patient. Supports advancement.
- **FAH** [hospital trade association] — Supports inclusion. Reflects data already routinely captured in clinical practice; would continue to facilitate interoperability gains consistent with current operational workflow without introducing data variability that could undermine interoperability goals.
- **TDH-OIA (jessilott)** [state public health agency] — Supports inclusion. Improves accuracy of patient records and supports reliable data management across health information systems.
- **Regenstrief Institute** [research/informatics institute] — Supports inclusion. Simple, high-value element for data quality and patient matching. Aligned with public health mortality tracking priorities. Boolean field; no vocabulary needed; complements existing Date of Death.

**Other relevant commentary:**
- **minigrrl** [individual public-health commenter] — Lists **Health Insurance Information: Medicare Patient Identifier** among 21 demoted Case Reporting elements that minigrrl protests, arguing 21 certified EHR products exchange these elements via electronic Case Reporting (eCR) specifications today, "which typically supports promotion, not demotion, within the USCDI maturity model." Urges ONC to either reverse the decision or publish a detailed, evidence-based rationale.

**Oppose / redesign**
- **TMA (Texas Medical Association)** [state physician professional society] — Lists both Patient Identifier and Deceased Indicator among 15 elements ONC should not adopt until each has a correlating vocabulary standard.

**Summary of Comments:** Patient Identifier and Deceased Indicator are both among the most cleanly supported v7 additions but for different reasons and with structurally different refinement asks. **Patient Identifier** has near-universal support but a single dominant refinement request: **add Patient Identifier Type and Assigning Authority elements alongside the bare identifier string.** This ask is made by CSTE [state epidemiologists], APHL [public health labs trade association], TDH-OIA [state public health agency], CDC [federal/public health], Regenstrief [research/informatics institute], AHA [hospital trade association], FAH [hospital trade association], and WEDI [administrative trade association] — eight independent voices converging on the same structural answer. APHL frames the issue most precisely: in all HL7 products, the assigning authority is part of the various supported data types for identifiers, so a USCDI Patient Identifier element without an assigning authority is technically incomplete relative to the standards USCDI is meant to govern. CSTE's recommendation to add the Type element separately (medical record number, Medicare number, SSN, laboratory patient identifier) directly addresses AHA's, FAH's, and WEDI's request that ONC clarify which identifier types are in scope. The vocabulary recommendation is also coordinated: Regenstrief points to **HL7 v2 identifier type codes** as the existing standard, and CDC notes the C-CDA 4.0 structure (HL7 II: InstanceIdentifier) already supports this design pattern. **Deceased Indicator** has even broader support — every voice that addresses it supports inclusion — but a different refinement cluster: **the element's accuracy is fundamentally limited by upstream notification.** Epic [EHR vendor], EHR Association [vendor trade association], and Altarum Institute [research org] all flag that EHRs are not reliably notified when patients die outside the healthcare system (at home, in non-affiliated facilities, recorded only in vital records). EHR Association proposes the most operationally useful response: ONC should acknowledge in usage notes that Deceased Indicator may not represent real-time or fully accurate information and that implementers should not rely on it as a definitive record of patient death without appropriate verification processes. Epic proposes the policy-level response: ONC should coordinate with federal and state vital records offices to propagate mortality information reliably to EHRs. Altarum proposes a definitional refinement: the indicator should primarily be used when death is known even if the exact date is not yet available — making the element useful for perinatal/newborn surveillance and other workflows where Date of Death may not be present. **david_rocha's** specific reference to the **Medicolegal Death Investigation FHIR IG** is the most concrete standards alignment recommendation in the Deceased Indicator commentary and is consistent with Epic's and EHR Association's calls for upstream coordination. Wolters Kluwer's [clinical content vendor] framing — that Deceased Indicator helps eliminate "undesired communications to grieving families" — provides a patient-experience justification absent from the more technical commentary. **The most striking pattern across both elements** is the depth of public health engagement: CDC [federal/public health], CSTE [state epidemiologists], APHL [public health labs trade association], and TDH-OIA [state public health agency] all engage substantively, and all four reach the same structural conclusion that USCDI's identifier elements need Type + Assigning Authority structure to support cross-organizational matching, NHSN reporting, NHCS-to-NDI linkage, and TEFCA-mediated query. **minigrrl's** protest of the demotion of the existing Medicare Patient Identifier element — alongside 20 other Case Reporting elements — frames the Patient Identifier addition as part of a broader USCDI restructuring whose direction (toward a unified Patient Identifier with Type/Assigning Authority) is sound but whose implementation may be losing operational granularity that 21 certified EHR products already exchange.

**Notably absent:** AMIA, ANI, AAAAI, AHIP (notable — AHIP discussed Member Identifier in their Health Insurance Information critique but didn't engage with the Patient Identifier proposal directly), AMA, AQIPS, NCQA, MEDITECH (engaged briefly), Allina Health, Emory Healthcare, UI Health, Providence Health, FDA, AHIMA (especially notable — patient identification is squarely AHIMA's professional domain), ACLA, SHIELD, CARIN Alliance, PACIO, SNOMED International, NCPDP, Vega Health, and Vizient are silent on Patient Identifier and Deceased Indicator despite filing v7 letters. AHIMA's complete silence on Patient Identifier is the single most striking gap given that health information management professionals manage MRNs and patient matching daily and have historically led the National Patient Identifier policy debate. Patient advocacy and consumer groups are entirely absent from the Deceased Indicator commentary despite the element directly affecting families receiving outreach about deceased loved ones — a use case Wolters Kluwer cites but no patient-facing organization corroborates.

---




