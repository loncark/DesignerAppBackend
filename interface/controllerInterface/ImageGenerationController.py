from abc import ABC, abstractmethod
from interface.serviceInterface.ImageGenerationService import ImageGenerationService

class ImageGenerationController(ABC):
    @abstractmethod
    def __init__(self, service: ImageGenerationService):
        self.service = service

    async def textToImage(self):
        pass

    async def imageToImage(self):
        pass