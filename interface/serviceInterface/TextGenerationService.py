from abc import ABC, abstractmethod
from interface.repositoryInterface.TextGenerationRepository import TextGenerationRepository

class TextGenerationService(ABC):
    @abstractmethod
    def __init__(self, repository: TextGenerationRepository):
        self.repository = repository
    
    def generateText(self):
        pass