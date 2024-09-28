from abc import ABC, abstractmethod

class DatabaseRepository(ABC):
    @abstractmethod
    def __init__(self):
        pass

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
