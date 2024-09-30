from interface.controllerInterface.TrademarkCheckController import TrademarkCheckController
from interface.serviceInterface.TrademarkCheckService import TrademarkCheckService
from flask import Blueprint, request

class USTrademarkController(TrademarkCheckController):
    def __init__(self, service: TrademarkCheckService):
        super().__init__(service)
        self.blueprint = Blueprint('trademarkBp', __name__)
        self.blueprint.route('/tess', methods=['POST'])(self.getTrademarks)

    def getTrademarks(self):
        data = request.get_json()
        prompt = data.get('prompt')
        return self.service.getTrademarks(prompt)