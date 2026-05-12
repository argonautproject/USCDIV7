{%- comment -%}
=============================================================================
profile-intro-generator.md   --  place in _includes/
=============================================================================
Generates the introductory narrative sections for a US Core profile page
from its FHIR StructureDefinition.

USAGE
-----
  {% include profile-intro-generator.md sd_id="us-core-allergyintolerance" %}

ASSUMPTIONS
-----------
  * The StructureDefinition JSON is exposed under
    site.data.structuredefinitions, keyed by StructureDefinition.id.
    (Adjust the `assign sd = ...` line if your IG places SDs elsewhere,
    e.g. site.data.profiles or site.data.resources.)
  * These includes exist in _includes/ :
      - additional-requirements-intro.md
      - provenance-author-bullet-generator.md
      - link-list.md

WHAT IS GENERATED
-----------------
  * Example Usage Scenarios   - generic, fixed boilerplate (req #1)
  * Mandatory / Must Support  - heading and intro paragraph, verbatim (req #2)
  * "Must Have" list          - differential elements with min == 1 (req #4)
  * "Must Support" list       - differential elements with
                                  mustSupport == true,
                                  min == 0,
                                  AND no uscdi-requirement extension  (req #5)
  * additional-requirements-intro.md
                              - included only when at least one element
                                carries the uscdi-requirement extension (req #6)
  * USCDI requirements list   - elements with uscdi-requirement extension
  * Profile Specific
    Implementation Guidance   - heading and intro paragraph (fixed);
                                bullets are MANUALLY edited (req #8) EXCEPT
                                for the provenance-author-bullet-generator
                                include, which is auto-added when any
                                element has a W5 mapping to author (req #9).
                                The same author element gets a <sup>2</sup>
                                footnote in the Must Support / USCDI list.
  * link-list.md              - always included at the end.

NOT GENERATED (manual content)
------------------------------
  * Bullets under Profile Specific Implementation Guidance, other than
    the provenance/author bullet.
=============================================================================
{%- endcomment -%}

{%- assign sd = site.data.structuredefinitions[include.sd_id] -%}
{%- assign rt = sd.type -%}
{%- assign uscdi_url = "http://hl7.org/fhir/us/core/StructureDefinition/uscdi-requirement" -%}

{%- comment -%} ---------- First pass: detect USCDI and W5 author ---------- {%- endcomment -%}
{%- assign has_uscdi  = false -%}
{%- assign has_author = false -%}
{%- assign author_path = "" -%}

{%- for el in sd.differential.element -%}
  {%- if el.extension -%}
    {%- for ext in el.extension -%}
      {%- if ext.url == uscdi_url -%}
        {%- assign has_uscdi = true -%}
      {%- endif -%}
    {%- endfor -%}
  {%- endif -%}
  {%- if el.mapping -%}
    {%- for m in el.mapping -%}
      {%- if m.identity == "w5" and m.map contains "author" -%}
        {%- assign has_author  = true -%}
        {%- assign author_path = el.path -%}
      {%- endif -%}
    {%- endfor -%}
  {%- endif -%}
{%- endfor -%}

**Example Usage Scenarios:**

The following are example usage scenarios for the US Core {{ rt }} profile:

-   Query for {{ rt }} resources belonging to a Patient
-   [Record or update]  a Patient {{ rt }}

### Mandatory and Must Support Data Elements

The following data elements must always be present ([Mandatory] definition) or must be supported if the data is present in the sending system ([Must Support] definition). They are presented below in a simple human-readable explanation. Profile specific guidance and examples are provided as well. The [Formal Views] below provides the formal summary, definitions, and terminology requirements.

**Each {{ rt }} Must Have:**

{% for el in sd.differential.element -%}
{%- if el.path != rt and el.min == 1 -%}
{%- assign label = el.short | default: el.path | downcase -%}
{%- assign first = label | slice: 0, 1 -%}
{%- assign article = "a" -%}
{%- if "aeiou" contains first -%}{%- assign article = "an" -%}{%- endif -%}
{%- assign sup = "" -%}
{%- if has_author and el.path == author_path -%}{%- assign sup = "<sup>2</sup>" -%}{%- endif %}
1. {{ article }} {{ label }}{{ sup }}
{% endif -%}
{%- endfor %}

**Each {{ rt }} Must Support:**

{% for el in sd.differential.element -%}
{%- if el.path != rt and el.mustSupport and el.min == 0 -%}
{%- assign is_uscdi = false -%}
{%- if el.extension -%}
{%- for ext in el.extension -%}
{%- if ext.url == uscdi_url -%}{%- assign is_uscdi = true -%}{%- endif -%}
{%- endfor -%}
{%- endif -%}
{%- unless is_uscdi -%}
{%- assign label = el.short | default: el.path | downcase -%}
{%- assign first = label | slice: 0, 1 -%}
{%- assign article = "a" -%}
{%- if "aeiou" contains first -%}{%- assign article = "an" -%}{%- endif -%}
{%- assign sup = "" -%}
{%- if has_author and el.path == author_path -%}{%- assign sup = "<sup>2</sup>" -%}{%- endif %}
1. {{ article }} {{ label }}{{ sup }}
{% endunless -%}
{%- endif -%}
{%- endfor %}

{% if has_uscdi %}
{% include additional-requirements-intro.md type=rt plural="false" %}

{% for el in sd.differential.element -%}
{%- if el.path != rt and el.extension -%}
{%- assign is_uscdi = false -%}
{%- for ext in el.extension -%}
{%- if ext.url == uscdi_url -%}{%- assign is_uscdi = true -%}{%- endif -%}
{%- endfor -%}
{%- if is_uscdi -%}
{%- assign label = el.short | default: el.path | downcase -%}
{%- assign first = label | slice: 0, 1 -%}
{%- assign article = "a" -%}
{%- if "aeiou" contains first -%}{%- assign article = "an" -%}{%- endif -%}
{%- assign sup = "" -%}
{%- if has_author and el.path == author_path -%}{%- assign sup = "<sup>2</sup>" -%}{%- endif %}
1. {{ article }} {{ label }}{{ sup }}
{% endif -%}
{%- endif -%}
{%- endfor %}
{% endif %}

### Profile Specific Implementation Guidance

This section provides detailed implementation guidance for the US Core Profile to support implementation and certification.

<!-- Bullets in this section are manually maintained after community feedback. -->
{% if has_author %}{% include provenance-author-bullet-generator.md footnote-symbol='<sup>2</sup> ' %}{% endif %}

{% include link-list.md %}