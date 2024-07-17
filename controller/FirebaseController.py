import service.FirebaseService
from flask import Blueprint, request, jsonify, send_file

firebase_bp = Blueprint('firebase_bp', __name__)

@firebase_bp.route('/db/saveDesign', methods=['POST'])
def saveDesignToRealtimeDb():
    data = request.get_json()
    return service.FirebaseService.storeDesignToDb(**data)

@firebase_bp.route('/db/deleteDesign', methods=['DELETE'])
def deleteDesignFromDb():
    data = request.get_json()
    return service.FirebaseService.deleteDesign(**data)

@firebase_bp.route('/db/allDesigns', methods=['GET'])
def getAllDesigns():
    return service.FirebaseService.getAllDesigns()

@firebase_bp.route('/storage', methods=['POST'])
def saveToStorage():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400

    if 'design_id' not in request.form or not request.form['design_id']:
        return jsonify({'error': 'No design_id provided'}), 400

    image = request.files['image']
    design_id = request.form['design_id']
    
    try:
        download_url = service.FirebaseService.storeToStorage(image, design_id)
        return jsonify({'url': download_url}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@firebase_bp.route('/storageDelete', methods=['DELETE'])
def deleteFromStorage():
    url = request.get_json().get('imgUrl')  
    boolean = service.FirebaseService.deleteFromStorageByUrl(url)

    if boolean:
        return jsonify({'msg': 'File deleted successfully'}), 200
    else:
        return jsonify({'msg': 'File does not exist or incorrect url'}), 400
    

@firebase_bp.route('/downloadDesign', methods=['POST'])
def download_design():
    design = request.json
    try:
        zip_file = service.FirebaseService.createDesignZip(design)
        return send_file(
            zip_file,
            mimetype='application/zip',
            as_attachment=True,
            download_name=f"{design['design_name']}_{design['design_id'] or 'noID'}.zip"
        )
    except Exception as e:
        return jsonify({'error': 'Error downloading file.'}), 500
