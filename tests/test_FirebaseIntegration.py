import unittest, json
from app import createApp
from unittest.mock import patch, Mock
import io
from PIL import Image

class TestFirebaseIntegration(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        app = createApp(providerConfigName = 'Primary', repositoryConfigName='Development')
        self.client = app.flaskInstance.test_client()

    @patch('firebase_admin.db.reference')
    def test_saveDesign(self, mock_db_reference):
        mockDbRef = Mock()
        mock_db_reference.return_value = mockDbRef
        mockDesignRef = Mock()
        mockDbRef.child.return_value = mockDesignRef

        design_name = "Test Design"
        title = "Test Title"
        tags = ["tag1", "tag2"]
        related_links = []
        image_links = []
        description = "Some description."
        design_id = "12345"

        # case 1
        mockDesignRef.get.return_value = True

        result = self.client.post('/db/saveDesign', json={'design_name': design_name, 'title': title, 'tags': tags, 'related_links': related_links, 'image_links': image_links, 'description': description, 'design_id': design_id})

        mock_db_reference.assert_called_once_with('/Designs')
        mockDbRef.child.assert_called_once_with(design_id)
        mockDesignRef.get.assert_called_once()
        mockDesignRef.update.assert_called_once_with({
            'design_name': design_name,
            'title': title,
            'tags': tags,
            'related_links': related_links,
            'image_links': image_links,
            'description': description 
        })
        self.assertEqual(result.get_data(as_text=True), "Design with ID 12345 updated successfully")

        # case 2
        mock_db_reference.reset_mock()
        mockDesignRef.get.return_value = False

        result = self.client.post('/db/saveDesign', json={'design_name': design_name, 'title': title, 'tags': tags, 'related_links': related_links, 'image_links': image_links, 'description': description, 'design_id': design_id})

        mock_db_reference.assert_called_once_with('/Designs')
        mockDbRef.child.assert_called_once_with(design_id)
        mockDesignRef.get.assert_called_once()
        mockDesignRef.set.assert_called_once_with({
            'design_name': design_name,
            'title': title,
            'tags': tags,
            'related_links': related_links,
            'image_links': image_links,
            'description': description 
        })
        self.assertEqual(result.get_data(as_text=True), "Design with ID 12345 added successfully")

        # case 3
        mockDesignRef.get.side_effect = Exception("Test exception")

        result = self.client.post('/db/saveDesign', json={'design_name': design_name, 'title': title, 'tags': tags, 'related_links': related_links, 'image_links': image_links, 'description': description, 'design_id': design_id})

        self.assertEqual(result.get_data(as_text=True), 'Error uploading design data: Test exception')


    @patch('firebase_admin.db.reference')
    def test_getAllDesigns(self, mock_db_reference):       
        mockDbRef = Mock()
        mock_db_reference.return_value = mockDbRef
        mockDesigns = {
            '12345': {
                'design_name':'Some name'
            },
            '67890':{
                'description':'Some description'
            }
        }

        # case 1
        mockDbRef.get.return_value = mockDesigns
        expectedResult = [
            {
                'description': '',
                'design_id': '12345',
                'design_name': 'Some name',
                'image_links': [],
                'related_links': [],
                'tags': [],
                'title': ''
            },
            {
                'description':'Some description',
                'design_id': '67890',
                'design_name': '',
                'image_links': [],
                'related_links': [],
                'tags': [],
                'title': ''
            }
        ]

        result = self.client.get('/db/allDesigns')
        
        mock_db_reference.assert_called_once_with('/Designs')
        mockDbRef.get.assert_called_once()
        self.assertListEqual(json.loads(result.get_data(as_text=True)), expectedResult)
        
        # case 2
        mock_db_reference.reset_mock()
        mockDbRef.get.return_value = None
        mock_db_reference.return_value = mockDbRef
        expectedResult = []

        result = self.client.get('/db/allDesigns')
        
        mock_db_reference.assert_called_once_with('/Designs')
        mockDbRef.get.assert_called_once()
        self.assertEqual(json.loads(result.get_data(as_text=True)), expectedResult)
        
        # case 3
        mock_db_reference.reset_mock()
        mockDbRef.get.side_effect = Exception("Test exception")

        result = self.client.get('/db/allDesigns')

        mock_db_reference.assert_called_once_with('/Designs')
        self.assertEqual(json.loads(result.get_data(as_text=True))['error'], 'Error retrieving design data: Test exception')
        

    @patch('firebase_admin.db.reference')
    def test_deleteDesign(self, mock_db_reference):
        mockDbRef = Mock()
        mock_db_reference.return_value = mockDbRef

        # case 1
        result = self.client.delete('/db/deleteDesign', json={'design_id': '12345'})
        mockDbRef.delete.assert_called_once()
        self.assertEqual(result.get_data(as_text=True), "Design with ID 12345 deleted successfully")

        # case 2
        mock_db_reference.reset_mock()
        mockDbRef.delete.side_effect = Exception("Test exception")
        result = self.client.delete('/db/deleteDesign', json={'design_id': '12345'})
        self.assertEqual(result.get_data(as_text=True), 'Error deleting design data: Test exception')


    @patch('repository.RealFirebaseRepository.storage.bucket')
    @patch('uuid.uuid4')
    def test_saveImage(self, mock_uuid, mock_storage_bucket):
        mockBucket = Mock()
        mock_storage_bucket.return_value = mockBucket
        mockBlob = Mock()
        mockBucket.blob.return_value = mockBlob
        mock_uuid.return_value = 'testId'

        img = Image.new('RGB', (30, 30))
        imgByteArray = io.BytesIO()
        img.save(imgByteArray, format='PNG')

        # case 1
        mockBlob.public_url = 'test-url'
        data={'design_id': '12345', 'image': (io.BytesIO(imgByteArray.getvalue()), 'test_image.png')}

        result = self.client.post('/storage', data=data, content_type='multipart/form-data')

        mock_storage_bucket.assert_called_once()
        mockBucket.blob.assert_called_once_with(f'images/12345/testId.png')
        mockBlob.upload_from_filename.assert_called_once_with('/tmp/image.png')
        mockBlob.make_public.assert_called_once()
            
        resultUrl = json.loads(result.get_data(as_text=True))['url'] 
        self.assertEqual(resultUrl, 'test-url')
            
        # case 2
        mock_storage_bucket.side_effect = Exception('Test exception')
        data={'design_id': '12345', 'image': (io.BytesIO(imgByteArray.getvalue()), 'test_image.png')}
            
        result = self.client.post('/storage', data=data, content_type='multipart/form-data')

        self.assertEqual(result.status_code, 500)
        resultMsg = json.loads(result.get_data(as_text=True))['error'] 
        self.assertEqual(resultMsg, 'Test exception')
    
    
    @patch('repository.RealFirebaseRepository.storage.bucket')
    def test_deleteImage(self, mock_storage_bucket):
        mockBucket = Mock()
        mock_storage_bucket.return_value = mockBucket
        mockBlob = Mock()
        mockBucket.blob.return_value = mockBlob
        testUrl = "https://storage.googleapis.com/bucket_name/folder/file.txt"

        # case 1
        mockBlob.exists.return_value = True

        result = self.client.delete('/storageDelete', json={"imgUrl":testUrl})
        
        mockBucket.blob.assert_called_once_with('folder/file.txt')
        mockBlob.exists.assert_called_once()
        mockBlob.delete.assert_called_once()
        self.assertEqual(result.status_code, 200)
        resultMsg = json.loads(result.get_data(as_text=True))['msg']
        self.assertEqual(resultMsg, 'File deleted successfully')

        # case 2
        mockBucket.blob.reset_mock()
        mockBlob.exists.return_value = False
        
        result = self.client.delete('/storageDelete', json={"imgUrl":testUrl})

        mockBucket.blob.assert_called_once_with('folder/file.txt')
        mockBlob.exists.assert_called_once()
        mockBlob.delete.assert_not_called()
        self.assertEqual(result.status_code, 400)
        resultMsg = json.loads(result.get_data(as_text=True))['msg']
        self.assertEqual(resultMsg, 'File does not exist or incorrect url')
        
        # case 3
        mockBucket.blob.reset_mock()
        mockBlob.delete.side_effect = Exception("Test exception")

        result = self.client.delete('/storageDelete', json={"imgUrl":testUrl})
        
        self.assertEqual(result.status_code, 400)
        resultMsg = json.loads(result.get_data(as_text=True))['msg']
        self.assertEqual(resultMsg, 'File does not exist or incorrect url')    
