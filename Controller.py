from flask import jsonify
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

def SDtextToImage():
    return service.StableDiffusionService.fetch_and_save_image('')

def saveToStorage():
    return service.FirebaseService.storeToStorage()

def queryTESS():
    return service.TrademarkService.fetchResponse()