---
layout: page
title: Settings
permalink: /settings
---

- [Description](#description)
- [Schema](#schema)
- [Examples](#examples)

**Agency** entity presents information about certain provider. It could be
a bus operator, a rail agency, or a mobility provider for shared vehicles.


<div class="field">
    <div>schemaVersion<br /><span class="required">required</span></div>
    <div>string</div>
    <div>Version of the schema</div>
</div>

<div class="field">
    <div>dataVersion<br /><span class="required">required</span></div>
    <div>string</div>
    <div>Version of the data</div>
</div>

<div class="field">
    <div>name</div>
    <div>string</div>
    <div>Name of the data</div>
</div>

<div class="field">
    <div>language<br /><span class="required">required</span></div>
    <div>string</div>
    <div>Default language of the data</div>
</div>

<div id="block1" class="active" onclick="toggle(event);">
    
<div class="field">
    <div>validity&nbsp;&gt;<br /><span class="required">required</span></div>
    <div>object</div>
    <div>Validity of the data</div>
</div>

</div>
<div id="sub_block1" class="shift">
    
<div class="field">
    <div>from<br /><span class="required">required</span></div>
    <div>string</div>
    <div></div>
</div>

<div class="field">
    <div>to<br /><span class="required">required</span></div>
    <div>string</div>
    <div></div>
</div>

</div>

<div class="field">
    <div>sameStopTransferTime<br /><span class="required">required</span></div>
    <div>integer</div>
    <div>Default transfer time on the same stop</div>
</div>

<div class="field">
    <div>childStopTransferTime<br /><span class="required">required</span></div>
    <div>integer</div>
    <div>Default transfer time between child stops</div>
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
