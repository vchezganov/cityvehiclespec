---
layout: page
title: Agency
permalink: /agencies
---

- [Description](#description)
- [Schema](#schema)
- [Examples](#examples)

**Agency** entity presents information about certain provider. It could be
a bus operator, a rail agency, or a mobility provider for shared vehicles.

## Description
{% include agencies.html %}

## Schema
```json
{% include_relative data/schema/agencies.json -%}
```

## Examples
{% assign counter = 0 %}
{% for ex in site.static_files %}
  {% if ex.path contains 'examples/agencies' %}
  {% assign counter = counter | plus: 1 %}
### #{{ counter }}
```json
{% include_relative {{ ex.path }} -%}
```
  {% endif %}
{% endfor %}
