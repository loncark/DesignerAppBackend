from abc import ABC, abstractmethod

class ProductResearchRepository(ABC):
    @abstractmethod
    def __init__(self):
        pass

    def getProducts(self):
        pass