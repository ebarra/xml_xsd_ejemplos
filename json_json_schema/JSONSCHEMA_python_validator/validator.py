import jsonschema
import json

with open('example.schema.json', 'r') as f:
    schema = json.load(f)

json_obj = {"name": "eggs", "price": 21.47}
jsonschema.validate(json_obj, schema)

json_obj = {"name": "eggs", "price": "blue"}
jsonschema.validate(json_obj, schema)
# jsonschema.exceptions.ValidationError: 'blue' is not of type 'number'
#
# Failed validating 'type' in schema['properties']['price']:
#     {'type': 'number'}
#
# On instance['price']:
#     'blue'