import service.GeminiService
from flask import Blueprint, request

gemini_bp = Blueprint('gemini_bp', __name__)

@gemini_bp.route('/gemini', methods=['POST'])
def queryGemini():
    data = request.get_json()
    prompt = data.get('prompt')
    return service.GeminiService.fetchResponse(prompt)

@gemini_bp.route('/gemini/tags', methods=['POST'])
def generateTags():
    data = request.get_json()
    prompt = data.get('prompt')
    return service.GeminiService.generateTags(prompt)

@gemini_bp.route('/gemini/title', methods=['POST'])
def generateTitle():
    data = request.get_json()
    prompt = data.get('prompt')
    return service.GeminiService.generateTitle(prompt)