from db import initialize_db
from flask import Flask
import os

app = Flask(__name__)
app.config["MONGODB_HOST"] = os.environ.get("MONGODB_HOST")
initialize_db(app)

if __name__ == "__main__":
    app.run()
