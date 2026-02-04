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

# (Way Too Early) US Core V10 Design

- [Introduction](#)
- [Summary of Design Decisions](#)

## References

- [*DRAFT* ASTP USCDI website](https://isp.healthit.gov/united-states-core-data-interoperability-uscdi#draft-uscdi-v7)
- [*DRAFT* ASTP USCDI v6 PDF](https://isp.healthit.gov/sites/default/files/2026-01/Draft-USCDI-Version-7-January-2026.pdf)
- [Draft United States Core Data for Interoperability Version 7 Standard Bulletin](https://healthit.gov/standards-and-technology/onc-standards-bulletin/onc-standards-bulletin-2026-1/)

## US Core Design Principles

- [US Core Design](/r-VtK_20Rw25Vf81p5Lyvg#Design-Principles)

## US Core Strawman Proposals

**List of detailed strawman proposals by USCDI Data Class/Element**

:slightly_smiling_face: = Low LOE: USCDI Data Elements are already represented in US Core v9 as Must Support and require little or no changes or guidance.

:thinking_face: = Medium LOE: USCDI Data Elements require some interpretation and probably new elements to US Core Profiles with additional guidance

:exploding_head: = High LOE: USCDI Data Elements require interpretation and probably new US Core profiles

1. [Adverse Events](/CKyBxeRYQJ6SrkYPj3zUbw) (NEW DATA CLASS) :exploding_head: 
2. [Allergies and Intolerances](/ziEuzkenRnqZ55h7L7vV_Q):thinking_face:
3. [Healthcare Agent](/5VanJRHKQ12dIPtS-16hWQ) :exploding_head:
4. [Referral Note](/5YMuiYySSzmhFSymS2PHnA) :slightly_smiling_face:
5. [Diagnostic Imaging Reference](/CNYwm7OsQ7S4EBxct2yvkg) :exploding_head:
6. [Appointment](/5VD6Yd4WQ5m929CrY7X3jw) :thinking_face:
7. [Facility Information](/osTHZxJpRveYPTwpDQDmVg) :slightly_smiling_face:
8. [Healthcare Information Attributes](/uwyK8MoTReG1ev02XIY-lA) (NEW DATA CLASS)]  :thinking_face:
9. [Health Insurance Information](/fTF4vhmGTneSxejvpdOuBA) :slightly_smiling_face:
10. [Health Status Assessment](/_s1WbP-9SxGOEt8IcST0Ow) :thinking_face:
11. [Immunizations](/mcuKzClMQYCtWyODyfLJdQ) :slightly_smiling_face:
12. [Laboratory](/38xa1BZ7TjaPMao6LJHuCA) :thinking_face:
13. [Medical Devices](/Q7IK0ASkRVWrJQF4t3zJTQ) :slightly_smiling_face:
14. [Medications](/2654oTa6R7CNK1T-CsKvdQ) :exploding_head:
15. [Orders](/2c5wMyJaSRORwN5F-F5CAQ) :exploding_head:  :exploding_head:
16. [Patient Demographics/Information](/VoQgkVxsQsKmBRei3Oxi4Q)  :thinking_face:
17. [Problems](/nsjWBx5WQlKQHua_xKhLEQ) :slightly_smiling_face:
18. [Procedures](/TLixyzIBRs6Wz_ulqrWUzA) :slightly_smiling_face:

## TODOS

- [Review of Other Draft USCDI v7 Changes](https://healthit.gov/standards-and-technology/onc-standards-bulletin/onc-standards-bulletin-2026-1#h-other-draft-uscdi-v7-changes)
