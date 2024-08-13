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
    def test_get_all_designs(self, mock_db_reference):
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
    def test_get_all_designs_empty(self, mock_db_reference):
        mock_ref = Mock()
        mock_db_reference.return_value = mock_ref

        mock_ref.get.return_value = None

        response = self.client.get('/db/allDesigns')

        mock_db_reference.assert_called_once_with('/Designs')
        mock_ref.get.assert_called_once()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, [])

    @patch('firebase_admin.db.reference')
    def test_get_all_designs_exception(self, mock_db_reference):
        mock_ref = Mock()
        mock_db_reference.return_value = mock_ref
        mock_ref.get.side_effect = Exception("Database error")

        response = self.client.get('/db/allDesigns')

        mock_db_reference.assert_called_once_with('/Designs')
        mock_ref.get.assert_called_once()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), 'Error retrieving designs: Database error')

