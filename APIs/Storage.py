import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage

# Initialize Firebase app (replace with your credentials)
cred = credentials.Certificate('C:\\Users\\Kristina\\Documents\\Diplomski rad\\DesignerAppBackend\\DesignerAppFirebaseCreds.json')  # Replace with your credentials file path
firebase_admin.initialize_app(cred, {
    'storageBucket': 'designerapp-65092.appspot.com'
})

# Get a reference to the storage service
bucket = storage.bucket()

# Define the file path and destination in your storage bucket
image_path = 'images/slika.jpg'
image_ref = bucket.blob(image_path)

# Upload the image file
try:
    with open('C:\\Users\\Kristina\\Documents\\Diplomski rad\\DesignerAppBackend\\slika.png', 'rb') as image_file:  # Replace with your image file path
        image_ref.upload_from_file(image_file)
        print('Upload complete!')

        # Get the download URL (optional)
        download_url = image_ref.public_url
        print(f'Download URL: {download_url}')

except Exception as e:
    print(f'Error uploading image: {e}')
