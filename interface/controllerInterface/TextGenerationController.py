from abc import ABC, abstractmethod

class TextGenerationController(ABC):
    @abstractmethod
    def __init__(self):
        pass

    def generateText(self):
        pass