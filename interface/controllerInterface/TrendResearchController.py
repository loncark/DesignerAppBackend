from abc import ABC, abstractmethod
from interface.serviceInterface.TrendResearchService import TrendResearchService

class TrendResearchController(ABC):
    @abstractmethod
    def __init__(self, service: TrendResearchService):
        self.service = service

    def getTrends(self):
        pass

    def getRelatedQueries(self):
        pass

    def getInterestByRegion(self):
        pass

    def getInterestOverTime(self):
        pass
