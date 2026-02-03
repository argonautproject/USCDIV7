
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

## Diagnostic Imaging Reference: Update US Core DiagnosticReport Profile for Report and Note Exchange Profile


<!-- image of summary of changes-->
![image](https://hackmd.io/_uploads/H1WTz5Jw-g.png)

<!-- **:new: Definition :point_down:** -->

![image](https://hackmd.io/_uploads/SkQem9kwWg.png)

<!-- markdown table summary of proposal use adobe to convert to excel and then script to markdown or just copy/paste -->

➕ In USCDI+

DATA ELEMENT|<br/>Standards listed are required.<br/>If more than one is listed,<br/> at least one is required unless<br/>otherwise noted.<br/>Standards versions represent the most recent <br/>available at time of publication.</center>|US Core V10 Proposal
---|---|---
| **Diagnostic Imaging Reference ➕**<br>The information that can be used to access a diagnostic imaging study.<br>Examples include but are not limited to imaging study endpoint weblink, unique identifiers, and contextual information needed to retrieve a diagnostic imaging study. |  | Add `DiagnosticReport.media.link`,`DiagnosticReport.imagingStudy`, and  `DiagnosticReport.identifier` as min = 0 *Additional USCDI* element to the US Core DiagnosticReport for Report and Note Exchange Profile .|
### CCDA Design Notes

### Issues :thinking_face: 

1.  Does there need to be a US Core ImagingStudy Profile?
2.  Should we scrap Media and use the Cross-version extension to support DocumentReference instead?
3.  How deep do we go into the reference to support the identifiers mentioned in the draft rule?
4.  Add search API requirements?


### Proposal

1.  Add the `DiagnosticReport.media.link` as a min = 0 *Additional USCDI* element to the US Core DiagnosticReport for Report and Note Exchange Profile to support links to various patient-friendly content, such as jpg images of x-rays.
1. Add the `DiagnosticReport.imagingStudy`as a min=0 *Additional USCDI* element to support exchange with systems that can view DICOM (Digital Imaging and Communications in Medicine) studies, series, and SOP (Service-Object Pair) instances referenced in the ImagingStudy resource.
1. Add the `DiagnosticReport.identifier` as a min=0 *Additional USCDI* element to access the source images from external sources using Business identifiers such as ascession numbers.


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

- https://confluence.hl7.org/spaces/AP/pages/161060067/SMART+Imaging+Access
- IHE MHD
- IPS (ImagingStudy)
