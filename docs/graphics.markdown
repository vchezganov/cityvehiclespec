---
layout: page
title: Graphic
permalink: /graphics
---

- [Description](#description)
- [Schema](#schema)
- [Examples](#examples)


## Description
<div class="main">

<div class="field">
    <div>id</div>
    <div>string</div>
    <div>Unique identifier</div>
</div>

</div>

## Schema
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://github.com/vchezganov/cityjson/schema/graphics.json",
  "title": "Graphics",
  "type": "object",
  "properties": {
    "id": {
      "description": "Unique identifier",
      "type": "string"
    }
  },
  "required": []
}
```

## Examples
### #1
```json
{
  "type": "FeatureCollection",
  "features": [
    {
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
  ]
}
```
