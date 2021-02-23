from db import db
from datetime import datetime

class HistoryEntry(db.EmbeddedDocument):
    filename = db.StringField(required=True)
    date = db.DateTimeField(required=True,default=datetime.utcnow)
