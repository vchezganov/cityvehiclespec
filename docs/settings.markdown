---
layout: page
title: Settings
permalink: /settings
---

- [Description](#description)
- [Schema](#schema)
- [Examples](#examples)

**Settings** contains information about data like version, validity, etc. In addition to that,
there are settings for default language, default transfer times between trips,
links for realtime data, etc.

## Description
<div class="main">

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

</div>

## Schema
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://github.com/vchezganov/cityjson/schema/settings.json",
  "title": "Settings",
  "type": "object",
  "properties": {
    "schemaVersion": {
      "description": "Version of the schema",
      "type": "string"
    },
    "dataVersion": {
      "description": "Version of the data",
      "type": "string"
    },
    "name": {
      "description": "Name of the data",
      "type": "string"
    },
    "language": {
      "description": "Default language of the data",
      "type": "string"
    },
    "validity": {
      "description": "Validity of the data",
      "type": "object",
      "properties": {
        "from": {
          "type": "string",
          "format": "date"
        },
        "to": {
          "type": "string",
          "format": "date"
        }
      },
      "required": [
        "from",
        "to"
      ]
    },
    "sameStopTransferTime": {
      "description": "Default transfer time on the same stop",
      "type": "integer"
    },
    "childStopTransferTime": {
      "description": "Default transfer time between child stops",
      "type": "integer"
    }
  },
  "required": [
    "schemaVersion",
    "dataVersion",
    "language",
    "validity",
    "sameStopTransferTime",
    "childStopTransferTime"
  ]
}
```

## Examples
### #1
```json
{
  "schemaVersion": "0.1.0",
  "dataVersion": "0.1.0",
  "language": "en",
  "validity": {
    "from": "2023-01-01",
    "to": "2023-12-31"
  },
  "sameStopTransferTime": 120,
  "childStopTransferTime": 240
}
```
