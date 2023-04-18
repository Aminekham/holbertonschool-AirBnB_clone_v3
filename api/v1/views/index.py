#!/usr/bin/python3
"""This is the routing of our API"""
from flask import jsonify
from api.v1.views import app_views

@app_views.route('/status')
def status():
    """Return the status of the API"""
    return ({'status': 'OK'})