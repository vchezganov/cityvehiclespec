---
layout: page
title: {% block title %}{{ title }}{% endblock %}
permalink: /{{ permalink }}
---

- [Description](#description)
{% if examples %}
- [Examples](#examples)
{% endif %}
- [Schema](#schema)

{% block head %}{% endblock %}

## Description
<div class="main">
{{ description }}
</div>

{% if examples %}
## Examples
{% for example in examples %}
### #{{ loop.index }}
```json
{{ example }}
```
{% endfor %}
{% endif %}

## Schema
```json
{{ schema }}
```
