import unittest
from unittest.mock import patch, Mock
from repository.RealFirebaseRepository import RealFirebaseRepository

class TestFirebaseRepository(unittest.TestCase):
    def setUp(self):
        self.repository = RealFirebaseRepository()

    @patch('firebase_admin.db.reference')
    def test_storeDesignToDb(self, mock_db_reference):
        mockDbRef = Mock()
        mock_db_reference.return_value = mockDbRef
        mockDesignRef = Mock()
        mockDbRef.child.return_value = mockDesignRef

        design_name = "Test Design"
        title = "Test Title"
        tags = ["tag1", "tag2"]
        related_links = []
        image_links = [],
        description = "Some description."
        design_id = "12345"

        # case 1
        mockDesignRef.get.return_value = True
        result = self.repository.storeDesignToDb(design_name, title, tags, related_links, image_links, description, design_id)

        mockDesignRef.update.assert_called_once()
        self.assertEqual(result, "Design with ID 12345 updated successfully")

        # case 2
        mockDesignRef.get.return_value = False
        result = self.repository.storeDesignToDb(design_name, title, tags, related_links, image_links, description, design_id)

        mockDesignRef.set.assert_called_once()
        self.assertEqual(result, "Design with ID 12345 added successfully")

        # case 3
        mockDesignRef.get.side_effect = Exception("Test exception")

        result = self.repository.storeDesignToDb(design_name, title, tags, related_links, image_links, description, design_id)

        self.assertEqual(result, 'Error uploading design data: Test exception')


    @patch('firebase_admin.db.reference')
    def test_fetchData(self, mock_db_reference):
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
        expectedResult = mockDesigns

        result = self.repository.fetchData()
        
        mockDbRef.get.assert_called_once()
        mock_db_reference.assert_called_once()
        self.assertEqual(result, expectedResult)

        # case 2
        mock_db_reference.reset_mock()
        mockDbRef.get.return_value = None
        expectedResult = []

        result = self.repository.fetchData()

        mockDbRef.get.assert_called_once()
        mock_db_reference.assert_called_once()
        self.assertEqual(result, expectedResult)

        # case 3
        mockDbRef.get.side_effect = Exception("Test exception")
        result = self.repository.fetchData()
        self.assertEqual(result, "Error retrieving designs: Test exception")


    @patch('firebase_admin.db.reference')
    def test_deleteDesign(self, mock_db_reference):
        mockDbRef = Mock()
        mock_db_reference.return_value = mockDbRef

        # case 1
        result = self.repository.deleteDesign('12345')
        mockDbRef.delete.assert_called_once()
        self.assertEqual(result, "Design with ID 12345 deleted successfully")

        # case 2
        mockDbRef.delete.side_effect = Exception("Test exception")
        result = self.repository.deleteDesign('12345')
        self.assertEqual(result, 'Error deleting design data: Test exception')


    @patch('firebase_admin.storage.bucket')
    @patch('PIL.Image.open')
    @patch('uuid.uuid4')
    def test_storeToStorage(self, mock_uuid, mock_image_open, mock_storage_bucket):
            mockBucket = Mock()
            mock_storage_bucket.return_value = mockBucket
            mockImage = Mock()
            mock_image_open.return_value = mockImage
            mockBlob = Mock()
            mockBucket.blob.return_value = mockBlob
            mock_uuid.return_value = 'testId'

            # case 1
            mockBlob.public_url = 'test-url'

            result = self.repository.storeToStorage('test.png', '12345')

            mockImage.save.assert_called_once_with('/tmp/image.png', format='PNG')
            mockBucket.blob.assert_called_once_with(f'images/12345/testId.png')
            mockBlob.upload_from_filename.assert_called_once_with('/tmp/image.png')
            mockBlob.make_public.assert_called_once()
            
            self.assertEqual(result, 'test-url')
            
            # case 2
            mockImage.save.side_effect = Exception
            
            with self.assertRaises(Exception):
                self.repository.storeToStorage('test.png', '12345')


    @patch('firebase_admin.storage.bucket')
    def test_deleteFromStorageByUrl(self, mock_storage_bucket):
        mockBucket = Mock()
        mock_storage_bucket.return_value = mockBucket
        mockBlob = Mock()
        mockBucket.blob.return_value = mockBlob
        testUrl = "https://storage.googleapis.com/bucket_name/folder/file.txt"

        # case 1
        mockBlob.exists.return_value = True

        result = self.repository.deleteFromStorageByUrl(testUrl)
        
        mockBucket.blob.assert_called_once_with('folder/file.txt')
        mockBlob.delete.assert_called_once()
        self.assertTrue(result)

        # case 2
        mockBlob.exists.return_value = False
        
        result = self.repository.deleteFromStorageByUrl(testUrl)

        self.assertFalse(result)
        
        # case 3
        mockBlob.delete.side_effect = Exception("Test exception")

        result = self.repository.deleteFromStorageByUrl(testUrl)
        
        self.assertFalse(result)
        