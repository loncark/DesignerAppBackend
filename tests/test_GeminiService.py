import unittest
from unittest.mock import patch, Mock
from service.GeminiService import fetchResponse, generateTags, generateTitle

class TestGeminiService(unittest.TestCase):

    @patch('google.generativeai.GenerativeModel.generate_content')
    def test_fetchResponse(self, mockGenerateContent):
        mockResponse = Mock()
        mockResponse.text = "Cats are furry, domesticated mammals often kept as pets."
        mockGenerateContent.return_value = mockResponse

        result = fetchResponse("Tell me what cats are in one sentence.")
        
        mockGenerateContent.assert_called_once_with("Tell me what cats are in one sentence.")
        self.assertEqual(result, "Cats are furry, domesticated mammals often kept as pets.")

    @patch('google.generativeai.GenerativeModel.generate_content')
    def test_generateTags(self, mockGenerateContent):
        mockResponse = Mock()
        mockResponse.text = "handmade, vintage, unique, colorful"
        mockGenerateContent.return_value = mockResponse

        result = generateTags("vintage necklace")
        
        expectedPrompt = """Generate me a list of tags I could use for Etsy SEO optimization of my "vintage necklace" listing. Separate these tags using a comma and write out nothing else."""
        mockGenerateContent.assert_called_once_with(expectedPrompt)
        self.assertEqual(result, ["handmade", "vintage", "unique", "colorful"])

    @patch('google.generativeai.GenerativeModel.generate_content')
    def test_generateTitle(self, mockGenerateContent):
        mockResponse = Mock()
        mockResponse.text = "Vintage Jewelry, Pretty Necklace, Cool Accessories"
        mockGenerateContent.return_value = mockResponse

        result = generateTitle("vintage necklace")
        
        expectedPrompt = """Generate me a list of synonyms I could use in the title of my "vintage necklace" listing of Etsy. They should be some phrases that people usually type in the search bar when looking for similar items. The first letter of every word in a synonym should be capitalized. Separate these tags using a comma and write out nothing else."""
        mockGenerateContent.assert_called_once_with(expectedPrompt)
        self.assertEqual(result, ["Vintage Jewelry", "Pretty Necklace", "Cool Accessories"])