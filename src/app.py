from .db import initialize_db
from flask import Flask

app = Flask(__name__)
initialize_db(app)

if __name__ == "__main__":
    app.run()
