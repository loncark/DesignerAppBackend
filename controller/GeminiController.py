from service.GeminiService import GeminiService
from flask import Blueprint, request

class GeminiController:
    def __init__(self):
        self.service = GeminiService()
        self.blueprint = Blueprint('geminiBp', __name__)
        self.blueprint.route('/gemini', methods=['POST'])(self.queryGemini)

    def queryGemini(self):
        data = request.get_json()
        prompt = data.get('prompt')
        return self.service.fetchResponse(prompt)