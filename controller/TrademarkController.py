import service.TrademarkService

from flask import Blueprint, request

trademark_bp = Blueprint('trademark_bp', __name__)

@trademark_bp.route('/tess', methods=['POST'])
def queryTESS():
    return service.TrademarkService.fetchAndFilterResponse()