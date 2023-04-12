---
layout: page
title: Translations
permalink: /translations
---

- [Description](#description)
- [Schema](#schema)
- [Examples](#examples)

**Agency** entity presents information about certain provider. It could be
a bus operator, a rail agency, or a mobility provider for shared vehicles.


<div class="field">
    <div>text<br /><span class="required">required</span></div>
    <div>string</div>
    <div>Text having translations</div>
</div>

<div class="field">
    <div>translations</div>
    <div>object</div>
    <div>Translations of the text</div>
</div>


```json
{% include_relative data/schema/agencies.json -%}
```

{% assign counter = 0 %}
{% for ex in site.static_files %}
  {% if ex.path contains 'examples/agencies' %}
  {% assign counter = counter | plus: 1 %}
```json
{% include_relative {{ ex.path }} -%}
```
  {% endif %}
{% endfor %}
