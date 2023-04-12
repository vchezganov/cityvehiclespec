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
<div class="main">

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

</div>

## Schema
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://github.com/vchezganov/cityjson/schema/stops.json",
  "title": "Stop",
  "type": "object",
  "properties": {
    "id": {
      "description": "Unique identifier for the stop",
      "type": "string"
    },
    "name": {
      "description": "Name of the stop",
      "$ref": "definitions.json#/$defs/translation"
    },
    "description": {
      "description": "Description of the stop",
      "$ref": "definitions.json#/$defs/translation"
    },
    "loc": {
      "description": "Location of the stop",
      "$ref": "definitions.json#/$defs/location"
    },
    "web": {
      "description": "Website of the stop",
      "type": "string"
    },
    "features": {
      "description": "Features of the stop. All access points and child stops, if any, inherit these features.",
      "$ref": "definitions.json#/$defs/stopFeatures"
    },
    "timezone": {
      "description": "Timezone where the agency operates and that is used for timetables",
      "type": "string"
    },
    "accessPoints": {
      "description": "Access points of the stop",
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "description": "Unique identifier for the access point",
            "type": "string"
          },
          "name": {
            "description": "Name of the access point",
            "type": "string"
          },
          "loc": {
            "description": "Location of the access point",
            "$ref": "definitions.json#/$defs/location"
          },
          "features": {
            "description": "Features of the access point (additionally to inherited from the parent stop)",
            "$ref": "definitions.json#/$defs/stopFeatures"
          }
        },
        "required": [
          "id",
          "name",
          "loc"
        ]
      }
    },
    "childStops": {
      "description": "Child stops of the stop",
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "description": "Unique identifier for the child point",
            "type": "string"
          },
          "name": {
            "description": "Name of the child point",
            "type": "string"
          },
          "loc": {
            "description": "Location of the child point",
            "$ref": "definitions.json#/$defs/location"
          },
          "features": {
            "description": "Features of the child point (additionally to inherited from the parent stop)",
            "$ref": "definitions.json#/$defs/stopFeatures"
          }
        },
        "required": [
          "id",
          "name",
          "loc"
        ]
      }
    },
    "icon": {
      "description": "Icon for the agency in base64 format",
      "type": "string"
    },
    "graphics": {
      "$ref": "definitions.json#/$defs/graphics"
    }
  },
  "required": [
    "id",
    "name",
    "loc"
  ]
}
```

## Examples
### #1
```json
{
  "id": "01",
  "name": "Stop 01",
  "description": {
    "en": "Bus stop for interregional trips",
    "de-de": "Bushaltestelle für interregionale Reisen"
  },
  "loc": [
    13.404954,
    52.520008,
    34
  ],
  "stopType": "parent",
  "timezone": "Europe/Berlin",
  "features": [
    "wheelchair_access",
    "elevator",
    "upstairs_escalator"
  ],
  "accessPoints": [
    {
      "id": "01-ap01",
      "name": "West side entrance",
      "loc": [
        12.345678,
        87.654321
      ],
      "features": [
        "downstairs_escalator"
      ]
    }
  ],
  "childStops": [],
  "icon": "",
  "graphics": {
    "format": "geojson",
    "data": {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "coordinates": [
          [
            [
              13.368270255270005,
              52.52573885487206
            ],
            [
              13.36928032987069,
              52.52428739765102
            ],
            [
              13.369625881706838,
              52.52428335452754
            ],
            [
              13.369708947053311,
              52.524160039088116
            ],
            [
              13.37039340549967,
              52.524162060655414
            ],
            [
              13.370293727085027,
              52.52428335452754
            ],
            [
              13.370635956307524,
              52.52427931140406
            ],
            [
              13.369632526935476,
              52.52573885487206
            ],
            [
              13.36928032987069,
              52.52573885487206
            ],
            [
              13.369190619297001,
              52.525866208857366
            ],
            [
              13.368542709603389,
              52.52586823034653
            ],
            [
              13.36862577494847,
              52.525734811882614
            ],
            [
              13.368270255270005,
              52.52573885487206
            ]
          ]
        ],
        "type": "Polygon"
      }
    }
  }
}
```
### #2
```json
{
  "id": "02",
  "name": "Stop 02",
  "loc": [
    13.404954,
    52.520008,
    0
  ],
  "stopType": "parent",
  "timezone": "Europe/Berlin",
  "features": [
    "wheelchair_access",
    "elevator",
    "upstairs_escalator"
  ],
  "accessPoints": [
    {
      "id": "02-ap01",
      "name": "West side entrance",
      "loc": [
        12.345678,
        87.654321
      ],
      "features": {
        "exclude": [
          "upstairs_escalator"
        ],
        "include": [
          "downstairs_escalator"
        ]
      }
    }
  ],
  "childStops": [
    {
      "id": "02-child01",
      "name": "Platform 1",
      "description": "Has no features",
      "loc": {
        "lon": 12.345678,
        "lat": 87.654321
      },
      "features": []
    }
  ]
}
```
