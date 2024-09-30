from abc import ABC, abstractmethod
from interface.repositoryInterface.ImageGenerationRepository import ImageGenerationRepository

class ImageGenerationService(ABC):
    @abstractmethod
    def __init__(self, repository: ImageGenerationRepository):
        self.repository = repository

    async def textToImage(self):
        pass

    async def imageToImage(self):
        pass