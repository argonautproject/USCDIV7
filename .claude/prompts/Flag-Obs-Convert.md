Convert the US Core Flag Profile at /Users/ehaas/Documents/FHIR/USCDIV7/input/resources-yaml/StructureDefinition-us-core-flag.yml to a US Core Observation Patient Accomodation Profile.


1. Follow US Core Observation profile conventions for a narrow use case Observation as demonstrated by the US Core Care Experience Preference Profile: /Users/ehaas/Documents/FHIR/US-Core/input/resources-yaml/StructureDefinition-us-core-care-experience-preference.yml

2. use the Flag category code for both `.code` and `.category`
3. for value(x) use type string and CodeableConcept with the must support extension as true
