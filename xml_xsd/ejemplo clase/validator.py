from lxml import etree

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
validator.validate("catalogo_simple.xml")