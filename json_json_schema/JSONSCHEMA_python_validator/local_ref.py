import os
import json
from pathlib import Path
from urllib.parse import urljoin

import jsonschema

def add_local_schemas_to(resolver, schema_folder, base_uri, schema_ext='.schema.json'):
    ''' Add local schema instances to a resolver schema cache. 
        Para poder resolver las refs locales en lugar de URLs: https://gist.github.com/mrtj/d59812a981da17fbaa67b7de98ac3d4b
        https://github.com/Julian/jsonschema/issues/313
    Arguments:
        resolver (jsonschema.RefResolver): the reference resolver
        schema_folder (str): the local folder of the schemas. 
        base_uri (str): the base URL that you actually use in your '$id' tags 
            in the schemas
        schema_ext (str): filter files with this extension in the schema_folder
    '''
    for dir, _, files in os.walk(schema_folder):
        for file in files:
            if file.endswith(schema_ext):
                schema_path = Path(dir) / Path(file)
                rel_path = schema_path.relative_to(schema_folder)
                with open(schema_path) as schema_file:
                    schema_doc = json.load(schema_file)
                key = urljoin(base_uri, str(rel_path))
                resolver.store[key] = schema_doc