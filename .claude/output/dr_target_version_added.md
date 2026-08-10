## DocumentReference target — version added (summary)

| # | Resource | Element | Version added | Prior state | Is Sole Target | Confidence |
|---|---|---|---|---|---|---|
| 1 | AdverseEvent | `AdverseEvent.contributingFactor` | R5 | no_dr |  | high |
| 2 | AdverseEvent | `AdverseEvent.mitigatingAction` | R5 | element_absent |  | high |
| 3 | AdverseEvent | `AdverseEvent.preventiveAction` | R5 | element_absent |  | high |
| 4 | AdverseEvent | `AdverseEvent.supportingInfo` | R5 | element_absent |  | high |
| 5 | Appointment | `Appointment.patientInstruction` | R5 | no_dr |  | high |
| 6 | Consent | `Consent.policyText` | R5 | element_absent | ✓ | high |
| 7 | Consent | `Consent.sourceReference` | ≤ R4 | earlier_release_unavailable |  | high |
| 8 | Contract | `Contract.friendly.content[x]` | ≤ R4 | earlier_release_unavailable |  | high |
| 9 | Contract | `Contract.legal.content[x]` | ≤ R4 | earlier_release_unavailable |  | high |
| 10 | Contract | `Contract.legallyBinding[x]` | ≤ R4 | earlier_release_unavailable |  | high |
| 11 | Contract | `Contract.rule.content[x]` | ≤ R4 | earlier_release_unavailable | ✓ | high |
| 12 | Contract | `Contract.term.action.reason` | ≤ R4 | earlier_release_unavailable |  | high |
| 13 | DeviceRequest | `DeviceRequest.reason` | ≤ R4 | earlier_release_unavailable |  | high |
| 14 | DiagnosticReport | `DiagnosticReport.media.link` | R5 | no_dr | ✓ | high |
| 15 | DiagnosticReport | `DiagnosticReport.supportingInfo.reference` | R6 | no_dr |  | high |
| 16 | DocumentReference | `DocumentReference.relatesTo.target` | ≤ R4 | earlier_release_unavailable | ✓ | high |
| 17 | FamilyMemberHistory | `FamilyMemberHistory.reason` | ≤ R4 | earlier_release_unavailable |  | high |
| 18 | ImagingSelection | `ImagingSelection.derivedFrom` | R5 | resource_absent |  | high |
| 19 | ImagingStudy | `ImagingStudy.reason` | ≤ R4 | earlier_release_unavailable |  | high |
| 20 | MedicinalProductDefinition | `MedicinalProductDefinition.attachedDocument` | R5 | resource_absent | ✓ | high |
| 21 | MedicinalProductDefinition | `MedicinalProductDefinition.masterFile` | R5 | resource_absent | ✓ | high |
| 22 | NutritionIntake | `NutritionIntake.reason` | R5 | resource_absent |  | high |
| 23 | Observation | `Observation.derivedFrom` | ≤ R4 | earlier_release_unavailable |  | high |
| 24 | PackagedProductDefinition | `PackagedProductDefinition.attachedDocument` | R5 | resource_absent | ✓ | high |
| 25 | Procedure | `Procedure.reason` | ≤ R4 | earlier_release_unavailable |  | high |
| 26 | Procedure | `Procedure.report` | ≤ R4 | earlier_release_unavailable |  | high |
| 27 | RegulatedAuthorization | `RegulatedAuthorization.attachedDocument` | R5 | resource_absent | ✓ | high |
| 28 | RequestOrchestration | `RequestOrchestration.reason` | ≤ R4 | earlier_release_unavailable |  | high |
| 29 | RiskAssessment | `RiskAssessment.reason` | ≤ R4 | earlier_release_unavailable |  | high |
| 30 | ServiceRequest | `ServiceRequest.basedOn` | R6 | no_dr |  | high |
| 31 | ServiceRequest | `ServiceRequest.patientInstruction.instruction[x]` | R5 | element_absent | ✓ | high |
| 32 | ServiceRequest | `ServiceRequest.reason` | ≤ R4 | earlier_release_unavailable |  | high |
| 33 | SubstanceDefinition | `SubstanceDefinition.code.source` | R5 | resource_absent | ✓ | high |
| 34 | SubstanceDefinition | `SubstanceDefinition.name.source` | R5 | resource_absent | ✓ | high |
| 35 | SubstanceDefinition | `SubstanceDefinition.relationship.source` | R5 | resource_absent | ✓ | high |
| 36 | SubstanceDefinition | `SubstanceDefinition.structure.representation.document` | R5 | resource_absent | ✓ | high |
| 37 | SubstanceDefinition | `SubstanceDefinition.structure.sourceDocument` | R5 | resource_absent | ✓ | high |

_No low-confidence (auto-resolved) rows._
