**Example Usage Scenarios:**

The following are example usage scenarios for the US Core Appointment profile:

-   Query for Appointment resources belonging to a Patient
-   [Record or update]  a Patient Appointment

### Mandatory and Must Support Data Elements

The following data elements must always be present ([Mandatory] definition) or must be supported if the data is present in the sending system ([Must Support] definition). They are presented below in a simple human-readable explanation. Profile specific guidance and examples are provided as well. The [Formal Views] below provides the formal summary, definitions, and terminology requirements.

**Each Appointment Must Have:**


1. a status
2. a participant (person, location/healthcare service or device)

**Each Appointment Must Support:**


1. external identifiers for this appointment
2. the specific service to be performed during the appointment
3. when the appointment starts
4. when the appointment ends
5. a patient participant involved in the appointment



### Profile Specific Implementation Guidance

This section provides detailed implementation guidance for the US Core Profile to support implementation and certification.






{% include structure-table-block.md file_name="StructureDefinition-us-core-appointment" %}

{% include link-list.md %}
