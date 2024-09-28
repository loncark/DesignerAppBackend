from interface.controllerInterface.TrademarkCheckController import TrademarkCheckController
from interface.Service import Service
from flask import Blueprint, request

class TrademarkController(TrademarkCheckController):
    def __init__(self, service: Service):
        self.service = service
        self.blueprint = Blueprint('trademarkBp', __name__)
        self.blueprint.route('/tess', methods=['POST'])(self.getTrademarks)

    def getTrademarks(self):
        data = request.get_json()
        prompt = data.get('prompt')
        return self.service.fetchAndFilterResponse(prompt)