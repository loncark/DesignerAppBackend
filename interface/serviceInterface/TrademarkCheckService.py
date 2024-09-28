from abc import ABC, abstractmethod

class TrademarkCheckService(ABC):
    @abstractmethod
    def __init__(self):
        pass

    def getTrademarks(self):
        pass