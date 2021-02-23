from models.history import HistoryEntry
from db import db

class UserHistoryEntry(db.Document):
    user_id = db.ObjectIdField()
    history = db.ListField(HistoryEntry())