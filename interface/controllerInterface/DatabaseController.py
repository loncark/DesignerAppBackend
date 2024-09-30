from abc import ABC, abstractmethod
from interface.serviceInterface.DatabaseService import DatabaseService

class DatabaseController(ABC):
    @abstractmethod
    def __init__(self, service: DatabaseService):
        self.service = service

    def saveDesignToDb(self):
        pass

    def deleteDesignFromDb(self):
        pass

    def getAllDesigns(self):
        pass

    def saveImageToStorage(self):
        pass

    def deleteImageFromStorage(self):
        pass

    def downloadDesign(self):
        pass