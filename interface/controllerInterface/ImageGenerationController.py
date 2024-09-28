from abc import ABC, abstractmethod

class ImageGenerationController(ABC):
    @abstractmethod
    def __init__(self):
        pass

    async def textToImage(self):
        pass

    async def imageToImage(self):
        pass