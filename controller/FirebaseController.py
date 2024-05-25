import service.FirebaseService
from flask import Blueprint, request, jsonify

firebase_bp = Blueprint('firebase_bp', __name__)

@firebase_bp.route('/db/design', methods=['POST'])
def saveDesignToRealtimeDb():
    data = request.get_json()
    return service.FirebaseService.storeDesignToDb(**data)

@firebase_bp.route('/db/idea', methods=['POST'])
def saveIdeaToRealtimeDb():
    data = request.get_json()
    return service.FirebaseService.storeIdeaToDb(**data)

@firebase_bp.route('/storage', methods=['POST'])
def saveToStorage():
    if 'image' not in request.files:
        return jsonify({"error": "No image file in the request"}), 400

    image_file = request.files['image']
    image_filename = image_file.filename
    if image_file:
        download_url = service.FirebaseService.storeToStorage(image_file, image_filename)
        if "Error" in download_url:
            return jsonify({"error": download_url}), 500
        return jsonify({"download_url": download_url}), 200
    return jsonify({"error": "File upload failed"}), 500
