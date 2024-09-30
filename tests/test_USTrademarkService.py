import unittest, json
from service.USTrademarkService import USTrademarkService
from repository.DummyUSTrademarkRepository import DummyUSTrademarkRepository

class TestUSTrademarkService(unittest.TestCase):
    def setUp(self):
        self.service = USTrademarkService(DummyUSTrademarkRepository())

    def test_filterJson(self):
        inputData = self.service.fetchTrademarks("Some Prompt")
        result = self.service.filterJson(inputData)

        expectedDataPath = r"C:\Users\Kristina\Documents\Diplomski rad\DesignerAppBackend\tests\testData\TrademarksFiltered.json"
        with open(expectedDataPath, 'r') as f:
            expectedData = json.load(f)

        self.assertEqual(result, expectedData)
