
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

## Orders: New Profiles Needed


<!-- image of summary of changes-->

![image](https://hackmd.io/_uploads/HkKiY1lPbe.png)
![image](https://hackmd.io/_uploads/rJeR3F1ePbx.png)
![image](https://hackmd.io/_uploads/SJx5KkxDWe.png)

<!-- **:new: Definition :point_down:** -->

![image](https://hackmd.io/_uploads/ry8J9kgvbl.png)


<!-- markdown table summary of proposal use adobe to convert to excel and then script to markdown or just copy/paste -->

DATA ELEMENT|<br/>Standards listed are required.<br/>If more than one is listed,<br/> at least one is required unless<br/>otherwise noted.<br/>Standards versions represent the most recent <br/>available at time of publication.</center>|US Core V10 Proposal
---|---|---
| **Medical Device Order ➕**<br>Provider-authored request for medical devices.<br>Examples include but are not limited to therapeutic footwear, insulin infusion pump, and continuous positive airway pressure (CPAP) machine. |  | 🆕 US Core DeviceRequest Profile (See Proposal)
| **Nutrition Order ➕**<br>Provider-authored request for therapeutic diet, nutrition support, and nutrition to promote and maintain health.<br>Examples include but are not limited to cardiac diet, Mediterranean diet, whole food diet, clear liquid diet, enteral nutrition, and nutritional<br>supplement. |  |🆕 US Core NutritionOrder Profile (See Proposal)
| **Referral Order**<br>Provider-authored request to another provider, specialist, or organization for care services.<br>Examples include but are not limited to referral<br>orders to a wound care specialist and to a podiatrist. |  | Update guidance in US Core ServiceRequest Profile

➕ In USCDI+

### CCDA Design Notes

### Issues :thinking_face: 

1. DeviceRequest is FMM=1, NutritionOrder is FMM =2 in FHIR R4  (both part of FHIR R6)
2. Implementer Support?
3. Terminology???

### Proposal
1.  🆕 US Core DeviceRequest Profile
     - Mandatory and Must Support elements: Must Support elements: `status, intent (m),code[x] (m), subject (m), authoredOn, requester`  (m = mandatory in base)
     - Search Parameters: patient, status, authored, code
1.  🆕 US Core NutritionOrder Profile
     - Mandatory and Must Support elements: Must Support elements: `status (m), intent (m), patient (m), dateTime (m), orderer, oralDiet.type`  (m = mandatory in base)
     - Search Parameters: patient, status, datetime, type
1.  Update guidance in US Core ServiceRequest Profile
   - Category codes for referrals
   - Additional bindings referrals

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

#### DeviceRequest
- [QI Core](https://packages2.fhir.org/xig/resource/hl7.fhir.us.qicore%7Ccurrent/StructureDefinition/qicore-devicerequest)
- [DME](https://packages2.fhir.org/xig/resource/hl7.fhir.us.dme-orders%7Ccurrent/StructureDefinition/PAOX-devicerequest)
- [PCT](http://hl7.org/fhir/us/davinci-pct/STU2/StructureDefinition-davinci-pct-devicerequest.html)

#### NutritionOrder
- [PACIO]([pfe-nutrition-order](https://packages2.fhir.org/xig/resource/hl7.fhir.us.pacio-pfe%7Ccurrent/StructureDefinition/pfe-nutrition-order))
- [QI Core](https://packages2.fhir.org/xig/resource/hl7.fhir.us.qicore%7Ccurrent/StructureDefinition/qicore-nutritionorder)
- [MCC](https://packages2.fhir.org/xig/resource/hl7.fhir.us.mcc%7Ccurrent/StructureDefinition/MCCNutritionOrder)



