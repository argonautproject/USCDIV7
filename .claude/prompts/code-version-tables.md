create a tables listing the code for version 6.1.0, 8.0.1, and 9.0.0 of US Core these three codesystems:

http://hl7.org/fhir/us/core/CodeSystem/condition-category
6.1.0
http://hl7.org/fhir/us/core/CodeSystem/us-core-category
6.1.0
http://hl7.org/fhir/us/core/CodeSystem/us-core-documentreference-category
6.1.0
http://hl7.org/fhir/us/core/CodeSystem/us-core-provenance-participant-type

for each table list the codes in the rows and for each versions add a column for a flag for added or and deleted if the code has been added or retired/deprecated between versions.

for example

code system 6.1.0 = foo,baz
code system 8.0.1 = foo,bar,baz
code system 6.1.0 = foo,bar,baz-marked as deprecated

code|6.1.0 | 8.0.1 |9.0.0 |notes
---|---|---|---|---
foo||||same in all three versions- most common scenario
bar||➕||added in version 8.0.1
baz|||⛔|retired or deprecated in version 9.0.0


Repeat the US Core version analysis and table generation for all the US Core ValueSets.

create a tables listing the code for version 6.1.0, 8.0.1, and 9.0.0 for all the US Core ValueSets.

for each table list the codes in the rows and for each versions add a column for a flag for added or and deleted if the code has been added or retired/deprecated between versions.

for example

code system 6.1.0 = foo,baz
code system 8.0.1 = foo,bar,baz
code system 6.1.0 = foo,bar,baz-marked as deprecated

code|6.1.0 | 8.0.1 |9.0.0 |notes
---|---|---|---|---
foo||||same in all three versions- most common scenario
bar||➕||added in version 8.0.1
baz|||⛔|retired or deprecated in version 9.0.0

  - indicate in the notes:
    - if the Valueset Definition in ValueSet.compose has changed
    - if the Valueset has been removed, deprecated or retired
    - if if it can not be expanded ( for example, because of too many code, intellectual property restrictions, etc)

update the markdown file as follows:
    1.  add this page header to the top of file:

    # US Core Terminology Version Comparisons

    Comparison of US Core Terminology Artifacts across versions 6.1.0, 8.0.1, and 9.0.0.

    2. create subheaders: "## Code Systems" and "## Value Sets" for each set of tables
    3. change the table headers from "##" to "###"
    4. Add the Valueset tables to the file.

the US Core packages are at:

- 9.0.0:  /Users/ehaas/.fhir/packages/hl7.fhir.us.core#9.0.0
- 8.0.1: /Users/ehaas/.fhir/packages/hl7.fhir.us.core#8.0.1
- 6.1.0 /Users/ehaas/.fhir/packages/hl7.fhir.us.core#6.1.0