from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
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


@users.route("/api/user", methods=["POST"])
def user_login():
    body = request.get_json()

    try:
        user_data = UserModel.objects.get(username=body["username"])
    except:
        return Response(status=500)
    else:
        if check_password_hash(user_data["password"], body["password"]):
            return create_access_token(str(user_data.id))