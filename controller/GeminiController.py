from interface.controllerInterface.TextGenerationController import TextGenerationController
from interface.Service import Service
from flask import Blueprint, request

class GeminiController(TextGenerationController):
    def __init__(self, service: Service):
        self.service = service
        self.blueprint = Blueprint('geminiBp', __name__)
        self.blueprint.route('/gemini', methods=['POST'])(self.generateText)

    def generateText(self):
        data = request.get_json()
        prompt = data.get('prompt')
        return self.service.fetchResponse(prompt)