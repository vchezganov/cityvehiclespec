---
layout: page
title: Stop
permalink: /stops
---

- [Description](#description)
- [Schema](#schema)
- [Examples](#examples)

**Stop** entity presents information about certain stop.

## Description
{% include stops.html %}

## Schema
```json
{% include_relative data/schema/stops.json -%}
```

## Examples
{% assign counter = 0 %}
{% for ex in site.static_files %}
  {% if ex.path contains 'examples/stops' %}
  {% assign counter = counter | plus: 1 %}
### #{{ counter }}
```json
{% include_relative {{ ex.path }} -%}
```
  {% endif %}
{% endfor %}
