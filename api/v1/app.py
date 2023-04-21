#!/usr/bin/python3
"""This is the main module that defines the Flask app instance"""
from flask import Flask, jsonify, make_response, current_app
from os import environ
from api.v1.views import app_views
from models import storage


app = Flask(__name__)


@app_views.route('/status')
def status():
    """Return the status of the API"""
    return jsonify({'status': 'OK'})


@app.errorhandler(404)
def not_found(error):
    """Handles 404 errors"""
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request"""
    storage.close()


if __name__ == "__main__":
    app.register_blueprint(app_views, url_prefix='/api/v1')

    host = environ.get('HBNB_API_HOST', '0.0.0.0')
    port = environ.get('HBNB_API_PORT', 5000)
    app.run(host=host, port=port, threaded=True)
