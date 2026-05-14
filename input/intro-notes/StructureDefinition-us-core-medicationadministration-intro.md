**Example Usage Scenarios:**

The following are example usage scenarios for the US Core MedicationAdministration profile:

-   Query for MedicationAdministration resources belonging to a Patient
-   [Record or update]  a Patient MedicationAdministration

### Mandatory and Must Support Data Elements

The following data elements must always be present ([Mandatory] definition) or must be supported if the data is present in the sending system ([Must Support] definition). They are presented below in a simple human-readable explanation. Profile specific guidance and examples are provided as well. The [Formal Views] below provides the formal summary, definitions, and terminology requirements.

**Each MedicationAdministration Must Have:**


1. a status
1. a medication
1. a patient
1. when the medication was administered

**Each MedicationAdministration Must Support:**

<!-- 1. reason administration was not performed -->

1. who administered the medication
2. reference to the  administration order
3. free text dosage instructions (e.g. SIG)
4. the route of administration
5. the dose and rate

### Profile Specific Implementation Guidance

This section provides detailed implementation guidance for the US Core Profile to support implementation and certification.






{% include structure-table-block.md file_name="StructureDefinition-us-core-medicationadministration" %}

{% include link-list.md %}
