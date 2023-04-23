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


@app.route('/stats')
def stats():
    """giving the stats of our objects"""
    amenity_count = storage.count(amenity.Amenity)
    city_count = storage.count(city.City)
    place_count = storage.count(place.Place)
    review_count = storage.count(review.Review)
    state_count = storage.count(state.State)
    user_count = storage.count(user.User)
    result = jsonify({
        "amenities": amenity_count,
        "cities": city_count,
        "places": place_count,
        "reviews": review_count,
        "states": state_count,
        "users": user_count
    })
    return(result)