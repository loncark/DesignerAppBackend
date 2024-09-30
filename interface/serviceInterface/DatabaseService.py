from abc import ABC, abstractmethod
from interface.repositoryInterface.DatabaseRepository import DatabaseRepository

class DatabaseService(ABC):
    @abstractmethod
    def __init__(self, repository: DatabaseRepository):
        self.repository = repository

    def getAllDesigns(self):
        pass

    def saveDesign(self):
        pass

    def deleteDesign(self):
        pass

    def saveImage(self):
        pass

    def deleteImageByUrl(self):
        pass

    def createDesignZip(self):
        pass