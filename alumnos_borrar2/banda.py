from lxml import etree

import xmltodict,json

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


validator = Validator('banda.xsd')
validator.validate('banda.xml')





with open ('banda.xml', mode = 'r', encoding= 'UTF8') as f :
    data = xmltodict.parse(f.read())

data['Banda']['Nombre'] = 'Familia'


data['Banda']['Miembros']['Miembro'][0] = 'Carlota Munoz de Luna '
data['Banda']['Miembros']['Miembro'][1] = 'Alberto Munoz de luna'
data['Banda']['Miembros']['Miembro'][2] = 'Manrta Munoz de luna'
data['Banda']['Miembros']['Miembro'][3] = 'Maria Jose Eusebio'
data['Banda']['Miembros']['Nacionalidad'][0]= 'Espanola'
data['Banda']['Miembros']['Nacionalidad'][1]= 'Espanola'
data['Banda']['Miembros']['Nacionalidad'][2]= 'Espanola'
data['Banda']['Miembros']['Nacionalidad'][3]= 'Espanola'



pasar=  json.dumps(data)
with open ('banda.json',mode='w', encoding='UTF-8') as f:
    json.dump(data, f, indent=3)





