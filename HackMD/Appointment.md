
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

## Appointments: Update to US Core Encounter Profile


<!-- image of summary of changes-->
![image](https://hackmd.io/_uploads/BJkQsqywbg.png)


<!-- **:new: Definition :point_down:** -->

![image](https://hackmd.io/_uploads/HyjUo9yvWl.png)

<!-- markdown table summary of proposal use adobe to convert to excel and then script to markdown or just copy/paste -->

<!-- ➕ In USCDI+ -->

DATA ELEMENT|<br/>Standards listed are required.<br/>If more than one is listed,<br/> at least one is required unless<br/>otherwise noted.<br/>Standards versions represent the most recent <br/>available at time of publication.</center>|US Core V10 Proposal
---|---|---
| **Appointment**<br>A planned healthcare event for a future date/time.<br>Usage note: Created, tracked and managed for planned participation. An appointment may be called a future encounter and may result in one or more Encounters. |  | Add `Encounter.appointment` as a min = 0 *Additional USCDI* element to the US Core Encounter Profile |


### CCDA Design Notes

### Issues :thinking_face:

1. Do we need to support a :new: US Core Appointment/Slot Profiles?
2. In the USCDI Usage notes, is  ***"An appointment may be called a future encounter..."*** relevant and an important consideration in our design?


### Proposal

1.  Add `Encounter.appointment` as a min = 0 *Additional USCDI* element to the US Core Encounter Profile to support links to the appointment that scheduled the encounter.

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
- Argonaut/IHE Scheduling



