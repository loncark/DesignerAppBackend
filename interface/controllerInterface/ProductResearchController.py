from abc import ABC, abstractmethod

class ProductResearchController(ABC):
    @abstractmethod
    def __init__(self):
        pass

    def getProducts(self):
        pass