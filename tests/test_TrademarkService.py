import json, requests
import unittest
from unittest.mock import patch, Mock
from service.TrademarkService import fetchAndFilterResponse, fetchResponse, filterJson

class TestTrademarkService(unittest.TestCase):
    @patch('requests.get')
    def test_fetchResponse(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {"whatever":"whatever"}

        mock_get.return_value = mock_response

        data = fetchResponse("prompt")
        mock_get.assert_called_with("https://uspto-trademark.p.rapidapi.com/v1/trademarkSearch/prompt/active", headers={'X-RapidAPI-Key': '39c42055c4msh632b3c92f3544ebp1ced69jsnb3f52628032e', 'X-RapidAPI-Host': 'uspto-trademark.p.rapidapi.com'})
        self.assertEqual(data, {"whatever":"whatever"})

if __name__ == '__main__':
    unittest.main()