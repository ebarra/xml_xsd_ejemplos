# Example usage for add_local_schemas_to

import json
import jsonschema
from local_ref import add_local_schemas_to
from pathlib import Path

instance_filename = 'data.json'
schema_folder = Path('schemas')
schema_filename = schema_folder / 'root.schema.json'
base_uri = 'https://www.example.com/schemas/'

with open("schemas/file.schema.json") as schema_file:
    schema = json.load(schema_file)
    
with open("file.json") as instance_file:
    instance = json.load(instance_file)

resolver = jsonschema.RefResolver(base_uri=base_uri, referrer=schema)
add_local_schemas_to(resolver, schema_folder, base_uri)
jsonschema.validate(instance, schema, resolver=resolver)