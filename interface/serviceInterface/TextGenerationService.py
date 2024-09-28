from abc import ABC, abstractmethod

class TextGenerationService(ABC):
    @abstractmethod
    def __init__(self):
        pass
    
    def generateText(self):
        pass