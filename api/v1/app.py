#!/usr/bin/python3
"""
This module is the main app in our API.
"""

from flask import Flask
from models import storage
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_storage():
    """
    Function to be called when the Flask app context is torn down.
    This function closes the storage engine to prevent resource leaks.
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", threaded=True)