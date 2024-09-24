from repository.DummyEtsyRepository import DummyEtsyRepository
from repository.RealEtsyRepository import RealEtsyRepository

class EtsyService:
    def __init__(self, global_test=True):
        if global_test:
            self.repository = DummyEtsyRepository()
        else:
            self.repository = RealEtsyRepository()

    def fetchProducts(self, keyword, page):
        return self.repository.fetchData(keyword, page)
