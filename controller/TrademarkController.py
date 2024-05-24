import service.TrademarkService

from flask import Blueprint

trademark_bp = Blueprint('trademark_bp', __name__)

@trademark_bp.route('/tess')
def queryTESS():
    return service.TrademarkService.fetchAndFilterResponse()