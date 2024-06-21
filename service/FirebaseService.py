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

def storeDesignToDb(design_name, title, tags, related_links, image_links, design_id=None):
    ref = db.reference('/Designs')

    data = {
        'design_name': design_name,
        'title': title,
        'tags': tags,
        'related_links': related_links,
        'image_links': image_links      
    }

    try:
        if design_id:
            design_ref = ref.child(design_id)
            design_ref.update(data)
            return f"Design with ID {design_id} updated successfully"
        else:
            ref.push(data)
            return "Design added to DB successfully"
    except Exception as e:
        return f'Error uploading design data: {e}'

def updateImageLinksOnDesignWithId(image_links, design_id):
    ref = db.reference('/Designs')

    data = {
        'image_links': image_links      
    }

    try:
        if design_id:
            design_ref = ref.child(design_id)
            design_ref.update(data)
            return f"Image links for design with ID {design_id} updated successfully"
        else:
            return "Design ID is required to update image links"
    except Exception as e:
        return f'Error updating image links: {e}'



def getAllDesigns():
    ref = db.reference('/Designs')
    try:
        designs = ref.get()
        if designs:
            designs_with_ids = []
            for design_id, design_data in designs.items():
                designs_with_ids.append({
                    'design_name': design_data.get('design_name', ''),
                    'design_id': design_id,
                    'related_links': design_data.get('related_links', []),
                    'image_links': design_data.get('image_links', []),
                    'tags': design_data.get('tags', []),
                    'title': design_data.get('title', '')
                })
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

        blob = bucket.blob(f'images/{uuid.uuid4()}.png')
        blob.upload_from_filename(temp_path)

        blob.make_public()
        return blob.public_url
    except Exception as e:
        return f'Error uploading image: {e}'
    
def deleteFromStorageByUrl(download_url):
    try:
        file_name = download_url.split('/')[-2] + '/' + download_url.split('/')[-1]
        print(file_name)
        blob = bucket.blob(file_name)
        
        # Delete the file if it exists
        if blob.exists():
            blob.delete()
            print("I deleted the image")
            return True
        else:
            print("Deletion failed")
            return False
    except Exception as e:
        print(f"Error deleting file: {e}")
        return False


