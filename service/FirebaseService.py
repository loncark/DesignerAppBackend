import firebase_admin
from firebase_admin import credentials, db, storage
import uuid
from PIL import Image
from config import REALTIMEDB_URL, FIREBASE_CREDS_JSON_LOCATION
from config import FIREBASE_CREDS_JSON_LOCATION, STORAGE_BUCKET_LOCATION
import os
import requests
from io import BytesIO
from zipfile import ZipFile

# needs to be done only once
creds = credentials.Certificate(FIREBASE_CREDS_JSON_LOCATION)
firebase_admin.initialize_app(creds, {
    'databaseURL': REALTIMEDB_URL,
    'storageBucket': STORAGE_BUCKET_LOCATION
})

# REALTIME DATABASE

def storeDesignToDb(design_name, title, tags, related_links, image_links, description, design_id):
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

def getAllDesigns():
    dbRef = db.reference('/Designs')

    try:
        designs = dbRef.get()
        if designs:
            return designsWithIds(designs)
        else:
            return []
    except Exception as e:
        return f'Error retrieving designs: {e}'
    
def designsWithIds(designs):
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

def deleteDesign(design_id):
    dbRef = db.reference(f'Designs/{design_id}')
    
    try:
        dbRef.delete()
        return f"Design with ID {design_id} deleted successfully"
        
    except Exception as e:
        return f'Error deleting design data: {e}'
    
# STORAGE

def storeToStorage(image_file, design_id):
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
        return f'Error uploading image: {e}'
    
def deleteFromStorageByUrl(download_url):
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
    

def createDesignZip(design):
    try:
        tempDir = createTemporaryDirectory(design)
        createAndWriteTextFile(tempDir, design)
        downloadImages(tempDir, design)
        memoryFile = createZip(tempDir)
        removeTemporaryDirectory(tempDir)

        # prepare zip file for sending
        memoryFile.seek(0)
        return memoryFile
    except Exception as e:
        print(f"Error creating design zip: {e}")
        raise

def createTemporaryDirectory(design):
    tempDir = f"temp_{design['design_name']}_{design['design_id'] or 'noID'}"
    os.makedirs(tempDir, exist_ok=True)
    return tempDir

def createAndWriteTextFile(tempDir, design):
    text = f"""Design name: {design['design_name']}
Design id: {design['design_id'] or 'N/A'}

Tags: {', '.join(design['tags'])}
Title: {design['title']}
Description: {design['description']}

Related links:
{os.linesep.join(design['related_links'])}"""

    with open(f"{tempDir}/design_info_{design['design_id']}.txt", 'w') as f:
        f.write(text)

def downloadImages(tempDir, design):
    i = 0
    for url in design['image_links']:
        response = requests.get(url)
        if response.status_code == 200:
            with open(f"{tempDir}/image_{i+1}.png", 'wb') as f:
                f.write(response.content)
        i += 1

def createZip(tempDir):
    memoryFile = BytesIO()
    with ZipFile(memoryFile, 'w') as zf:
        for root, dirs, files in os.walk(tempDir):
            for file in files:
                zf.write(os.path.join(root, file), file)

    return memoryFile

def removeTemporaryDirectory(tempDir):
    for file in os.listdir(tempDir):
        os.remove(os.path.join(tempDir, file))
    os.rmdir(tempDir)