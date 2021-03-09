from flask import current_app
from threading import Thread
from flask_mail import Mail

mail = Mail()


def initialize_mail(app):
    mail.init_app(app)


def send_message_async(msg):
    obj = current_app._get_current_object()
    Thread(target=send_async, args=[obj, msg]).start()

def send_async(app, msg):
    with app.app_context():
        mail.send(msg)
