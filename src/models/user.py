from db import db

class UserModel(db.Document):
    meta = {
        "collection": "users"
    }

    username = db.StringField(required=True, unique=True, max_length=50)
    password = db.StringField(required=True)
    email = db.EmailField(required=True, unique=True)
    mailVerified = db.BooleanField(required=True, default=False)