from service.FirebaseService import FirebaseService
from flask import Blueprint, request, jsonify, send_file

class FirebaseController:
    def __init__(self):
        self.service = FirebaseService()
        self.blueprint = Blueprint('firebaseBp', __name__)
        self.registerRoutes()

    def registerRoutes(self):
        self.blueprint.route('/db/saveDesign', methods=['POST'])(self.saveDesignToRealtimeDb)
        self.blueprint.route('/db/deleteDesign', methods=['DELETE'])(self.deleteDesignFromDb)
        self.blueprint.route('/db/allDesigns', methods=['GET'])(self.getAllDesigns)
        self.blueprint.route('/storage', methods=['POST'])(self.saveToStorage)
        self.blueprint.route('/storageDelete', methods=['DELETE'])(self.deleteFromStorage)
        self.blueprint.route('/downloadDesign', methods=['POST'])(self.downloadDesign)

    
    def saveDesignToRealtimeDb(self):
        data = request.get_json()
        return self.service.storeDesignToDb(**data)

    def deleteDesignFromDb(self):
        data = request.get_json()
        return self.service.deleteDesign(**data)

    def getAllDesigns(self):
        return self.service.getAllDesigns()

    def saveToStorage(self):
        image = request.files['image']
        designId = request.form['design_id']
        
        try:
            downloadUrl = self.service.storeToStorage(image, designId)
            return jsonify({'url': downloadUrl}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def deleteFromStorage(self):
        url = request.get_json().get('imgUrl')  
        boolean = self.service.deleteFromStorageByUrl(url)

        if boolean:
            return jsonify({'msg': 'File deleted successfully'}), 200
        else:
            return jsonify({'msg': 'File does not exist or incorrect url'}), 400
        
    def downloadDesign(self):
        design = request.json
        try:
            zip_file = self.service.createDesignZip(design)
            return send_file(
                zip_file,
                mimetype='application/zip',
                as_attachment=True,
                download_name=f"{design['design_name']}_{design['design_id'] or 'noID'}.zip"
            )
        except Exception as e:
            return jsonify({'error': str(e)}), 500
