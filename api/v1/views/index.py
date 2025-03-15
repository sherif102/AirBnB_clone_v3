#!/usr/bin/python3
"""index app"""
from api.v1.views import app_views
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from flask import jsonify


@app_views.route('/status')
def status():
    return jsonify({"status": "OK"})


@app_views.route('/stats')
def stats():
    classes = {
        'amenities': Amenity,
        'cities': City,
        'places': Place,
        'reviews': Review,
        'states': State,
        'users': User
    }
    records = {}
    for key, value in classes.items():
        try:
            records[key] = storage.count(value)
        except Exception:
            pass
    return jsonify(records)
