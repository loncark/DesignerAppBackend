import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from config import REALTIMEDB_URL, FIREBASE_CREDS_JSON_LOCATION

# Initialize Firebase app (replace with your credentials)
cred = credentials.Certificate(FIREBASE_CREDS_JSON_LOCATION)  # Replace with your credentials file path
firebase_admin.initialize_app(cred, {
    'databaseURL': REALTIMEDB_URL  # Replace with your database URL
})

# Get a reference to the database
ref = db.reference('/')

# Test data (replace with your desired data)
test_data = {
    'message': 'This is a test message!',
    'number': 42,
    'array': ['apple', 'banana', 'cherry']
}

# Push data to the database
ref.push(test_data)

print('Test data written to Firebase Realtime Database!')
