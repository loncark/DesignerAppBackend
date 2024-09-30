from abc import ABC, abstractmethod
from interface.serviceInterface.TextGenerationService import TextGenerationService

class TextGenerationController(ABC):
    @abstractmethod
    def __init__(self, service: TextGenerationService):
        self.service = service

    def generateText(self):
        pass