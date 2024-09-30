from abc import ABC, abstractmethod
from interface.serviceInterface.DatabaseService import DatabaseService

class DatabaseController(ABC):
    @abstractmethod
    def __init__(self, service: DatabaseService):
        self.service = service

    def saveDesign(self):
        pass

    def deleteDesign(self):
        pass

    def getAllDesigns(self):
        pass

    def saveImage(self):
        pass

    def deleteImageByUrl(self):
        pass

    def createDesignZip(self):
        pass