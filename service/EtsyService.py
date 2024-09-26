from interface.Repository import Repository

class EtsyService:
    def __init__(self, repository: Repository):
        self.repository = repository

    def fetchProducts(self, keyword, page):
        return self.repository.fetchData(keyword, page)
