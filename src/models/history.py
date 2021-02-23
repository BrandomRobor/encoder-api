from db import db

class HistoryEntry(db.EmbeddedDocument):
    filename = db.StringField(required=True)
    date = db.DateTimeField(required=True)
