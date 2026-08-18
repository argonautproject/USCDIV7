**Example Usage Scenarios:**

The following are example usage scenarios for the US Core ImagingStudy profile:

-   Query for ImagingStudy resources belonging to a Patient
-   [Record or update]  a Patient ImagingStudy

### Mandatory and Must Support Data Elements

The following data elements must always be present ([Mandatory] definition) or must be supported if the data is present in the sending system ([Must Support] definition). They are presented below in a simple human-readable explanation. Profile specific guidance and examples are provided as well. The [Formal Views] below provides the formal summary, definitions, and terminology requirements.

**Each ImagingStudy Must Have:**


1. one or more identifiers for the study
1. a DICOM Study Instance UID
1. a status
1. one or more study modalities
1. a subject (the patient)
1. one or more study access endpoints (e.g., WADO-RS)
1. a DICOM Series Instance UID for each series
1. a modality for each series
1. a DICOM SOP Instance UID for each instance
1. a DICOM SOP class for each instance

**Each ImagingStudy Must Support:**


1. the number of series in the study
1. the number of instances in the study
1. one or more series of instances
1. a series number
1. one or more SOP instances in each series
1. an instance number



### Profile Specific Implementation Guidance

This section provides detailed implementation guidance for the US Core Profile to support implementation and certification.






{% include structure-table-block.md file_name="StructureDefinition-us-core-imagingstudy" %}

{% include link-list.md %}
