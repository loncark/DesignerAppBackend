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
cred = credentials.Certificate(FIREBASE_CREDS_JSON_LOCATION)
firebase_admin.initialize_app(cred, {
    'databaseURL': REALTIMEDB_URL,
    'storageBucket': STORAGE_BUCKET_LOCATION
})

# REALTIME DATABASE

def storeDesignToDb(design_name, title, tags, related_links, image_links, design_id):
    ref = db.reference('/Designs')

    data = {
        'design_name': design_name,
        'title': title,
        'tags': tags,
        'related_links': related_links,
        'image_links': image_links      
    }

    try:
        design_ref = ref.child(design_id)
        if design_ref.get():
            design_ref.update(data)
            return f"Design with ID {design_id} updated successfully"
        else:
            design_ref.set(data)
            return f"Design with ID {design_id} added successfully"
    except Exception as e:
        return f'Error uploading design data: {e}'

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

def deleteDesign(design_id):
    ref = db.reference(f'Designs/{design_id}')
    
    try:
        ref.delete()
        return f"Design with ID {design_id} deleted successfully"
        
    except Exception as e:
        return f'Error deleting design data: {e}'

# STORAGE

def storeToStorage(image_file, design_id):
    try:
        bucket = storage.bucket()
        image = Image.open(image_file)

        # Save image to a temporary location
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
        file_name = download_url.split('/')[-2] + '/' + download_url.split('/')[-1]
        print(file_name)
        blob = bucket.blob(file_name)

        # Delete the file if it exists
        if blob.exists():
            blob.delete()
            print("I deleted the image")
            return True
        else:
            print("File not found.") 
            return False

    except Exception as e:
        print(f"Error deleting file: {e}")
        return False
    

def createDesignZip(design):
    try:
        # Create a temporary directory
        temp_dir = f"temp_{design['design_name']}_{design['design_id'] or 'noID'}"
        os.makedirs(temp_dir, exist_ok=True)

        # Create and write text file
        txt_content = f"""Design name: {design['design_name']}
Design id: {design['design_id'] or 'N/A'}

Tags: {', '.join(design['tags'])}
Title: {design['title']}

Related links:
{os.linesep.join(design['related_links'])}"""

        with open(f"{temp_dir}/design_info_{design['design_id']}.txt", 'w') as f:
            f.write(txt_content)

        # Download images
        for i, url in enumerate(design['image_links']):
            response = requests.get(url)
            if response.status_code == 200:
                with open(f"{temp_dir}/image_{i+1}.png", 'wb') as f:
                    f.write(response.content)

        # Create a zip file
        memory_file = BytesIO()
        with ZipFile(memory_file, 'w') as zf:
            for root, dirs, files in os.walk(temp_dir):
                for file in files:
                    zf.write(os.path.join(root, file), file)

        # Clean up the temporary directory
        for file in os.listdir(temp_dir):
            os.remove(os.path.join(temp_dir, file))
        os.rmdir(temp_dir)

        # Prepare the zip file for sending
        memory_file.seek(0)
        return memory_file
    except Exception as e:
        print(f"Error creating design zip: {str(e)}")
        raise