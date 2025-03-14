from api.v1.views import app_views
from flask import jsonify

@app_views.run('/status')
def status():
    return jsonify({"status": "OK"})
