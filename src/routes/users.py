from werkzeug.security import generate_password_hash
from flask import Blueprint, request, Response
from models.user import UserModel

users = Blueprint(__name__, __name__)

@users.route("/api/user", methods=["PUT"])
def register_user():
    body = request.get_json()

    body["password"] = generate_password_hash(body["password"])

    try:
        UserModel(**body).save()
    except:
        return Response(status=500)
    else:
        return Response(status=201)