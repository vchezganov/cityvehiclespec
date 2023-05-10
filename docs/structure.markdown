---
layout: page
title: File structure
permalink: /structure
---

All files should be located in a folder or in a ZIP archive, and follow the structure:
```
settings.json
operator.json
operator/
├── operator_one.json
├── operator_two.json
│   ...
└── operator_n.json
place.json
place/
├── place_foo.json
├── place_bar.json
├── berlin/
│   ├── stop_a.json
│   └── stop_b.json
├── hamburg/
│   ├── stop_a.json
│   └── stop_b.json
│   ...
└── place_another.json
route.json
route/
├── route_0.json
├── route_1.json
│   ...
└── route_X1.json
...
```

Every entity (except `settings.json`) could be presented either in the corresponding root JSON file together with another entities,
or separately in the own JSON file inside the corresponding entity's subfolder. JSON files in the entity's
subfolder can be additionaly grouped using subfolders, for example, by location name, operator, or any other
logic grouping.

Depends on the data complexity, it is allowed to have data in any combination of having root JSON files and/or
files in entity's subfolders.

The main idea behind it, if entities are simple in terms of properties,
then they could be located in one file. But if any of entities has complex structure
or many properties, then it could be extracted into a separate file.

For example, below three options how data for operators could be presented:
### Only root JSON file
operator.json
```json
[
    {
        "id": "operator_foo",
        "name": "Foo Operator",
        "web": "https://foo.example.com"
    },
    {
        "id": "bar_operator",
        "name": "Bar Operator",
        "web": "https://bar.example.com"
    },
    {
        "id": "another",
        "name": "Another Operator",
        "web": "https://another.example.com"
    }
]
```


### Only inside entity's subfolder
operator/operator_foo.json
```json
{
    "id": "operator_foo",
    "name": "Foo Operator",
    "web": "https://foo.example.com"
}
```

operator/bar_operator.json
```json
{
    "id": "bar_operator",
    "name": "Bar Operator",
    "web": "https://bar.example.com"
}
```

operator/another.json
```json
{
    "id": "another",
    "name": "Another Operator",
    "web": "https://another.example.com"
}
```


### Root JSON file and inside entity's subfolder
operator.json
```json
[
    {
        "id": "operator_foo",
        "name": "Foo Operator",
        "web": "https://foo.example.com"
    },
    {
        "id": "bar_operator",
        "name": "Bar Operator",
        "web": "https://bar.example.com"
    }
]
```

operator/another.json
```json
{
    "id": "another",
    "name": "Another Operator",
    "web": "https://another.example.com",
    "icon": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAo0lEQVR4nO2TUQrCMBBE30cR/OmZvJifpb2Vd6kEv3qGSGURusnGtF1BsAMDy2Y2kwkJHPgLRAf+hsEWRIOXbxvcLIM99YwWmHQKPcDKOrLEVaconY6VCbIpvBMkKWoN4odap3ivebyiHEyDBuiAu7CTXmmTAXgofWKgOQprf7OlN8VnYY1JSZ8gZAaCcUVb9K/71JF7Rz0nGQrCQXpe+gMs8AQ318H4QPqjvwAAAABJRU5ErkJggg==",
    "loc": [52.5255170, 13.4153366]
}
```
