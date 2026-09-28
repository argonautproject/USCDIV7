
<!-- uscdi-v7-nav-banner -->
:::info
**Source page:** https://hackmd.io/WoGZh1mVRTek92MmpBtwlA

**Back to the US Core V10 Design Main Page:** https://hackmd.io/@erichaas/SJo4QLYL-g
:::
<!--/ uscdi-v7-nav-banner -->

## USCDI v7 New Data Elements — USCDI+ Domain and USCDI+ Quality v2 Mapping


![image](https://hackmd.io/_uploads/HJFCn4GIfe.png)


| # | USCDI v7 data element | USCDI+ | USCDI+ domain | USCDI+ Quality v2 match | Notes |
|---|---|---|---|---|---|
| 1 | Accommodation |  | **-** | — | Not found in any USCDI+ domain |
| 2 | Adverse Event Condition | + | Quality | Adverse Event Condition | Draft Quality V2  |
| 3 | Adverse Event Outcome |  | **-** | (Adverse Event Outcome) | ⚠  no '+' in list, but present in Quality V2 |
| 4 | Allergy Intolerance Criticality |  | **-** | — | Not found in any USCDI+ domain |
| 5 | Appointment |  | **-** | — | Not found in any USCDI+ domain |
| 6 | Diagnostic Imaging Reference | + | Quality | Diagnostic Imaging Reference | Draft Quality V2  |
| 7 | Healthcare Agent | + | **Behavioral Health** | — | Nearest: BH/Comprehensive Care 'Durable Medical Power of Attorney' (Advance Directives). No exact element in any domain |
| 8 | Medication Administration | + | Quality | Medication Administration | Draft Quality V2  |
| 9 | Medical Device Order | + | Quality | Medical Device Order | Draft Quality V2  |
| 10 | Nutrition Assessment | + | Quality | — | **DISCREPANCY:** in Draft Quality V2 per platform export, but absent from the Quality v2 mapping table |
| 11 | Nutrition Order | + | Quality | Nutrition Order | Draft Quality V2  |
| 12 | Reason Not Performed | + | Quality | Reason Not Performed | Draft Quality V2  |
| 13 | Referral Note |  | **-** | — | Not found in any USCDI+ domain |
| 14 | Referral Order | + | **(none found)** | — | **CONFLICT:** no 'Referral Order' in any USCDI+ domain. Quality V2 has Referral Status / Referral Date and Time only. ASTP Draft v7 deck shows Referral Order WITHOUT '+' |
| 15 | Specimen Collection Method |  | **-** | — | ⚠  no '+', but present in Quality Overarching (not V2) |
| 16 | Tobacco and Nicotine Product Use |  | **-** | — | Not found in any USCDI+ domain |
| 17 | Condition Status | + | Quality | Condition Status | Draft Quality V2  |
| 18 | Deceased Indicator | + | **Cancer** | — | Nearest: Cancer/Enhancing Oncology Model 'Patient Deceased'. Quality has 'Date of Death' only |
| 19 | Device Type | + | Quality | Device Type | Draft Quality V2  |
| 20 | Diagnostic Report Date and Time | + | Quality | — | In Quality Overarching only, NOT Draft Quality V2 - which is why it is absent from the V2 table |
| 21 | Facility Telecom | + | **Public Health** | — | Public Health/DRAFT Case Reporting has 'Facility Phone' and 'Facility Fax'. Quality Facility Information has no telecom element |
| 22 | Health Insurance Coverage Period | + | Quality | Health Insurance Coverage Period | Draft Quality V2  |
| 23 | Health Insurance Payer | + | Quality | Health Insurance Payer | Draft Quality V2  |
| 24 | Health Insurance Plan | + | Quality | Insurance Plan Name | Different name in Quality V2 |
| 25 | Health Insurance Plan Identifier | + | Quality | Health Insurance Plan Identifier | Draft Quality V2  |
| 26 | Immunization Record Source | + | Quality | Immunization Record Source | Draft Quality V2  |
| 27 | Immunization Status | + | Quality; Maternal Health; Public Health | Immunization Status | 3 domains |
| 28 | Medication Dispense Quantity | + | Quality | Medication Quantity | Different name in Quality V2 (broader - covers request and dispense) |
| 29 | Patient Identifier | + | Quality; Behavioral Health; Cancer; Maternal Health; Public Health | Patient Identifier | All 5 domains - the most widely shared new element |
| 30 | Procedure Status | + | Quality; Maternal Health | Procedure Status | 2 domains |
| 31 | Specimen Collection Date and Time |  | **-** | (Specimen Collection Date and Time) | ⚠  no '+', but present in Quality V2 + 4 other domains |

Source: USCDI+ platform element export (1,369 rows / 6 domains), matched on `Data Element Parent`;
USCDI+ Quality v2 column matched against the Quality v2 data element table `Name` column.
`-` in the USCDI+ domain column means the element carries no `+` flag in the USCDI v7 list.