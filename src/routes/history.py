from flask_jwt_extended import jwt_required, get_jwt_identity
from models.user_history import UserHistoryEntry
from flask import Blueprint, Response
from mongoengine import DoesNotExist
from bson import ObjectId

history = Blueprint(__name__, __name__)

@history.route("/api/history", methods=["GET"])
@jwt_required()
def get_history():
    try:
        user_history = UserHistoryEntry.objects.get(user_id=get_jwt_identity())
    except DoesNotExist:
        return Response(status=404)
    else:
        return user_history.to_json()
    