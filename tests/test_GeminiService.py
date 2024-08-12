import unittest
from unittest.mock import patch, Mock
from service.GeminiService import fetchResponse, generateTags, generateTitle

class TestGeminiService(unittest.TestCase):

    @patch('google.generativeai.GenerativeModel.generate_content')
    def test_fetchResponse(self, mock_generate_content):
        mock_response = Mock()
        mock_response.text = "Cats are furry, domesticated mammals often kept as pets."
        mock_generate_content.return_value = mock_response

        result = fetchResponse("Tell me what cats are in one sentence.")
        
        mock_generate_content.assert_called_once_with("Tell me what cats are in one sentence.")
        self.assertEqual(result, "Cats are furry, domesticated mammals often kept as pets.")

    @patch('google.generativeai.GenerativeModel.generate_content')
    def test_generateTags(self, mock_generate_content):
        mock_response = Mock()
        mock_response.text = "handmade, vintage, unique, colorful, bohemian"
        mock_generate_content.return_value = mock_response

        result = generateTags("boho necklace")
        
        expected_prompt = """Generate me a list of tags I could use for Etsy SEO optimization of my "boho necklace" listing. Separate these tags using a comma and write out nothing else."""
        mock_generate_content.assert_called_once_with(expected_prompt)
        self.assertEqual(result, ["handmade", "vintage", "unique", "colorful", "bohemian"])

    @patch('google.generativeai.GenerativeModel.generate_content')
    def test_generateTitle(self, mock_generate_content):
        mock_response = Mock()
        mock_response.text = "Bohemian Jewelry, Hippie Necklace, Gypsy Accessories"
        mock_generate_content.return_value = mock_response

        result = generateTitle("boho necklace")
        
        expected_prompt = """Generate me a list of synonyms I could use in the title of my "boho necklace" listing of Etsy. They should be some phrases that people usually type in the search bar when looking for similar items. The first letter of every word in a synonym should be capitalized. Separate these tags using a comma and write out nothing else."""
        mock_generate_content.assert_called_once_with(expected_prompt)
        self.assertEqual(result, ["Bohemian Jewelry", "Hippie Necklace", "Gypsy Accessories"])