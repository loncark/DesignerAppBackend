import service.FirebaseService
from flask import Blueprint, request, jsonify

firebase_bp = Blueprint('firebase_bp', __name__)

@firebase_bp.route('/db', methods=['POST'])
def saveDesignToRealtimeDb():
    data = request.get_json()
    return service.FirebaseService.storeDesignToDb(**data)

@firebase_bp.route('/storage', methods=['POST'])
def saveToStorage():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400

    downloadUrl = service.FirebaseService.storeToStorage(request.files['image'])

    return jsonify({'url': downloadUrl}), 200
