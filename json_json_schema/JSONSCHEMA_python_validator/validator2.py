import jsonschema
import json

with open('example.schema.json', 'r') as f:
    schema = json.load(f)

with open('example.json', 'r') as f:
    json_obj = json.load(f)

jsonschema.validate(json_obj, schema)