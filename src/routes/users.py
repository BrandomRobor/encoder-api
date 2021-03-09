from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from flask import Blueprint, request, Response
from models.user import UserModel
from flask_mail import Message
from threading import Thread
from mail import mail, send_message_async

users = Blueprint(__name__, __name__)


@users.route("/api/user", methods=["PUT"])
def register_user():
    body = request.get_json()

    body["password"] = generate_password_hash(body["password"])

    new_user = UserModel(**body)
    new_user.save()
    confirm_mail = Message(
        subject="Mail verification",
        recipients=[body["email"]],
        body="Please confirm your address by clicking this link: " +
        str(new_user.id)
    )

    send_message_async(confirm_mail)
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