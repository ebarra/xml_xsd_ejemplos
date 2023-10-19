import xmltodict, json
import ast
import io

#obtenido de: https://github.com/martinblech/xmltodict/issues/209
def auto_cast_str(val):
  # Try fails if cannot eval, therefore is string
  try:
    val = ast.literal_eval(val)
  except:
    pass
  return val

def xml_postprocessor(path, key, value):
  # XML standard requires lower case bools
  if value == "true": value = "True"
  if value == "false": value = "False"
  return key, auto_cast_str(value)

#otro ejemplo de postprocessor
def postprocessor(path, key, value):
    if key == 'age':
        return key, int(value)
    return key, value


with io.open('data.xml', mode='r', encoding='utf8') as myfile:
    obj = xmltodict.parse(myfile.read(), postprocessor=xml_postprocessor)


print("EMPLOYEE NAME:")
print(obj["employees"]["employee"]['name'])

print("JSON DEL XML:")
print(json.dumps(obj, ensure_ascii=False))

#save json to file with indent, with uf8 encoding
with io.open('data.json', mode='w', encoding='utf8') as outfile:
    json.dump(obj, outfile, indent=4, ensure_ascii=False)