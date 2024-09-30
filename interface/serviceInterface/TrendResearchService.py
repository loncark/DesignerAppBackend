from abc import ABC, abstractmethod
from interface.repositoryInterface.TrendResearchRepository import TrendResearchRepository

class TrendResearchService(ABC):
    @abstractmethod
    def __init__(self, repository: TrendResearchRepository):
        self.repository = repository

    def getTrends(self):
        pass

    def getRelatedQueries(self):
        pass

    def getInterestByRegion(self):
        pass

    def getInterestOverTime(self):
        pass
