import service.FirebaseService
from flask import Blueprint

firebase_bp = Blueprint('firebase_bp', __name__)

@firebase_bp.route('/db')
def saveToRealtimeDb():
    return service.FirebaseService.storeToDb('')

@firebase_bp.route('/storage')
def saveToStorage():
    return service.FirebaseService.storeToStorage()
