from service.TrademarkService import TrademarkService
from flask import Blueprint, request

class TrademarkController:
    def __init__(self):
        self.service = TrademarkService()
        self.blueprint = Blueprint('trademarkBp', __name__)
        self.blueprint.route('/tess', methods=['POST'])(self.queryTESS)

    def queryTESS(self):
        data = request.get_json()
        prompt = data.get('prompt')
        return self.service.fetchAndFilterResponse(prompt)