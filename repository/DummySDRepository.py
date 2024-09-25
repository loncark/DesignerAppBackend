from interface.Repository import Repository
import json

class DummySDRepository(Repository):
    async def fetchData(self, url, payload):
        filePath = r"C:\Users\Kristina\Documents\Diplomski rad\DesignerAppBackend\sample JSONs\SdResponse.json"

        with open(filePath, 'r') as file:
            data = json.load(file)
            
        return data