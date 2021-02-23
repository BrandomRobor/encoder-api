from .db import initialize_db
from flask import Flask

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {
    "host": app.config.from_envvar("MONGODB_HOST")
}
initialize_db(app)

if __name__ == "__main__":
    app.run()
