from werkzeug.security import generate_password_hash, check_password_hash
from flask import Blueprint, request, Response, url_for
from flask_jwt_extended import create_access_token
from mail import mail, send_message_async
from models.user import UserModel
from flask_mail import Message
from threading import Thread
from bson import ObjectId

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
        html="<body></p>Please confirm your address by clicking this <a href='" +
        url_for("routes.users.validate_mail", id=str(new_user.id),
                _external=True) + "'>link</a>.</p></body>"
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


@users.route("/api/validate/<id>", methods=["GET"])
def validate_mail(id):
    user_data = UserModel.objects(pk=ObjectId(id)).get()
    user_data.mailVerified = True
    user_data.save()
    return Response(status=200)
