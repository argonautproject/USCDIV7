{%- comment -%}
  Include: structure-table.md

  Markdown version of the StructureDefinition element table. Outputs a Markdown
  table that the page's Markdown processor (kramdown by default in Jekyll) will
  render to HTML. HTML tags like <br> and <small> are passed through by kramdown
  inside table cells; we use those for line breaks and de-emphasized detail rows
  (bindings, fixed values, slicing, constraints).

  Generate from a StructureDefinition that lives in Jekyll's _data folder
  (typically populated via the IG Publisher's `produce-jekyll-data` parameter).

  Usage:
    {% include structure-table.md sd=site.data.my_profile %}
    {% include structure-table.md sd=site.data.my_profile source="differential" %}
    {% include structure-table.md sd=site.data.my_profile filter="Encounter.meta" %}
    {% include structure-table.md sd=site.data.my_profile show_must_support=true show_uscdi=true %}

  Parameters:
    sd                - the StructureDefinition object (required)
    show_metadata     - render the metadata block above the table (default: true)
    source            - "snapshot" or "differential" (default: "snapshot").
                        When "differential", row selection is driven by
                        differential.element but each row is rendered using the
                        matching snapshot.element when a snapshot is published
                        (matched on ElementDefinition.id).
    filter            - render only one element and its descendants. Matches
                        against ElementDefinition.id (e.g. "Encounter.meta"
                        includes meta plus meta.lastUpdated, meta.profile, etc.).
                        Accepts "Encounter.meta", ".meta", or "meta" — the
                        resource type prefix is added automatically.
    show_modifier     - include the "Modifier Element" column (default: false)
    show_must_support - include the "Must Support" column (default: false)
    show_uscdi        - include the "Add'l USCDI" column, populated from a
                        "𝗔𝗗𝗗𝗜𝗧𝗜𝗢𝗡𝗔𝗟 𝗨𝗦𝗖𝗗𝗜:" marker in the element's
                        short text (default: false). The marker is stripped from
                        the displayed short regardless of this flag.
    show_constraints  - include ElementDefinition.constraint[] entries in the
                        description column and append "& Constraints" to that
                        column header (default: false)

  Default columns: Element, Cardinality, Type, Description.
{%- endcomment -%}
{%- assign sd                = include.sd -%}
{%- assign show_metadata     = include.show_metadata     | default: true -%}
{%- assign source            = include.source            | default: "snapshot" -%}
{%- assign raw_filter        = include.filter            | default: "" -%}
{%- assign show_modifier     = include.show_modifier     | default: false -%}
{%- assign show_must_support = include.show_must_support | default: false -%}
{%- assign show_uscdi        = include.show_uscdi        | default: false -%}
{%- assign show_constraints  = include.show_constraints  | default: false -%}

{%- if sd %}

{% if show_metadata -%}
## {{ sd.name }}{% if sd.title %} — {{ sd.title }}{% endif %}

{% if sd.description %}{{ sd.description }}

{% endif -%}
{% if sd.url %}- **URL:** `{{ sd.url }}`
{% endif -%}
{% if sd.version %}- **Version:** {{ sd.version }}
{% endif -%}
- **Status:** {{ sd.status }}
- **Kind:** {{ sd.kind }}
- **Type:** `{{ sd.type }}`
{% if sd.baseDefinition %}- **Base Definition:** `{{ sd.baseDefinition }}`
{% endif -%}
- **Derivation:** {{ sd.derivation | default: "specialization" }}
{% if sd.abstract == true %}- **Abstract:** Yes
{% endif -%}
{% if sd.experimental == true %}- **Experimental:** Yes
{% endif -%}
{% endif -%}

{%- comment -%} Pick driver list (and snapshot lookup table when in differential mode) {%- endcomment -%}
{%- if source == "differential" -%}
  {%- assign driver_elements   = sd.differential.element -%}
  {%- assign snapshot_elements = sd.snapshot.element -%}
{%- else -%}
  {%- assign driver_elements   = sd.snapshot.element -%}
{%- endif -%}

{%- comment -%} Normalize filter (accepts "Encounter.meta", ".meta", or "meta") {%- endcomment -%}
{%- assign filter_full   = "" -%}
{%- assign filter_prefix = "" -%}
{%- assign filter_depth  = 0 -%}
{%- if raw_filter != "" -%}
  {%- assign f = raw_filter -%}
  {%- assign first_char = f | slice: 0, 1 -%}
  {%- if first_char == "." -%}
    {%- assign rest_size = f | size | minus: 1 -%}
    {%- assign f = f | slice: 1, rest_size -%}
  {%- endif -%}
  {%- assign type_prefix = sd.type | append: "." -%}
  {%- assign tp_size = type_prefix | size -%}
  {%- assign f_head = f | slice: 0, tp_size -%}
  {%- if f_head == type_prefix -%}
    {%- assign filter_full = f -%}
  {%- else -%}
    {%- assign filter_full = type_prefix | append: f -%}
  {%- endif -%}
  {%- assign filter_prefix = filter_full | append: "." -%}
  {%- assign filter_segments = filter_full | split: "." -%}
  {%- assign filter_depth = filter_segments | size | minus: 1 -%}
{%- endif -%}

{%- if driver_elements and driver_elements != empty -%}

  {%- comment -%} Pre-flight match count so we can show a notice when filter matches nothing {%- endcomment -%}
  {%- assign filter_match_count = 0 -%}
  {%- if filter_full != "" -%}
    {%- for el in driver_elements -%}
      {%- if el.id == filter_full -%}
        {%- assign filter_match_count = filter_match_count | plus: 1 -%}
      {%- else -%}
        {%- assign fp_size = filter_prefix | size -%}
        {%- assign id_head = el.id | slice: 0, fp_size -%}
        {%- if id_head == filter_prefix -%}
          {%- assign filter_match_count = filter_match_count | plus: 1 -%}
        {%- endif -%}
      {%- endif -%}
    {%- endfor -%}
  {%- endif -%}

  {%- if filter_full != "" and filter_match_count == 0 %}

*No elements in {{ source }} match filter `{{ filter_full }}`.*
  {%- else %}

### Elements ({{ source }}{% if filter_full != "" %} — filtered to `{{ filter_full }}`{% endif %})

| Element |{% if show_modifier %} Modifier Element |{% endif %}{% if show_must_support %} Must Support |{% endif %}{% if show_uscdi %} Add'l USCDI |{% endif %} Cardinality | Type | Description{% if show_constraints %} & Constraints{% endif %} |
|---|{% if show_modifier %}:---:|{% endif %}{% if show_must_support %}:---:|{% endif %}{% if show_uscdi %}:---:|{% endif %}---|---|---|
{% for driver in driver_elements -%}
  {%- assign include_row = true -%}
  {%- if filter_full != "" -%}
    {%- assign fp_size = filter_prefix | size -%}
    {%- assign id_head = driver.id | slice: 0, fp_size -%}
    {%- if driver.id == filter_full -%}
      {%- assign include_row = true -%}
    {%- elsif id_head == filter_prefix -%}
      {%- assign include_row = true -%}
    {%- else -%}
      {%- assign include_row = false -%}
    {%- endif -%}
  {%- endif -%}
  {%- if include_row -%}
    {%- comment -%} Resolve to snapshot element when available, fall back to driver {%- endcomment -%}
    {%- assign el = driver -%}
    {%- if source == "differential" and snapshot_elements -%}
      {%- for snap_el in snapshot_elements -%}
        {%- if snap_el.id == driver.id -%}
          {%- assign el = snap_el -%}
          {%- break -%}
        {%- endif -%}
      {%- endfor -%}
    {%- endif -%}

    {%- assign segments     = el.path | split: "." -%}
    {%- assign depth        = segments | size | minus: 1 -%}
    {%- assign render_depth = depth | minus: filter_depth -%}
    {%- assign last_seg     = segments | last -%}

    {%- comment -%} Build indent string: 4 nbsp per depth level (HTML entities pass through kramdown) {%- endcomment -%}
    {%- assign indent = "" -%}
    {%- if render_depth > 0 -%}
      {%- for i in (1..render_depth) -%}
        {%- assign indent = indent | append: "&nbsp;&nbsp;&nbsp;&nbsp;" -%}
      {%- endfor -%}
    {%- endif -%}

    {%- comment -%} Detect "Additional USCDI" marker and strip it from displayed short {%- endcomment -%}
    {%- assign uscdi_marker = "𝗔𝗗𝗗𝗜𝗧𝗜𝗢𝗡𝗔𝗟 𝗨𝗦𝗖𝗗𝗜:" -%}
    {%- if el.short and el.short contains uscdi_marker -%}
      {%- assign is_uscdi = true -%}
      {%- assign clean_short = el.short | replace: uscdi_marker, "" | strip -%}
    {%- else -%}
      {%- assign is_uscdi = false -%}
      {%- assign clean_short = el.short -%}
    {%- endif -%}

    {%- comment -%} Build cell contents in captures so the row stays on one line {%- endcomment -%}
    {%- capture name_cell -%}
{{ indent }}{% if render_depth > 0 %}↳ {% endif %}`{{ last_seg }}`{% if el.sliceName %}<br><small>slice: `{{ el.sliceName }}`</small>{% endif %}
    {%- endcapture -%}

    {%- capture types_cell -%}
{%- if el.type -%}
{%- for t in el.type -%}
`{{ t.code }}`
{%- if t.profile %}{% for p in t.profile %}<br><small>profile: {{ p }}</small>{% endfor %}{%- endif -%}
{%- if t.targetProfile %}{% for tp in t.targetProfile %}<br><small>target: {{ tp }}</small>{% endfor %}{%- endif -%}
{%- if t.aggregation %}<br><small>aggregation: {{ t.aggregation | join: ", " }}</small>{%- endif -%}
{%- unless forloop.last %}<br>{% endunless -%}
{%- endfor -%}
{%- elsif el.contentReference -%}
see `{{ el.contentReference }}`
{%- endif -%}
    {%- endcapture -%}

    {%- capture desc_cell -%}
{%- if clean_short and clean_short != "" -%}**{{ clean_short | replace: "|", "\|" | strip_newlines }}**{%- endif -%}
{%- if el.definition and el.definition != el.short -%}<br>{{ el.definition | replace: "|", "\|" | strip_newlines }}{%- endif -%}
{%- if el.binding -%}<br><small>**Binding:**{% if el.binding.valueSet %} `{{ el.binding.valueSet }}`{% endif %}{% if el.binding.strength %} ({{ el.binding.strength }}){% endif %}{% if el.binding.description %} — {{ el.binding.description | replace: "|", "\|" | strip_newlines }}{% endif %}</small>{%- endif -%}
{%- if el.fixedCode -%}<br><small>**Fixed (code):** `{{ el.fixedCode }}`</small>{%- endif -%}
{%- if el.fixedString -%}<br><small>**Fixed (string):** `{{ el.fixedString | replace: "|", "\|" | strip_newlines }}`</small>{%- endif -%}
{%- if el.fixedUri -%}<br><small>**Fixed (uri):** `{{ el.fixedUri }}`</small>{%- endif -%}
{%- if el.fixedBoolean != nil -%}<br><small>**Fixed (boolean):** `{{ el.fixedBoolean }}`</small>{%- endif -%}
{%- if el.patternCodeableConcept -%}<br><small>**Pattern (CodeableConcept):**{% for c in el.patternCodeableConcept.coding %} `{{ c.system }}#{{ c.code }}`{% unless forloop.last %},{% endunless %}{% endfor %}</small>{%- endif -%}
{%- if el.patternIdentifier -%}<br><small>**Pattern (Identifier):** system `{{ el.patternIdentifier.system }}`</small>{%- endif -%}
{%- if el.slicing -%}<br><small>**Slicing:**{% if el.slicing.discriminator %} discriminator{% for d in el.slicing.discriminator %} `{{ d.type }}@{{ d.path }}`{% unless forloop.last %},{% endunless %}{% endfor %}{% endif %}{% if el.slicing.rules %} — rules: {{ el.slicing.rules }}{% endif %}{% if el.slicing.ordered %} — ordered{% endif %}</small>{%- endif -%}
{%- if show_constraints and el.constraint -%}{%- for c in el.constraint -%}<br><small>**{{ c.key }}** ({{ c.severity }}): {{ c.human | replace: "|", "\|" | strip_newlines }}</small>{%- endfor -%}{%- endif -%}
    {%- endcapture -%}

| {{ name_cell | strip_newlines }} |{% if show_modifier %} {% if el.isModifier == true %}✅{% endif %} |{% endif %}{% if show_must_support %} {% if el.mustSupport == true %}✅{% endif %} |{% endif %}{% if show_uscdi %} {% if is_uscdi %}✅{% endif %} |{% endif %} {{ el.min | default: 0 }}..{{ el.max | default: "*" }} | {{ types_cell | strip_newlines }} | {{ desc_cell | strip_newlines }} |
{% endif -%}
{%- endfor -%}
  {%- endif -%}

{%- else %}

*No elements found in {{ source }}.*
{%- endif %}

{% else %}

*No StructureDefinition data provided.*
{% endif -%}
