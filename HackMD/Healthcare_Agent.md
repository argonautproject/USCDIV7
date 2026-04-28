
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

## Healthcare Agent: See Options below


<!-- image of summary of changes-->
![image](https://hackmd.io/_uploads/HJD2scC8Ze.png)

<!-- **:new: Definition :point_down:** -->

![image](https://hackmd.io/_uploads/rkA0nqRU-x.png)

### Summary of USCDI Comments:

*This content was developed with the assistance of Claude.*

| Position | Organizations | Reasons |
|---|---|---|
| **OPPOSE** | *(no outright opposition)* | — |
| **OPPOSE / REDESIGN** | Allina Health (provider), TMA (state physician society) | Allina: not discretely captured today; new build/workflow burden; frontline staff can't validate legal authority. TMA: defer until vocabulary specified |
| **MIXED / OPPOSE** | Emory Healthcare (academic medical center), Oracle Health (EHR vendor) | Emory: name without legal-instrument linkage creates false legal certainty; need to distinguish agent vs. guardian vs. surrogate, link to source document, capture jurisdiction. Oracle: existing Care Team Role element already covers this — enhance that instead of creating new element |
| **SUPPORT / with CHANGES** | ANI (nursing informatics), MEDITECH (EHR vendor), Regenstrief Institute (research/informatics), Altarum Institute (research org), LisaRNelsonRI (standards consultant) | ANI: term "agent" risks AI-agent confusion — use "proxy"; add scope/activation fields. MEDITECH: clarify relationship to advance directives. Regenstrief: clarify boundary with Related Person and Advance Directive Observation. Altarum: specify a vocabulary. Nelson: add ordinal primary/alternate; add Healthcare Agent Telecom |
| **SUPPORT** | CMS-CCSQ (federal/payer), PACIO Project (post-acute care interop community), NCQA (quality measurement), Epic (EHR vendor), Wolters Kluwer (clinical content vendor) | High-value, mature, supports care coordination and transitions. PACIO: easier entry point to advance care planning than specifying treatment preferences. Epic: already captured and exchanged today |

For a complete summary of the comments, see the Appendix below:

<!-- markdown table summary of proposal use adobe to convert to excel and then script to markdown or just copy/paste -->


## US Core Proposed Design

### Summary

DATA ELEMENT|<br/>Standards listed are required.<br/>If more than one is listed,<br/> at least one is required unless<br/>otherwise noted.<br/>Standards versions represent the most recent <br/>available at time of publication.</center>|US Core V10 Proposal
---|---|---
| **Healthcare Agent ➕**<br>Individual legally authorized to make healthcare decisions on behalf of a patient when the patient is unable to do so because of an illness or injury. |  |See Options below |
➕ In USCDI+

## CCDA Design Notes

### Issues

### Proposal Options:

1.  Use CareTeam: Add role code to the [Care Team Member Function](https://vsac.nlm.nih.gov/valueset/2.16.840.1.113762.1.4.1099.30/expansion) ValueSet
2.  Use Patient: Add code to the `Patient.contact.relationship` ValueSet
3.  Use RelatedPerson: Add code to RelatedPerson.relationship
4.  Consent Resource (see: https://build.fhir.org/ig/HL7/fhir-pacio-adi/StructureDefinition-ADI-HealthcareAgentConsent.html)

## Decisions

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

[PACIO ADI](https://build.fhir.org/ig/HL7/fhir-pacio-adi)


### Healthcare Agent (Care Team Members data class) — Comment Position Summary

**Comments grouped by position:**

**Strongly supportive**
- **CMS-CCSQ** [federal agency / payer] — "CMS-CCSQ supports the inclusion of Healthcare Agent in USCDI v7."
- **PACIO Project** [post-acute care interoperability community] — Vitally important for advance care planning. Notes that experts and SMEs find individuals often complete agent designation more readily than they complete explicit treatment preferences, so Healthcare Agent provides "a floor of critical information" and a feasible entry point to advance care planning. Frames the element as a broader concept that may include "Durable Medical Power of Attorney" as a subset, alongside other powers and limitations.
- **NCQA** [quality measurement org] — Lists Healthcare Agent among the v7 additions NCQA "strongly supports" as a high-value addition with limited implementation burden given overlap with other exchange requirements.
- **Epic** [EHR vendor] — Supports the addition. Epic software captures and exchanges this information today; element maturity warrants USCDI inclusion. Notable contrast with Epic's strong opposition to Adverse Events — for Healthcare Agent the workflow and capture concerns Epic raised elsewhere don't apply.
- **Wolters Kluwer** [clinical content vendor] — Cites Healthcare Agent alongside Appointment, Accommodation, and Deceased Indicator as elements that "enrich the context required for efficient, safe, and equitable care delivery" and improve interoperability around transitions of care, referral workflows, and patient-centric planning.

**Supportive with refinements**
- **Alliance for Nursing Informatics / ANI** [nursing informatics professional society] — Among the most clinically impactful proposals in Draft v7. Identifying and rapidly contacting a legally authorized decision-maker is a core nursing responsibility currently hampered by lack of structured, interoperable data. Two recommendations: (1) **terminology** — as AI-enabled systems, autonomous software agents, and agentic workflows become prevalent, "agent" risks semantic confusion; recommends "healthcare proxy" or similar unambiguous language in implementation guidance and value-set documentation; (2) **structure** — systems capturing this data should include structured fields for contact information, scope of authority, and activation status to deliver full clinical utility, particularly in palliative and intensive care.
- **MEDITECH** [EHR vendor] — Recognizes the value but flags lack of standardized discrete fields, which could result in inconsistent implementation and reduced interoperability. Suggests the definition evolve to clarify the Healthcare Agent's relationship to legal documentation and advance directives.
- **Regenstrief Institute** [research/informatics institute] — Supports inclusion. Notes no vocabulary specified and that the element complements the Advance Directive Observation in Goals and Preferences. Recommendation: clarify relationships to existing Related Person data and the Advance Directive Observation element to prevent implementer confusion.
- **Altarum Institute** [health-services research org] — Lists Healthcare Agent among elements without applicable vocabulary standards (alongside Adverse Event Outcome, Allergy Intolerance Criticality, Specimen Collection Method, and Appointment) and creates "moderate risk" of inconsistent implementation. Recommends ASTP/ONC specify vocabulary standards before finalizing v7, or at minimum provide implementation guidance identifying commonly used code systems.
- **Lisa Nelson / LisaRNelsonRI** [individual standards consultant] — Strong support for inclusion. Two refinements: (1) **ordinal designation** — when a patient appoints multiple agents in preferred order ("eldest daughter primary, youngest daughter first alternate"), the definition should capture that ordinal relationship; recommends adding language: "A patient may appoint more than one Healthcare Agent provided the preferred order is made clear in terms of which Healthcare Agent is primary and which may fulfill that role as an alternative if the initial Healthcare Agent can't be contacted"; (2) **contactability** — name and role aren't enough; provider needs to actually reach the agent in emergencies, so a Healthcare Agent Telecom element is needed (Nelson cross-references their separate recommendation for a generalized Telecom Information element in Healthcare Information Attributes).

**Mixed / oppose**
- **Emory Healthcare** [academic medical center] — Strongly supports interoperable exchange of advance directive information conceptually, but raises a fundamental redesign concern: the proposal fails to distinguish patient-authored preferences (PACP-style content) from legally validated decision-making authority. In Georgia (and many states), an agent's authority depends on a properly executed and legally valid advance directive or medical power of attorney. Identifying someone as "Healthcare Agent" without linkage to and verification of the underlying legal instrument may create **false legal certainty**, inappropriate reliance in clinical decision-making, or improper PHI disclosure. Emory's five required safeguards: (1) distinguish formally appointed Healthcare Agent vs. court-appointed guardian vs. statutory surrogate under state law; (2) structurally link to the governing advance directive or POA document; (3) include document provenance and verification status (on file, verified, revoked, expired); (4) capture governing jurisdiction (state law); (5) support successor or alternate agent designation. Without these, exchange of agent identity alone may not meaningfully support transitions of care and may introduce legal/regulatory risk in emergency care, interfacility transfers, and interstate exchange.
- **Oracle Health** [EHR vendor] — Generally supports the concept but argues the existing CareTeam Role data element already effectively covers it via the FHIR US Core role value set (`http://cts.nlm.nih.gov/fhir/ValueSet/2.16.840.1.113762.1.4.1099.30`), which already includes roles similar to Healthcare Agent (e.g., legal guardian) — although "healthcare agent" and synonyms (healthcare proxy, medical power of attorney) are not yet included. Recommends enhancing the Care Team Role element definition to explicitly call out healthcare agent as a relevant role, and working with HL7 and NIH NLM to formally recognize it as a distinct function rather than creating a separate USCDI data element.

**Oppose / redesign**
- **Allina Health** [provider / health system] — Recognizes the value of capturing healthcare agent for decision-making support, but raises operational and legal complexity concerns. Information is not always discretely captured today and would require new system build and workflow development. Designation can change over time and depends on availability and validity of legal documentation (advance directives, POA), requiring robust verification processes, clear policies, and ongoing updates. Frontline clinical and administrative staff may not be well-positioned to validate legal authority or ensure documentation currency, introducing data accuracy and legal compliance risks. Maintaining current information would require significant operational resources.
- **TMA (Texas Medical Association)** [state physician professional society] — Lists Healthcare Agent among 15 elements ONC should not adopt until each has a correlating vocabulary standard.

**Summary of Comments:** Healthcare Agent draws broad conceptual support — every commenter agrees exchanging the identity of a patient's legally authorized decision-maker is clinically valuable, particularly in emergency, intensive-care, and palliative-care settings. Disagreement clusters around three implementation concerns. **Legal/structural rigor** is the most prominent: Emory Healthcare [academic medical center], Allina Health [provider], and MEDITECH [EHR vendor] argue that exchanging an agent's name without binding it to the underlying advance directive or power-of-attorney document, document provenance, verification status, governing jurisdiction (state law varies materially), and the distinction between formally appointed agents, court-appointed guardians, and statutory surrogates risks creating false legal certainty and improper PHI disclosure. **Element duplication** is the second cluster: Oracle Health [EHR vendor] argues the existing Care Team Role data element with the FHIR US Core role value set already covers this concept and recommends enhancing that element rather than creating a new one — coordinating with HL7 and NIH NLM to formally recognize "healthcare agent" as a role. Regenstrief [research/informatics institute] makes a softer version of this point, asking ONC to clarify boundaries with the existing Related Person data and Advance Directive Observation element. **Vocabulary and structural detail** is the third cluster: Altarum [health-services research org] flags the missing applicable vocabulary; ANI [nursing informatics professional society] wants structured scope-of-authority and activation-status fields; LisaRNelsonRI [individual standards consultant] notes that name alone isn't actionable without contact information and proposes a Healthcare Agent Telecom element plus ordinal primary/alternate semantics. ANI also raises a forward-looking terminology concern unique to this element: as AI agents and agentic workflows proliferate in health IT, "agent" risks semantic confusion with autonomous software, and "healthcare proxy" would be less ambiguous. The "support with caveats" position from MEDITECH and the EHR Association's general posture (defer until standards mature, applied here through TMA) point to the same underlying issue — the data exists in clinical practice but isn't captured discretely or consistently across systems today.

**Notably absent:** AHA, FAH, AMIA, AMA, AHIP, AQIPS, FDA, CDC, APHL, CSTE, AHIMA, HL7, SHIELD, and Vega Health are all silent on Healthcare Agent despite filing v7 comment letters. The hospital trade associations' silence is particularly noteworthy given their detailed engagement on Adverse Events — Healthcare Agent doesn't appear to register the same workflow or legal-conflict concerns. Patient advocacy and consumer groups, which would be expected stakeholders on a decision-making-authority element, are entirely absent.

---



