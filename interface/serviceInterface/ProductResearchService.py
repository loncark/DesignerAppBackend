from abc import ABC, abstractmethod
from interface.repositoryInterface.ProductResearchRepository import ProductResearchRepository

class ProductResearchService(ABC):
    @abstractmethod
    def __init__(self, repository: ProductResearchRepository):
        self.repository = repository

    def getProducts(self):
        pass