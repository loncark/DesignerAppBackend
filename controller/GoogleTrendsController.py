import service.GoogleTrendsService

from flask import Blueprint

gt_bp = Blueprint('gt_bp', __name__)

@gt_bp.route('/trends')
def queryGoogleTrends():
    return service.GoogleTrendsService.fetchResponse('')