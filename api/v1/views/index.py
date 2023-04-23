#!/usr/bin/python3
"""This is the routing of our API"""
from flask import Flask, jsonify
from api.v1.views import app_views
from models import storage, amenity, city, place, review, state, user
from api.v1.app import app


@app_views.route('/status')
def status():
    """Return the status of the API"""
    return(jsonify({"status": "OK"}))


@app_views.route('/stats')
def stats():
    """giving the stats of our objects"""
    count_values = {}
    obj_list = [amenity.Amenity, city.City, place.Place, review.Review, state.State, user.User]
    for class_name in obj_list:
        count_values[class_name.__name__.lower()] = storage.count(class_name)
    return(jsonify(count_values))
