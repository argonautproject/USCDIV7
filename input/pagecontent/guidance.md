

### Terminology

#### Category Codes

API consumers **MAY** query by category when accessing patient information.<sup>[§][CONF-0275]</sup> Each profile's *Quick Start* section shows searches by category if the category element is defined in the profile. US Core defines these USCDI Health Assessments Data Element category codes:

<!-- ========================================================
The liquid syntax below generates the screening and assessment
categories table. The source is a csv file at
input/data/assessments-valuesets.csv where edits to the table contents
are made manually.

assessments-valuesets.csv columns:
- Data Class Number: number to group by USCDI Data Element
- USCoreStarterCodes: Whether the codes are a starter set
- USCDI Data Element: ONC assigned Data Element for the Health Status Assessments Data Class
- Category Code: US Core assigned Observation category codes
- ValueSet Name: US Core or VSAC assigned value set name
- VSAC Link: url to VSAC value set
- VSAC OID: VSAC assigned OID for the value set
- Clinical Judgement: Whether code is a clinical judgement code
- Panel: Whether code is a panel code
- Panel: Item: Whether code is a panel item code
- Comment: notes
- MCC: If codes came from MCC

The script retrieves, sorts, and selects the table data.
==============================================================-->

<table class="grid">
<thead>
<tr>
<th>USCDI Data Element</th>
<th>Category Code</th>
</tr>
</thead>
<tbody>
{% assign rows = site.data.assessments-valuesets %}
{% assign USCDI = "" %}
{% for item in rows %}
{% unless USCDI == item["USCDI Data Element"] %}
<tr>
<td>{{item["USCDI Data Element"]}}</td>
<td>"{{item["Category Code"]}}"</td>
</tr>
{% assign USCDI = item["USCDI Data Element"] %}
{% endunless %}
{% endfor %}
</tbody>
</table>

<!-- ================== End Liquid ================================ -->


For the US Core Simple Observation Profile and US Core Observation Screening Assessment Profiles, Servers **SHALL** support all the category codes listed above.<sup>[§][CONF-0822],[§][CONF-0823]</sup>

For the US Core Condition Problems and Health Concerns Profile Servers **SHALL** support the code, "sdoh"<sup>[§][CONF-0824]</sup>, and **SHOULD** support the other category codes listed above.<sup>[§][CONF-0825]</sup>

For the US Core ServiceRequest Profile, Servers **SHOULD** support all the above category codes.<sup>[§][CONF-0826]</sup>

The category element is optional in US Core Procedure and US Core Goal, but implementers can categorize them using one of the above category codes or infer the context by inspecting the referenced ServiceRequest if available. Similarly, they can review the Questionnaire resource's metadata to determine the context of the US Core QuestionnaireResponse.



 <span class= "bg-warning" markdown= "1">Clients need to understand that data categorization is somewhat subjective. The categorization applied by the source may not align with the Client's expectations. Clients may find it more beneficial to use queries based on a specific code or set of codes or to perform additional Client-side filtering of query results.</span><!-- bg-warning -->

#### Screening and Assessment Codes

The US Core Observation Screening Assessment Profile, SDC Base Questionnaire, and US Core Simple Observation Profile have [preferred] or [example] bindings to broadly defined LOINC value sets. These value sets contain concepts that span many use cases and are not bound to any USCDI Health Assessments Data Element.

##### USCDI Health Assessments Data Element Value Sets

The following sections and [Health Status Assessments Value Sets Table] below identify the associated value sets for each USCDI Health Status Assessments Data Element. This guidance intends to promote interoperability by introducing "starter" value sets *where available* for the USCDI Data Elements covered by Screenings and Assessments. These value sets are divided into clinical judgment codes, structured screening and assessment panel codes, and structured screening and assessment panel item codes. Note that a suitable value set has yet to be identified in several instances. Implementers **SHOULD** treat these value sets as having an [extensible] binding.<sup>[§][CONF-0280]</sup> In other words, the *Clinical Judgement Codes* code sets are extensibly bound to the US Core Condition Problems and Health Concerns Profile and the US Core Simple Observation Profile when representing clinical judgments. Similarly, *Panel Codes* and *Panel Item Codes* are extensibly bound to the US Core Observation Screening Assessment Profile and SDC Base Questionnaire/US Core QuestionnaireResponse Profile when representing structured screening and assessments. Because the value sets in the Health Status Assessments Value Sets Table are not formally bound to a US Core Profile in the StructureDefinitions, "automatic" validation (confirmation) that a code is a member of a value set will not occur using the standard validation tools.

###### SDOH value sets

