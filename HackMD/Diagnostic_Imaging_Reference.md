
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

## Diagnostic Imaging Reference: Update US Core DiagnosticReport Profile for Report and Note Exchange Profile


<!-- image of summary of changes-->
![image](https://hackmd.io/_uploads/H1WTz5Jw-g.png)

<!-- **:new: Definition :point_down:** -->

![image](https://hackmd.io/_uploads/SkQem9kwWg.png)

### Summary of USCDI Comments:

*This content was developed with the assistance of Claude.*

Diagnostic Imaging Reference is the most strongly opposed element in Draft USCDI v7.

| Position | Organizations | Reasons |
|---|---|---|
| **OPPOSE** | Epic (EHR vendor), EHR Association (vendor trade association), FAH (hospital trade association), HL7 (SDO), Oracle Health (EHR vendor) | Premature for USCDI inclusion. PACS and VNAs are not in the ONC Health IT Certification Program — requiring certified EHRs to facilitate imaging exchange on their behalf has unresolved workflow and standards implications. No balloted, published implementation guide exists. DICOMweb standard needs further updates. Argonaut Project work on FHIR/DICOMweb interoperability is not yet mature. ONC's parallel Diagnostic Imaging Interoperability Standards and Certification RFI (RIN 0955-AA11, Jan 30, 2026) should drive policy first; this element should not advance via USCDI alone |
| **OPPOSE / REDESIGN** | TMA (state physician society) | Defer until correlating vocabulary standard is specified |
| **MIXED / OPPOSE** | AHA (hospital trade association), Allina Health (provider/health system), LisaRNelsonRI (standards consultant) | AHA: recognizes value but recommends ONC pursue uniform regulatory approach for imaging interoperability through formal rulemaking before adopting USCDI element. Allina: supports intent but imaging references are not captured as discrete EHR data today; access is via embedded functionality with dynamic links; persistent externally resolvable links are system-specific and security-dependent — recommend flexible approach prioritizing standardized identifiers (accession number, DICOM Study Instance UID), with links optional and context-dependent. Nelson: too narrow — generalize to "Document Reference" in Healthcare Information Attributes since reports, plans, notes, letters, and explanations can all be retrieved via the same pattern |
| **SUPPORT / with CHANGES** | Medicom (imaging interoperability vendor), WEDI (admin/transactions trade association), Regenstrief Institute (research/informatics) | Medicom: most consequential addition in v7 from enterprise-imaging perspective — but specify FHIR ImagingStudy resource as preferred representation, DICOM Study Instance UID as required identifier, DICOMweb WADO-RS endpoint as required retrieval mechanism, and sufficient patient/study context. WEDI: provide guidance on minimum metadata for safe retrieval and matching (study identifiers, modality, performing organization, acquisition date/time, patient matching hints); secure access patterns for patient-facing vs. provider-facing use; align with parallel federal imaging-interoperability workstreams. Regenstrief: ensure alignment with DICOMweb and IHE profiles for consistent image retrieval |
| **SUPPORT** | Emory Healthcare (academic medical center), Wolters Kluwer (clinical content vendor) | Emory: strongly supports; weblinks for images are an important part of efficient patient-facing image sharing. Wolters Kluwer: reflects real-world clinical workflows; provides deeper granularity for care planning, treatment management, and evidence-based practice |

For a complete summary of the comments, see the Appendix below:

<!-- markdown table summary of proposal use adobe to convert to excel and then script to markdown or just copy/paste -->

## US Core Proposed Design

### Summary

DATA ELEMENT|<br/>Standards listed are required.<br/>If more than one is listed,<br/> at least one is required unless<br/>otherwise noted.<br/>Standards versions represent the most recent <br/>available at time of publication.</center>|US Core V10 Proposal
---|---|---
| **Diagnostic Imaging Reference ➕**<br>The information that can be used to access a diagnostic imaging study.<br>Examples include but are not limited to imaging study endpoint weblink, unique identifiers, and contextual information needed to retrieve a diagnostic imaging study. |  | Add `DiagnosticReport.media.link`,`DiagnosticReport.imagingStudy`, and  `DiagnosticReport.identifier` as min = 0 *Additional USCDI* element to the US Core DiagnosticReport for Report and Note Exchange Profile .|

➕ In USCDI+

### CCDA Design Notes

### Issues :thinking_face:

1.  Does there need to be a US Core ImagingStudy Profile?
2.  Should we scrap Media and use the Cross-version extension to support DocumentReference instead?
3.  How deep do we go into the reference to support the identifiers mentioned in the draft rule?
4.  Add search API requirements?


### Proposal

1.  Add the `DiagnosticReport.media.link` as a min = 0 *Additional USCDI* element to the US Core DiagnosticReport for Report and Note Exchange Profile to support links to various patient-friendly content, such as jpg images of x-rays.
1. Add the `DiagnosticReport.imagingStudy`as a min=0 *Additional USCDI* element to support exchange with systems that can view DICOM (Digital Imaging and Communications in Medicine) studies, series, and SOP (Service-Object Pair) instances referenced in the ImagingStudy resource.
1. Add the `DiagnosticReport.identifier` as a min=0 *Additional USCDI* element to access the source images from external sources using Business identifiers such as ascession numbers.


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

- https://confluence.hl7.org/spaces/AP/pages/161060067/SMART+Imaging+Access
- IHE MHD
- IPS (ImagingStudy)

### Diagnostic Imaging Reference (Diagnostic Imaging data class) — Comment Position Summary


**Comments grouped by position:**

**Strongly supportive**
- **Emory Healthcare** [academic medical center] — Strongly supports inclusion of Diagnostic Imaging Reference and the broader exchange of diagnostic imaging tests and results. Frames patient-facing image sharing — letting patients access their own radiology images on-demand — as the use case making this element important.
- **Wolters Kluwer** [clinical content vendor] — Cites Diagnostic Imaging Reference among the v7 additions (alongside Nutrition Order, Medical Device Order, Medication Administration, and Specimen Collection Method) that "reflect real-world clinical workflows and provide deeper granularity needed for care planning, treatment management, and evidence-based practice."

**Supportive with refinements**
- **Medicom** [imaging interoperability vendor] — Calls Diagnostic Imaging Reference "the single most consequential addition in Draft USCDI v7 from the perspective of enterprise imaging interoperability" — the first USCDI data element to explicitly establish that diagnostic imaging studies must be electronically accessible and referenceable across health IT systems. Argues the current definition correctly captures intent but is "insufficiently specific to ensure consistent, interoperable implementation." Without greater specificity, implementation will vary across EHR vendors, PACS vendors, and imaging exchange platforms, "resulting in a fragmented ecosystem in which a reference generated by one system cannot be reliably consumed by another." Four specific recommendations:
  1. **FHIR ImagingStudy as preferred representation** — the HL7 FHIR ImagingStudy resource (R4/R5) is the most complete structured representation; natively captures DICOM Study Instance UID, series-level metadata, the DICOMweb WADO-RS endpoint, and contextual links to ServiceRequest (ordering provider) and DiagnosticReport. ASTP/ONC should specify FHIR ImagingStudy as the required representation for certified health IT systems.
  2. **DICOM Study Instance UID as required identifier** — globally unique, persistent identifier for every imaging study, universally captured by all PACS and VNA systems worldwide. Any compliant Diagnostic Imaging Reference must include this identifier. Accession number, while operationally important within a facility's RIS/PACS workflow, is facility-specific and not globally unique — should be characterized as complementary, not primary.
  3. **DICOMweb WADO-RS endpoint as required retrieval mechanism** — DICOMweb (DICOM PS3.18) enables web-based retrieval using standard HTTP APIs, compatible with modern EHR and application integration frameworks. Implemented in production by leading PACS vendors and imaging platforms; cornerstone of SMART Imaging Access and IHE SMART-on-FHIR workflows for imaging.
  4. **Sufficient patient and study context** — beyond technical identifiers, references should include patient identifier (MRN or national identifier), study date/time, modality, and ordering organization so studies can be unambiguously identified across organizational boundaries.
- **WEDI** [administrative/transactions trade association] — Cites Diagnostic Imaging Reference among the v7 additions that "could materially reduce administrative burden and improve interoperability." Three specific recommendations: (1) provide guidance on minimum metadata needed for safe retrieval and matching — study identifiers, modality, performing organization, acquisition date/time, patient matching hints; (2) provide guidance on secure access patterns appropriate for patient-facing vs. provider-facing use cases; (3) align with parallel federal workstreams addressing imaging interoperability to support, rather than fragment, the emerging approach — image retrieval across organizations is a persistent administrative burden.
- **Regenstrief Institute** [research/informatics institute] — Supports the element. No vocabulary specified but contextual/structural data; element provides information to access a diagnostic imaging study (endpoint weblink, unique identifiers). Recommendation: ensure alignment with DICOMweb and IHE profiles for consistent image retrieval.

**Mixed / oppose**
- **American Hospital Association / AHA** [hospital trade association] — Lists Diagnostic Imaging Reference among the v7 elements requiring "clarifying guidance and vocabulary standards prior to adoption." Recognizes that access to secure, high-resolution images is often a critical component of diagnosis and early intervention and can improve outcomes and reduce costs, and that seamless image transfer has historically been hampered by silos from proprietary systems, inconsistent formats, and lack of exchange frameworks. Recognizes new USCDI data elements may be an important part of improving imaging interoperability — but **before finalizing new data elements, AHA encourages ONC to promote platform and exchange standardization through a uniform regulatory approach for imaging interoperability** via formal rulemaking to gather public stakeholder feedback.
- **Allina Health** [provider / health system] — Appreciates and supports the intent to improve access to imaging studies. However, in current workflows, imaging references are not typically captured as discrete data elements within the EHR — instead, access is facilitated through embedded functionality with underlying identifiers and links managed dynamically. Feasibility depends on definition: standard identifiers (accession numbers, DICOM Study Instance UIDs) could be implemented since they're already widely used; requiring a persistent, externally resolvable link would be challenging because such links are often system-specific, security-dependent, and not stable across environments. Recommends ASTP clarify the intended use case(s) and prioritize a flexible approach focused on standardized identifiers, with links treated as optional and context-dependent.
- **Lisa Nelson / LisaRNelsonRI** [individual standards consultant] — Recommends generalization. Notes that many different kinds of documents — reports, plans, notes, letters, explanations — can be retrieved via the same pattern (endpoint weblink, unique identifiers, contextual information). The data element should be introduced generally to "minimize the bloat of USCDI data elements." Proposed: create a general data element in the Healthcare Information Attributes data class called **Document Reference**, defined as "the information that can be used to access a document or referenceable collection of information which can be retrieved as a meaningful assemblage of information about the patient or a patient's encounter or delivered healthcare service(s)." Examples to include endpoint weblinks, unique identifiers, and contextual information.

**Oppose / redesign**
- **TMA (Texas Medical Association)** [state physician professional society] — Lists Diagnostic Imaging Reference among 15 elements ONC should not adopt until each has a correlating vocabulary standard.

**Oppose**
- **Epic** [EHR vendor] — Refers ONC to Epic's feedback on the Diagnostic Imaging Interoperability Standards and Certification RFI (RIN 0955-AA11, submitted March 16, 2026), which addresses the role of USCDI in diagnostic imaging exchange in detail; "we do not support inclusion of this data element until ONC has pursued the foundational steps outlined in that feedback." Argues diagnostic imaging data — pixel data or imaging manifests — is chiefly stored in DICOM archives such as PACS and VNA systems, which **do not participate in the ONC Health IT Certification Program**. Requiring a system that does participate (the EHR) to facilitate imaging data exchange on behalf of PACS and VNAs introduces significant workflow and standards considerations that have not been adequately addressed. If ONC were to expand certification to PACS and VNAs, multiple new criteria written specifically for the different entities involved in image exchange would be needed, with consensus-standard adoption aligned across all participants. "Until USCDI is more flexible for different types of implementers, this data element should not be included in USCDI."
- **EHR Association** [vendor trade association] — "Significant concerns regarding the readiness" of the proposed element for v7 inclusion. Supports the broader goal of improving access to and exchange of diagnostic imaging, but the current state of standards, implementation guidance, and industry alignment does not yet support consistent, secure, and interoperable use. **Urges ONC to withdraw the Diagnostic Imaging Reference data element from USCDI v7 pending resolution of feedback received through the Diagnostic Imaging Interoperability Standards and Certification RFI and further maturation of supporting standards.**
- **Federation of American Hospitals / FAH** [hospital trade association] — Recommends ONC reconsider advancement. Argues ONC should prioritize standardization of PACS or VNA platforms and imaging exchange standards before expanding requirements for image access and exchange. Image viewing through patient portals is feasible, but **download and transmit capabilities present significantly greater technical and operational challenges**: imaging studies vary widely in modality and file size, from small radiographs to multi-gigabyte CT and MRI scans, creating challenges for bandwidth, storage, system performance, and transmission. Additional barriers — identity provisioning, authentication, infrastructure limitations, vendor variability — further complicate scalable exchange. A uniform regulatory approach to all imaging modalities risks imposing requirements that are not technically feasible or operationally scalable. **Before advancing this element, ONC should review public comment from the January 30, 2026, Diagnostic Imaging Interoperability Standards and Certification RFI** and offer a subsequent proposal informed by that public comment after developing a more formal structure for imaging interoperability.
- **HL7** [SDO] — Recommends that **rather than including this data element in USCDI v7**, ONC work with CMS, HL7, and DICOM in particular to progress the Argonaut Accelerator's work to establish clear guidance on how DICOMweb, HL7 FHIR, and other standards are to be used supporting this use case. Once such guidance is sufficiently mature, it can be included in USCDI.
- **Oracle Health** [EHR vendor] — Agrees with the need to enable sharing images across providers, with patients, and with other parties — but argues it is "premature to advance a Diagnostic Imaging Reference into USCDI as there is no balloted and published implementation guide nor sufficient implementation and deployment that enables implementation at scale." Recognizes progress from the Argonaut Project and individual organizations, but issue must be resolved first with the source imaging systems (PACS/VNA); much work is left to enable adoption from imaging systems to EHRs, patient apps, and other HIT. Further updates to the DICOMweb standard are necessary, along with payment-system incentives to drive infrastructure investment essential for image access, sharing, and clinical workflow integration. **Urges ONC not to include this data element in USCDI at this time** but rather to work with industry and CMS to advance the essential implementation guides and funding/payment considerations that will enable successful adoption — "starting with the imaging services making the references available."

**Summary of Comments:** Diagnostic Imaging Reference is the most strongly opposed element in Draft USCDI v7. Five major voices — both top EHR vendors (Epic, Oracle Health), the EHR Association [vendor trade association], a hospital trade association (FAH), and the principal SDO (HL7) — explicitly recommend ONC not include the element at all. AHA [hospital trade association] reaches a similar conclusion through a different route, recommending formal rulemaking on imaging interoperability before any USCDI element is finalized. The opposition is technically grounded and converges tightly on three concerns. **First, the certification scope mismatch**: Epic and Oracle Health argue that PACS and VNA systems hold the data and provide the retrieval interfaces, but those systems are not in the ONC Health IT Certification Program. Requiring certified EHRs to surface imaging references on behalf of uncertified PACS/VNAs creates accountability and conformance gaps that USCDI alone cannot resolve. **Second, standards immaturity**: Oracle Health, the EHR Association, HL7, and FAH all note there is no balloted, published implementation guide; the Argonaut Project's FHIR/DICOMweb work is in progress; DICOMweb itself needs further updates; and the certified-product ecosystem hasn't deployed enough to support consistent exchange at scale. **Third, the parallel federal RFI**: ONC issued a Diagnostic Imaging Interoperability Standards and Certification RFI on January 30, 2026 (RIN 0955-AA11), with public comment closing in mid-March. Epic, Oracle Health, the EHR Association, and FAH all urge ONC to let that RFI drive policy first rather than locking in a USCDI definition before the resulting standards work is complete. The **supporting voices** are technically deep but few. Medicom [imaging interoperability vendor] — the only voice with day-to-day skin in the enterprise-imaging interoperability game — frames the element as the most consequential addition in v7 and provides the most specific technical implementation roadmap: FHIR ImagingStudy resource as preferred representation, DICOM Study Instance UID as required identifier, DICOMweb WADO-RS as required retrieval mechanism, sufficient patient and study context for cross-organizational matching. Their roadmap, if adopted, would directly address the standards-maturity concerns Oracle Health and HL7 raise. Wolters Kluwer [clinical content vendor] and Emory Healthcare [academic medical center] support without technical specification. Regenstrief [research/informatics institute] supports with DICOMweb/IHE alignment. WEDI [administrative trade association] supports with implementation-guidance asks that mirror Medicom's. The **mixed/oppose voices** offer constructive paths forward: Allina Health [provider] would scope the element to standardized identifiers (already widely captured in EHRs) and treat persistent links as optional; LisaRNelsonRI [individual] would generalize the element to a broader Document Reference applicable across all USCDI document-bearing exchanges. Both would reduce the standards-readiness gap but at different costs to the element's specificity. The single most striking pattern: **the opposition isn't ideological** — every opposer explicitly endorses the goal (cross-organizational image exchange) and disagrees only on whether USCDI v7 is the right vehicle or the right time. Almost all of them point to the same alternative path: develop the FHIR/DICOMweb implementation guide first through Argonaut and the parallel RFI, then USCDI catches up.

**Notably absent:** AMIA, AMA, ANI, AHIP, AQIPS, NCQA, MEDITECH, AHIMA, FDA (notably — FDA regulates much imaging-device output), CDC, APHL, CSTE, ACLA, SHIELD, SNOMED International, CARIN Alliance, PACIO, Vega Health, UI Health, Vizient, Altarum Institute, and CMS-CCSQ are all silent on Diagnostic Imaging Reference despite filing v7 letters. CMS-CCSQ's silence is the most surprising given they issued comments applauding nearly every other v7 element — possibly indicating internal disagreement about whether USCDI should advance imaging exchange ahead of the parallel RFI process. The radiology professional societies (ACR, RSNA), DICOM Standards Committee, and IHE are all conspicuously absent — none filed a v7 letter despite the element's direct relevance to their domains. Patient advocacy groups, despite imaging download/share being a frequent patient-rights concern, are also silent. UI Health's silence is notable because they were verbose on every other Healthcare Information Attributes element and on prior-authorization-related infrastructure, but offered no comment on imaging.


