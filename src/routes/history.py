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
    try:
        user_history = UserHistoryEntry.objects.get(user_id=get_jwt_identity())
    except DoesNotExist:
        user_history = UserHistoryEntry()
        user_history.user_id = get_jwt_identity()
    except:
        return Response(status=500)

    try:
        user_history.history.append(HistoryEntry(**request.get_json()))
        user_history.save()
    except:
        return Response(status=500)
    else:
        return Response(status=201)


@history.route("/api/history", methods=["DELETE"])
@jwt_required()
def delete_from_history():
    try:
        UserHistoryEntry.objects(user_id=get_jwt_identity()).update_one(
            pull__history__entry_id=request.json["entry_id"])
    except:
        return Response(status=500)
    else:
        return Response(status=204)
