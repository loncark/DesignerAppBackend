import service.EtsyService
from flask import Blueprint, request

etsy_bp = Blueprint('etsy_bp', __name__)

@etsy_bp.route('/etsy', methods=['POST'])
def queryEtsy():
    data = request.get_json()
    keyword = data.get('keyword')
    return service.EtsyService.fetchProducts(keyword)