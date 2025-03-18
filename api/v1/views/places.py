#!/usr/bin/python3
"""fetches all default RESTFul API actions"""
from api.v1.views import app_views
from api.v1.views import storage
from models.city import City
from models.state import State
from models.place import Place
from models.user import User
from flask import jsonify, request


@app_views.route('/cities/<city_id>/places', strict_slashes=False)
def get_places_of_a_city(city_id):
    """retrieve all places in a city"""
    city = storage.get(City, city_id)
    if not city:
        return jsonify({"error": "Not found"}), 404
    if len(city.places) > 0:
        all_places = []
        for place in city.places:
            all_places.append(place.to_dict())
        return jsonify(all_places)
    else:
        return jsonify([])


@app_views.route('/places/<place_id>', strict_slashes=False)
def get_place_with_id(place_id):
    """retrieve a place"""
    place = storage.get(Place, place_id)
    if place:
        return jsonify(place.to_dict())
    return jsonify({"error": "Not found"}), 404


@app_views.route('/places/<place_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_place(place_id):
    """delete a place"""
    place = storage.get(Place, place_id)
    if place:
        if place.reviews:
            for review in place.reviews:
                storage.delete(review)
        if place.amenities:
            for amenity in place.amenities:
                storage.delete(amenity)
                storage.delete(place)
        storage.delete(place)
        storage.save()
        return jsonify({}), 200
    return jsonify({"error": "Not found"}), 404


@app_views.route('/cities/<city_id>/places', methods=['POST'],
                 strict_slashes=False)
def post_place(city_id):
    """insert a place"""
    city = storage.get(City, city_id)
    if not city:
        return jsonify({"error": "Not found"}), 404
    try:
        if not request.is_json:
            raise Exception
        input_data = request.get_json()
    except Exception:
        return jsonify({'error': 'Not a JSON'}), 400

    if "user_id" not in input_data:
        return jsonify({'error': 'Missing user_id'}), 400
    if "name" not in input_data:
        return jsonify({'error': 'Missing name'}), 400

    if input_data["user_id"] != storage.get(User, input_data["user_id"]).id:
        return jsonify({"error": "Not found"}), 404

    new_place = Place(city_id=city_id, **input_data)
    storage.new(new_place)
    storage.save()
    return jsonify(new_place.to_dict()), 201


@app_views.route('/places/<place_id>', methods=['PUT'], strict_slashes=False)
def put_place(place_id):
    """update a place"""
    place = storage.get(Place, place_id)
    if not place:
        return jsonify({"error": "Not found"}), 404
    try:
        if not request.is_json:
            raise Exception
        data = request.get_json()

        for key, value in data.items():
            if key in ['id', 'created_at', 'updated_at']:
                continue
            setattr(place, key, value)
        storage.save()
        return jsonify(place.to_dict()), 200
    except Exception:
        return jsonify({'error': 'Not a JSON'}), 400
    # return jsonify({"error": "Not found"}), 404


# def check_input(data_dict):
#     """checks the input for correctness"""
#     check_keys = ['name']
#     for key in check_keys:
#         if key not in list(data_dict.keys()):
#             return jsonify({'error': 'Missing name'}), 400
#     return True
