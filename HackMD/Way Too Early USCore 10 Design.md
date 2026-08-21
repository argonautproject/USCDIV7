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

source: https://hackmd.io/@erichaas/SJo4QLYL-g

parallel C-CDA design: 

![argo_small](https://hackmd.io/_uploads/SyiP7bKrR.png)

# US Core V10 Design

- [Introduction](#)
- [Summary of Design Decisions](#)

## References

- [ASTP USCDI website](https://isp.healthit.gov/united-states-core-data-interoperability-uscdi#uscdi-v7)
- [ASTP USCDI V7 PDF](https://isp.healthit.gov/sites/default/files/2026-07/USCDI-Version-7-Standard-Document.pdf)
    - [USCDI v7: Draft (January 2026) vs. Final (July 2026)](/mHqlwgfyTnyIpIqWJADdTg)
- [United States Core Data for Interoperability Version 7 Standard Bulletin](https://healthit.gov/standards-and-technology/onc-standards-bulletin/onc-standards-bulletin-2026-2/)
- [USCDI v7 New Data Elements — USCDI+ Domain and USCDI+ Quality v2 Mapping](/WoGZh1mVRTek92MmpBtwlA)

## US Core Design Principles

- [US Core Design](/r-VtK_20Rw25Vf81p5Lyvg#Design-Principles)

## US Core Strawman Proposals

**List of detailed strawman proposals by USCDI Data Class/Element**


### :exploding_head: = High LOE

USCDI Data Elements require interpretation and probably new US Core profiles


1. [Healthcare Information Attributes](/uwyK8MoTReG1ev02XIY-lA) (NEW DATA CLASS) :exploding_head: :exploding_head: :exploding_head:
   - Previously Community Review on 5/6.  For the Reason Not Performed data element, follow [US Quality Core](https://build.fhir.org/ig/HL7/fhir-us-quality-core/en/) pattern, starting with Immunization, MedicationAdministration, MedicationDispense, Procedure
3. [Adverse Events](/CKyBxeRYQJ6SrkYPj3zUbw) (NEW DATA CLASS) :exploding_head:
   - Previously Community Review on 4/22. **NEW** US Core AdverseEvent Profile based on the [US Quality Core AdverseEvent Profile](https://build.fhir.org/ig/HL7/fhir-us-quality-core/branches/params-table/en/StructureDefinition-us-quality-core-adverseevent.html)  (with exceptions)
8. [Appointment](/5VD6Yd4WQ5m929CrY7X3jw) :exploding_head:
   - Previously Community Review on 5/6. **NEW** US Core Appointment Profile
4. [Diagnostic Imaging Reference](/CNYwm7OsQ7S4EBxct2yvkg) :exploding_head:
   - Previously Community Review on 4/22.  **ADD** DiagnosticReport references to ImagingStudy and Media.
5. [Healthcare Agent](/5VanJRHKQ12dIPtS-16hWQ) :exploding_head:
   - Previously Community Review on 4/22.  **Proposal**: Updated role code for for US Core CareTeam Profile,  Updated relationship codes for US Core RelatedPerson Profile
6. [Medications](/2654oTa6R7CNK1T-CsKvdQ) :exploding_head:
   - Previously Community Review on 5/6. **NEW** US Core MedicationAdministration Profile
7. [Patient Demographics/Information](/VoQgkVxsQsKmBRei3Oxi4Q) :exploding_head:
    - Previously Community Review on 5/6. **REVIEW OPTIONS** US Core Patient Accommodation Extension, US Core Patient Accommodation Flag Profiles US Core Patient Accommodation Observation Profiles, or US Core Simple Observation 
2. [Orders](/2c5wMyJaSRORwN5F-F5CAQ) :exploding_head:
    - Review pending: **NEW** US Core DeviceRequest Profile,  **NEW** US Core NutritionOrder Profile, **UPDATE** US Core ServiceRequest Profile's terminology guidance


### :thinking_face: = Medium LOE

USCDI Data Elements require some interpretation and probably new elements to US Core Profiles with additional guidance
 

9. [Allergies and Intolerances](/ziEuzkenRnqZ55h7L7vV_Q) :thinking_face:
    - Review pending: **Update** US Core AllergyIntolerance Profile
11. [Health Status Assessment](/_s1WbP-9SxGOEt8IcST0Ow) :thinking_face:
    - Review pending: 
        - Nutrition Assessments: **Define** terminology (pending)
        - Tobacco Use: **REVIEW OPTIONS** Overload US Core Core Smoking Status Observation Profile, Replace with **NEW** US Core Tobacco Use Observation Profile, or Switch to Assessments/Observations Framework.
13. [Laboratory](/38xa1BZ7TjaPMao6LJHuCA) :thinking_face:
    - Review pending: **Update** US Core Specimen Profile
14. [Other Draft USCDI v7 Changes](/D5TZacmHQKqkcniD-aT-Ag)
    - Review pending: **Review** Impact of [Other Draft USCDI v7 Changes](https://healthit.gov/standards-and-technology/onc-standards-bulletin/onc-standards-bulletin-2026-1#h-other-draft-uscdi-v7-changes) on US Core


### :slightly_smiling_face: = Low LOE

USCDI Data Elements are already represented in US Core v9 as Must Support and require little or no changes or guidance

15. [Facility Information](/osTHZxJpRveYPTwpDQDmVg) :slightly_smiling_face:
13. [Health Insurance Information](/fTF4vhmGTneSxejvpdOuBA) :slightly_smiling_face:
14. [Immunizations](/mcuKzClMQYCtWyODyfLJdQ) :slightly_smiling_face:
15. [Medical Devices](/Q7IK0ASkRVWrJQF4t3zJTQ) :slightly_smiling_face:
16. [Problems](/nsjWBx5WQlKQHua_xKhLEQ) :slightly_smiling_face:
17. [Procedures](/TLixyzIBRs6Wz_ulqrWUzA) :slightly_smiling_face:
18. [Referral Note](/5YMuiYySSzmhFSymS2PHnA) :slightly_smiling_face:


