from abc import ABC, abstractmethod
from interface.serviceInterface.TrademarkCheckService import TrademarkCheckService

class TrademarkCheckController(ABC):
    @abstractmethod
    def __init__(self, service: TrademarkCheckService):
        self.service = service

    def getTrademarks(self):
        pass