- The Gravity project created and maintains the [Social Determinants of Health Screening Assessments And Questions](https://vsac.nlm.nih.gov/valueset/2.16.840.1.113762.1.4.1247.206/expansion) value set for the SDOH USCDI Health Assessments Data Element. This value set contains both panel and panel item codes.

   In addition to these concepts, implementers should consider using several SDOH value sets maintained and updated in VSAC by [Multiple Chronic Condition (MCC) Care Plan Implementation Guide] and the HL7 Patient Care work group with support from the National Institute of Health. These are panel item codes that may be part of a LOINC panel.

<!-- ========================================================
The liquid syntax below generates a list of SDOH screening and
assessment valuesets. The source is a csv file at
input/data/assessments-valuesets.csv where edits to the table contents
are made manually.

assessments-valuesets.csv columns:
- Data Class Number: number to group by USCDI Data Element
- USCoreStarterCodes: Whether the codes are a starter set
- USCDI Data Element: ONC assigned Data Element for the Health Status Assessments Data Class
- Category Code: US Core assigned Observation category codes
- ValueSet Name: US Core or VSAC assigned value set name
- VSAC Link: url to VSAC value set
- VSAC OID: VSAC assigned OID for the value set
- Clinical Judgement: Whether code is a clinical judgement code
- Panel: Whether code is a panel code
- Panel: Item: Whether code is a panel item code
- Comment: notes
- MCC: If codes came from MCC

The script retrieves, sorts, and selects the list data.
==============================================================-->
{% assign rows = site.data.assessments-valuesets %}
<ul>
{% for item in rows -%}
{% unless item["USCDI Data Element"] contains "!" -%}
{% if item["MCC"] == "TRUE" -%}
{% unless forloop.first -%}
<li>
<a href="{{item["VSAC Link"]}}">{{item["ValueSet Name"]}}</a>
</li>
{% endunless -%}
{% endif -%}
{% endunless -%}
{% endfor %}
</ul>

<!-- ===================== end liquid =========================== -->


###### Functional Status

- The [Functional Status Related Questionnaire Panel Codes](https://vsac.nlm.nih.gov/valueset/2.16.840.1.113762.1.4.1222.1586/expansion) contains LOINC panel codes that represent functional status questionnaire LOINC panel code, such as CMS Assessment.

###### Mental and Cognitive Health

- The [Cognitive Health Related Questionnaire Panel Codes](https://vsac.nlm.nih.gov/valueset/2.16.840.1.113762.1.4.1222.979/expansion) contains LOINC panel codes that represent Mental or Cognitive health screening assessments, such as FACIT, PROMIS, and MoCA.

- The [Cognitive Function Clinician Interpretation](https://vsac.nlm.nih.gov/valueset/2.16.840.1.113762.1.4.1222.979/expansion) represents clinical judgment codes such as "Cognitive Function Interpretation".

- The [Mental Status Observation](https://vsac.nlm.nih.gov/valueset/2.16.840.1.113762.1.4.1240.1/expansion) value set contains SNOMED CT clinical judgment codes related to mental status observations that can come from a broad range of subjective and objective information such as Assessment and Screening tools. In many cases, the value (answer) at `Observation.value` may be boolean true \| false.

###### Disability Status

- The [Disability Status Assessment](https://vsac.nlm.nih.gov/valueset/2.16.840.1.113762.1.4.1099.49/expansion) contains LOINC panel item codes that represent detailed patient questions about functional status, such as difficulty dressing or bathing.

###### Accommodation

- No standard terminology currently exists for the USCDI Accommodation Data Element, which covers the modifications, tools, technologies, and other supports a patient needs to access care, such as sign language interpreters, wheelchair accessibility, and sensory accommodations. For clinical judgement observations, use the US Core Simple Observation Profile with the US Core category code, "accommodation", in *both* `Observation.categpory` and `Observation.code`. `Observation.value` is a local code (valueCodeableConcept) or free text (valueString) that identifies the accommodation, for example, "American Sign Language interpreter".

###### Physical Activity

- The [Physical Activity Observation Questions](https://vsac.nlm.nih.gov/valueset/2.16.840.1.113762.1.4.1240.9/expansion) are panel item codes taken from the [Physical Activity Implementation Guide], sponsored by the [American Heart Association] and the [Physical Activity Alliance]. In addition to contributing to the terminology for the USCDI Health Assessments Physical Activity Data Element, the guide documents a standardized way of measuring and sharing a patient's physical activity.

   In addition to these concepts, implementers should consider using   [Physical Activity Level](https://vsac.nlm.nih.gov/valueset/2.16.840.1.113762.1.4.1222.1068/expansion) referenced in the SDOH section above. It represents simple question-and-answer assessment questions such as, "Kinds of physical activity you usually performed while on the job this last year" or "Days per week of moderate to vigorous physical activity".

###### Substance Use (Including Alcohol Use)

- The [Substance Use](https://vsac.nlm.nih.gov/valueset/2.16.840.1.113762.1.4.1222.1015/expansion) contain LOINC panel item codes such as, "How often do you have a drink containing alcohol" or "How often have you used any prescription medications just for the feeling, more than prescribed or that were not prescribed for you in past 12 months (TAPS)"

- The [Alcohol Use Related Questionnaire Panel Codes](https://vsac.nlm.nih.gov/valueset/2.16.840.1.113762.1.4.1222.1585/expansion) contains the LOINC Panel Codes for Alcohol Use Disorder Identification Test - Consumption AUDIT-C and PROMIS short form - alcohol use 7a - version 1.0.

- The [Drug Misuse](https://vsac.nlm.nih.gov/valueset/2.16.840.1.113762.1.4.1222.707/expansion) values set contains SNOMED CT clinical judgment codes
to represent conclusions or diagnoses about drug misuse or abuse. In many cases, the value (answer) at `Observation.value` may be boolean true \| false.

**Health Status Assessments Value Sets Table:**
{: #health-status-assessments-value-sets-table}

<!-- ========================================================
The liquid syntax below generates the screening and assessment
valuesets table. The source is a csv file at
input/data/assessments-valuesets.csv where edits to the table contents
are made manually.

assessments-valuesets.csv columns:
Data Class Number: number to group by USCDI Data Element
USCoreStarterCodes: Whether the codes are a starter set
USCDI Data Element: ONC assigned Data Element for the Health Status Assessments Data Class
Category Code: US Core assigned Observation category codes
ValueSet Name: US Core or VSAC assigned value set name
VSAC Link: url to VSAC value set
VSAC OID: VSAC assigned OID for the value set
Clinical Judgement: Whether code is a clinical judgement code
Panel: Whether code is a panel code
Panel: Item: Whether code is a panel item code
Comment: notes
MCC: If codes came from MCC

The script retrieves, sorts, and selects the table data.
==============================================================-->

<table class="grid">
<thead>
<tr>
<th>USCDI Data Element</th>
<th>ValueSet (VSAC link)</th>
<th>Clinical Judgement Codes</th>
<th>Panel Codes</th>
<th>Panel Item Codes</th>
</tr>
</thead>
<tbody>
{% assign rows = site.data.assessments-valuesets %}
{% for item in rows %}
{% if item["USCoreStarterCodes"] == "TRUE" %}
<tr>
<td>{{item["USCDI Data Element"]}}</td>
<td><a href="{{item["VSAC Link"]}}">{{item["ValueSet Name"]}}</a></td>
{% if item["Clinical Judgement"] == "TRUE" %}<td style="text-align:center; color:green">&#x2714;</td>{% else %}<td></td>{% endif %}
{% if item["Panel"] == "TRUE" %}<td style="text-align:center; color:green">&#x2714;</td>{% else %}<td></td>{% endif %}
{% if item["Panel Item"] == "TRUE" %}<td style="text-align:center; color:green">&#x2714;</td>{% else %}<td></td>{% endif %}
<!-- <td><a href="{ {site.data.fhir.path} }terminologies.html#{ {item["Binding Strength"]} }">{ {item["Binding Strength"]} }</a></td> -->
</tr>
{% endif %}
{% endfor %}
</tbody>
</table>

<!-- ================== End Liquid ================================ -->


This information is also available as a [csv](tables/assessments-valuesets.csv) or [excel](tables/assessments-valuesets.xlsx) file:


#### Codes for Problems/HealthConcerns, Goals, Service Requests, and Procedures

US Core uses broadly defined value sets that contain concepts used across use cases, including SDOH. For the SDOH Clinical Care HL7 Implementation Guide, the Gravity Project has defined "Grouped Value Sets" across specific social risk factor domains for problems/health concerns, goals, procedures, and service requests. Value sets for each SDOH domain are bundled together to create the groupings. The links below are to these Gravity Project-managed value sets in the [Value Set Authority Center (VSAC)]. In VSAC, clicking "Grouping Members" within the Value Set Details tab will present the many individual value sets in the group representing the various SDOH domains. These grouped value sets are narrower subsets of the value sets allowed in the respective US Core Profiles. However, when recording SDOH data US Core Profiles, Servers **SHOULD** use them.<sup>[§][CONF-0281]</sup>

* [Social Determinants of Health Conditions Value Set](https://vsac.nlm.nih.gov/valueset/2.16.840.1.113762.1.4.1196.788/expansion)
* [Social Determinants of Health Procedures Value Set](https://vsac.nlm.nih.gov/valueset/2.16.840.1.113762.1.4.1196.789/expansion)
* [Social Determinants of Health Goals Value Set](https://vsac.nlm.nih.gov/valueset/2.16.840.1.113762.1.4.1247.71/expansion)
* [Social Determinants of Health Service Requests Value Set](https://vsac.nlm.nih.gov/valueset/2.16.840.1.113762.1.4.1196.790/expansion)

 The figure below illustrates how the Gravity value sets are grouped for use in the US Core Condition Problems and Health Concerns Profile and how the grouped value set is compatible with the broader US Core Problem code value set.



{% include img-med.html img="sdoh_condition.svg" caption="SDOH Grouped Value Set Reuse in US Core" %}



