from lxml import etree
import xmltodict, json

class Validator:
    def __init__(self, xsd_path: str):
        xmlschema_doc = etree.parse(xsd_path)
        self.xmlschema = etree.XMLSchema(xmlschema_doc)

    #see https://lxml.de/validation.html#xmlschema
    def validate(self, xml_path: str) -> bool:
        xml_doc = etree.parse(xml_path)
        result = self.xmlschema.validate(xml_doc)
        log = self.xmlschema.error_log
        print(log.last_error)
        return result

#descomentar si se ejecuta este archivo directamente en lugar que desde main.py
validator = Validator("catalogo.xsd")
validator.validate("catalogo.xml")

with open('catalogo.xml', 'r', encoding='utf8') as myfile:
    #directamente cojo "catalogo" porque en xml hay un único root y en json eso no me convence
    obj = xmltodict.parse(myfile.read())["catalogo"]
    #también existe un parámetro de xmltodict.parse que es force_list que se puede probar para forzar que transforme en listas determinados elementos
    #obj = xmltodict.parse(myfile.read(), force_list=('productos'))["catalogo"]


print(obj)

#Los arrays los transforma un poco raro, hace un objeto con el primer elemento y ahí pone el array
obj["productos"] = obj["productos"]["producto"]

#añadimos la propiedad $schema
obj["$schema"] = "./banda.schema.json"

print("JSON DEL XML:")
print(json.dumps(obj, indent=4, ensure_ascii=False))

with open('catalogo.json', 'w', encoding='utf8') as outfile:
    json.dump(obj, outfile, indent=4, ensure_ascii=False)