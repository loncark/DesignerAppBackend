from abc import ABC, abstractmethod

class DatabaseController(ABC):
    @abstractmethod
    def __init__(self):
        pass

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