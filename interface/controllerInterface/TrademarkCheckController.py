from abc import ABC, abstractmethod

class TrademarkCheckController(ABC):
    @abstractmethod
    def __init__(self):
        pass

    def getTrademarks(self):
        pass