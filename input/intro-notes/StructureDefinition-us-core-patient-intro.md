**Example Usage Scenarios:**

The following are example usage scenarios for the US Core Patient profile:

-   Query for Patient resources belonging to a Patient
-   [Record or update]  a Patient Patient

### Mandatory and Must Support Data Elements

The following data elements must always be present ([Mandatory] definition) or must be supported if the data is present in the sending system ([Must Support] definition). They are presented below in a simple human-readable explanation. Profile specific guidance and examples are provided as well. The [Formal Views] below provides the formal summary, definitions, and terminology requirements.

**Each Patient Must Have:**


1. an identifier for this patient
1. the namespace for the identifier value
1. the value that is unique within the system
1. a name associated with the patient
1. a system
1. the actual contact point details
1. the language which can be used to communicate with the patient about his or her health

**Each Patient Must Support:**


1. family name (often called 'Surname')
1. given names (not always 'first'). Includes middle names
1. home | work | temp | old | mobile - purpose of this contact point
1. the date of birth for the individual
1. an address for the individual
1. street name, number, direction & P.O. Box etc
1. name of city, town etc
1. sub-unit of country (abbreviations ok)
1. uS Zip Codes
1. the kind of relationship
1. a name associated with the contact person
1. a contact detail for the person


{% include additional-requirements-intro.md type="Patient" plural="false" %}


1. 𝗔𝗗𝗗𝗜𝗧𝗜𝗢𝗡𝗔𝗟 𝗨𝗦𝗖𝗗𝗜: US Core Race Extension. (multiple races are supported in the extension)
1. 𝗔𝗗𝗗𝗜𝗧𝗜𝗢𝗡𝗔𝗟 𝗨𝗦𝗖𝗗𝗜: US Core ethnicity Extension (multiple ethnicities are supported in the extension)
1. 𝗔𝗗𝗗𝗜𝗧𝗜𝗢𝗡𝗔𝗟 𝗨𝗦𝗖𝗗𝗜: Tribal Affiliation Extension
1. 𝗔𝗗𝗗𝗜𝗧𝗜𝗢𝗡𝗔𝗟 𝗨𝗦𝗖𝗗𝗜: Sex Extension
1. 𝗔𝗗𝗗𝗜𝗧𝗜𝗢𝗡𝗔𝗟 𝗨𝗦𝗖𝗗𝗜: Whether the patient needs an interpreter
1. 𝗔𝗗𝗗𝗜𝗧𝗜𝗢𝗡𝗔𝗟 𝗨𝗦𝗖𝗗𝗜: usual | official | temp | nickname | anonymous | old | maiden
1. 𝗔𝗗𝗗𝗜𝗧𝗜𝗢𝗡𝗔𝗟 𝗨𝗦𝗖𝗗𝗜: Parts that come after the name
1. 𝗔𝗗𝗗𝗜𝗧𝗜𝗢𝗡𝗔𝗟 𝗨𝗦𝗖𝗗𝗜: Time period when name was/is in use
1. 𝗔𝗗𝗗𝗜𝗧𝗜𝗢𝗡𝗔𝗟 𝗨𝗦𝗖𝗗𝗜: A contact detail for the individual
1. 𝗔𝗗𝗗𝗜𝗧𝗜𝗢𝗡𝗔𝗟 𝗨𝗦𝗖𝗗𝗜: Indicates if the individual is deceased or not
1. 𝗔𝗗𝗗𝗜𝗧𝗜𝗢𝗡𝗔𝗟 𝗨𝗦𝗖𝗗𝗜: home | work | temp | old | billing - purpose of this address
1. 𝗔𝗗𝗗𝗜𝗧𝗜𝗢𝗡𝗔𝗟 𝗨𝗦𝗖𝗗𝗜: Time period when address was/is in use
1. 𝗔𝗗𝗗𝗜𝗧𝗜𝗢𝗡𝗔𝗟 𝗨𝗦𝗖𝗗𝗜: A contact party (e.g., guardian, healthcare agent, friend) for the patient
1. 𝗔𝗗𝗗𝗜𝗧𝗜𝗢𝗡𝗔𝗟 𝗨𝗦𝗖𝗗𝗜: A language which may be used to communicate with the patient about his or her health


### Profile Specific Implementation Guidance

This section provides detailed implementation guidance for the US Core Profile to support implementation and certification.






{% include structure-table-block.md file_name="StructureDefinition-us-core-patient" %}

{% include link-list.md %}
