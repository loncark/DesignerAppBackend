from abc import ABC, abstractmethod

class ImageGenerationRepository(ABC):
    @abstractmethod
    def __init__(self):
        pass

    async def generateImage(self):
        pass
