from interface.Repository import Repository

class FirebaseService:
    def __init__(self, repository: Repository):
        self.repository = repository

    # REALTIME DATABASE

    def getAllDesigns(self):
        return self.designsWithIds(self.repository.fetchData())
        
    def designsWithIds(self, designs):
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
    
    def storeDesignToDb(self, design_name, title, tags, related_links, image_links, description, design_id):
        return self.repository.storeDesignToDb(design_name, title, tags, related_links, image_links, description, design_id)

    def deleteDesign(self, design_id):
        return self.repository.deleteDesign(design_id)
        
    # STORAGE

    def storeToStorage(self, image_file, design_id):
        return self.repository.storeToStorage(image_file, design_id)
        
    def deleteFromStorageByUrl(self, download_url):
        return self.repository.deleteFromStorageByUrl(download_url)

    def createDesignZip(self, design):
        return self.repository.createDesignZip(design)