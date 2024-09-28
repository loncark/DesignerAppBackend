from abc import ABC, abstractmethod

class TextGenerationRepository(ABC):
    @abstractmethod
    def __init__(self):
        pass
    
    def generateText(self):
        pass