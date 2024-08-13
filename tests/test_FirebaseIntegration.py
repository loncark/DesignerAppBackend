import unittest
from flask import Flask
from unittest.mock import patch, Mock
from controller.FirebaseController import firebase_bp

class TestGetAllDesignsRoute(unittest.TestCase):

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

