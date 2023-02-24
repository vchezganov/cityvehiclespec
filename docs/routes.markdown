---
layout: page
title: Route
permalink: /routes
---

- [Description](#description)
- [Schema](#schema)
- [Examples](#examples)

**Route** entity presents information about certain route. It contains information
about the route (name, line color, vehicle type, shape etc) and timetables for trips.

## Description
{% include routes.html %}

## Schema
```json
{% include_relative data/schema/routes.json -%}
```

## Examples
{% assign counter = 0 %}
{% for ex in site.static_files %}
  {% if ex.path contains 'examples/routes' %}
  {% assign counter = counter | plus: 1 %}
### #{{ counter }}
```json
{% include_relative {{ ex.path }} -%}
```
  {% endif %}
{% endfor %}
