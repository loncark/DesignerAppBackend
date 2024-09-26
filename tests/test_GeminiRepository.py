import unittest
from unittest.mock import patch, Mock
from repository.RealGeminiRepository import RealGeminiRepository

class TestGeminiRepository(unittest.TestCase):
    def setUp(self):
        self.repository = RealGeminiRepository()

    @patch('google.generativeai.GenerativeModel.generate_content')
    def test_fetchData(self, mockGenerateContent):
        mockResponse = Mock()
        mockResponse.text = "Cats are furry, domesticated mammals often kept as pets."
        mockGenerateContent.return_value = mockResponse

        result = self.repository.fetchData("Tell me what cats are in one sentence.")
        
        mockGenerateContent.assert_called_once_with("Tell me what cats are in one sentence.")
        self.assertEqual(result, "Cats are furry, domesticated mammals often kept as pets.")
