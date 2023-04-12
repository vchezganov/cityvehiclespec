---
layout: page
title: {% block title %}{{ title }}{% endblock %}
permalink: /{{ permalink }}
---

- [Description](#description)
- [Schema](#schema)
{% if examples %}
- [Examples](#examples)
{% endif %}

{% block head %}{% endblock %}

## Description
<div class="main">
{{ description }}
</div>

## Schema
```json
{{ schema }}
```

{% if examples %}
## Examples
{% for example in examples %}
### #{{ loop.index }}
```json
{{ example }}
```
{% endfor %}
{% endif %}