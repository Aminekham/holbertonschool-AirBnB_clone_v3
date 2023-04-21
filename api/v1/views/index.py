#!/usr/bin/python3
"""This is the routing of our API"""
from flask import Flask, jsonify
from api.v1.views import app_views
from models import storage

@app_views.route('/status')
def status():
    """Return the status of the API"""
    return(jsonify({"status": "OK"}))

