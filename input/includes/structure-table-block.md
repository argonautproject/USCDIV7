


### Liquid Script to Generate StructureDefinition All Nice N Pretty Like

{% assign sd = site.data[include.file_name] %}


{% raw %} {% include structure-table.md sd={% endraw %}sd{% raw %} source="differential" show_must_support=true show_uscdi=true %}{% endraw %}

{% include structure-table.md sd=sd source="differential" show_must_support=true show_uscdi=true %}

{% capture md_table %}{% include structure-table.md sd=sd source="differential" show_must_support=true show_uscdi=true %}
{% endcapture %}

```text
{{ md_table }}
```