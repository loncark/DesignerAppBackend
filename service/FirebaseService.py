import firebase_admin
from firebase_admin import credentials, db, storage
import uuid
from PIL import Image
from config import REALTIMEDB_URL, FIREBASE_CREDS_JSON_LOCATION
from config import FIREBASE_CREDS_JSON_LOCATION, STORAGE_BUCKET_LOCATION

# needs to be done only once
cred = credentials.Certificate(FIREBASE_CREDS_JSON_LOCATION)
firebase_admin.initialize_app(cred, {
    'databaseURL': REALTIMEDB_URL,
    'storageBucket': STORAGE_BUCKET_LOCATION
})

# REALTIME DATABASE

def storeDesignToDb(design_name, title, tags, image_links):
    ref = db.reference('/Designs')
    data = {
        'design_name': design_name,
        'title': title,
        'tags': tags,
        'image_links': image_links
    }

    try:
        ref.push(data)
        return "Db design query success"  
    except Exception as e:
        return f'Error uploading design data: {e}'

def getAllDesigns():
    ref = db.reference('/Designs')
    try:
        designs = ref.get()
        if designs:
            designs_with_ids = []
            for design_id, design_data in designs.items():
                design_data['id'] = design_id
                designs_with_ids.append(design_data)
            return designs_with_ids
        else:
            return []
    except Exception as e:
        return f'Error retrieving designs: {e}'


# STORAGE

bucket = storage.bucket()

def storeToStorage(image_file):
    try:
        image = Image.open(image_file)

        # Save image to a temporary location
        temp_path = '/tmp/image.png'
        image.save(temp_path, format='PNG')

        # Upload to Firebase Storage
        blob = bucket.blob(f'images/{uuid.uuid4()}.png')
        blob.upload_from_filename(temp_path)

        return blob.public_url
    except Exception as e:
        return f'Error uploading image: {e}'