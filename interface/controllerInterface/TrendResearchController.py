from abc import ABC, abstractmethod

class TrendResearchController(ABC):
    @abstractmethod
    def __init__(self):
        pass

    def getTrends(self):
        pass

    def getRelatedQueries(self):
        pass

    def getInterestByRegion(self):
        pass

    def getInterestOverTime(self):
        pass
