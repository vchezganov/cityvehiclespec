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
<div class="main">

<div class="field">
    <div>id<br /><span class="required">required</span></div>
    <div>string</div>
    <div>The unique identifier for an agency</div>
</div>

<div id="block2" class="active" onclick="toggle(event);">
    
<div class="field">
    <div>name&nbsp;&gt;<br /><span class="required">required</span></div>
    <div>one of</div>
    <div>Name of the agency</div>
</div>

</div>
<div id="sub_block2" class="shift">
    
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

<div id="block3" class="active" onclick="toggle(event);">
    
<div class="field">
    <div>description&nbsp;&gt;</div>
    <div>one of</div>
    <div>Description of the agency</div>
</div>

</div>
<div id="sub_block3" class="shift">
    
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
    <div>web</div>
    <div>string</div>
    <div>Website of the agency</div>
</div>

<div id="block5" class="active" onclick="toggle(event);">
    
<div class="field">
    <div>phone&nbsp;&gt;</div>
    <div>one of</div>
    <div>Phone number(s) of the agency</div>
</div>

</div>
<div id="sub_block5" class="shift">
    
<div class="field">
    <div>#1</div>
    <div>string</div>
    <div>Main phone number of the agency
<div markdown="1">
```json
"phone": "+1234567890"
```
</div>
                </div>
</div>

<div id="block4" class="active" onclick="toggle(event);">
    
<div class="field">
    <div>#2&nbsp;&gt;</div>
    <div>[]object</div>
    <div>Various phone number of the agency
<div markdown="1">
```json
"phone": [
  {
    "phoneType": "support",
    "value": "+1234567890"
  },
  {
    "phoneType": "information",
    "value": "+0987654321"
  }
]
```
</div>
                </div>
</div>

</div>
<div id="sub_block4" class="shift">
    
<div class="field">
    <div>phoneType<br /><span class="required">required</span></div>
    <div>enum</div>
    <div>Type of the phone (support, information, etc)
<pre class="addition">
main
support
information
</pre>
            </div>
</div>

<div class="field">
    <div>value<br /><span class="required">required</span></div>
    <div>string</div>
    <div>Phone number</div>
</div>

</div>

</div>

<div id="block7" class="active" onclick="toggle(event);">
    
<div class="field">
    <div>email&nbsp;&gt;</div>
    <div>one of</div>
    <div>Email address(es) of the agency</div>
</div>

</div>
<div id="sub_block7" class="shift">
    
<div class="field">
    <div>#1</div>
    <div>string</div>
    <div>Main email address of the agency</div>
</div>

<div id="block6" class="active" onclick="toggle(event);">
    
<div class="field">
    <div>#2&nbsp;&gt;</div>
    <div>[]object</div>
    <div></div>
</div>

</div>
<div id="sub_block6" class="shift">
    
<div class="field">
    <div>emailType<br /><span class="required">required</span></div>
    <div>enum</div>
    <div>Type of the email (support, information, etc)
<pre class="addition">
main
support
information
</pre>
            </div>
</div>

<div class="field">
    <div>value<br /><span class="required">required</span></div>
    <div>string</div>
    <div>Email address</div>
</div>

</div>

</div>

<div class="field">
    <div>timezone</div>
    <div>string</div>
    <div>Timezone where the agency operates and that is used for timetables</div>
</div>

<div id="block10" class="active" onclick="toggle(event);">
    
<div class="field">
    <div>loc&nbsp;&gt;</div>
    <div>one of</div>
    <div>Location of the agency</div>
</div>

</div>
<div id="sub_block10" class="shift">
    
<div id="block8" class="active" onclick="toggle(event);">
    
<div class="field">
    <div>#1&nbsp;&gt;</div>
    <div>[number, number, number]</div>
    <div>Array of coordinates</div>
</div>

</div>
<div id="sub_block8" class="shift">
    
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

<div id="block9" class="active" onclick="toggle(event);">
    
<div class="field">
    <div>#2&nbsp;&gt;</div>
    <div>object</div>
    <div>Object of coordinates</div>
</div>

</div>
<div id="sub_block9" class="shift">
    
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
    <div>icon</div>
    <div>string</div>
    <div>Icon for the agency in base64 format</div>
</div>

<div class="field">
    <div>language<br /><span class="required">required</span></div>
    <div>string</div>
    <div>Default language for the agency</div>
</div>

</div>

## Schema
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://github.com/vchezganov/cityjson/schema/agencies.json",
  "title": "Agency",
  "type": "object",
  "properties": {
    "id": {
      "description": "The unique identifier for an agency",
      "type": "string"
    },
    "name": {
      "description": "Name of the agency",
      "$ref": "definitions.json#/$defs/translation"
    },
    "description": {
      "description": "Description of the agency",
      "$ref": "definitions.json#/$defs/translation"
    },
    "web": {
      "description": "Website of the agency",
      "type": "string"
    },
    "phone": {
      "description": "Phone number(s) of the agency",
      "oneOf": [
        {
          "description": "Main phone number of the agency",
          "type": "string",
          "examples": [
            {
              "phone": "+1234567890"
            }
          ]
        },
        {
          "type": "array",
          "items": {
            "description": "Various phone number of the agency",
            "type": "object",
            "properties": {
              "phoneType": {
                "description": "Type of the phone (support, information, etc)",
                "enum": [
                  "main",
                  "support",
                  "information"
                ]
              },
              "value": {
                "description": "Phone number",
                "type": "string"
              }
            },
            "required": [
              "phoneType",
              "value"
            ],
            "uniqueItems": true
          }
        }
      ]
    },
    "email": {
      "description": "Email address(es) of the agency",
      "oneOf": [
        {
          "description": "Main email address of the agency",
          "type": "string"
        },
        {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "emailType": {
                "description": "Type of the email (support, information, etc)",
                "enum": [
                  "main",
                  "support",
                  "information"
                ]
              },
              "value": {
                "description": "Email address",
                "type": "string"
              }
            },
            "required": [
              "emailType",
              "value"
            ],
            "uniqueItems": true
          }
        }
      ]
    },
    "timezone": {
      "description": "Timezone where the agency operates and that is used for timetables",
      "type": "string"
    },
    "loc": {
      "description": "Location of the agency",
      "$ref": "definitions.json#/$defs/location"
    },
    "icon": {
      "description": "Icon for the agency in base64 format",
      "type": "string"
    },
    "language": {
      "description": "Default language for the agency",
      "type": "string"
    }
  },
  "required": [
    "id",
    "name",
    "language"
  ]
}
```

## Examples
### #1
```json
{
  "id": "A01",
  "name": "Agency 01",
  "language": "en"
}
```
### #2
```json
{
  "id": "A02",
  "name": "Agency 02",
  "language": "en-US",
  "phone": [
    {
      "phoneType": "information",
      "value": "54321"
    },
    {
      "phoneType": "support",
      "value": "12345"
    }
  ]
}
```
### #3
```json
{
  "id": "A03",
  "name": {
    "en": "Agency 03",
    "de": "Verkehrsbetriebe 03"
  },
  "language": "de",
  "phone": [
    {
      "phoneType": "information",
      "value": "54321"
    },
    {
      "phoneType": "support",
      "value": "12345"
    }
  ],
  "loc": [
    52.525517,
    13.4153366
  ]
}
```
