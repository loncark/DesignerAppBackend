from interface.repositoryInterface.ProductResearchRepository import ProductResearchRepository
from interface.serviceInterface.ProductResearchService import ProductResearchService

class EtsyService(ProductResearchService):
    def __init__(self, repository: ProductResearchRepository):
        super().__init__(repository)

    def getProducts(self, keyword, page):
        return self.repository.getProducts(keyword, page)
