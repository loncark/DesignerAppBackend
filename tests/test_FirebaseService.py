import unittest
from unittest.mock import patch, Mock, MagicMock
from service.FirebaseService import storeDesignToDb, getAllDesigns, deleteDesign, storeToStorage, deleteFromStorageByUrl, createDesignZip

class TestFirebaseService(unittest.TestCase):

    @patch('firebase_admin.db.reference')
    def test_storeDesignToDb(self, mock_reference):
        mock_ref = Mock()
        mock_design_ref = Mock()
        mock_reference.return_value = mock_ref
        mock_ref.child.return_value = mock_design_ref

        design_name = "Test Design"
        title = "Test Title"
        tags = ["tag1", "tag2"]
        related_links = ["http://example.com"]
        image_links = ["http://example.com/image.png"]
        design_id = "12345"

        # update case
        mock_design_ref.get.return_value = True
        result = storeDesignToDb(design_name, title, tags, related_links, image_links, design_id)
        mock_design_ref.update.assert_called_once_with({
            'design_name': design_name,
            'title': title,
            'tags': tags,
            'related_links': related_links,
            'image_links': image_links
        })
        self.assertEqual(result, f"Design with ID {design_id} updated successfully")

        mock_design_ref.reset_mock()

        # create
        mock_design_ref.get.return_value = None
        result = storeDesignToDb(design_name, title, tags, related_links, image_links, design_id)
        mock_design_ref.set.assert_called_once_with({
            'design_name': design_name,
            'title': title,
            'tags': tags,
            'related_links': related_links,
            'image_links': image_links
        })
        self.assertEqual(result, f"Design with ID {design_id} added successfully")

    @patch('firebase_admin.db.reference')
    def test_getAllDesigns(self, mock_reference):
        mock_ref = Mock()
        mock_reference.return_value = mock_ref

        mock_designs = {
            '12345': {
                'design_name': 'Design 1',
                'related_links': ['http://example.com/1'],
                'image_links': ['http://example.com/image1.png'],
                'tags': ['tag1', 'tag2'],
                'title': 'Title 1'
            },
            '67890': {
                'design_name': 'Design 2',
                'related_links': ['http://example.com/2'],
                'image_links': ['http://example.com/image2.png'],
                'tags': ['tag3', 'tag4'],
                'title': 'Title 2'
            }
        }

        mock_ref.get.return_value = mock_designs

        result = getAllDesigns()

        expected = [
            {
                'design_name': 'Design 1',
                'design_id': '12345',
                'related_links': ['http://example.com/1'],
                'image_links': ['http://example.com/image1.png'],
                'tags': ['tag1', 'tag2'],
                'title': 'Title 1'
            },
            {
                'design_name': 'Design 2',
                'design_id': '67890',
                'related_links': ['http://example.com/2'],
                'image_links': ['http://example.com/image2.png'],
                'tags': ['tag3', 'tag4'],
                'title': 'Title 2'
            }
        ]

        self.assertEqual(result, expected)

        # no designs case
        mock_ref.get.return_value = None
        result = getAllDesigns()
        self.assertEqual(result, [])

        # exception handling
        mock_ref.get.side_effect = Exception("Test exception")
        result = getAllDesigns()
        self.assertEqual(result, 'Error retrieving designs: Test exception')

    @patch('firebase_admin.db.reference')
    def test_deleteDesign(self, mock_reference):
        mock_ref = Mock()
        mock_reference.return_value = mock_ref

        # success
        design_id = '12345'
        result = deleteDesign(design_id)
        mock_ref.delete.assert_called_once()
        self.assertEqual(result, f"Design with ID {design_id} deleted successfully")

        # exception
        mock_ref.delete.side_effect = Exception("Test exception")
        result = deleteDesign(design_id)
        self.assertEqual(result, 'Error deleting design data: Test exception')

    @patch('firebase_admin.storage.bucket')
    @patch('PIL.Image.open')
    @patch('uuid.uuid4')
    def test_storeToStorage(self, mock_uuid, mock_image_open, mock_bucket):
        mock_image = Mock()
        mock_image_open.return_value = mock_image

        mock_uuid.return_value = 'test-uuid'

        mock_blob = Mock()
        mock_bucket.return_value.blob.return_value = mock_blob

        image_file = 'test_image.png'
        design_id = '12345'
        temp_path = '/tmp/image.png'

        result = storeToStorage(image_file, design_id)

        mock_image.save.assert_called_once_with(temp_path, format='PNG')

        mock_bucket.return_value.blob.assert_called_once_with(f'images/{design_id}/test-uuid.png')
        mock_blob.upload_from_filename.assert_called_once_with(temp_path)

        mock_blob.make_public.assert_called_once()
        self.assertEqual(result, mock_blob.public_url)

        # exception case
        mock_image.save.side_effect = Exception("Test exception")
        result = storeToStorage(image_file, design_id)
        self.assertEqual(result, 'Error uploading image: Test exception')