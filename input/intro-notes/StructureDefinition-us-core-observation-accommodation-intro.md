**Example Usage Scenarios:**

The following are example usage scenarios for the US Core Observation profile:

-   Query for Observation resources belonging to a Patient
-   [Record or update]  a Patient Observation

### Mandatory and Must Support Data Elements

The following data elements must always be present ([Mandatory] definition) or must be supported if the data is present in the sending system ([Must Support] definition). They are presented below in a simple human-readable explanation. Profile specific guidance and examples are provided as well. The [Formal Views] below provides the formal summary, definitions, and terminology requirements.

**Each Observation Must Have:**


1. a status
1. patient accommodation code
1. a patient

**Each Observation Must Support:**


1. classification of type of observation
1. clinically relevant time or time period for the observation
1. coded or free text patient accommodation


{% include additional-requirements-intro.md type="Observation" plural="false" %}


1. 𝗔𝗗𝗗𝗜𝗧𝗜𝗢𝗡𝗔𝗟 𝗨𝗦𝗖𝗗𝗜: who is responsible for the observation


### Profile Specific Implementation Guidance

This section provides detailed implementation guidance for the US Core Profile to support implementation and certification.






{% include structure-table-block.md file_name="StructureDefinition-us-core-observation-accommodation" %}

{% include link-list.md %}
