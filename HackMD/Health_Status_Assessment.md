
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

## Health Status Assessments: Updated Guidance and Terminology


<!-- image of summary of changes-->
![image](https://hackmd.io/_uploads/ryWnq2JP-g.png)

![image](https://hackmd.io/_uploads/rJwMGakP-l.png)

<!-- **:new: Definition :point_down:** -->

![image](https://hackmd.io/_uploads/rJYAqhJw-x.png)

<!-- markdown table summary of proposal use adobe to convert to excel and then script to markdown or just copy/paste -->

DATA ELEMENT|<br/>Standards listed are required.<br/>If more than one is listed,<br/> at least one is required unless<br/>otherwise noted.<br/>Standards versions represent the most recent <br/>available at time of publication.</center>|US Core V10 Proposal
---|---|---
| **Nutrition Assessment ➕**<br>Assessment of a person's dietary intake.  | •  Logical Observation Identifiers Names and Codes (LOINC) version 2.81 | Add terminology to Screening and Assessments guidance page.
| **Tobacco Use**<br>Assessment of a patient's tobacco product use behaviors. Tobacco products may include smokeless tobacco, cigarette tobacco, cigars, pipe tobacco, waterpipes (or hookah), nicotine pouches, nicotine gum, e-cigarettes, and other electronic nicotine delivery systems.<br>Examples include but are not limited to duration and frequency of use, mode of consumption, and type of product used. | • Logical Observation Identifiers Names and Codes (LOINC) version 2.81<br>• SNOMED Clinical Terms (SNOMED CT) U.S. Edition, September 2025 Release | **Possible** rename from "*US Core Core Smoking Status Observation Profile*" to "*US Core Tobacco Use Observation Profile*".

➕ In USCDI+

### CCDA Design Notes

### Issues

1.  Nutrition Assessment has a functional overlap with:
    -  SDOH
    -  US Core Vitals profiles (obesity, wt loss)

### Proposals

1. Nutrition Assessment Data Element aligns with clinical judgement guidance in Screening and Assessments guidance page.
   - Category code = 75305-3 Nutrition status
   - Results values from SNOMED CT (SNOMED CT code '238131007' = 'Overweight (finding)' and '238136002' = 'Morbid obesity (disorder)')
1. **Possible** rename from "*US Core Core Smoking Status Observation Profile*" to "*US Core Tobacco Use Observation Profile*".
    - Review terminology
    - Add guidance on usage for different products and modes of consumption. 


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


