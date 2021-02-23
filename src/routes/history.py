from models.user_history import UserHistoryEntry
from flask import Blueprint

history = Blueprint(__name__, __name__)

@history.route("/api/history", methods=["GET"])
def get_history():
    return UserHistoryEntry.objects().to_json()
    