#!/usr/bin/python3
"""This is the routing of our API"""
from flask import Flask, jsonify
from api.v1.views import app_views
from models import storage
from api.v1.app import app


@app_views.route('/status')
def status():
    """Return the status of the API"""
    return(jsonify({"status": "OK"}))


@app.route('/stats')
def stats():
    """giving the stats of our objects"""
    all_objects = {"amenities": 1, "cities": 0, "places": 0, "reviews": 0, "states": 0, "users": 0}
    for i in all_objects.keys():
        all_objects[i] = storage.count(i)
    return jsonify(all_objects)