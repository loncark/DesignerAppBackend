from interface.Repository import Repository
import json
from io import BytesIO
from zipfile import ZipFile


class DummyFirebaseRepository(Repository):
    def fetchData(self, success=True, exception=False):
        if exception:
            return f'Error retrieving designs: Test exception'
        elif success:
            filePath = r"C:\Users\Kristina\Documents\Diplomski rad\DesignerAppBackend\sample JSONs\DesignsInDatabase.json"
                
            with open(filePath, 'r') as file:
                data = json.load(file)
                
            return data
        else:
            return []
        
    def storeDesignToDb(self, design_name, title, tags, related_links, image_links, description, design_id, idExists=False, exception=False):
        if exception:
           return f'Error uploading design data: Test exception'
        elif idExists:
            return f"Design with ID {design_id} updated successfully"
        else:
            return f"Design with ID {design_id} added successfully"
        
    def deleteDesign(self, design_id, exception=False):
        if exception:
            return f'Error deleting design data: Test exception'
        else:
            return f"Design with ID {design_id} deleted successfully"
        
    # STORAGE

    def storeToStorage(self, image_file, design_id, exception=False):
        if exception:
            raise Exception('Test exception')
        else:
            return 'https://firebasestorage.googleapis.com/v0/b/designerapp-65092.appspot.com/o/testImage.jpg?alt=media&token=3bf25245-5cab-4a69-81cc-e301e484c676'
        
    def deleteFromStorageByUrl(self, download_url, imageExists=True, exception=False):
        if exception or not imageExists:
            return False
        else:
            return True
        
    def createDesignZip(self, design, exception=False):
        if exception:
            raise Exception('Test exception')    
        else:
            memoryFile = BytesIO()

            with ZipFile(memoryFile, 'w') as zf:                
                zf.writestr('DesignsInDatabase.json', data="Some dummy text")

            memoryFile.seek(0)
            return memoryFile