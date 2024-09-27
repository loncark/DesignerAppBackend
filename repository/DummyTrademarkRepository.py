from interface.Repository import Repository
import json

class DummyTrademarkRepository(Repository):
    def fetchTrademarks(self, prompt):
        if prompt != '':
            filePath = r"C:\Users\Kristina\Documents\Diplomski rad\DesignerAppBackend\sample JSONs\Trademarks1.json"
        else:
            filePath = r"C:\Users\Kristina\Documents\Diplomski rad\DesignerAppBackend\sample JSONs\Trademarks2.json"

        with open(filePath, 'r') as file:
            data = json.load(file)
            
        return data