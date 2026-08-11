**Example Usage Scenarios:**

The following are example usage scenarios for the US Core AdverseEvent profile:

-   Query for AdverseEvent resources belonging to a Patient
-   [Record or update]  a Patient AdverseEvent

### Mandatory and Must Support Data Elements

The following data elements must always be present ([Mandatory] definition) or must be supported if the data is present in the sending system ([Must Support] definition). They are presented below in a simple human-readable explanation. Profile specific guidance and examples are provided as well. The [Formal Views] below provides the formal summary, definitions, and terminology requirements.

**Each AdverseEvent Must Have:**


1. whether the event is an actual or potential adverse event (actuality)
1. the type of adverse event
1. the patient the event is about

**Each AdverseEvent Must Support:**


1. when the event occurred
1. when the event was recorded
1. the outcome of the event
1. who recorded the adverse event
1. the suspected entity (immunization, medication administration, or medication) that caused the event



### Profile Specific Implementation Guidance

This section provides detailed implementation guidance for the US Core Profile to support implementation and certification.



{% include provenance-author-bullet-generator.md footnote-symbol='<sup>2</sup> ' %}



{% include structure-table-block.md file_name="StructureDefinition-us-core-adverseevent" %}

{% include link-list.md %}
