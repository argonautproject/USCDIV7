Fastest form — paste a table. For example:

Create a new profile us-core-adverseevent for USCDI v7 "[AdverseEvents]".

| Element        | Card | MS | Binding / Notes                    |
|----------------|------|----|------------------------------------|
| actuality     | 1..1 | Y  | required, http://hl7.org/fhir/ValueSet/adverse-event-actuality               |
| event           | 1..1 | Y  | extensible, http://hl7.org/fhir/ValueSet/adverse-event-type             |
| subject        | 1..1 | Y  | Reference(us-core-patient)         |
| date   | 0..1 | Y  | dateTime                           |
| recordedDate   | 0..1 | Y  | dateTime                           |
| outcome   | 0..1 | Y  | required                           |
| recorder   | 0..1 | Y  | Reference(us-core-practitioner)                          |
| suspectedEntity  | 0..* | Y  |                           |
| suspectedEntity.instance  | 1..1 | Y  | Reference(us-core-immmunization, us-core-medicationadministration, us-core-medication)    |
| recorder   | 0..1 | Y  | Reference(us-core-practitioner)                          |


Then create 2 examples covering 1) patient experiences a fever after immunization and 2) patient experiences a rash after taking a medication.