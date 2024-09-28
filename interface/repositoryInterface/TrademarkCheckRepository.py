from abc import ABC, abstractmethod

class TrademarkCheckRepository(ABC):
    @abstractmethod
    def __init__(self):
        pass

    def getTrademarks(self):
        pass