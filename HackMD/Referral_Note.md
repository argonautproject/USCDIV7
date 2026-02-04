
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

## Referral Note: Add note type code to Clinical Notes Guidances and US Core DocumentReference Profile


<!-- image of summary of changes-->
Referral Order represents a provider-authored request to another provider, specialist, or organization for care services, such as a referral order from a primary care provider to a wound care specialist or podiatrist. **Referral Note** provides a narrative summary that may include the reason for referral, relevant patient history, and requested services or questions to support continuity and coordination of care between providers. Together, these data elements create a more complete referral workflow, ensuring that receiving providers have both the structured order information and the clinical context necessary to deliver appropriate care. The interoperable exchange of referral orders and notes reduces redundant communication, supports care coordination across specialties and organizations, and helps ensure that patients receive timely access to needed specialty services.

<!-- **:new: Definition :point_down:** -->

![image](https://hackmd.io/_uploads/HkjVEoALbg.png)

<!-- markdown table summary of proposal use adobe to convert to excel and then script to markdown or just copy/paste -->

<!-- ➕ In USCDI+ -->

DATA ELEMENT|<br/>Standards listed are required.<br/>If more than one is listed,<br/> at least one is required unless<br/>otherwise noted.<br/>Standards versions represent the most recent <br/>available at time of publication.</center>|US Core V10 Proposal
---|---|---
| **Referral Note**<br>Narrative summary requesting an opinion, advice, or service from a clinician.<br>Examples include but are not limited to primary care referral to dermatology, dentistry, and acupuncture. | • Logical Observation Identifiers Names and Codes (LOINC) version 2.81<br>• At minimum: Referral note (LOINC code 57133-1) | Add Referral note (LOINC code 57133-1) to US Core's [“Common Clinical Notes” list](https://build.fhir.org/ig/HL7/US-Core/clinical-notes.html#clinical-notes)|

### CCDA Design Notes

### Issues

### Proposal

1.  Add Referral note to the minimum US Core Clinical Note Type Valueset and Clinical Notes Page documentation.

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


