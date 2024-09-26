from interface.Service import Service
from flask import Blueprint, request

class TrademarkController:
    def __init__(self, service: Service):
        self.service = service
        self.blueprint = Blueprint('trademarkBp', __name__)
        self.blueprint.route('/tess', methods=['POST'])(self.queryTESS)

    def queryTESS(self):
        data = request.get_json()
        prompt = data.get('prompt')
        return self.service.fetchAndFilterResponse(prompt)