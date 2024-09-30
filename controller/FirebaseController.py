from interface.controllerInterface.DatabaseController import DatabaseController
from interface.serviceInterface.DatabaseService import DatabaseService
from flask import Blueprint, request, jsonify, send_file

class FirebaseController(DatabaseController):
    def __init__(self, service: DatabaseService):
        super().__init__(service)
        self.blueprint = Blueprint('firebaseBp', __name__)
        self.registerRoutes()

    def registerRoutes(self):
        self.blueprint.route('/db/saveDesign', methods=['POST'])(self.saveDesign)
        self.blueprint.route('/db/deleteDesign', methods=['DELETE'])(self.deleteDesign)
        self.blueprint.route('/db/allDesigns', methods=['GET'])(self.getAllDesigns)
        self.blueprint.route('/storage', methods=['POST'])(self.saveImage)
        self.blueprint.route('/storageDelete', methods=['DELETE'])(self.deleteImageByUrl)
        self.blueprint.route('/downloadDesign', methods=['POST'])(self.createDesignZip)

    def getAllDesigns(self):
        response = self.service.getAllDesigns()
        return jsonify({'error': response}) if isinstance(response, str) else response

    def saveDesign(self):
        data = request.get_json()
        return self.service.saveDesign(**data)

    def deleteDesign(self):
        data = request.get_json()
        return self.service.deleteDesign(**data)

    def saveImage(self):
        image = request.files['image']
        designId = request.form['design_id']
        
        try:
            downloadUrl = self.service.saveImageToStorage(image, designId)
            return jsonify({'url': downloadUrl}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def deleteImageByUrl(self):
        url = request.get_json().get('imgUrl')  
        boolean = self.service.deleteImageByUrl(url)

        if boolean:
            return jsonify({'msg': 'File deleted successfully'}), 200
        else:
            return jsonify({'msg': 'File does not exist or incorrect url'}), 400
        
    def createDesignZip(self):
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
