import os
from validator import Validator

validator = Validator("xml/xsd/marcadores.xsd")

# The directory with XML files
XML_DIR = "xml"

for file_name in os.listdir(XML_DIR):
    if file_name.endswith(".xml"):
        print('{}: '.format(file_name), end='')

        file_path = '{}/{}'.format(XML_DIR, file_name)
        print("VALIDANDO: " + file_path)
        if validator.validate(file_path):
            print('Valid! :)')
        else:
            print('Not valid! :(')