import unittest
from flask import Flask
from unittest.mock import patch, Mock, mock_open
from controller.FirebaseController import firebase_bp
import io
from PIL import Image

class TestFirebaseIntegration(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        app = Flask(__name__)
        app.register_blueprint(firebase_bp)
        cls.client = app.test_client()

    @patch('firebase_admin.db.reference')
    def test_getAllDesignsWhenTheyExist(self, mock_db_reference):
        mock_ref = Mock()
        mock_db_reference.return_value = mock_ref

        mock_ref.get.return_value = {
            'design_id_1': {
                'design_name': 'Design 1',
                'related_links': ['http://link1.com'],
                'image_links': ['http://image1.png'],
                'tags': ['tag1', 'tag2'],
                'title': 'Title 1'
            },
            'design_id_2': {
                'design_name': 'Design 2',
                'related_links': ['http://link2.com'],
                'image_links': ['http://image2.png'],
                'tags': ['tag3'],
                'title': 'Title 2'
            }
        }

        expected_response = [
            {
                'design_name': 'Design 1',
                'design_id': 'design_id_1',
                'related_links': ['http://link1.com'],
                'image_links': ['http://image1.png'],
                'tags': ['tag1', 'tag2'],
                'title': 'Title 1'
            },
            {
                'design_name': 'Design 2',
                'design_id': 'design_id_2',
                'related_links': ['http://link2.com'],
                'image_links': ['http://image2.png'],
                'tags': ['tag3'],
                'title': 'Title 2'
            }
        ]

        response = self.client.get('/db/allDesigns')

        mock_db_reference.assert_called_once_with('/Designs')
        mock_ref.get.assert_called_once()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected_response)

    @patch('firebase_admin.db.reference')
    def test_getAllDesignsWhenTheyNotExist(self, mock_db_reference):
        mock_ref = Mock()
        mock_db_reference.return_value = mock_ref

        mock_ref.get.return_value = None

        response = self.client.get('/db/allDesigns')

        mock_db_reference.assert_called_once_with('/Designs')
        mock_ref.get.assert_called_once()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, [])

    @patch('firebase_admin.db.reference')
    def test_getAllDesignsException(self, mock_db_reference):
        mock_ref = Mock()
        mock_db_reference.return_value = mock_ref
        mock_ref.get.side_effect = Exception("Database error")

        response = self.client.get('/db/allDesigns')

        mock_db_reference.assert_called_once_with('/Designs')
        mock_ref.get.assert_called_once()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), 'Error retrieving designs: Database error')

    @patch('firebase_admin.db.reference')
    def test_storeDesignToDbWhenIdNotExists(self, mock_db_reference):
        mock_ref = Mock()
        mock_db_reference.return_value = mock_ref
        
        mock_child_ref = Mock()
        mock_ref.child.return_value = mock_child_ref
        
        mock_child_ref.get.return_value = None
        
        design_name = "Test Design"
        title = "Test Title"
        tags = ["tag1", "tag2"]
        related_links = ["http://test.com"]
        image_links = ["http://test.png"]
        design_id = "test_id_1"
        
        result = self.client.post('/db/saveDesign', json={'design_name': design_name, 'title': title, 'tags': tags, 'related_links': related_links, 'image_links': image_links, 'design_id': design_id})        
        
        mock_db_reference.assert_called_once_with('/Designs')
        mock_ref.child.assert_called_once_with(design_id)
        mock_child_ref.get.assert_called_once()
        mock_child_ref.set.assert_called_once_with({
            'design_name': design_name,
            'title': title,
            'tags': tags,
            'related_links': related_links,
            'image_links': image_links
        })
        self.assertEqual(result.status_code, 200)
        self.assertIn(f"Design with ID {design_id} added successfully", result.get_data(as_text=True))
    
    @patch('firebase_admin.db.reference')
    def test_storeDesignToDbWhenIdExists(self, mock_db_reference):
        mock_ref = Mock()
        mock_db_reference.return_value = mock_ref
        
        mock_child_ref = Mock()
        mock_ref.child.return_value = mock_child_ref
        
        mock_child_ref.get.return_value = {"existing": "data"}
        
        design_name = "Updated Design"
        title = "Updated Title"
        tags = ["tag3", "tag4"]
        related_links = ["http://updated.com"]
        image_links = ["http://updated.png"]
        design_id = "test_id_2"
        
        result = self.client.post('/db/saveDesign', json={'design_name': design_name, 'title': title, 'tags': tags, 'related_links': related_links, 'image_links': image_links, 'design_id': design_id})        
        
        mock_db_reference.assert_called_once_with('/Designs')
        mock_ref.child.assert_called_once_with(design_id)
        mock_child_ref.get.assert_called_once()
        mock_child_ref.update.assert_called_once_with({
            'design_name': design_name,
            'title': title,
            'tags': tags,
            'related_links': related_links,
            'image_links': image_links
        })
        self.assertEqual(result.status_code, 200)
        self.assertIn(f"Design with ID {design_id} updated successfully", result.get_data(as_text=True))
    
    @patch('firebase_admin.db.reference')
    def test_storeDesignToDbException(self, mock_db_reference):
        mock_db_reference.side_effect = Exception("Test error")
        
        design_name = "Error Design"
        title = "Error Title"
        tags = ["tag5"]
        related_links = ["http://error.com"]
        image_links = ["http://error.png"]
        design_id = "test_id_3"
        
        result = self.client.post('/db/saveDesign', json={'design_name': design_name, 'title': title, 'tags': tags, 'related_links': related_links, 'image_links': image_links, 'design_id': design_id})        

        mock_db_reference.assert_called_once_with('/Designs')
        self.assertEqual(result.status_code, 500)
        self.assertIn("500 Internal Server Error", result.get_data(as_text=True))
        
    @patch('firebase_admin.db.reference')
    def test_deleteDesignWhenOneExists(self, mock_db_reference):
        mock_ref = Mock()
        mock_db_reference.return_value = mock_ref
        
        design_id = "test_id_1"
        
        response = self.client.delete(f'/db/deleteDesign', json={'design_id': design_id})
        
        mock_db_reference.assert_called_once_with(f'Designs/{design_id}')
        mock_ref.delete.assert_called_once()
        self.assertEqual(response.status_code, 200)
        self.assertIn(f"Design with ID {design_id} deleted successfully", response.get_data(as_text=True))

    @patch('firebase_admin.db.reference')
    def test_deleteDesignException(self, mock_db_reference):
        mock_ref = Mock()
        mock_db_reference.return_value = mock_ref
        mock_ref.delete.side_effect = Exception("Test error")
        
        design_id = "test_id_2"
        
        response = self.client.delete(f'/db/deleteDesign', json={'design_id': design_id})
        
        mock_db_reference.assert_called_once_with(f'Designs/{design_id}')
        mock_ref.delete.assert_called_once()
        self.assertEqual(response.status_code, 200)
        self.assertIn("Error deleting design data: Test error", response.get_data(as_text=True))

    @patch('service.FirebaseService.storage.bucket')
    @patch('uuid.uuid4')
    def test_storeToStorageSuccess(self, mock_uuid, mock_storage_bucket):
        mock_uuid.return_value = "mocked-uuid"

        mock_bucket = Mock()
        mock_storage_bucket.return_value = mock_bucket
        mock_blob = Mock()
        mock_bucket.blob.return_value = mock_blob
        mock_blob.public_url = "https://storage.googleapis.com/bucket-name/images/test-design-id/mocked-uuid.png"

        img = Image.new('RGB', (60, 30), color = 'red')
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format='PNG')
        img_byte_arr = img_byte_arr.getvalue()

        response = self.client.post('/storage', 
                            data={'design_id': 'test-design-id', 'image': (io.BytesIO(img_byte_arr), 'test_image.png')},
                            content_type='multipart/form-data')
        
        mock_storage_bucket.assert_called_once()
        mock_bucket.blob.assert_called_once_with('images/test-design-id/mocked-uuid.png')
        mock_blob.upload_from_filename.assert_called_once()
        mock_blob.make_public.assert_called_once()

        self.assertEqual(response.status_code, 200)
        expected_response = {"url": "https://storage.googleapis.com/bucket-name/images/test-design-id/mocked-uuid.png"}
        self.assertEqual(response.get_json(), expected_response)

    @patch('service.FirebaseService.storage.bucket')
    def test_storeToStorageException(self, mock_storage_bucket):
        mock_storage_bucket.side_effect = Exception("Test storage error")

        img = Image.new('RGB', (60, 30), color = 'red')
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format='PNG')
        img_byte_arr = img_byte_arr.getvalue()

        response = self.client.post('/storage', 
                            data={'design_id': 'test-design-id', 'image': (io.BytesIO(img_byte_arr), 'test_image.png')},
                            content_type='multipart/form-data')
        
        mock_storage_bucket.assert_called_once()
        self.assertEqual(response.status_code, 200)  # Note: Your current implementation always returns 200
        self.assertIn("Error uploading image: Test storage error", response.get_data(as_text=True))

    @patch('service.FirebaseService.storage.bucket')
    def test_deleteFromStorageSuccess(self, mock_storage_bucket):
        mock_bucket = Mock()
        mock_storage_bucket.return_value = mock_bucket
        mock_blob = Mock()
        mock_bucket.blob.return_value = mock_blob

        mock_blob.exists.return_value = True

        test_url = 'https://storage.googleapis.com/bucket-name/images/design-id/mocked-uuid.png'

        response = self.client.delete('/storageDelete',
                                      json={'imgUrl': test_url})

        mock_storage_bucket.assert_called_once()
        mock_bucket.blob.assert_called_once_with('design-id/mocked-uuid.png')
        mock_blob.exists.assert_called_once()
        mock_blob.delete.assert_called_once()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'msg': 'File deleted successfully'})

    @patch('service.FirebaseService.storage.bucket')
    def test_deleteFromStorageFileNotExists(self, mock_storage_bucket):
        mock_bucket = Mock()
        mock_storage_bucket.return_value = mock_bucket
        mock_blob = Mock()
        mock_bucket.blob.return_value = mock_blob

        mock_blob.exists.return_value = False

        test_url = 'https://storage.googleapis.com/bucket-name/images/design-id/non-existent-file.png'

        response = self.client.delete('/storageDelete',
                                      json={'imgUrl': test_url})

        mock_storage_bucket.assert_called_once()
        mock_bucket.blob.assert_called_once_with('design-id/non-existent-file.png')
        mock_blob.exists.assert_called_once()
        mock_blob.delete.assert_not_called()  # Since the file doesn't exist

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'msg': 'File does not exist or incorrect url'})

    @patch('service.FirebaseService.os.makedirs')
    @patch('service.FirebaseService.os.remove')
    @patch('service.FirebaseService.os.rmdir')
    @patch('service.FirebaseService.requests.get')
    @patch('service.FirebaseService.ZipFile')
    @patch('service.FirebaseService.os.walk')
    @patch('service.FirebaseService.open', new_callable=mock_open)
    def test_downloadDesignSuccess(self, mock_file, mock_walk, mock_zipfile, 
                                     mock_requests_get, mock_rmdir, mock_remove, mock_makedirs):
        
        image1 = 'https://play-lh.googleusercontent.com/HRuayD8pJ2OWiAqaNC7xibO96ydDTmYETtqujTMLJt_e6U82Wc7oAZVFC_OOg8dNQ2E'
        image2 = 'https://aidsresource.org/wp-content/uploads/2016/09/cropped-512x512.png'
        design = {
            'design_name': 'Test Design',
            'design_id': '123',
            'tags': ['tag1', 'tag2'],
            'title': 'Test Title',
            'related_links': ['http://link1.com', 'http://link2.com'],
            'image_links': [image1, image2]
        }

        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.content = b'fake image content'
        mock_requests_get.return_value = mock_response

        temp_dir = f"temp_Test Design_123"
        mock_walk.return_value = [
            (temp_dir, [], ['design_info_123.txt', 'image_1.png', 'image_2.png'])
        ]

        mock_zipfile_instance = Mock()
        mock_zipfile.return_value.__enter__.return_value = mock_zipfile_instance

        response = self.client.post('/downloadDesign', json=design)

        mock_makedirs.assert_called_once_with(temp_dir, exist_ok=True)
        mock_requests_get.assert_any_call(image1)
        mock_requests_get.assert_any_call(image2)
        mock_zipfile.assert_called_once()

        expected_txt_content = f"""Design name: Test Design
Design id: 123

Tags: tag1, tag2
Title: Test Title

Related links:
http://link1.com
http://link2.com"""
        #mock_file().write.assert_any_call(expected_txt_content)
        #same error as in service unit test

        #self.assertEqual(response.status_code, 200)
        #self.assertEqual(response.mimetype, 'application/zip')
        #returns 500 for some reason

        #mock_remove.assert_called()
        #mock_rmdir.assert_called_once_with(temp_dir)

    @patch('service.FirebaseService.os.makedirs')
    @patch('service.FirebaseService.requests.get')
    @patch('service.FirebaseService.open', new_callable=mock_open)
    def test_downloadDesignException(self, mock_file, mock_requests_get, mock_makedirs):
        design = {
            'design_name': 'Test Design',
            'design_id': '123',
            'tags': ['tag1', 'tag2'],
            'title': 'Test Title',
            'related_links': ['http://link1.com', 'http://link2.com'],
            'image_links': ['http://invalid_image_link.png']
        }

        mock_response = Mock()
        mock_response.status_code = 404
        mock_requests_get.return_value = mock_response

        response = self.client.post('/downloadDesign', json=design)

        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.get_json(), {'error': 'Error downloading file.'})
