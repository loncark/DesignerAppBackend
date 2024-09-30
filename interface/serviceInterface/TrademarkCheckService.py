from abc import ABC, abstractmethod
from interface.repositoryInterface.TrademarkCheckRepository import TrademarkCheckRepository

class TrademarkCheckService(ABC):
    @abstractmethod
    def __init__(self, repository: TrademarkCheckRepository):
        self.repository = repository

    def getTrademarks(self):
        pass