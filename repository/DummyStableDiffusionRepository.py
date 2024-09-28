from interface.repositoryInterface.ImageGenerationRepository import ImageGenerationRepository
import json

class DummyStableDiffusionRepository(ImageGenerationRepository):
    def __init__(self):
        pass
    
    async def generateImage(self, url, payload):
        filePath = r"C:\Users\Kristina\Documents\Diplomski rad\DesignerAppBackend\sample JSONs\SdResponse.json"

        with open(filePath, 'r') as file:
            data = json.load(file)
            
        return data