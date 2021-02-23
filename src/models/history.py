from datetime import datetime
from bson import ObjectId
from db import db


class HistoryEntry(db.EmbeddedDocument):
    entry_id = db.ObjectIdField(
        required=True, default=ObjectId, unique=True, primary_key=True)
    filename = db.StringField(required=True)
    date = db.DateTimeField(required=True, default=datetime.utcnow)
