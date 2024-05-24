import service.FirebaseService

def saveToRealtimeDb():
    return service.FirebaseService.storeToDb('')


def saveToStorage():
    return service.FirebaseService.storeToStorage()
