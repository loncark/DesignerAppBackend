from abc import ABC, abstractmethod

class Repository(ABC):
    @abstractmethod
    def fetchData(self):
        pass
