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
    return jsonify(amenities=storage.count(amenity.Amenity),
                   cities=storage.count(city),
                   places=storage.count(place.Place),
                   reviews=storage.count(review.Review),
                   states=storage.count(state.State),
                   users=storage.count(user.User))
