from interface.repositoryInterface.TrademarkCheckRepository import TrademarkCheckRepository
import json

class DummyTrademarkRepository(TrademarkCheckRepository):
    def __init__(self):
        pass
    
    def getTrademarks(self, prompt):
        if prompt != '':
            filePath = r"C:\Users\Kristina\Documents\Diplomski rad\DesignerAppBackend\sample JSONs\Trademarks1.json"
        else:
            filePath = r"C:\Users\Kristina\Documents\Diplomski rad\DesignerAppBackend\sample JSONs\Trademarks2.json"

        with open(filePath, 'r') as file:
            data = json.load(file)
            
        return data