
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

## Laboratory: Changes to US Core Specimen Profile

### Changes Between Draft and Final USCDI v7

| Draft v7 element | Final v7 element | What changed |
|---|---|---|
| Specimen Collection Method | Specimen Collection Method | **Applicable standard added**: SNOMED CT U.S. Edition. |
| Specimen Collection Date and Time || no change


<!-- image of summary of changes-->
![image](https://hackmd.io/_uploads/rJGP0KBBzg.png)


<!-- **:new: Definition :point_down:** -->

![image](https://hackmd.io/_uploads/SJVxsaJw-x.png)

<!-- markdown table summary of proposal use adobe to convert to excel and then script to markdown or just copy/paste -->

## US Core Proposed Design

### Summary

DATA ELEMENT|<br/>Standards listed are required.<br/>If more than one is listed,<br/> at least one is required unless<br/>otherwise noted.<br/>Standards versions represent the most recent <br/>available at time of publication.</center>|US Core V10 Proposal
---|---|---
| **Specimen Collection Method**<br>Technique or procedure used to obtain a specimen.<br>Examples include but are not limited to venipuncture, swab, biopsy, aspiration, and<br>catheter collection. | SNOMED Clinical Terms (SNOMED CT) U.S. Edition, March 2026 Release  | Add `Specimen.collection.method` min = 0 *Additional USCDI* to the *US Core Specimen Profile*
| **Specimen Collection Date and Time**<br>Date and time when the specimen was obtained.  | | Add `Specimen.collection.collected[x]` min = 0 *Additional USCDI* to the *US Core Specimen Profile*.  Note that based on the base FHIR definition, [US Core Laboratory Result Observation Profile](https://hl7.org/fhir/us/core/StructureDefinition-us-core-observation-lab.html) `effective[x]` also maps to this data element 

<!-- ➕ In USCDI+ -->

### Issues

1. Terminology - see options below.

### Proposal

1. Add `Specimen.collection.collectd[x]` min = 0 *Additional USCDI* to the *US Core Specimen Profile*. 
      -  Note that based on the base FHIR definition, [US Core Laboratory Result Observation Profile](https://hl7.org/fhir/us/core/StructureDefinition-us-core-observation-lab.html) `effective[x]` also maps to this data element 


1. Add `Specimen.collection.method` min = 0 *Additional USCDI* to the *US Core Specimen Profile*
   - [Examples](https://argonautproject.github.io/USCDIV7/artifacts.html#specimen-examples) for this Profile:
   - Open issues :thinking_face:
     1. Terminology options:
      
        1. [FHIR Specimen Collection Method](https://hl7.org/fhir/R4/valueset-specimen-collection-method.html) ~ dozen SNOMED Codes
        3. [FHIM's Specimen Collection Method](https://vsac.nlm.nih.gov/valueset/2.16.840.1.113762.1.4.1062.5/expansion/Latest)  VSAC -65 SNOMED Codes only two FHIR Specimen Collection Method are members!
        4. :thumbsup: :new:  [US Core Specimen Collection Method](https://argonautproject.github.io/USCDIV7/ValueSet-us-core-specimen-collection-method.html)
            - 211 concepts
            - SNOMED CT 17636008 | Specimen collection (procedure) hierarchy. ~140 concepts
            - 66 enumerated codes from (now defunct) CDC PHConnect specimen mapping project
            - 2 codes from FHIM's Specimen Collection Method not already covered.
            - These common method codes:
            
            | Method | SNOMED code | Display (en-US PT) |
            |---|---|---|
            | Bone Marrow Biopsy | `56241004` | Bone marrow biopsy, needle or trocar |
            | Anal Pap Test | `405281009` | Anal pap smear |
            | Broncho-Alveolar Lavage (active replacement for retired `397394009`) | `397397002` | Bronchoscopy and bronchoalveolar lavage |
            | Broncho-Alveolar Lavage (non-bronchoscopic) | `782762003` | Blind bronchoalveolar lavage |
            | Gout Crystal Analysis (joint fluid) | `90131007` | Arthrocentesis |
            | Body Fluid Cytology (pericardial) | `309849004` | Pericardiocentesis |
            | Blood Culture | `30088009` | Blood culture |
            | Blood Venipuncture (more specific than the in-VS parent `82078001`) | `28520004` | Venipuncture for blood test |
            
            - see Appendix :point_down: for Gap Analysis with HL7 V2 Table 0488


      2. Binding Strength: Preferred  vs Extensible ? :thinking_face: 


    **Elements (differential)**

    | Element | Must Support | Add'l USCDI | Cardinality | Type | Description |
    |---|:---:|:---:|---|---|---|
    | `Specimen` |  |  | 0..* |  | **Sample for analysis**<br/>A sample to be used for analysis. |
    | <span style="padding-left: 1.5em;">↳</span> `identifier` | ✅ |  | 0..* | `Identifier` | **Specimen identifier**<br/>Id for specimen. |
    | <span style="padding-left: 1.5em;">↳</span> `accessionIdentifier` | ✅ |  | 0..1 | `Identifier` | **Identifier assigned by the lab**<br/>The identifier assigned by the lab when accessioning specimen(s). This is not necessarily the same as the specimen identifier, depending on local lab procedures. |
    | <span style="padding-left: 1.5em;">↳</span> `type` | ✅ |  | 1..1 | `CodeableConcept` | **Kind of material that forms the specimen**<br/>The kind of material that forms the specimen.<br/><span style="font-size: 0.85em;">**Binding:** `http://cts.nlm.nih.gov/fhir/ValueSet/2.16.840.1.113762.1.4.1099.54` (extensible)</span> |
    | <span style="padding-left: 1.5em;">↳</span> `subject` | ✅ |  | 0..1 | `Reference`<br/><span style="font-size: 0.85em;">target: http://hl7.org/fhir/us/core/StructureDefinition/us-core-patient</span>(✅ Must Support)<br/><span style="font-size: 0.85em;">target: http://hl7.org/fhir/StructureDefinition/Group</span><br/><span style="font-size: 0.85em;">target: http://hl7.org/fhir/us/core/StructureDefinition/us-core-device</span><br/><span style="font-size: 0.85em;">target: http://hl7.org/fhir/StructureDefinition/Substance</span><br/><span style="font-size: 0.85em;">target: http://hl7.org/fhir/us/core/StructureDefinition/us-core-location</span> | **The patient where the specimen came from.**<br/>Where the specimen came from. This may be from patient(s), from a location (e.g., the source of an environmental sample), or a sampling of a substance or a device. |
    | <span style="padding-left: 1.5em;">↳</span> `collection` |  | ✅ | 0..1 | `BackboneElement` | **Collection details**<br/>Details concerning the specimen collection. |
    | <span style="padding-left: 3.0em;">↳</span> <font  color=red>collected[x]</font> |  | ✅ | 0..1 | `dateTime`<br/>`Period` | **Collection time**<br/>Time when specimen was collected from subject - the physiologically relevant time. |
    | <span style="padding-left: 3.0em;">↳</span> <font  color=red>method</font>|  | ✅ | 0..1 | `CodeableConcept` | **Specimen Collection Method**<br/>A coded value specifying the technique that is used to perform the procedure.<br/><span style="font-size: 0.85em;">**Binding:** `http://hl7.org/fhir/ValueSet/specimen-collection-method` (preferred):thinking_face:</span> |
    | <span style="padding-left: 3.0em;">↳</span> `bodySite` |  | ✅ | 0..1 | `CodeableConcept` | **Specimen Source Site**<br/>Anatomical location from which the specimen was collected (if subject is a patient). This is the target site.  This element is not used for environmental specimens.<br/><span style="font-size: 0.85em;">**Binding:** `http://hl7.org/fhir/ValueSet/body-site` (extensible)</span> |
    | <span style="padding-left: 1.5em;">↳</span> `condition` |  | ✅ | 0..* | `CodeableConcept` | **Specimen condition**<br/>A mode or state of being that describes the nature of the specimen.<br/><span style="font-size: 0.85em;">**Binding:** `http://hl7.org/fhir/us/core/ValueSet/us-core-specimen-condition` (extensible)</span> |


### Decisions

1. Aug 6th CGP Call
   - Add `.collected[x]` min= 0 Add'l USCDI to profile
   - Map USDCI element to `.collected[x]`
1. Sep 10th CGP Call
   - Add `Specimen.collection.method` min = 0 *Additional USCDI*  to profile
   - Map USDCI Specimen Collection Method to `Specimen.collection.method`
   - Terminology
       - concepts TBD (review with Gay and Riki)
       - *preferred* binding
       - VSAC


---

## Appendix

### Prior Art

NA

### Gap Analysis: HL7 v2 Table 0488 vs US Core Specimen Collection Method

The only published ConceptMap I found that maps V2 table 0488 to SNOMED CT is in the HL7 V2-to-FHIR IG, and its SNOMED coverage is minimal.

#### Draft Gap Analysis

Created by Claude (***unverified***)

<!-- **Source:** `http://terminology.hl7.org/CodeSystem/v2-0488` (specimenCollectionMethod, version 3.0.0)
from `.claude/config/v20488-codesystem.yml` -- 42 concepts, all active, none deprecated.

**Target:** `http://hl7.org/fhir/us/core/ValueSet/us-core-specimen-collection-method`
from `input/resources-yaml/ValueSet-us-core-specimen-collection-method.yml`.

The target value set is intensional (SNOMED CT `is-a 17636008 |Specimen collection|`
plus enumerated additions), so the comparison uses the built expansion in
`output/ValueSet-us-core-specimen-collection-method.html` -- 211 concepts,
SNOMED CT United States edition 01-Sep-2025.

Direction convention throughout: **source = v2-0488**, **target = US Core Specimen Collection Method**. -->

#### Summary

| Measure | Count |
|---|---|
| v2-0488 concepts | 42 |
| Fully covered (`equivalent`) | 10 |
| **Gaps (no equivalent target)** | **32** |
| -- partially covered by a broader target (`source-is-narrower-than-target`) | 13 |
| -- partially covered by a narrower or oblique target (`source-is-broader-than-target`) | 3 |
| -- `related-to` only | 12 |
| -- no candidate target at all | 4 |

#### Table 1 -- Gaps

v2-0488 concepts with no equivalent concept in the US Core value set.

| # | v2 code | v2 display | Nature of the gap | Closest concept in the value set |
|---|---|---|---|---|
| 1 | PNA | Arterial puncture | Value set has no generic "arterial puncture"; only the lab-collection concept and three named arteries | 32564009 Arterial specimen collection for laboratory test |
| 2 | BCAE | Blood Culture, Aerobic Bottle | Container and atmosphere distinction (aerobic bottle) not represented | 30088009 Blood culture |
| 3 | BCAN | Blood Culture, Anaerobic Bottle | Container and atmosphere distinction not represented | 30088009 Blood culture |
| 4 | BCPD | Blood Culture, Pediatric Bottle | Pediatric bottle distinction not represented | 30088009 Blood culture |
| 5 | CATH | Catheterized | v2 code is site-agnostic; value set has only site- and device-specific catheter collection concepts | 705156009 Collection of urine via straight catheter |
| 6 | EPLA | Environmental, Plate | No environmental (non-patient) specimen collection concept in the value set | 441378005 Collection of specimen by culture plate |
| 7 | ESWA | Environmental, Swab | No environmental (non-patient) specimen collection concept | 285570007 Taking of swab |
| 8 | CVP | Line, CVP | No central-venous-pressure-line collection concept | 243763007 Venous sampling catheter procedure |
| 9 | MARTL | Martin-Lewis Agar | Named culture medium not represented | 441378005 Collection of specimen by culture plate |
| 10 | ML11 | Mod. Martin-Lewis Agar | Named culture medium not represented | 441378005 Collection of specimen by culture plate |
| 11 | PACE | Pace, Gen-Probe | Proprietary collection and transport kit not represented | 439599008 Collection of specimen by device |
| 12 | MLP | Plate, Martin-Lewis | Named plate medium not represented | 441378005 Collection of specimen by culture plate |
| 13 | NYP | Plate, New York City | Named plate medium not represented | 441378005 Collection of specimen by culture plate |
| 14 | TMP | Plate, Thayer-Martin | Named plate medium not represented | 441378005 Collection of specimen by culture plate |
| 15 | ANP | Plates, Anaerobic | Plate form is lost; only the general anaerobic microbiology collection concept exists | 83917009 Specimen collection for microbiology, anaerobic |
| 16 | BAP | Plates, Blood Agar | Named plate medium not represented | 441378005 Collection of specimen by culture plate |
| 17 | PRIME | Pump Prime | Priming-fluid sample not represented | 243780006 Blood sampling from cardiopulmonary bypass circuit |
| 18 | PUMP | Pump Specimen | Generic "pump" sample not represented; value set names specific circuits | 243780006 Blood sampling from cardiopulmonary bypass circuit |
| 19 | QC5 | Quality Control For Micro | **No candidate.** Not a specimen collection method; quality control material has no analogue | -- |
| 20 | SCLP | Scalp, Fetal Vein | **No candidate.** No fetal scalp blood sampling concept in the expansion | -- |
| 21 | SHA | Shaving | No shave-biopsy or shaving collection concept (hair cutting and nail clipping exist but are different acts) | 240977001 Biopsy of skin |
| 22 | SWD | Swab, Dacron tipped | Swab tip material not represented | 285570007 Taking of swab |
| 23 | WOOD | Swab, Wooden Shaft | Swab shaft material not represented | 285570007 Taking of swab |
| 24 | TMOT | Transport Media, | No transport-medium concepts at all in the value set | 439599008 Collection of specimen by device |
| 25 | TMAN | Transport Media, Anaerobic | No anaerobic transport medium concept | 83917009 Specimen collection for microbiology, anaerobic |
| 26 | TMCH | Transport Media, Chalamydia [sic] | No chlamydia transport medium concept | 285586000 Taking swab for Chlamydia test |
| 27 | TMM4 | Transport Media, M4 | **No candidate.** Proprietary medium | -- |
| 28 | TMMY | Transport Media, Mycoplasma | No mycoplasma transport medium concept | 439599008 Collection of specimen by device |
| 29 | TMPV | Transport Media, PVA | **No candidate.** Polyvinyl alcohol fixative not represented | -- |
| 30 | TMSC | Transport Media, Stool Culture | No stool transport medium concept | 225105004 Collection of stool specimen |
| 31 | TMUP | Transport Media, Ureaplasma | No ureaplasma transport medium concept | 439599008 Collection of specimen by device |
| 32 | TMVI | Transport Media, Viral | No viral transport medium concept | 439599008 Collection of specimen by device |

Three themes account for most of the gaps:

- **Culture media and plates:** MARTL, ML11, MLP, NYP, TMP, ANP, BAP
- **Transport media:** TMOT, TMAN, TMCH, TMM4, TMMY, TMPV, TMSC, TMUP, TMVI
- **Container and device attributes:** BCAE, BCAN, BCPD, SWD, WOOD

These are properties of the container or the medium rather than of the collection act,
which is why the SNOMED CT procedure hierarchy does not carry them. In FHIR they align
more closely with `Specimen.container.type` and `Specimen.processing` than with
`Specimen.collection.method`.

#### Table 2 -- Mappings

| v2 code | v2 display | Target code | Target display | Relationship |
|---|---|---|---|---|
| FNA | Aspiration, Fine Needle | 48635004 | Fine needle biopsy | equivalent |
| PNA | Arterial puncture | 32564009 | Arterial specimen collection for laboratory test | source-is-narrower-than-target |
| BIO | Biopsy | 86273004 | Biopsy | equivalent |
| BCAE | Blood Culture, Aerobic Bottle | 30088009 | Blood culture | source-is-narrower-than-target |
| BCAN | Blood Culture, Anaerobic Bottle | 30088009 | Blood culture | source-is-narrower-than-target |
| BCPD | Blood Culture, Pediatric Bottle | 30088009 | Blood culture | source-is-narrower-than-target |
| CAP | Capillary Specimen | 1048003 | Capillary specimen collection | equivalent |
| CATH | Catheterized | 705156009 | Collection of urine via straight catheter | source-is-broader-than-target |
| EPLA | Environmental, Plate | 441378005 | Collection of specimen by culture plate | related-to |
| ESWA | Environmental, Swab | 285570007 | Taking of swab | related-to |
| LNA | Line, Arterial | 699873000 | Collection of blood via arterial catheter | equivalent |
| CVP | Line, CVP | 243763007 | Venous sampling catheter procedure | source-is-narrower-than-target |
| LNV | Line, Venous | 243763007 | Venous sampling catheter procedure | equivalent |
| MARTL | Martin-Lewis Agar | 441378005 | Collection of specimen by culture plate | source-is-narrower-than-target |
| ML11 | Mod. Martin-Lewis Agar | 441378005 | Collection of specimen by culture plate | source-is-narrower-than-target |
| PACE | Pace, Gen-Probe | 439599008 | Collection of specimen by device | related-to |
| PIN | Pinworm Prep | 21217000 | Collection of pinworm specimen | equivalent |
| KOFFP | Plate, Cough | 709500005 | Collection of specimen by cough culture plate | equivalent |
| MLP | Plate, Martin-Lewis | 441378005 | Collection of specimen by culture plate | source-is-narrower-than-target |
| NYP | Plate, New York City | 441378005 | Collection of specimen by culture plate | source-is-narrower-than-target |
| TMP | Plate, Thayer-Martin | 441378005 | Collection of specimen by culture plate | source-is-narrower-than-target |
| ANP | Plates, Anaerobic | 83917009 | Specimen collection for microbiology, anaerobic | source-is-narrower-than-target |
| BAP | Plates, Blood Agar | 441378005 | Collection of specimen by culture plate | source-is-narrower-than-target |
| PRIME | Pump Prime | 243780006 | Blood sampling from cardiopulmonary bypass circuit | related-to |
| PUMP | Pump Specimen | 243780006 | Blood sampling from cardiopulmonary bypass circuit | source-is-broader-than-target |
| QC5 | Quality Control For Micro | -- | *(no candidate)* | -- |
| SCLP | Scalp, Fetal Vein | -- | *(no candidate)* | -- |
| SCRAPS | Scrapings | 56757003 | Scraping | equivalent |
| SHA | Shaving | 240977001 | Biopsy of skin | related-to |
| SWA | Swab | 285570007 | Taking of swab | equivalent |
| SWD | Swab, Dacron tipped | 285570007 | Taking of swab | source-is-narrower-than-target |
| WOOD | Swab, Wooden Shaft | 285570007 | Taking of swab | source-is-narrower-than-target |
| TMOT | Transport Media, | 439599008 | Collection of specimen by device | related-to |
| TMAN | Transport Media, Anaerobic | 83917009 | Specimen collection for microbiology, anaerobic | related-to |
| TMCH | Transport Media, Chalamydia | 285586000 | Taking swab for Chlamydia test | related-to |
| TMM4 | Transport Media, M4 | -- | *(no candidate)* | -- |
| TMMY | Transport Media, Mycoplasma | 439599008 | Collection of specimen by device | related-to |
| TMPV | Transport Media, PVA | -- | *(no candidate)* | -- |
| TMSC | Transport Media, Stool Culture | 225105004 | Collection of stool specimen | related-to |
| TMUP | Transport Media, Ureaplasma | 439599008 | Collection of specimen by device | related-to |
| TMVI | Transport Media, Viral | 439599008 | Collection of specimen by device | related-to |
| VENIP | Venipuncture | 28520004 | Venipuncture for blood test | equivalent |



---

<!-- appended-from: laboratory-draft.md -->


### Summary of USCDI Comments:

*This content was developed with the assistance of Claude.*

| Position | Organizations | Reasons |
|---|---|---|
| **OPPOSE** | *(no outright opposition to Specimen Collection Method)* | — |
| **OPPOSE / REDESIGN** | TMA (state physician society) | Defer until vocabulary specified |
| **MIXED / OPPOSE** | ACLA (clinical lab trade association) | Often not provided by ordering provider; presumable from ordered item; not supported in certified HIT; adds burden |
| **SUPPORT / with CHANGES** | SNOMED International (SDO), HL7 (SDO), SHIELD (lab data standards coalition), APHL (public health labs), CSTE (state epidemiologists), Altarum Institute (research org), FAH (hospital trade association), TDH-OIA (state public health) | Specify SNOMED CT procedure hierarchy; clarify level of detail; CSTE wants additional CLIA elements |
| **SUPPORT** | Epic (EHR vendor), Oracle Health (EHR vendor), Regenstrief Institute (research/informatics) | Clinically valuable; widely captured today; SNOMED CT/FHIR R4 ready |

For a complete summary of the comments, see the Appendix below:


### Laboratory data class — Comment Position Summary

**Class additions and updates in v7:**
- **Specimen Collection Method** (new) — technique or procedure used to obtain a specimen.
- **Specimen Condition** (existing element renamed from "Specimen Condition Acceptability").

**Several commenters also propose adding** Laboratory Test Performed Date/Time, Specimen Received Date/Time, and Laboratory Results Date/Time to v7, and renaming Laboratory Order to "Ordered Laboratory Test" — these are summarized after the v7 addition.

| Position | Organizations | Reasons |
|---|---|---|
| **OPPOSE** | *(no outright opposition to Specimen Collection Method)* | — |
| **OPPOSE / REDESIGN** | TMA (state physician society) | Defer until vocabulary specified |
| **MIXED / OPPOSE** | ACLA (clinical lab trade association) | Often not provided by ordering provider; presumable from ordered item; not supported in certified HIT; adds burden |
| **SUPPORT / with CHANGES** | SNOMED International (SDO), HL7 (SDO), SHIELD (lab data standards coalition), APHL (public health labs), CSTE (state epidemiologists), Altarum Institute (research org), FAH (hospital trade association), TDH-OIA (state public health) | Specify SNOMED CT procedure hierarchy; clarify level of detail; CSTE wants additional CLIA elements |
| **SUPPORT** | Epic (EHR vendor), Oracle Health (EHR vendor), Regenstrief Institute (research/informatics) | Clinically valuable; widely captured today; SNOMED CT/FHIR R4 ready |

**Comments grouped by position:**

**Strongly supportive (Specimen Collection Method)**
- **Epic** [EHR vendor] — Supports the addition. Clinically valuable and widely captured and exchanged today. Brief, unqualified support.
- **Oracle Health** [EHR vendor] — Supports the inclusion. Recommends USCDI include SNOMED as the applicable vocabulary standard, citing the FHIR R4 ValueSet-specimen-collection-method as an example set.
- **Regenstrief Institute** [research/informatics institute] — Supports inclusion. Notes no vocabulary specified in draft; SNOMED CT procedure hierarchy would be appropriate. Strongly aligned with SHIELD priorities — collection method critical for lab result interpretation and ELR.

**Supportive with refinements (Specimen Collection Method)**
- **SNOMED International** [SDO — terminology] — Recommends ONC designate SNOMED CT U.S. Edition as recommended or required vocabulary standard for the element. SNOMED CT procedure hierarchy includes precise concepts: 28520004 |Venipuncture (procedure)|, 14766002 |Biopsy (procedure)|, 447339001 |Aspiration of fluid (procedure)|, 257261003 |Swab (specimen)|. Standardized coding is essential because the collection method directly affects analyte stability, reference ranges, and result validity. Notes the established LOINC–SNOMED CT complementarity model already used across USCDI (LOINC for Laboratory Order and Results, SNOMED CT for Specimen Type and now Collection Method); cites SNOMED International–Regenstrief formal collaboration on laboratory terminology harmonization. SNOMED CT is referenced for specimen type and collection method coding in HL7 FHIR US Core Laboratory profiles, the FHIR artifacts through which USCDI laboratory data will be exchanged under ONC certification.
- **HL7** [SDO] — Observes that the element supports the need for detail around the specimen when not included in the precoordinated specimen type element — the laboratory does not need the full detail of the collection procedure. Recommends USCDI v7 use the same vocabulary as for the procedure (SNOMED CT from the procedure hierarchy), to allow for post-coordination with the specimentype element, which also uses SNOMED CT.
- **SHIELD (Riki Merrick)** [lab/diagnostic data standards coalition] — Supports inclusion; provides detail around the specimen when not included in the precoordinated specimen type element. Recommends SNOMED CT from the procedure hierarchy for post-coordination with specimentype.
- **APHL (Association of Public Health Laboratories)** [public health labs trade association] — Supports inclusion as providing additional detail not available in the existing Specimen Type element, even when Specimen Type uses pre-coordinated concepts. Recommends ONC consider using the same vocabulary used to describe procedures, specifically SNOMED CT from the procedure hierarchy.
- **CSTE (Council of State and Territorial Epidemiologists)** [state public health surveillance] — Supports inclusion of Specimen Collection Method. Frames it as part of a broader recommendation: collection of more granular laboratory data is critical for case adjudication, patient deduplication, and linking ELR data to cases. CSTE's coordinated comments (filed across all laboratory date/time and identifier elements) recommend ONC also add: name of testing/performing laboratory and CLIA identifier (HIGH PRIORITY), name of ordering provider/submitter, address of testing/performing laboratory, accession number at testing laboratory (HIGH PRIORITY for matching), date the test was ordered, date the test was performed (reconcile with results date/timestamp), specimen collection date and time (HIGH PRIORITY), test result value with units/reference range/interpretation (HIGH PRIORITY), abnormal flag (HIGH PRIORITY), and test kit identifier. Argues dates and times are critical for evaluating timeliness of public-health reporting and currently sparse in practice.
- **Altarum Institute** [health-services research org] — Flags Specimen Collection Method as a "significant gap" — missing vocabulary will result in inconsistent coded representation across LIS and public health ELR destinations. Cites Altarum's engineers who implemented HL7 v2 and FHIR-based laboratory interfaces from individual hospitals to national health systems: the distinction between a **nasopharyngeal swab and an anterior nares swab affects the sensitivity profile of respiratory pathogen tests**. Without standardized vocabulary, receiving public health systems cannot reliably interpret or validate specimen data. Also lists Specimen Collection Method among elements without vocabulary standards (alongside Adverse Event Outcome, Allergy Intolerance Criticality, Appointment, Healthcare Agent) creating moderate risk of inconsistent implementation.
- **Federation of American Hospitals / FAH** [hospital trade association] — Recommends ONC provide clarification on the expected level of detail and applicable vocabulary standards to reduce variability in representation.
- **Texas Department of Health (jessilott / TDH-OIA)** [state public health agency] — Supports inclusion. Recommends ASTP/ONC clearly document all associated standards and value sets to ensure consistent implementation and interoperability.

**Mixed / oppose (Specimen Collection Method)**
- **American Clinical Laboratory Association / ACLA** [clinical laboratory trade association] — The most cautionary voice. Notes Specimen Collection Method is **not always received from the ordering provider** and could be provided when available but not required. Many collection methods can be presumed based on the ordered item — for example, blood tests are commonly obtained using venipuncture. **The data element is not supported in certified HIT today.** Adding it as a required element may add burden to the ordering provider. ACLA's framing positions Specimen Collection Method as something that should be opportunistically captured rather than required.

**Oppose / redesign (Specimen Collection Method)**
- **TMA (Texas Medical Association)** [state physician professional society] — Lists Specimen Collection Method among 15 elements ONC should not adopt until each has a correlating vocabulary standard.

**Other Laboratory class commentary (not Specimen Collection Method):**

- **Specimen Condition** (existing element renamed): **HL7**, **SHIELD**, **APHL**, and **Oracle Health** all support the rename from "Specimen Condition Acceptability" to "Specimen Condition." HL7 and APHL note the renamed term clarifies the element applies to the specimen (and container) regardless of which test is to be performed; affects result interpretation; can also describe the reason a specific test is not performed. Oracle notes the updated definition aligns with FHIR US Core.

- **Laboratory Order** (existing element — coordinated rename request): **HL7**, **SHIELD**, **APHL**, and **CSTE** all recommend ONC rename Laboratory Order to "**Ordered Laboratory Test**" with the definition: "The name and code, ideally as defined by the performing laboratory, for the provider requested test." Argument: the current Laboratory Order element doesn't sufficiently narrow scope, since CLIA's Test Request (42 CFR 493.1241) requires multiple data elements beyond just the test identifier. The proposed rename narrows scope to the test-identification component. HL7 also recommends including a LOINC code with this element. SHIELD lays out the full mapping of CLIA Test Request requirements to existing USCDI elements (Care Team Member Name/Location/Telecom, Patient name/identifier/sex/DOB) plus this one being the test identifier itself.

- **Laboratory Test Performed Date/Time** (proposed promotion from Level 0): **HL7**, **APHL**, **CSTE**, and **Wolters Kluwer** all recommend ONC add this as a USCDI v7 element. Proposed definition: "Date (and optionally time) when the instrument or technologist (for manual testing) generated the result." APHL proposes the usage note to disambiguate from the existing Performance Date/Time. APHL provides extensive use cases: re-analyzing samples (genetics), internal QA, understanding relationships between tests at different institutions, blood transfusion cross-match timing (within 72 hours), CT-with-contrast scheduling needing kidney function results first, stroke or heart attack protocol adherence, and pharmacy needing current kidney function before drug administration. APHL is "confident that most EHRs already track and have the capability to send" this element.

- **Laboratory Test Result Released Date/Time** (HL7's second proposed addition): HL7 recommends adding this element with the definition: "Date (and optionally time) when the result was verified and released by the testing laboratory." Usage note: "This would be the date/time when the results are verified in the LIS and available for exchange."

- **Specimen Received Date/Time** (proposed promotion from Level 0): **APHL** recommends elevating this Level 0 element to USCDI with the definition "The date/time when the testing laboratory received the specimen." Use cases: (1) notification that a specimen is in the lab, supporting both patient treatment and lab workflow (urgent tests, avoiding re-orders, add-on tests); (2) evaluating specimen acceptability and medicolegal chronology; (3) **CLIA-required at 42 CFR 493.1242(b)**; (4) determining turnaround time for lab testing; (5) used by public health as a proxy for clinical temporal context when specimen collection date/time is not provided.

- **Laboratory Results: Date and Timestamps** (Wolters Kluwer's proposed addition): WK recommends adding this element alongside Vital Sign Results: Date and Timestamps and Laboratory Test Performed Date.

- **Specimen Collection Date/Time** (currently Level 0 — significant push to elevate): **CDC**, **CSTE**, **TDH-OIA (jessilott)**, and **minigrrl** all advocate for promotion to USCDI v7. CDC frames it as critical for NHSN measure logic and time-based quality measure evaluation. TDH-OIA notes the element is used by over 3,000 public health agencies, has been tested at scale between multiple production environments, and is required for reporting reportable lab results from hospitals to public health. **minigrrl** specifically protests what they characterize as the **demotion** of Specimen Collection Date/Time (alongside other Case Reporting elements like Patient Birth Place, Tribal Enrollment, Pregnancy elements, Work Information, SDOH Housing Instability, and others) — arguing 21 certified EHR products exchange these elements via electronic Case Reporting (eCR) specifications today, which "typically supports promotion, not demotion, within the USCDI maturity model." minigrrl urges ONC to either reverse the decision or publish a detailed, evidence-based rationale.

**Summary of Comments:** The Laboratory data class has the deepest and most coordinated public-health voice in the v7 comment record. **Specimen Collection Method** itself is broadly supported with a clean vocabulary consensus — every voice that recommends a vocabulary (SNOMED International [SDO], HL7 [SDO], SHIELD [lab data standards coalition], APHL [public health labs trade association], Oracle Health [EHR vendor], Regenstrief [research/informatics institute]) recommends the **same answer: SNOMED CT from the procedure hierarchy**, with concrete codes (28520004 Venipuncture, 14766002 Biopsy, 447339001 Aspiration, 257261003 Swab). This is the most unanimous vocabulary recommendation across any v7 element reviewed so far. The only mixed voice is **ACLA** [clinical laboratory trade association], whose concern is operational rather than structural: collection method information often isn't received from the ordering provider, can be presumed from the test ordered (venipuncture for blood draws), and is not supported in certified HIT today. ACLA's caution is consistent with their narrower v7 letter pattern of flagging operational realism on lab-side workflows. Altarum [research org] provides the most clinically grounded justification for vocabulary mandate: the distinction between a nasopharyngeal swab and an anterior nares swab measurably affects respiratory pathogen test sensitivity, so without standardized vocabulary, receiving public health systems can't reliably interpret results. **Beyond the v7 addition itself, the more consequential pattern in the Laboratory class commentary is the coordinated set of additional changes** that public-health and standards voices are jointly requesting. Four organizations (HL7, APHL, CSTE, Wolters Kluwer) recommend adding **Laboratory Test Performed Date/Time** to v7. APHL recommends adding **Specimen Received Date/Time**, citing CLIA 42 CFR 493.1242(b). Four organizations (HL7, SHIELD, APHL, CSTE) jointly recommend renaming **Laboratory Order to "Ordered Laboratory Test"** with a tightened definition aligned to CLIA's Test Request structure. The rename suggestions and additions cluster around a shared intent: align USCDI's Laboratory class more precisely with CLIA's regulatory framework (42 CFR 493.1241 Test Request, 493.1242 Specimen Submission, 493.1291 Test Report) so that USCDI elements correspond cleanly to lab-side regulatory requirements and downstream electronic laboratory reporting (ELR) workflows. **CSTE's** [state epidemiologists] more comprehensive recommended additions — name and CLIA identifier of testing laboratory, name of ordering provider/submitter, accession number, abnormal flag, test kit identifier — point to USCDI's continuing gap with the public health surveillance use case. **minigrrl's protest of the demotion of Specimen Collection Date/Time** (and 19 other Case Reporting elements) is the most pointed individual challenge to ONC's USCDI-leveling process in the comment record: 21 certified EHR products exchange these elements via eCR today, which by USCDI's own maturity criteria should support promotion, not demotion.

**Notably absent:** AHA, AHIP, AMA, AMIA, ANI, AAAAI, AQIPS, NCQA, WEDI, MEDITECH, Allina Health, Emory Healthcare, UI Health, Providence Health, FDA, AHIMA, CARIN Alliance, PACIO, NCPDP, Vega Health, and Vizient are silent on the Laboratory class additions despite filing v7 letters. The absence of CLIA-regulated stakeholders beyond ACLA — particularly hospital laboratory associations and reference lab networks — is striking given the depth of CLIA-alignment recommendations from public-health and standards voices. The complete absence of patient advocacy is consistent with a class focused on technical lab workflows rather than patient-facing concerns. AHIP's silence is notable given Laboratory Test Performed Date/Time and Specimen Received Date/Time both have potential implications for prior-authorization timelines under CMS-0057-F.

