from flask import url_for
from app import db


class Todo(db.Document):
    #si descomentamos el id, tendremos que gestionarlo nosotros
    #id = db.StringField(primary_key=True, required=True)
    name = db.StringField(required=True)
    desc = db.StringField(required=True)
    date = db.StringField(required=True)
    pr = db.StringField(required=True)
    done = db.StringField(required=True)
