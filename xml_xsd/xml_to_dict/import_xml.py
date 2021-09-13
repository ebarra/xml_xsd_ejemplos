import xmltodict, json

obj = xmltodict.parse("""
<employees>
	<employee>
  		<name>Dave</name>
        <role>Sale Assistant</role>
        <age>34</age>
    </employee>
</employees>
""")

print("OBJ ES UN PYTHON DICT:")
print(type(obj))

print("EMPLOYEE NAME:")
print(obj["employees"]["employee"]['name'])

print("JSON DEL XML:")
print(json.dumps(obj))

