#!/usr/bin/python3
"""This is the routing of our API"""
from flask import Flask, jsonify
from api.v1.views import app_views
from models import storage

@app_views.route('/status')
def status():
    """Return the status of the API"""
    return(jsonify({"status": "OK"}))


@app_views.route('/api/v1/stats')
def get_stats():
    """Retrieves the number of objects by type"""
    amenities_count = storage.count("Amenity")
    cities_count = storage.count("City")
    places_count = storage.count("Place")
    reviews_count = storage.count("Review")
    states_count = storage.count("State")
    users_count = storage.count("User")
    stats = {"amenities": amenities_count,
             "cities": cities_count,
             "places": places_count,
             "reviews": reviews_count,
             "states": states_count,
             "users": users_count}
    return(jsonify(stats))
