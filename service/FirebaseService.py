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

ref = db.reference('/')

def storeToDb(data):
    data = {
        'message': 'This is a test message!',
        'number': 42,
        'array': ['apple', 'banana', 'cherry']
    }

    ref.push(data)
    print('Test data written to Firebase Realtime Database!')

    return "Db query success"

# STORAGE

bucket = storage.bucket()

def storeToStorage(image_file, image_filename):
    try:
        image_path = f'images/{image_filename}'
        image_ref = bucket.blob(image_path)
        image_ref.upload_from_file(image_file)
        download_url = image_ref.public_url
        return download_url
    except Exception as e:
        return f'Error uploading image: {e}'