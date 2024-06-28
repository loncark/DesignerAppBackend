import service.GoogleTrendsService

from flask import Blueprint, request

gt_bp = Blueprint('gt_bp', __name__)

@gt_bp.route('/trends', methods=['POST'])
def queryGoogleTrends():
    data = request.get_json()
    country_code = data.get('country_code')
    date = data.get('date')
    return service.GoogleTrendsService.fetchTrends(date, country_code)

@gt_bp.route('/relatedQueries', methods=['POST'])
def queryRelatedQueries():
    data = request.get_json()
    keyword = data.get('keyword')
    return service.GoogleTrendsService.fetchRelatedQueries(keyword)