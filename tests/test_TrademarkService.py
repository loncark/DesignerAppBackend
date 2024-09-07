import json
import unittest
from unittest.mock import patch, Mock
from service.TrademarkService import fetchResponse, filterJson
from config import RAPIDAPI_API_KEY

class TestTrademarkService(unittest.TestCase):
    @patch('requests.get')
    def test_fetchResponse(self, mock_get):
        mockResponse = Mock()
        mockResponse.json.return_value = {"whatever":"whatever"}

        mock_get.return_value = mockResponse

        data = fetchResponse("prompt")
        mock_get.assert_called_with("https://uspto-trademark.p.rapidapi.com/v1/trademarkSearch/prompt/active", headers={'X-RapidAPI-Key': RAPIDAPI_API_KEY, 'X-RapidAPI-Host': 'uspto-trademark.p.rapidapi.com'})
        self.assertEqual(data, {"whatever":"whatever"})

    def test_filterJson(self):
        mockDataPath = r"C:\Users\Kristina\Documents\Diplomski rad\DesignerAppBackend\tests\mockdata\TrademarkMock.json"
        expectedDataPath = r"C:\Users\Kristina\Documents\Diplomski rad\DesignerAppBackend\tests\mockdata\TrademarkOut.json"

        with open(mockDataPath, 'r') as f:
            inputData = json.load(f)

        with open(expectedDataPath, 'r') as f:
            expectedData = json.load(f)

        result = filterJson(inputData)

        self.assertEqual(result, expectedData)
