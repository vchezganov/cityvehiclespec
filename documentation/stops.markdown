---
layout: page
title: Stops
permalink: /stops
---

- [Description](#description)
- [Schema](#schema)
- [Examples](#examples)

**Agency** entity presents information about certain provider. It could be
a bus operator, a rail agency, or a mobility provider for shared vehicles.


<div class="field">
    <div>id<br /><span class="required">required</span></div>
    <div>string</div>
    <div>Unique identifier for the stop</div>
</div>

<div id="block11" class="active" onclick="toggle(event);">
    
<div class="field">
    <div>name&nbsp;&gt;<br /><span class="required">required</span></div>
    <div>one of</div>
    <div>Name of the stop</div>
</div>

</div>
<div id="sub_block11" class="shift">
    
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

<div id="block12" class="active" onclick="toggle(event);">
    
<div class="field">
    <div>description&nbsp;&gt;</div>
    <div>one of</div>
    <div>Description of the stop</div>
</div>

</div>
<div id="sub_block12" class="shift">
    
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

<div id="block15" class="active" onclick="toggle(event);">
    
<div class="field">
    <div>loc&nbsp;&gt;<br /><span class="required">required</span></div>
    <div>one of</div>
    <div>Location of the stop</div>
</div>

</div>
<div id="sub_block15" class="shift">
    
<div id="block13" class="active" onclick="toggle(event);">
    
<div class="field">
    <div>#1&nbsp;&gt;<br /><span class="required">required</span></div>
    <div>[number, number, number]</div>
    <div>Array of coordinates</div>
</div>

</div>
<div id="sub_block13" class="shift">
    
<div class="field">
    <div>[0]<br /><span class="required">required</span></div>
    <div>number</div>
    <div>Longitude</div>
</div>

<div class="field">
    <div>[1]<br /><span class="required">required</span></div>
    <div>number</div>
    <div>Latitude</div>
</div>

<div class="field">
    <div>[2]</div>
    <div>number</div>
    <div>Altitude in meters</div>
</div>

</div>

<div id="block14" class="active" onclick="toggle(event);">
    
<div class="field">
    <div>#2&nbsp;&gt;<br /><span class="required">required</span></div>
    <div>object</div>
    <div>Object of coordinates</div>
</div>

</div>
<div id="sub_block14" class="shift">
    
<div class="field">
    <div>lon<br /><span class="required">required</span></div>
    <div>number</div>
    <div>Longitude</div>
</div>

<div class="field">
    <div>lat<br /><span class="required">required</span></div>
    <div>number</div>
    <div>Latitude</div>
</div>

<div class="field">
    <div>alt</div>
    <div>number</div>
    <div>Altitude in meters</div>
</div>

</div>

</div>

<div class="field">
    <div>web</div>
    <div>string</div>
    <div>Website of the stop</div>
</div>

<div id="block17" class="active" onclick="toggle(event);">
    
<div class="field">
    <div>features&nbsp;&gt;</div>
    <div>one of</div>
    <div>Features of the stop. All access points and child stops, if any, inherit these features.</div>
</div>

</div>
<div id="sub_block17" class="shift">
    
<div class="field">
    <div>#1</div>
    <div>[]enum</div>
    <div>List of stop features.
<pre class="addition">
wheelchair_access
elevator
upstairs_escalator
downstairs_escalator
</pre>
            </div>
</div>

<div id="block16" class="active" onclick="toggle(event);">
    
<div class="field">
    <div>#2&nbsp;&gt;</div>
    <div>object</div>
    <div>Stop features to be additionally included or excluded to inherited ones.</div>
</div>

</div>
<div id="sub_block16" class="shift">
    
<div class="field">
    <div>include</div>
    <div>[]enum</div>
    <div>Features to be included additionally to inherited ones.
<pre class="addition">
wheelchair_access
elevator
upstairs_escalator
downstairs_escalator
</pre>
            </div>
</div>

<div class="field">
    <div>exclude</div>
    <div>[]enum</div>
    <div>Features to be excluded additionally to inherited ones.
<pre class="addition">
wheelchair_access
elevator
upstairs_escalator
downstairs_escalator
</pre>
            </div>
</div>

</div>

</div>

<div class="field">
    <div>timezone</div>
    <div>string</div>
    <div>Timezone where the agency operates and that is used for timetables</div>
</div>

<div id="block23" class="active" onclick="toggle(event);">
    
<div class="field">
    <div>accessPoints&nbsp;&gt;</div>
    <div>[]object</div>
    <div>Access points of the stop</div>
</div>

</div>
<div id="sub_block23" class="shift">
    
<div class="field">
    <div>id<br /><span class="required">required</span></div>
    <div>string</div>
    <div>Unique identifier for the access point</div>
</div>

<div class="field">
    <div>name<br /><span class="required">required</span></div>
    <div>string</div>
    <div>Name of the access point</div>
</div>

<div id="block20" class="active" onclick="toggle(event);">
    
<div class="field">
    <div>loc&nbsp;&gt;<br /><span class="required">required</span></div>
    <div>one of</div>
    <div>Location of the access point</div>
</div>

</div>
<div id="sub_block20" class="shift">
    
<div id="block18" class="active" onclick="toggle(event);">
    
<div class="field">
    <div>#1&nbsp;&gt;<br /><span class="required">required</span></div>
    <div>[number, number, number]</div>
    <div>Array of coordinates</div>
</div>

</div>
<div id="sub_block18" class="shift">
    
<div class="field">
    <div>[0]<br /><span class="required">required</span></div>
    <div>number</div>
    <div>Longitude</div>
</div>

<div class="field">
    <div>[1]<br /><span class="required">required</span></div>
    <div>number</div>
    <div>Latitude</div>
</div>

<div class="field">
    <div>[2]</div>
    <div>number</div>
    <div>Altitude in meters</div>
</div>

</div>

<div id="block19" class="active" onclick="toggle(event);">
    
<div class="field">
    <div>#2&nbsp;&gt;<br /><span class="required">required</span></div>
    <div>object</div>
    <div>Object of coordinates</div>
</div>

</div>
<div id="sub_block19" class="shift">
    
<div class="field">
    <div>lon<br /><span class="required">required</span></div>
    <div>number</div>
    <div>Longitude</div>
</div>

<div class="field">
    <div>lat<br /><span class="required">required</span></div>
    <div>number</div>
    <div>Latitude</div>
</div>

<div class="field">
    <div>alt</div>
    <div>number</div>
    <div>Altitude in meters</div>
</div>

</div>

</div>

<div id="block22" class="active" onclick="toggle(event);">
    
<div class="field">
    <div>features&nbsp;&gt;</div>
    <div>one of</div>
    <div>Features of the access point (additionally to inherited from the parent stop)</div>
</div>

</div>
<div id="sub_block22" class="shift">
    
<div class="field">
    <div>#1</div>
    <div>[]enum</div>
    <div>List of stop features.
<pre class="addition">
wheelchair_access
elevator
upstairs_escalator
downstairs_escalator
</pre>
            </div>
</div>

<div id="block21" class="active" onclick="toggle(event);">
    
<div class="field">
    <div>#2&nbsp;&gt;</div>
    <div>object</div>
    <div>Stop features to be additionally included or excluded to inherited ones.</div>
</div>

</div>
<div id="sub_block21" class="shift">
    
<div class="field">
    <div>include</div>
    <div>[]enum</div>
    <div>Features to be included additionally to inherited ones.
<pre class="addition">
wheelchair_access
elevator
upstairs_escalator
downstairs_escalator
</pre>
            </div>
</div>

<div class="field">
    <div>exclude</div>
    <div>[]enum</div>
    <div>Features to be excluded additionally to inherited ones.
<pre class="addition">
wheelchair_access
elevator
upstairs_escalator
downstairs_escalator
</pre>
            </div>
</div>

</div>

</div>

</div>

<div id="block29" class="active" onclick="toggle(event);">
    
<div class="field">
    <div>childStops&nbsp;&gt;</div>
    <div>[]object</div>
    <div>Child stops of the stop</div>
</div>

</div>
<div id="sub_block29" class="shift">
    
<div class="field">
    <div>id<br /><span class="required">required</span></div>
    <div>string</div>
    <div>Unique identifier for the child point</div>
</div>

<div class="field">
    <div>name<br /><span class="required">required</span></div>
    <div>string</div>
    <div>Name of the child point</div>
</div>

<div id="block26" class="active" onclick="toggle(event);">
    
<div class="field">
    <div>loc&nbsp;&gt;<br /><span class="required">required</span></div>
    <div>one of</div>
    <div>Location of the child point</div>
</div>

</div>
<div id="sub_block26" class="shift">
    
<div id="block24" class="active" onclick="toggle(event);">
    
<div class="field">
    <div>#1&nbsp;&gt;<br /><span class="required">required</span></div>
    <div>[number, number, number]</div>
    <div>Array of coordinates</div>
</div>

</div>
<div id="sub_block24" class="shift">
    
<div class="field">
    <div>[0]<br /><span class="required">required</span></div>
    <div>number</div>
    <div>Longitude</div>
</div>

<div class="field">
    <div>[1]<br /><span class="required">required</span></div>
    <div>number</div>
    <div>Latitude</div>
</div>

<div class="field">
    <div>[2]</div>
    <div>number</div>
    <div>Altitude in meters</div>
</div>

</div>

<div id="block25" class="active" onclick="toggle(event);">
    
<div class="field">
    <div>#2&nbsp;&gt;<br /><span class="required">required</span></div>
    <div>object</div>
    <div>Object of coordinates</div>
</div>

</div>
<div id="sub_block25" class="shift">
    
<div class="field">
    <div>lon<br /><span class="required">required</span></div>
    <div>number</div>
    <div>Longitude</div>
</div>

<div class="field">
    <div>lat<br /><span class="required">required</span></div>
    <div>number</div>
    <div>Latitude</div>
</div>

<div class="field">
    <div>alt</div>
    <div>number</div>
    <div>Altitude in meters</div>
</div>

</div>

</div>

<div id="block28" class="active" onclick="toggle(event);">
    
<div class="field">
    <div>features&nbsp;&gt;</div>
    <div>one of</div>
    <div>Features of the child point (additionally to inherited from the parent stop)</div>
</div>

</div>
<div id="sub_block28" class="shift">
    
<div class="field">
    <div>#1</div>
    <div>[]enum</div>
    <div>List of stop features.
<pre class="addition">
wheelchair_access
elevator
upstairs_escalator
downstairs_escalator
</pre>
            </div>
</div>

<div id="block27" class="active" onclick="toggle(event);">
    
<div class="field">
    <div>#2&nbsp;&gt;</div>
    <div>object</div>
    <div>Stop features to be additionally included or excluded to inherited ones.</div>
</div>

</div>
<div id="sub_block27" class="shift">
    
<div class="field">
    <div>include</div>
    <div>[]enum</div>
    <div>Features to be included additionally to inherited ones.
<pre class="addition">
wheelchair_access
elevator
upstairs_escalator
downstairs_escalator
</pre>
            </div>
</div>

<div class="field">
    <div>exclude</div>
    <div>[]enum</div>
    <div>Features to be excluded additionally to inherited ones.
<pre class="addition">
wheelchair_access
elevator
upstairs_escalator
downstairs_escalator
</pre>
            </div>
</div>

</div>

</div>

</div>

<div class="field">
    <div>icon</div>
    <div>string</div>
    <div>Icon for the agency in base64 format</div>
</div>

<div id="block31" class="active" onclick="toggle(event);">
    
<div class="field">
    <div>graphics&nbsp;&gt;</div>
    <div>one of</div>
    <div></div>
</div>

</div>
<div id="sub_block31" class="shift">
    
<div class="field">
    <div>#1</div>
    <div>string</div>
    <div>Reference identifier to the geometry with or without format</div>
</div>

<div id="block30" class="active" onclick="toggle(event);">
    
<div class="field">
    <div>#2&nbsp;&gt;</div>
    <div>object</div>
    <div>Geometry of the entity</div>
</div>

</div>
<div id="sub_block30" class="shift">
    
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
