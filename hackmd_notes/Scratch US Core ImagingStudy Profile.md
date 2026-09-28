---
title: Scratch US Core ImagingStudy Profile
tags: [USCDI v7]

---

US Core ImagingStudy Profile: 

Goal: Minimum Necessary

Agreement

- `identifier` 0..* MS ***choice?*** (slice: ascession number - instance)
- `status` 1..1 MS
- `subject` 1..1 MS
- `endpoint` 0..* MS ***choice?*** ("The network service providing access (e.g., query, view, or retrieval) for the study" - might be different endpoints for different use cases - e.g., for a patient may provide a DICOMweb endpoint vs. for a provider may provide a foo widget
    :::warning
    caveat that access to images is not guaranteed. See SMART Imaging Access...
    :::

:thinking_face: Discuss

- `identifier`  (slice: study)
- `modality` (All series modality if actual acquisition modalities
A list of all the series.modality values that are actual acquisition modalities, i.e. those in the DICOM Context Group 29 (value set OID 1.2.840.10008.6.1.19).
Bin)
- ~~interpreter (Who read the study and interpreted the images or other content. Reference)~~
- ~~procedure code (The code for the performed procedure type)~~
- ~~reason code The code for the reason the study performed)~~
- ~~description~~
- ~~started (When the study was started)~~

---

