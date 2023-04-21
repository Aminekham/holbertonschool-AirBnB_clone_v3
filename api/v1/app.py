#!/usr/bin/python3
"""
This module is the main app in our API.
"""

from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from flask_cors import CORS
import os

app = Flask(__name__)




@app.teardown_appcontext
def teardown_db(exception):
    """ Function to be called when the Flask app context is torn down. 
    This function closes the storage engine to prevent resource leaks. 
    """
    storage.close()



if __name__ == "__main__":
    app.register_blueprint(app_views, url_prefix='/api/v1')
    host = os.getenv("HBNB_API_HOST", "0.0.0.0")
    port = os.getenv("HBNB_API_PORT", 5000)
    app.run(host=host, port=port, threaded=True)