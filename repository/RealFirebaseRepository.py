from interface.repositoryInterface.DatabaseRepository import DatabaseRepository
import firebase_admin, requests, os, uuid
from firebase_admin import credentials, db, storage
from constants import REALTIMEDB_URL, FIREBASE_CREDS_JSON_LOCATION
from constants import FIREBASE_CREDS_JSON_LOCATION, STORAGE_BUCKET_LOCATION
from PIL import Image
from io import BytesIO
from zipfile import ZipFile

class RealFirebaseRepository(DatabaseRepository):
    def __init__(self):
        if not firebase_admin._apps:
            creds = credentials.Certificate(FIREBASE_CREDS_JSON_LOCATION)
            firebase_admin.initialize_app(creds, {
                'databaseURL': REALTIMEDB_URL,
                'storageBucket': STORAGE_BUCKET_LOCATION
            })            

    # DESIGNS (FIREBASE REALTIME DATABASE)

    def getAllDesigns(self):
        dbRef = db.reference('/Designs')

        try:
            designs = dbRef.get()
            if designs:
                return designs
            else:
                return []
        except Exception as e:
            return f'Error retrieving design data: {e}'
        
    def saveDesign(self, design_name, title, tags, related_links, image_links, description, design_id):
        dbRef = db.reference('/Designs')

        data = {
            'design_name': design_name,
            'title': title,
            'tags': tags,
            'related_links': related_links,
            'image_links': image_links,
            'description': description      
        }

        try:
            designRef = dbRef.child(design_id)
            if designRef.get():
                designRef.update(data)
                return f"Design with ID {design_id} updated successfully"
            else:
                designRef.set(data)
                return f"Design with ID {design_id} added successfully"
        except Exception as e:
            return f'Error uploading design data: {e}'
        
    def deleteDesign(self, design_id):
        dbRef = db.reference(f'Designs/{design_id}')
        
        try:
            dbRef.delete()
            return f"Design with ID {design_id} deleted successfully"
            
        except Exception as e:
            return f'Error deleting design data: {e}'
        
    # IMAGES (FIREBASE STORAGE)

    def saveImage(self, image_file, design_id):
        try:
            bucket = storage.bucket()
            image = Image.open(image_file)

            # save image to a temporary location
            temp_path = '/tmp/image.png'
            image.save(temp_path, format='PNG')

            blob = bucket.blob(f'images/{design_id}/{uuid.uuid4()}.png')
            blob.upload_from_filename(temp_path)

            blob.make_public()
            return blob.public_url
        except Exception as e:
            raise e
        
    def deleteImageByUrl(self, download_url):
        try:
            bucket = storage.bucket()
            fileName = download_url.split('/')[-2] + '/' + download_url.split('/')[-1]
            blob = bucket.blob(fileName)

            if blob.exists():
                blob.delete()
                print("Image deleted.")
                return True
            else:
                print("File not found in Storage.") 
                return False

        except Exception as e:
            print(f"Error deleting file: {e}")
            return False
        
    def createDesignZip(self, design):
        try:
            tempDir = self.createTemporaryDirectory(design)
            self.createAndWriteTextFile(tempDir, design)
            self.downloadImages(tempDir, design)
            memoryFile = self.createZip(tempDir)
            self.removeTemporaryDirectory(tempDir)

            # prepare zip file for sending
            memoryFile.seek(0)
            return memoryFile
        except Exception as e:
            print(f"Error creating design zip: {e}")
            raise

    def createTemporaryDirectory(self, design):
        tempDir = f"temp_{design['design_name']}_{design['design_id'] or 'noID'}"
        os.makedirs(tempDir, exist_ok=True)
        return tempDir

    def createAndWriteTextFile(self, tempDir, design):
        text = f"""Design name: {design['design_name']}
    Design id: {design['design_id'] or 'N/A'}

    Tags: {', '.join(design['tags'])}
    Title: {design['title']}
    Description: {design['description']}

    Related links:
    {os.linesep.join(design['related_links'])}"""

        with open(f"{tempDir}/design_info_{design['design_id']}.txt", 'w') as f:
            f.write(text)

    def downloadImages(self, tempDir, design):
        i = 0
        for url in design['image_links']:
            response = requests.get(url)
            if response.status_code == 200:
                with open(f"{tempDir}/image_{i+1}.png", 'wb') as f:
                    f.write(response.content)
            i += 1

    def createZip(self, tempDir):
        memoryFile = BytesIO()
        with ZipFile(memoryFile, 'w') as zf:
            for root, dirs, files in os.walk(tempDir):
                for file in files:
                    zf.write(os.path.join(root, file), file)

        return memoryFile

    def removeTemporaryDirectory(self, tempDir):
        for file in os.listdir(tempDir):
            os.remove(os.path.join(tempDir, file))
        os.rmdir(tempDir)