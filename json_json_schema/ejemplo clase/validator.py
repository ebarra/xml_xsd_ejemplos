import jsonschema
import json

with open('catalogo.schema.json', 'r') as f:
    schema = json.load(f)

with open("catalogo.json") as instance_file:
    instance = json.load(instance_file)


jsonschema.validate(instance, schema)

