import firebase_admin
from firebase_admin import credentials, db, storage
from flask import request
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
    
def storeIdeaToDb(trend_title, trend_link, trend_thumbnail_link, trend_date, ideas):
    ref = db.reference('/Ideas')
    data = {
        'trend_title': trend_title,
        'trend_link': trend_link,
        'trend_thumbnail_link': trend_thumbnail_link,
        'trend_date': trend_date,
        'ideas': ideas
    }

    try:
        ref.push(data)
        return "Db idea query success"  
    except Exception as e:
        return f'Error uploading idea data: {e}'


# STORAGE

bucket = storage.bucket()

def storeToStorage(image_file, image_filename):
    try:
        image_path = f'images/{image_filename}'
        image_ref = bucket.blob(image_path)
        image_ref.upload_from_file(image_file, content_type='image/png')
        download_url = image_ref.public_url
        return download_url
    except Exception as e:
        return f'Error uploading image: {e}'