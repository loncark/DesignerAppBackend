from abc import ABC, abstractmethod
from interface.serviceInterface.ProductResearchService import ProductResearchService

class ProductResearchController(ABC):
    @abstractmethod
    def __init__(self, service: ProductResearchService):
        self.service = service

    def getProducts(self):
        pass