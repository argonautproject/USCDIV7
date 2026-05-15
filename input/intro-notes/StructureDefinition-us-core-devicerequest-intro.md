**Example Usage Scenarios:**

The following are example usage scenarios for the US Core DeviceRequest profile:

-   Query for DeviceRequest resources belonging to a Patient
-   [Record or update]  a Patient DeviceRequest

### Mandatory and Must Support Data Elements

The following data elements must always be present ([Mandatory] definition) or must be supported if the data is present in the sending system ([Must Support] definition). They are presented below in a simple human-readable explanation. Profile specific guidance and examples are provided as well. The [Formal Views] below provides the formal summary, definitions, and terminology requirements.

**Each DeviceRequest Must Have:**


1. an intent
1. device requested
1. focus of request

**Each DeviceRequest Must Support:**


1. a status
1. when recorded
1. who or what is requesting the device



### Profile Specific Implementation Guidance

This section provides detailed implementation guidance for the US Core Profile to support implementation and certification.



{% include provenance-author-bullet-generator.md footnote-symbol='<sup>2</sup> ' %}



{% include structure-table-block.md file_name="StructureDefinition-us-core-devicerequest" %}

{% include link-list.md %}
