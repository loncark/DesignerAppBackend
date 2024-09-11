import service.GeminiService
from flask import Blueprint, request

gemini_bp = Blueprint('gemini_bp', __name__)

@gemini_bp.route('/gemini', methods=['POST'])
def queryGemini():
    data = request.get_json()
    prompt = data.get('prompt')
    return service.GeminiService.fetchResponse(prompt)