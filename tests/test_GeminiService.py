import unittest
from unittest.mock import patch, Mock
from service.GeminiService import fetchResponse

class TestGeminiService(unittest.TestCase):

    @patch('google.generativeai.GenerativeModel.generate_content')
    def test_fetchResponse(self, mockGenerateContent):
        mockResponse = Mock()
        mockResponse.text = "Cats are furry, domesticated mammals often kept as pets."
        mockGenerateContent.return_value = mockResponse

        result = fetchResponse("Tell me what cats are in one sentence.")
        
        mockGenerateContent.assert_called_once_with("Tell me what cats are in one sentence.")
        self.assertEqual(result, "Cats are furry, domesticated mammals often kept as pets.")
