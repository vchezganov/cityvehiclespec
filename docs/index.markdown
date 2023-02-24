---
layout: page
permalink: /
---

**CityJSON** is the specification for _public transit_ data (stops, routes, timetables, etc)
and _mobility_ data (personal or shared scooters, bikes, cars, etc). It is an attempt
to improve and join two specifications
[GTFS](https://developers.google.com/transit/gtfs/reference){:target="_blank"} and
[GBFS](https://github.com/MobilityData/gbfs){:target="_blank"} into one.

The data format is [JSON](https://www.json.org/){:target="_blank"} and
every entity is described using [JSON schema](https://json-schema.org/){:target="_blank"}.
It also allows to validate entities for basic errors.

> All logic errors, like correctness of timetables, uniqueness of identifiers, etc, should be validated separatelly.

## Content
- [File structure](./structure.markdown)
- [Data settings](./settings.markdown)
- Entities
  - [Agency](./agencies.markdown)
  - [Stop](./stops.markdown)
  - [Route](./routes.markdown)
