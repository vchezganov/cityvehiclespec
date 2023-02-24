---
layout: page
title: Settings
permalink: /settings
---

- [Description](#description)
- [Schema](#schema)
- [Examples](#examples)

**Settings** contains information about data like version, validity, etc. In addition to that,
there are settings for default language, default transfer times between trips,
links for realtime data, etc.


## Description
{% include settings.html %}

## Schema
```json
{% include_relative data/schema/settings.json -%}
```

## Examples
{% assign counter = 0 %}
{% for ex in site.static_files %}
  {% if ex.path contains 'examples/settings' %}
  {% assign counter = counter | plus: 1 %}
### #{{ counter }}
```json
{% include_relative {{ ex.path }} -%}
```
  {% endif %}
{% endfor %}
