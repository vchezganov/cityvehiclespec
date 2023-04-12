---
layout: page
title: Routes
permalink: /routes
---

- [Description](#description)
- [Schema](#schema)
- [Examples](#examples)

**Agency** entity presents information about certain provider. It could be
a bus operator, a rail agency, or a mobility provider for shared vehicles.


<div class="field">
    <div>id<br /><span class="required">required</span></div>
    <div>string</div>
    <div>Unique identifier for the route</div>
</div>

<div class="field">
    <div>agency<br /><span class="required">required</span></div>
    <div>string</div>
    <div>Agency's identifier the route belongs to</div>
</div>

<div id="block32" class="active" onclick="toggle(event);">
    
<div class="field">
    <div>name&nbsp;&gt;<br /><span class="required">required</span></div>
    <div>one of</div>
    <div>Name of the route</div>
</div>

</div>
<div id="sub_block32" class="shift">
    
<div class="field">
    <div>#1<br /><span class="required">required</span></div>
    <div>string</div>
    <div>Text in agency's language. Translation can be specified using Translation entities.</div>
</div>

<div class="field">
    <div>#2<br /><span class="required">required</span></div>
    <div>object</div>
    <div>Texts for different languages. Agency's language must be present.</div>
</div>

</div>

<div id="block33" class="active" onclick="toggle(event);">
    
<div class="field">
    <div>description&nbsp;&gt;</div>
    <div>one of</div>
    <div>Description of the route</div>
</div>

</div>
<div id="sub_block33" class="shift">
    
<div class="field">
    <div>#1</div>
    <div>string</div>
    <div>Text in agency's language. Translation can be specified using Translation entities.</div>
</div>

<div class="field">
    <div>#2</div>
    <div>object</div>
    <div>Texts for different languages. Agency's language must be present.</div>
</div>

</div>

<div class="field">
    <div>lineColor</div>
    <div>string</div>
    <div>Line color of the route</div>
</div>

<div class="field">
    <div>fontColor</div>
    <div>string</div>
    <div>Font color of the route</div>
</div>

<div class="field">
    <div>vehicleType</div>
    <div>string | number</div>
    <div>Vehicle type of the route</div>
</div>

<div id="block35" class="active" onclick="toggle(event);">
    
<div class="field">
    <div>features&nbsp;&gt;</div>
    <div>one of</div>
    <div>Features of the trip.</div>
</div>

</div>
<div id="sub_block35" class="shift">
    
<div class="field">
    <div>#1</div>
    <div>[]enum</div>
    <div>List of route features.
<pre class="addition">
wheelchair_access
bike_allowed
air_condition
</pre>
            </div>
</div>

<div id="block34" class="active" onclick="toggle(event);">
    
<div class="field">
    <div>#2&nbsp;&gt;</div>
    <div>object</div>
    <div>Route features to be additionally included or excluded to inherited ones.</div>
</div>

</div>
<div id="sub_block34" class="shift">
    
<div class="field">
    <div>include</div>
    <div>[]enum</div>
    <div>Features to be included additionally to inherited ones.
<pre class="addition">
wheelchair_access
bike_allowed
air_condition
</pre>
            </div>
</div>

<div class="field">
    <div>exclude</div>
    <div>[]enum</div>
    <div>Features to be excluded additionally to inherited ones.
<pre class="addition">
wheelchair_access
bike_allowed
air_condition
</pre>
            </div>
</div>

</div>

</div>

<div id="block36" class="active" onclick="toggle(event);">
    
<div class="field">
    <div>operationDays&nbsp;&gt;</div>
    <div>object</div>
    <div>Operation days of the route</div>
</div>

</div>
<div id="sub_block36" class="shift">
    
<div class="field">
    <div>weekdays</div>
    <div>[]enum</div>
    <div>Array of weekdays
<pre class="addition">
Mo
Tu
We
Th
Fr
Sa
Su
</pre>
            </div>
</div>

<div class="field">
    <div>include</div>
    <div>[]string</div>
    <div></div>
</div>

<div class="field">
    <div>exclude</div>
    <div>[]string</div>
    <div></div>
</div>

</div>

<div class="field">
    <div>timezone</div>
    <div>string</div>
    <div>Timezone where the agency operates and that is used for timetables</div>
</div>

<div id="block38" class="active" onclick="toggle(event);">
    
<div class="field">
    <div>icon&nbsp;&gt;</div>
    <div>one of</div>
    <div>Icon of the route</div>
</div>

</div>
<div id="sub_block38" class="shift">
    
<div class="field">
    <div>#1</div>
    <div>string</div>
    <div>Reference identifier to the geometry with or without format</div>
</div>

<div id="block37" class="active" onclick="toggle(event);">
    
<div class="field">
    <div>#2&nbsp;&gt;</div>
    <div>object</div>
    <div>Geometry of the entity</div>
</div>

</div>
<div id="sub_block37" class="shift">
    
<div class="field">
    <div>format<br /><span class="required">required</span></div>
    <div>enum</div>
    <div>Format of the geometry data
<pre class="addition">
base64_svg
base64_png
base64_jpg
geojson
</pre>
            </div>
</div>

<div class="field">
    <div>data<br /><span class="required">required</span></div>
    <div>unknown</div>
    <div>Geometry data of the entity</div>
</div>

</div>

</div>

<div id="block40" class="active" onclick="toggle(event);">
    
<div class="field">
    <div>shape&nbsp;&gt;</div>
    <div>one of</div>
    <div>Shape of the route</div>
</div>

</div>
<div id="sub_block40" class="shift">
    
<div class="field">
    <div>#1</div>
    <div>string</div>
    <div>Reference identifier to the geometry with or without format</div>
</div>

<div id="block39" class="active" onclick="toggle(event);">
    
<div class="field">
    <div>#2&nbsp;&gt;</div>
    <div>object</div>
    <div>Geometry of the entity</div>
</div>

</div>
<div id="sub_block39" class="shift">
    
<div class="field">
    <div>format<br /><span class="required">required</span></div>
    <div>enum</div>
    <div>Format of the geometry data
<pre class="addition">
base64_svg
base64_png
base64_jpg
geojson
</pre>
            </div>
</div>

<div class="field">
    <div>data<br /><span class="required">required</span></div>
    <div>unknown</div>
    <div>Geometry data of the entity</div>
</div>

</div>

</div>

<div id="block50" class="active" onclick="toggle(event);">
    
<div class="field">
    <div>trips&nbsp;&gt;</div>
    <div>[]object</div>
    <div></div>
</div>

</div>
<div id="sub_block50" class="shift">
    
<div id="block41" class="active" onclick="toggle(event);">
    
<div class="field">
    <div>name&nbsp;&gt;</div>
    <div>one of</div>
    <div>Name of the trip.</div>
</div>

</div>
<div id="sub_block41" class="shift">
    
<div class="field">
    <div>#1</div>
    <div>string</div>
    <div>Text in agency's language. Translation can be specified using Translation entities.</div>
</div>

<div class="field">
    <div>#2</div>
    <div>object</div>
    <div>Texts for different languages. Agency's language must be present.</div>
</div>

</div>

<div id="block42" class="active" onclick="toggle(event);">
    
<div class="field">
    <div>direction&nbsp;&gt;</div>
    <div>one of</div>
    <div>Direction of the trip.</div>
</div>

</div>
<div id="sub_block42" class="shift">
    
<div class="field">
    <div>#1</div>
    <div>string</div>
    <div>Text in agency's language. Translation can be specified using Translation entities.</div>
</div>

<div class="field">
    <div>#2</div>
    <div>object</div>
    <div>Texts for different languages. Agency's language must be present.</div>
</div>

</div>

<div id="block44" class="active" onclick="toggle(event);">
    
<div class="field">
    <div>features&nbsp;&gt;</div>
    <div>one of</div>
    <div>Features of the trip additionally to the route's features.</div>
</div>

</div>
<div id="sub_block44" class="shift">
    
<div class="field">
    <div>#1</div>
    <div>[]enum</div>
    <div>List of route features.
<pre class="addition">
wheelchair_access
bike_allowed
air_condition
</pre>
            </div>
</div>

<div id="block43" class="active" onclick="toggle(event);">
    
<div class="field">
    <div>#2&nbsp;&gt;</div>
    <div>object</div>
    <div>Route features to be additionally included or excluded to inherited ones.</div>
</div>

</div>
<div id="sub_block43" class="shift">
    
<div class="field">
    <div>include</div>
    <div>[]enum</div>
    <div>Features to be included additionally to inherited ones.
<pre class="addition">
wheelchair_access
bike_allowed
air_condition
</pre>
            </div>
</div>

<div class="field">
    <div>exclude</div>
    <div>[]enum</div>
    <div>Features to be excluded additionally to inherited ones.
<pre class="addition">
wheelchair_access
bike_allowed
air_condition
</pre>
            </div>
</div>

</div>

</div>

<div id="block49" class="active" onclick="toggle(event);">
    
<div class="field">
    <div>timetables&nbsp;&gt;<br /><span class="required">required</span></div>
    <div>[]one of</div>
    <div></div>
</div>

</div>
<div id="sub_block49" class="shift">
    
<div id="block47" class="active" onclick="toggle(event);">
    
<div class="field">
    <div>#1&nbsp;&gt;<br /><span class="required">required</span></div>
    <div>object</div>
    <div></div>
</div>

</div>
<div id="sub_block47" class="shift">
    
<div id="block46" class="active" onclick="toggle(event);">
    
<div class="field">
    <div>times&nbsp;&gt;<br /><span class="required">required</span></div>
    <div>[]one of</div>
    <div></div>
</div>

</div>
<div id="sub_block46" class="shift">
    
<div id="block45" class="active" onclick="toggle(event);">
    
<div class="field">
    <div>#1&nbsp;&gt;<br /><span class="required">required</span></div>
    <div>[string, string, string]</div>
    <div></div>
</div>

</div>
<div id="sub_block45" class="shift">
    
<div class="field">
    <div>[0]<br /><span class="required">required</span></div>
    <div>string</div>
    <div>Stop identifier.</div>
</div>

<div class="field">
    <div>[1]<br /><span class="required">required</span></div>
    <div>string</div>
    <div>Arrival time to the stop</div>
</div>

<div class="field">
    <div>[2]<br /><span class="required">required</span></div>
    <div>string</div>
    <div>Departure time from the stop</div>
</div>

</div>

<div class="field">
    <div>#2<br /><span class="required">required</span></div>
    <div>object</div>
    <div></div>
</div>

</div>

</div>

<div id="block48" class="active" onclick="toggle(event);">
    
<div class="field">
    <div>#2&nbsp;&gt;<br /><span class="required">required</span></div>
    <div>object</div>
    <div></div>
</div>

</div>
<div id="sub_block48" class="shift">
    
<div class="field">
    <div>firstTrip<br /><span class="required">required</span></div>
    <div>unknown</div>
    <div></div>
</div>

<div class="field">
    <div>interval<br /><span class="required">required</span></div>
    <div>integer</div>
    <div>Interval between trips in seconds</div>
</div>

<div class="field">
    <div>endTime<br /><span class="required">required</span></div>
    <div>string</div>
    <div>Time of the last trip</div>
</div>

</div>

</div>

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
