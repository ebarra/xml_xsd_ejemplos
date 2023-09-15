from lxml import etree
import os

class Validator():
    def __init__(self, xsd_path):
          xmlschema_doc = etree.parse(xsd_path)
          self.xmlschema = etree.XMLSchema(xmlschema_doc)

    
    def validate(self, xml_path: str) -> bool:
        xml_doc = etree.parse(xml_path)
        result = self.xmlschema.validate(xml_doc)
        log = self.xmlschema.error_log
        print(log.last_error)
        return result


validator = Validator("banda.xsd")

# The directory with XML files
XML_DIR = "."

for file_name in os.listdir(XML_DIR):
    if file_name.endswith(".xml"):
        print('{}: '.format(file_name), end='')

        file_path = '{}/{}'.format(XML_DIR, file_name)
        print("VALIDANDO: " + file_path)
        if validator.validate(file_path):
            print('Valid! :)')
        else:
            print('Not valid! :(')