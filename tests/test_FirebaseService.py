import unittest
from service.FirebaseService import FirebaseService
from repository.DummyFirebaseRepository import DummyFirebaseRepository

class TestFirebaseService(unittest.TestCase):
    def setUp(self):
        self.service = FirebaseService(DummyFirebaseRepository())

    def test_designsWithIds(self):
        mockDesigns = {
            '12345': {
                'design_name':'Some name'
            },
            '67890':{
                'description':'Some description'
            }
        }
        
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

        result = self.service.designsWithIds(mockDesigns)

        self.assertEqual(result, expectedResult)