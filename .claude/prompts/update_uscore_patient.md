  1. Source US Core profile — /Users/ehaas/Documents/FHIR/US-Core/input/resources-yaml/StructureDefinition-us-core-patient.yml
  2. USCDI v7 Data Element or Data Class — Healthcare Agent
  3. Constraints:
      — add `Patient.contact` as a 0..1 Additional USCDI element
      - add ``Patient.contact.relationship` as must support
      - add ``Patient.contact.name` as must support
      - add ``Patient.contact.telecom` as must support
  1. Bindings — any binding strength / value set to apply on changed elements?
      - Create a new extensible valueset "US Core Patient Contact Relationship" composed of:
        - PatientContactRelationship ValueSet (http://hl7.org/fhir/ValueSet/patient-contactrelationship)
        - HPOWATT (http://terminology.hl7.org/CodeSystem/contractsignertypecodes) : Healthcare Power of Attorney
        - 154248006 (SNOMED CT) : Holds power of attorney (finding)
        - 58626002 (SNOMED CT) : Legal guardian (person)
        - 54056000 (SNOMED CT) : Trustee (person)
        - 75783-1 (LOINC) : Primary healthcare agent [Reported]
        - 75784-9 (LOINC) : First alternate healthcare agent [Reported]
        - 75785-6 (LOINC) : Second alternate healthcare agent [Reported]