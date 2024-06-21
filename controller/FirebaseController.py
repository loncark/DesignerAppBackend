import service.FirebaseService
from flask import Blueprint, request, jsonify

firebase_bp = Blueprint('firebase_bp', __name__)

@firebase_bp.route('/db/saveDesign', methods=['POST'])
def saveDesignToRealtimeDb():
    data = request.get_json()
    return service.FirebaseService.storeDesignToDb(**data)

@firebase_bp.route('/db/deleteDesign', methods=['DELETE'])
def deleteDesignFromDb():
    data = request.get_json()
    return service.FirebaseService.deleteDesign(**data)

@firebase_bp.route('/db/updateImageLinks', methods=['POST'])
def updateImageLinks():
    data = request.get_json()
    return service.FirebaseService.updateImageLinksOnDesignWithId(**data)

@firebase_bp.route('/db/allDesigns', methods=['GET'])
def getAllDesigns():
    return service.FirebaseService.getAllDesigns()

@firebase_bp.route('/storage', methods=['POST'])
def saveToStorage():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400

    downloadUrl = service.FirebaseService.storeToStorage(request.files['image'])

    return jsonify({'url': downloadUrl}), 200

@firebase_bp.route('/storageDelete', methods=['DELETE'])
def deleteFromStorage():
    url = request.get_json().get('imgUrl')  
    boolean = service.FirebaseService.deleteFromStorageByUrl(url)

    if boolean:
        return jsonify({'msg': 'File deleted successfully'}), 200
    else:
        return jsonify({'msg': 'File does not exist or incorrect url'}), 400
