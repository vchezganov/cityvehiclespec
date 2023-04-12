---
layout: page
title: Translation
permalink: /translations
---

- [Description](#description)
- [Schema](#schema)
- [Examples](#examples)


## Description
<div class="main">

<div class="field">
    <div>text<br /><span class="required">required</span></div>
    <div>string</div>
    <div>Text having translations</div>
</div>

<div class="field">
    <div>translations</div>
    <div>object</div>
    <div>Translations of the text</div>
</div>

</div>

## Schema
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://github.com/vchezganov/cityjson/schema/translations.json",
  "title": "Translations",
  "type": "object",
  "properties": {
    "text": {
      "description": "Text having translations",
      "type": "string"
    },
    "translations": {
      "description": "Translations of the text",
      "type": "object"
    }
  },
  "required": [
    "text"
  ]
}
```

## Examples
### #1
```json
{
  "text": "Main train station",
  "translations": {
    "de": "Hauptbahnhof",
    "ru": "Главный ж/д вокзал"
  }
}
```
