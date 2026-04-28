
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

## Health Insurance Information: No Changes to Profile


<!-- image of summary of changes-->
*No narrative summary of changes for Health Insurance Data Elements in the ASTP/ONC Standards Bulletin 2026-1.*

<!-- **:new: Definition :point_down:** -->

![image](https://hackmd.io/_uploads/HJihwc0Ibe.png)

<!-- markdown table summary of proposal use adobe to convert to excel and then script to markdown or just copy/paste -->

DATA ELEMENT|<br/>Standards listed are required.<br/>If more than one is listed,<br/> at least one is required unless<br/>otherwise noted.<br/>Standards versions represent the most recent <br/>available at time of publication.</center>|US Core V10 Proposal
---|---|---
**Health Insurance Coverage Period ➕**<br />The time frame in which the policy is in force.||**No Change**: `Coverage.period` is already a US Core *Must Support* element|
| **Health Insurance Payer**<br>Issuer of the policy. | | **No Change**: `Coverage.payor` is already a  US Core *Must Support* element|
| **Health Insurance Plan ➕**<br>Health insurance offering or package. |  | **No Change**:`Coverage.class:plan` is already a  US Core *Must Support* element|
| **Health Insurance Plan Identifier ➕**<br>Sequence of characters used to uniquely refer to an insurance plan. |  |**No Change**: `Coverage.class:plan.value` and `Coverage.class:plan.name` already are US Core *Must Support* elements|

➕ In USCDI+

### CCDA Design Notes

### Issues

### Proposal

1.  No Changes to US Core Coverage Profile nor additional guidance needed.

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


