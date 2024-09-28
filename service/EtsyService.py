from interface.repositoryInterface.ProductResearchRepository import ProductResearchRepository

class EtsyService:
    def __init__(self, repository: ProductResearchRepository):
        self.repository = repository

    def getProducts(self, keyword, page):
        return self.repository.getProducts(keyword, page)
