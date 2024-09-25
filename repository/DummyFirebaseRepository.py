from interface.Repository import Repository
import json

class DummyFirebaseRepository(Repository):

    def fetchData(self, success=True, exception=False):
        if exception:
            raise Exception('Test exception')
        elif success:
            filePath = r"C:\Users\Kristina\Documents\Diplomski rad\DesignerAppBackend\sample JSONs\DesignsInDatabase.json"
                
            with open(filePath, 'r') as file:
                data = json.load(file)
                
            return data
        else:
            return []
        
        
    def storeDesignToDb(self, design_name, title, tags, related_links, image_links, description, design_id):
        pass
        
    def deleteDesign(self, design_id):
        pass
        
    # STORAGE

    def storeToStorage(self, image_file, design_id):
        pass
        
    def deleteFromStorageByUrl(self, download_url):
        pass
        
    def createDesignZip(self, design):
        pass