import service.GeminiService
import service.GoogleTrendsService
import service.FirebaseService
import service.StableDiffusionService
import service.TrademarkService

def queryGemini():
    return service.GeminiService.fetchResponse('')

def queryGoogleTrends():
    return service.GoogleTrendsService.fetchResponse('')

def saveToRealtimeDb():
    return service.FirebaseService.storeToDb('')

async def SDtextToImage():
    return await service.StableDiffusionService.fetch_and_save_image('')

def saveToStorage():
    return service.FirebaseService.storeToStorage()

def queryTESS():
    return service.TrademarkService.fetchAndFilterResponse()