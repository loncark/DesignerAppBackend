from abc import ABC, abstractmethod

class ProductResearchService(ABC):
    @abstractmethod
    def __init__(self):
        pass

    def getProducts(self):
        pass