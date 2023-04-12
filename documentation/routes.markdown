---
layout: page
title: Route
permalink: /routes
---

- [Description](#description)
- [Schema](#schema)
- [Examples](#examples)

**Route** entity presents information about certain route. It contains information
about the route (name, line color, vehicle type, shape etc) and timetables for trips.

## Description
<div class="main">

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

</div>

## Schema
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://github.com/vchezganov/cityjson/schema/routes.json",
  "title": "Route",
  "type": "object",
  "properties": {
    "id": {
      "description": "Unique identifier for the route",
      "type": "string"
    },
    "agency": {
      "description": "Agency's identifier the route belongs to",
      "type": "string"
    },
    "name": {
      "description": "Name of the route",
      "$ref": "definitions.json#/$defs/translation"
    },
    "description": {
      "description": "Description of the route",
      "$ref": "definitions.json#/$defs/translation"
    },
    "lineColor": {
      "description": "Line color of the route",
      "$ref": "definitions.json#/$defs/color"
    },
    "fontColor": {
      "description": "Font color of the route",
      "$ref": "definitions.json#/$defs/color"
    },
    "vehicleType": {
      "description": "Vehicle type of the route",
      "type": [
        "string",
        "number"
      ]
    },
    "features": {
      "description": "Features of the trip.",
      "$ref": "definitions.json#/$defs/routeFeatures"
    },
    "operationDays": {
      "description": "Operation days of the route",
      "$ref": "definitions.json#/$defs/operationDays"
    },
    "timezone": {
      "description": "Timezone where the agency operates and that is used for timetables",
      "type": "string"
    },
    "icon": {
      "description": "Icon of the route",
      "$ref": "definitions.json#/$defs/graphics"
    },
    "shape": {
      "description": "Shape of the route",
      "$ref": "definitions.json#/$defs/graphics"
    },
    "trips": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "description": "Name of the trip.",
            "$ref": "definitions.json#/$defs/translation"
          },
          "direction": {
            "description": "Direction of the trip.",
            "$ref": "definitions.json#/$defs/translation"
          },
          "features": {
            "description": "Features of the trip additionally to the route's features.",
            "$ref": "definitions.json#/$defs/routeFeatures"
          },
          "timetables": {
            "type": "array",
            "items": {
              "oneOf": [
                {
                  "type": "object",
                  "properties": {
                    "times": {
                      "type": "array",
                      "items": {
                        "oneOf": [
                          {
                            "type": "array",
                            "minItems": 3,
                            "maxItems": 3,
                            "prefixItems": [
                              {
                                "description": "Stop identifier.",
                                "type": "string"
                              },
                              {
                                "description": "Arrival time to the stop",
                                "$ref": "definitions.json#/$defs/time24"
                              },
                              {
                                "description": "Departure time from the stop",
                                "$ref": "definitions.json#/$defs/time24"
                              }
                            ]
                          },
                          {
                            "type": "object"
                          }
                        ]
                      }
                    }
                  },
                  "required": [
                    "times"
                  ]
                },
                {
                  "type": "object",
                  "properties": {
                    "firstTrip": {},
                    "interval": {
                      "description": "Interval between trips in seconds",
                      "type": "integer"
                    },
                    "endTime": {
                      "description": "Time of the last trip",
                      "type": "string"
                    }
                  },
                  "required": [
                    "firstTrip",
                    "interval",
                    "endTime"
                  ]
                }
              ]
            }
          }
        },
        "required": [
          "timetables"
        ]
      }
    }
  },
  "required": [
    "id",
    "name",
    "agency"
  ]
}
```

## Examples
### #1
```json
{
  "id": "R01",
  "agency": "A01",
  "name": "Route 01",
  "description": "Route One",
  "lineColor": "#770077",
  "fontColor": "#000000",
  "vehicleType": "bus",
  "features": [
    "bike_allowed",
    "wheelchair_access"
  ],
  "operationDays": {
    "weekdays": [
      "Mo",
      "Tu",
      "Fr"
    ],
    "include": [
      "2023-02-28",
      "2023-03-08"
    ],
    "exclude": [
      "2023-02-27"
    ]
  },
  "trips": [
    {
      "name": "Long trip",
      "direction": "To city center",
      "features": {
        "include": [
          "bike_allowed"
        ]
      },
      "timetables": [
        {
          "times": [
            [
              "S01",
              "10:00:00",
              "10:01:00"
            ],
            [
              "S02",
              "10:10:00",
              "10:10:00"
            ],
            [
              "S03",
              "10:15:00",
              "10:15:00"
            ],
            [
              "S04",
              "10:25:00",
              "10:30:00"
            ],
            [
              "S05",
              "10:50:00",
              "10:50:00"
            ],
            [
              "S06",
              "11:00:00",
              "11:00:00"
            ]
          ]
        },
        {
          "times": [
            [
              "S01",
              "10:10:00",
              "10:11:00"
            ],
            [
              "S02",
              "10:20:00",
              "10:20:00"
            ],
            [
              "S03",
              "10:25:00",
              "10:25:00"
            ],
            [
              "S04",
              "10:35:00",
              "10:40:00"
            ],
            [
              "S05",
              "11:00:00",
              "11:00:00"
            ],
            [
              "S06",
              "11:10:00",
              "11:10:00"
            ],
            {
              "stopID": "S07",
              "arrival": "11:20:00",
              "arrivalFeature": "noPickUp",
              "departure": "11:20:00"
            }
          ]
        },
        {
          "direction": "Short trip to city center",
          "features": {
            "include": [
              "air_condition"
            ],
            "exclude": [
              "bike_allow"
            ]
          },
          "operationDays": {
            "weekdays": [
              "Sa",
              "Su"
            ]
          },
          "times": [
            [
              "S02",
              "11:10:00",
              "11:10:00"
            ],
            [
              "S03",
              "11:15:00",
              "11:15:00"
            ],
            [
              "S04",
              "11:25:00",
              "11:30:00"
            ],
            [
              "S05",
              "11:50:00",
              "11:50:00"
            ]
          ]
        }
      ]
    },
    {
      "description": "From city center",
      "timetables": [
        {
          "firstTrip": [
            [
              "S05",
              "11:10:00",
              "11:10:00"
            ],
            [
              "S04",
              "11:15:00",
              "11:15:00"
            ],
            [
              "S03",
              "11:25:00",
              "11:30:00"
            ],
            [
              "S02",
              "11:50:00",
              "11:50:00"
            ]
          ],
          "interval": 600,
          "endTime": "20:00:00"
        }
      ]
    }
  ],
  "graphics": "G01_R01.svg"
}
```
### #2
```json
{
  "id": "R02",
  "agency": "A01",
  "name": "Route 02",
  "description": "Route Two",
  "lineColor": "#770077",
  "fontColor": "#000000",
  "vehicleType": "bus",
  "features": [
    "wheelchair_access",
    "bike_allowed"
  ],
  "operationDays": {
    "weekdays": [
      "Mo",
      "Tu",
      "Fr"
    ],
    "include": [
      "2023-02-28",
      "2023-03-08"
    ],
    "exclude": [
      "2023-02-27"
    ]
  },
  "trips": [
    {
      "name": "Long trip",
      "direction": "To city center",
      "features": [
        "bike_allowed"
      ],
      "timetables": [
        {
          "times": [
            [
              "S01",
              "10:00:00",
              "10:01:00"
            ],
            [
              "S02",
              "10:10:00",
              "10:10:00"
            ],
            [
              "S03",
              "10:15:00",
              "10:15:00"
            ],
            [
              "S04",
              "10:25:00",
              "10:30:00"
            ],
            [
              "S05",
              "10:50:00",
              "10:50:00"
            ],
            [
              "S06",
              "11:00:00",
              "11:00:00"
            ]
          ]
        },
        {
          "times": [
            [
              "S01",
              "10:10:00",
              "10:11:00"
            ],
            [
              "S02",
              "10:20:00",
              "10:20:00"
            ],
            [
              "S03",
              "10:25:00",
              "10:25:00"
            ],
            [
              "S04",
              "10:35:00",
              "10:40:00"
            ],
            [
              "S05",
              "11:00:00",
              "11:00:00"
            ],
            [
              "S06",
              "11:10:00",
              "11:10:00"
            ],
            {
              "stopID": "S07",
              "arrival": "11:20:00",
              "arrivalFeature": "noPickUp",
              "departure": "11:20:00"
            }
          ]
        },
        {
          "direction": "Short trip to city center",
          "features": {
            "include": [
              "air_condition"
            ],
            "exclude": [
              "bike_allowed"
            ]
          },
          "operationDays": {
            "weekdays": [
              "Sa",
              "Su"
            ]
          },
          "times": [
            [
              "S02",
              "11:10:00",
              "11:10:00"
            ],
            [
              "S03",
              "11:15:00",
              "11:15:00"
            ],
            [
              "S04",
              "11:25:00",
              "11:30:00"
            ],
            [
              "S05",
              "11:50:00",
              "11:50:00"
            ]
          ]
        }
      ]
    },
    {
      "description": "From city center",
      "timetables": [
        {
          "firstTrip": [
            [
              "S05",
              "11:10:00",
              "11:10:00"
            ],
            [
              "S04",
              "11:15:00",
              "11:15:00"
            ],
            [
              "S03",
              "11:25:00",
              "11:30:00"
            ],
            [
              "S02",
              "11:50:00",
              "11:50:00"
            ]
          ],
          "interval": 600,
          "endTime": "20:00:00"
        }
      ]
    }
  ]
}
```
