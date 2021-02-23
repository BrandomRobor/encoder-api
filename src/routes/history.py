from flask_jwt_extended import jwt_required, get_jwt_identity
from models.user_history import UserHistoryEntry
from flask import Blueprint, Response, request
from models.history import HistoryEntry
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


@history.route("/api/history", methods=["PUT"])
@jwt_required()
def add_to_history():
    body = request.get_json()

    try:
        user_history = UserHistoryEntry.objects.get(user_id=get_jwt_identity())
    except DoesNotExist:
        new_user_history = UserHistoryEntry()
        new_user_history.user_id = get_jwt_identity()
        new_user_history.history.append(HistoryEntry(**body))
        new_user_history.save()
        return Response(status=201)
    else:
        try:
            user_history.history.append(HistoryEntry(**body))
            user_history.save()
        except:
            return Response(status=500)
        else:
            return Response(status=201)