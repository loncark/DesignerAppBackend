from service.FirebaseService import FirebaseService
from flask import Blueprint, request, jsonify, send_file


class FirebaseController:
    def __init__(self):
        self.firebaseService = FirebaseService()
        self.firebaseBp = Blueprint('firebaseBp', __name__)
        self.registerRoutes()

    def registerRoutes(self):
        self.firebaseBp.route('/db/saveDesign', methods=['POST'])(self.saveDesignToRealtimeDb)
        self.firebaseBp.route('/db/deleteDesign', methods=['DELETE'])(self.deleteDesignFromDb)
        self.firebaseBp.route('/db/allDesigns', methods=['GET'])(self.getAllDesigns)
        self.firebaseBp.route('/storage', methods=['POST'])(self.saveToStorage)
        self.firebaseBp.route('/storageDelete', methods=['DELETE'])(self.deleteFromStorage)
        self.firebaseBp.route('/downloadDesign', methods=['POST'])(self.downloadDesign)

    
    def saveDesignToRealtimeDb(self):
        data = request.get_json()
        return self.firebaseService.storeDesignToDb(**data)

    def deleteDesignFromDb(self):
        data = request.get_json()
        return self.firebaseService.deleteDesign(**data)

    def getAllDesigns(self):
        return self.firebaseService.getAllDesigns()

    def saveToStorage(self):
        image = request.files['image']
        designId = request.form['design_id']
        
        try:
            downloadUrl = self.firebaseService.storeToStorage(image, designId)
            return jsonify({'url': downloadUrl}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def deleteFromStorage(self):
        url = request.get_json().get('imgUrl')  
        boolean = self.firebaseService.deleteFromStorageByUrl(url)

        if boolean:
            return jsonify({'msg': 'File deleted successfully'}), 200
        else:
            return jsonify({'msg': 'File does not exist or incorrect url'}), 400
        
    def downloadDesign(self):
        design = request.json
        try:
            zip_file = self.firebaseService.createDesignZip(design)
            return send_file(
                zip_file,
                mimetype='application/zip',
                as_attachment=True,
                download_name=f"{design['design_name']}_{design['design_id'] or 'noID'}.zip"
            )
        except Exception as e:
            return jsonify({'error': 'Error downloading file.'}), 500
