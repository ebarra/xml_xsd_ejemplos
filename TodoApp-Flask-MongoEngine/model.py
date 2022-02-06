from app import db

# It maps the class to the name of the collection
class Todo(db.Document):
    name = db.StringField(required=True)
    desc = db.StringField(required=True)
    date = db.DateTimeField(required=True)
    pr = db.StringField(required=True)
    done = db.BooleanField(required=True, default=False)
