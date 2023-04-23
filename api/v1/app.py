#!/usr/bin/python3
"""This is the main module that defines the Flask app instance"""
from flask import Flask, jsonify, make_response, current_app
from flask_cors import CORS
from os import environ
from api.v1.views import app_views
from models import storage


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app_views.route('/status')
def status():
    """Return the status of the API"""
    return jsonify({'status': 'OK'})


@app.errorhandler(404)
def not_found(error):
    """Handles 404 errors"""
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/api/v1/stats')
def stats():
    """giving the stats of our objects"""
    all_objects = {"amenities": 1, "cities": 0, "places": 0, "reviews": 0, "states": 0, "users": 0}
    for i in all_objects.keys():
        all_objects[i] = storage.count(i)
    return jsonify(all_objects)


@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request"""
    storage.close()


if __name__ == "__main__":
    app.register_blueprint(app_views, url_prefix='/api/v1')

    host = environ.get('HBNB_API_HOST', '0.0.0.0')
    port = environ.get('HBNB_API_PORT', 5000)
    app.run(host=host, port=port, threaded=True)
