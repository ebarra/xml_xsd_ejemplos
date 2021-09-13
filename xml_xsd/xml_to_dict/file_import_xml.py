import xmltodict, json

with open('data.xml', 'r') as myfile:
    obj = xmltodict.parse(myfile.read())




print("EMPLOYEE NAME:")
print(obj["employees"]["employee"]['name'])

print("JSON DEL XML:")
print(json.dumps(obj))