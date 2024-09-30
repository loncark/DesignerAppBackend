from interface.serviceInterface.DatabaseService import DatabaseService
from interface.repositoryInterface.DatabaseRepository import DatabaseRepository

class FirebaseService(DatabaseService):
    def __init__(self, repository: DatabaseRepository):
        super().__init__(repository)

    # REALTIME DATABASE

    def getAllDesigns(self):
        response = self.repository.getAllDesigns()
        return response if isinstance(response, str) else self.designsWithIds(response)           
        
    def designsWithIds(self, designs):
        if not designs:
            return []
        
        newDesigns = []
        for designId, designData in designs.items():
            newDesigns.append({
                'design_name': designData.get('design_name', ''),
                'design_id': designId,
                'related_links': designData.get('related_links', []),
                'image_links': designData.get('image_links', []),
                'tags': designData.get('tags', []),
                'title': designData.get('title', ''),
                'description': designData.get('description', '')
            })
        return newDesigns
    
    def saveDesign(self, design_name, title, tags, related_links, image_links, description, design_id):
        return self.repository.saveDesign(design_name, title, tags, related_links, image_links, description, design_id)

    def deleteDesign(self, design_id):
        return self.repository.deleteDesign(design_id)
        
    # STORAGE

    def saveImage(self, image_file, design_id):
        return self.repository.saveImage(image_file, design_id)
        
    def deleteImageByUrl(self, download_url):
        return self.repository.deleteImageByUrl(download_url)

    def createDesignZip(self, design):
        return self.repository.createDesignZip(design)