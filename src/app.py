from flask_jwt_extended import JWTManager
from routes.history import history
from mail import initialize_mail
from routes.users import users
from db import initialize_db
from flask import Flask
from os import environ

app = Flask(__name__)
app.config["MONGODB_HOST"] = environ.get("MONGODB_HOST")
app.config["SECRET_KEY"] = environ.get("SECRET_KEY")
app.config["MAIL_SERVER"] = environ.get("MAIL_SERVER")
app.config["MAIL_PORT"] = environ.get("MAIL_PORT")
app.config["MAIL_USERNAME"] = environ.get("MAIL_USERNAME")
app.config["MAIL_PASSWORD"] = environ.get("MAIL_PASSWORD")
app.config["MAIL_DEFAULT_SENDER"] = eval(environ.get("MAIL_DEFAULT_SENDER"))
app.config["SERVER_NAME"] = environ.get("SERVER_NAME")
app.config["PREFERRED_URL_SCHEME"] = environ.get("PREFERRED_URL_SCHEME")
initialize_db(app)
initialize_mail(app)
jwt = JWTManager(app)

app.register_blueprint(history)
app.register_blueprint(users)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
