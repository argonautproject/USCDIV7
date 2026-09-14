
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

## Allergies and Intolerances: Add New *Must Support* element to US Core AllergyIntolerance Profile

### No Changes Between Draft and Final

<!-- image of summary of changes-->

![image](https://hackmd.io/_uploads/BkLvqurrfx.png)


<!-- **:new: Definition :point_down:** -->

![image](https://hackmd.io/_uploads/ryFFOcRLWx.png)


<!-- markdown table summary of proposal use adobe to convert to excel and then script to markdown or just copy/paste -->

## US Core Proposed Design

### Summary

DATA ELEMENT|<br/>Standards listed are required.<br/>If more than one is listed,<br/> at least one is required unless<br/>otherwise noted.<br/>Standards versions represent the most recent <br/>available at time of publication.</center>|US Core V10 Proposal
---|---|---
| **Allergy Intolerance Criticality**<br>Estimate of the potential clinical harm, or seriousness, of a reaction to an identified substance. |  | Add `AllergyIntolerance.criticality` as 0..1 *Must Support* with a *required binding* to 	[AllergyIntoleranceCriticality](https://hl7.org/fhir/R4/valueset-allergy-intolerance-criticality.html)|

<!-- ➕ In USCDI+ -->

### Issues

### Proposal

1. Add `AllergyIntolerance.criticality` as 0..1 *Must Support* with a *required binding* to [AllergyIntoleranceCriticality](https://hl7.org/fhir/R4/valueset-allergy-intolerance-criticality.html)
   - [Examples]([file:///Users/ehaas/Documents/FHIR](https://argonautproject.github.io/)/USCDIV7/output/artifacts.html#allergyintolerance-examples) for this Profile:
   - Open issues 
       - criticality v. severity: (See exhaustive discussion in reference cited below)
       - :thinking_face: Mapping to the AllergyIntoleranceCriticality codes is lossy (e.g., "medium" → "high").
           -  >A scale or rating system for criticality does not seem plausible. It is a clinical judgment. When a group of practicing allergists were assembled to comment on stage 2 of Meaningful Use, their recommendation was that the allergy list should carry an attribute indicating criticality as to whether the condition was life-threatening or organ system threatening, or not. - *[HL7 Version 3 Domain Analysis Model: Allergy and Intolerance, Release 1](https://www.hl7.org/implement/standards/product_brief.cfm?product_id=308)*
           -  Considering an extension to represent the source code.
               - [Alternate Codes extension](http://hl7.org/fhir/StructureDefinition/alternate-codes)
                   - :-1: Definition does not match intended use.
               - new US Core 'Source-Concept' extension with valueCode (or valueCoding) plus a definition that explicitly allows non-equivalence.
           - current FHIR R6 Trackers:
               - [FHIR-54013](https://jira.hl7.org/browse/FHIR-54013)- Make criticality an extension. Add rationale.

   **Elements (differential)**

    | Element | Must Support | Add'l USCDI | Cardinality | Type | Description |
    |---|:---:|:---:|---|---|---|
    | `AllergyIntolerance` |  |  | 0..* |  | **Allergy or Intolerance (generally: Risk of adverse reaction to a substance)**<br/>Risk of harmful or undesirable, physiological response which is unique to an individual and associated with exposure to a substance. |
    | <span style="padding-left: 1.5em;">↳</span>`clinicalStatus` | ✅ |  | 0..1 | `CodeableConcept` | **active \| inactive \| resolved**<br/>The clinical status of the allergy or intolerance.<br/><span style="font-size: 0.85em;">**Binding:** `http://hl7.org/fhir/ValueSet/allergyintolerance-clinical` (required)</span> |
    | <span style="padding-left: 1.5em;">↳</span>`verificationStatus` | ✅ |  | 0..1 | `CodeableConcept` | **unconfirmed \| confirmed \| refuted \| entered-in-error**<br/>Assertion about certainty associated with the propensity, or potential risk, of a reaction to the identified substance (including pharmaceutical product).<br/><span style="font-size: 0.85em;">**Binding:** `http://hl7.org/fhir/ValueSet/allergyintolerance-verification` (required)</span> |
    | <span style="padding-left: 1.5em;">↳</span><font color="green" size="5">criticality</font> || ✅  | 0..1 | `code` | **low \| high \| unable-to-assess**<br/>Estimate of the potential clinical harm, or seriousness, of the reaction to the identified substance.<br/><span style="font-size: 0.85em;">**Binding:** `http://hl7.org/fhir/ValueSet/allergy-intolerance-criticality` (required)</span> |
    | <span style="padding-left: 1.5em;">↳</span>`code` | ✅ |  | 1..1 | `CodeableConcept` | **Code that identifies the allergy or intolerance**<br/>Code for an allergy or intolerance statement (either a positive or a negated/excluded statement).  This may be a code for a substance or pharmaceutical product that is considered to be responsible for the adverse reaction risk (e.g., "Latex"), an allergy or intolerance condition (e.g., "Latex allergy"), or a negated/excluded code for a specific substance or class (e.g., "No latex allergy") or a general or categorical negated statement (e.g.,  "No known allergy", "No known drug allergies").  Note: the substance for a specific reaction may be different from the substance identified as the cause of the risk, but it must be consistent with it. For instance, it may be a more specific substance (e.g. a brand medication) or a composite product that includes the identified substance. It must be clinically safe to only process the 'code' and ignore the 'reaction.substance'.  If a receiving system is unable to confirm that AllergyIntolerance.reaction.substance falls within the semantic scope of AllergyIntolerance.code, then the receiving system should ignore AllergyIntolerance.reaction.substance.<br/><span style="font-size: 0.85em;">**Binding:** `http://cts.nlm.nih.gov/fhir/ValueSet/2.16.840.1.113762.1.4.1267.43` (extensible)</span> |
    | <span style="padding-left: 1.5em;">↳</span>`patient` | ✅ |  | 1..1 | `Reference`<br/><span style="font-size: 0.85em;">target: http://hl7.org/fhir/us/core/StructureDefinition/us-core-patient</span> | **Who the sensitivity is for**<br/>The patient who has the allergy or intolerance. |
    | <span style="padding-left: 1.5em;">↳</span>`recorder` |  | ✅ | 0..1 | `Reference`<br/><span style="font-size: 0.85em;">target: http://hl7.org/fhir/us/core/StructureDefinition/us-core-practitioner</span><br/><span style="font-size: 0.85em;">target: http://hl7.org/fhir/us/core/StructureDefinition/us-core-patient</span><br/><span style="font-size: 0.85em;">target: http://hl7.org/fhir/StructureDefinition/PractitionerRole</span><br/><span style="font-size: 0.85em;">target: http://hl7.org/fhir/us/core/StructureDefinition/us-core-relatedperson</span> | **Who recorded the sensitivity**<br/>Individual who recorded the record and takes responsibility for its content. |
    | <span style="padding-left: 1.5em;">↳</span>`reaction` | ✅ |  | 0..* | `BackboneElement` | **Adverse Reaction Events linked to exposure to substance**<br/>Details about each adverse reaction event linked to exposure to the identified substance. |
    | <span style="padding-left: 3.0em;">↳</span>`manifestation` | ✅ |  | 1..* | `CodeableConcept` | **Clinical symptoms/signs associated with the Event**<br/>Clinical symptoms and/or signs that are observed or associated with the adverse reaction event.<br/><span style="font-size: 0.85em;">**Binding:** `http://hl7.org/fhir/ValueSet/clinical-findings` (extensible)</span> |


<!-- 
3.  Add :thinking_face: criticality+patient search parameter -->

### Decisions

1. Sep 10th CGP Call
   - Add `AllergyIntolerance.criticality` as 0..1 `Add'l USCDI`
   - Map to USDCI Allergy Intolerance Criticality 
   - Terminology inherited from Base
       - required binding to AllergyIntoleranceCriticality
       - THO
       - explore option for an extension to avoid lossy mapping (for example - the concept for "medium" is missing) 
   - No new search

---

## Appendix

### Prior Art
 - NA
### Summary of USCDI Comments:

*This content was developed with the assistance of Claude.*

| Position | Organizations | Reasons |
|---|---|---|
| **OPPOSE** | *(no outright opposition)* | — |
| **OPPOSE / REDESIGN** | TMA (state physician society) | Defer until correlating vocabulary standard is specified |
| **MIXED / OPPOSE** | *(no mixed positions)* | — |
| **SUPPORT / with CHANGES** | AAAAI (physician specialty society — allergy/immunology), Emory Healthcare (academic medical center), SNOMED International (SDO), Oracle Health (EHR vendor), Regenstrief Institute (research/informatics), Altarum Institute (research org), J.P. Systems / Jay Lyle (individual informatics consultant), AmyJDalmas (individual standards commenter) | AAAAI: elevate from "should support" to **Must Support**. Emory: differentiate drug allergies (where criticality is highly actionable due to cross-reactivity) from food/environmental allergies (where utility varies); use simplified national values (low/high/unable-to-assess); flag provenance concern about patient-perceived severity. SNOMED Intl: designate SNOMED CT U.S. Edition for intra-class consistency with other Allergies/Intolerances elements. Oracle: reference HL7 FHIR AllergyIntoleranceCriticality value set. Regenstrief: reference FHIR criticality value set (low \| high \| unable-to-assess) explicitly. Altarum: flag missing vocabulary as moderate risk; specify or provide guidance. Lyle: criticality *evidence* more useful than criticality *judgment* — without evidence, judgments add burden and create ambiguity in high-acuity settings; if auto-assigned based on clinical norms, rationale should be explicit. Dalmas: correct the implementation-challenges note that says criticality has "replaced" severity — both are still used in clinical practice |
| **SUPPORT** | CMS-CCSQ (federal/payer), Epic (EHR vendor), UI Health (academic medical center) | CMS-CCSQ: applauds inclusion. Epic: software captures and exchanges allergy information today; reflects a clinically meaningful distinction well-suited for USCDI. UI Health: strong support — widely captured and exchanged today; highly useful across nearly all clinical contexts, particularly emergency and acute care |

For a complete summary of the comments, see the Appendix below:

### Allergy Intolerance Criticality (Allergies and Intolerances data class) — Comment Position Summary

**Comments grouped by position:**

**Strongly supportive**
- **CMS-CCSQ** [federal agency / payer] — Applauds inclusion of Allergy Intolerance Criticality in USCDI v7.
- **Epic** [EHR vendor] — Supports the addition. Epic software captures and exchanges allergy information today; the element reflects a clinically meaningful distinction well-suited for USCDI inclusion. Notably brief and unqualified support — Epic's "we support without qualification" tier in this v7 letter is small (Healthcare Agent, Allergy Intolerance Criticality), making this signal stronger than length suggests.
- **UI Health (University of Illinois Health)** [academic medical center] — Strong Support. Element — defined as the estimate of potential clinical harm or seriousness — is widely captured and exchanged today. Inclusion is highly useful across nearly all clinical contexts, particularly in emergency and acute care settings where rapid assessment of risk is required.

**Supportive with refinements**
- **American Academy of Allergy, Asthma & Immunology / AAAAI** [physician specialty professional society] — The most substantive single voice on this element. Strongly supports the addition. Frames the gap: the current allergy module in most EHRs fails to adequately communicate clinical criticality of documented reactions — a patient with a history of anaphylaxis to penicillin and a patient with a mild GI intolerance to penicillin "often carry identical allergy labels, an ambiguity that impairs clinical decision-making and contributes to unnecessary drug avoidance." The proposed element with standardized coded values (Low / High / Unable to Assess) addresses this gap directly. Argues inclusion will reduce reliance on free-text entries, enable clinical decision support tools to better prioritize allergy alerts, and meaningfully reduce **alert fatigue** — a documented problem causing clinicians to override warnings that may represent true safety hazards. Critical recommendation: although the Standards Bulletin shows the element is included, **it does not have a bold S** — meaning it's currently designated "should support" rather than "must support." AAAAI strongly recommends elevating it to **Must Support**. Frames AAAAI's broader work modernizing EHR allergy documentation as context.
- **Emory Healthcare** [academic medical center] — Strongly supports inclusion but recommends substantive refinements. The current Allergies and Intolerances class aggregates allergic reactions, non-allergic adverse drug reactions, side effects, and intolerances — Emory recommends segmenting drug reactions from other categories. **Drug allergies**: clear and significant use case for criticality given well-documented cross-reactivity and severe systemic reactions; standardized criticality is "invaluable for immediate patient safety." **Foods and other agents**: utility of criticality is less pronounced; clinical impact varies widely; blanket application may not always be beneficial. Flags **provenance concern**: what patients perceive as severe discomfort or significant impact on quality of life may not equate to a high-risk medical event — this inherent subjectivity makes it difficult to consistently apply standardized criticality. Despite challenges, strongly agrees with the need for a national standard. Proposes a simplified standardized approach: low / high / unable-to-assess risk. Recommends ONC further define requirements for capture and exchange while providing clear guidance on appropriate application.
- **SNOMED International** [SDO — terminology] — Recommends ONC designate SNOMED CT U.S. Edition as the applicable vocabulary standard. SNOMED CT includes validated clinical severity and risk concepts: 24484000 |Severe (severity modifier)|, 6736007 |Moderate (severity modifier)|, 255604002 |Mild (qualifier value)|. Frames designation as ensuring **intra-class consistency** — SNOMED CT is already required for Drug Class Allergy Intolerance, Non-Medication Allergy Intolerance, and Reaction within the same data class. Argues inconsistent coding of criticality severity across systems creates risk of medication errors and inappropriate care decisions, particularly in emergency and cross-organizational settings. Designation supports ONC Clinical Decision Support certification criteria (which already reference SNOMED CT for condition and severity coding) and aligns with patient-safety objectives of the 21st Century Cures Act information-blocking provisions.
- **Oracle Health** [EHR vendor] — Supports inclusion of the proposed element. Recommends USCDI reference the HL7 value set AllergyIntoleranceCriticality.
- **Regenstrief Institute** [research/informatics institute] — Supports inclusion. Important for clinical decision support; no vocabulary specified but consistent with FHIR AllergyIntolerance.criticality (low | high | unable-to-assess). Recommendation: reference the FHIR criticality value set explicitly for consistency across implementations.
- **Altarum Institute** [health-services research org] — Lists Allergy Intolerance Criticality among elements without specified vocabulary standards (alongside Adverse Event Outcome, Specimen Collection Method, Appointment, and Healthcare Agent). Frames as "moderate risk" of inconsistent implementation. Recommends ASTP/ONC specify vocabulary standards before finalizing v7, or at minimum provide implementation guidance identifying commonly used code systems.
- **Jay Lyle / J.P. Systems** [individual informatics consultant] — Distinct conceptual concern. Argues criticality *evidence* would be more useful than criticality *judgment*. The current requirement envisions a scenario where the documenting provider has information about criticality the receiving provider doesn't — and it would be good for the receiving provider to have that information. But asking prior providers to assign criticality judgments doesn't necessarily produce that outcome: criticality judgments without evidence add burden to the recording provider, potentially degrading data quality, without clear benefit to the receiver. Criticality can often be *inferred* from known combinations of medication and symptom (penicillin + dyspnea, morphine + nausea) — adding an explicit judgment provides little value. A judgment might add value if it deviates from clinical norms, but without supporting evidence it can create ambiguity: "in a high-acuity setting, a 'High' criticality rating for a common, non-severe reaction (like nausea) without evidence why the provider determines that this case is different could lead to unnecessary care delays or diagnostic distraction." Optional **criticality evidence** would be useful in such cases. If less-knowledgeable providers are supported by automatically assigning judgments based on clinical norms, the rationale should be explicit (e.g., "expected criticality for this substance & reaction pair; no additional information").
- **AmyJDalmas** [individual standards / informatics commenter] — Substantive correction request. The proposed implementation-challenges note states "Educational awareness for clinicians will be necessary since this field has replaced severity in clinical practice." Dalmas requests rephrasing because the statement is incorrect: criticality has *not* replaced severity in clinical practice. **Severity** is the clinical assessment of a specific allergic reaction when it occurs (mild, moderate, severe). **Criticality** is an estimate of potential clinical harm or seriousness of a reaction to an identified substance (low, high, unknown). Clinicians use both. In some systems, criticality may be derived in part from the severity of a previous reaction. Proposed replacement: "Educational awareness for clinicians may be necessary since this field can be derived from severity or has replaced severity in some clinical systems." Also notes Reaction Severity exists as a Level 2 USCDI element and supports its addition to a future version.

**Oppose / redesign**
- **TMA (Texas Medical Association)** [state physician professional society] — Lists Allergy Intolerance Criticality among 15 elements ONC should not adopt until each has a correlating vocabulary standard.

**Summary of Comments:** Allergy Intolerance Criticality is the most uncontested major v7 addition reviewed so far — no outright opposition, no mixed positions, and only TMA's pro-forma vocabulary-deferral request raising a process concern. The supporting voices are unusually concentrated and credentialed: AAAAI [physician specialty professional society] is the only specialty-medical-society voice on any v7 element to this point and brings the deepest subject-matter authority in the comment record. Their core argument — that the current EHR allergy module fails to distinguish anaphylaxis-to-penicillin from mild-GI-intolerance-to-penicillin, contributing to unnecessary drug avoidance and alert fatigue — is the clinical justification the rest of the supporting comments rely on. AAAAI's specific procedural ask is the most consequential request in this comment cycle: **elevate the element from "should support" to "must support"**. The vocabulary cluster converges tightly. Three independent commenters propose three valid options for the same gap: SNOMED International [SDO] proposes SNOMED CT severity codes (24484000 Severe, 6736007 Moderate, 255604002 Mild), Oracle Health [EHR vendor] and Regenstrief Institute [research/informatics] both point to the FHIR AllergyIntoleranceCriticality value set (low | high | unable-to-assess), and Altarum [research org] flags the gap without prescribing a fix. The FHIR value set choice has the advantage of matching what AAAAI proposes ("Low Criticality, High Criticality, Unable to Assess") and what Emory Healthcare [academic medical center] proposes (low / high / unable-to-assess) almost word-for-word — meaning ONC could adopt the FHIR value set and satisfy the specialty society, the academic medical center, two EHR/research voices, and the SDO simultaneously. **Three constructive concerns are unique** to this element and don't appear elsewhere. **Emory's segmentation argument** — drug allergies vs. food/environmental allergies have different criticality utility — surfaces a structural question about whether a single criticality element should apply across all reaction types. **Lyle's evidence-vs-judgment argument** — that documented criticality reasoning is more useful than bare criticality labels, and that auto-derived labels should expose their derivation rationale — reframes the element from a code-assignment task to a CDS-supporting structured note. **Dalmas's correction** — that criticality has not replaced severity, but is used alongside it — points to a definitional error in the implementation-challenges text that ONC should fix in the final v7 to prevent confusion as the element rolls out.

**Notably absent:** AHA, FAH, AMA, AMIA, ANI, AHIP, AQIPS, NCQA (silent despite addressing every other major v7 addition), WEDI, HL7 (especially notable given they engaged with most other elements), AHIMA, Allina Health, MEDITECH, EHR Association, Wolters Kluwer, CDC, APHL, CSTE, FDA, ACLA, SHIELD, CARIN Alliance, PACIO, and Vega Health are all silent on Allergy Intolerance Criticality despite filing v7 letters. The pediatric specialty societies (AAP) are absent despite pediatric food-allergy management being a major use case. AHIP's silence is interesting given the prior-authorization implications — high-criticality allergies often drive coverage decisions for branded biologics and alternatives. The general absence of patient advocacy groups, food allergy advocacy, and the major nursing professional societies (ANI was verbose elsewhere) means the AAAAI letter stands as the only dedicated specialty-society voice — making its "Must Support" recommendation harder for ONC to ignore but easier for ONC to position as a single specialty's request rather than a broad consensus.




