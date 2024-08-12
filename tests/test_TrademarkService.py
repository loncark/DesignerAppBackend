import json
import unittest, os
from unittest.mock import patch, Mock
from service.TrademarkService import fetchResponse, filterJson

class TestTrademarkService(unittest.TestCase):
    @patch('requests.get')
    def test_fetchResponse(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {"whatever":"whatever"}

        mock_get.return_value = mock_response

        data = fetchResponse("prompt")
        mock_get.assert_called_with("https://uspto-trademark.p.rapidapi.com/v1/trademarkSearch/prompt/active", headers={'X-RapidAPI-Key': '39c42055c4msh632b3c92f3544ebp1ced69jsnb3f52628032e', 'X-RapidAPI-Host': 'uspto-trademark.p.rapidapi.com'})
        self.assertEqual(data, {"whatever":"whatever"})

    def test_filterJson(self):
        current_dir = os.path.dirname(__file__)
        mockdata_path = os.path.join(current_dir, 'mockdata', 'TrademarkMock.json')
        expected_path = os.path.join(current_dir, 'mockdata', 'TrademarkOut.json')

        with open(mockdata_path, 'r') as f:
            input_data = json.load(f)

        with open(expected_path, 'r') as f:
            expected_data = json.load(f)

        result = filterJson(input_data)

        self.assertEqual(result, expected_data)
