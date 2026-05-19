**Example Usage Scenarios:**

The following are example usage scenarios for the US Core NutritionOrder profile:

-   Query for NutritionOrder resources belonging to a Patient
-   [Record or update]  a Patient NutritionOrder

### Mandatory and Must Support Data Elements

The following data elements must always be present ([Mandatory] definition) or must be supported if the data is present in the sending system ([Must Support] definition). They are presented below in a simple human-readable explanation. Profile specific guidance and examples are provided as well. The [Formal Views] below provides the formal summary, definitions, and terminology requirements.

**Each NutritionOrder Must Have:**


1. a status
2. an intent
3. a patient
4. when requested

**Each NutritionOrder Must Support:**

1. the requester
2. what diet is being requested
3. patient instructions


### Profile Specific Implementation Guidance

This section provides detailed implementation guidance for the US Core Profile to support implementation and certification.


{% include provenance-author-bullet-generator.md footnote-symbol='<sup>2</sup> ' %}


{% include structure-table-block.md file_name="StructureDefinition-us-core-nutritionorder" %}

{% include link-list.md %}
