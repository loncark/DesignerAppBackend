import unittest
from unittest.mock import patch, Mock
from constants import RAPIDAPI_API_KEY
from repository.RealUSTrademarkRepository import RealUSTrademarkRepository

class TestUSTrademarkRepository(unittest.TestCase):
    def setUp(self):
        self.repository = RealUSTrademarkRepository()

    @patch('requests.get')
    def test_getTrademarks(self, mock_get):
        mockResponse = Mock()
        mockResponse.json.return_value = {"whatever":"whatever"}

        mock_get.return_value = mockResponse

        data = self.repository.getTrademarks("prompt")
        mock_get.assert_called_with("https://uspto-trademark.p.rapidapi.com/v1/trademarkSearch/prompt/active", headers={'X-RapidAPI-Key': RAPIDAPI_API_KEY, 'X-RapidAPI-Host': 'uspto-trademark.p.rapidapi.com'})
        self.assertEqual(data, {"whatever":"whatever"})
