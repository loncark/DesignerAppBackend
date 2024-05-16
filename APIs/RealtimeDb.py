import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Initialize Firebase app (replace with your credentials)
cred = credentials.Certificate('C:\\Users\\Kristina\\Documents\\Diplomski rad\\DesignerAppBackend\\DesignerAppFirebaseCreds.json')  # Replace with your credentials file path
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://designerapp-65092-default-rtdb.europe-west1.firebasedatabase.app/'  # Replace with your database URL
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
