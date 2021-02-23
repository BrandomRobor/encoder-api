from routes.history import history
from db import initialize_db
from flask import Flask
import os

app = Flask(__name__)
app.config["MONGODB_HOST"] = os.environ.get("MONGODB_HOST")
initialize_db(app)

app.register_blueprint(history)

if __name__ == "__main__":
    app.run()
