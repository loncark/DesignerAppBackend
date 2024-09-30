from interface.serviceInterface.TrendResearchService import TrendResearchService
from interface.controllerInterface.TrendResearchController import TrendResearchController
from flask import Blueprint, request

class GoogleTrendsController(TrendResearchController):
    def __init__(self, service: TrendResearchService):
        super().__init__(service)
        self.blueprint = Blueprint('gtBp', __name__)
        self.registerRoutes()

    def registerRoutes(self):
        self.blueprint.route('/trends', methods=['POST'])(self.getTrends)
        self.blueprint.route('/relatedQueries', methods=['POST'])(self.getRelatedQueries)
        self.blueprint.route('/interestByRegion', methods=['POST'])(self.getInterestByRegion)
        self.blueprint.route('/chart', methods=['POST'])(self.getInterestOverTime)

    def getTrends(self):
        data = request.get_json()
        country_code = data.get('country_code')
        date = data.get('date')
        return self.service.getTrends(date, country_code)

    def getRelatedQueries(self):
        data = request.get_json()
        keyword = data.get('keyword')
        return self.service.getRelatedQueries(keyword)

    def getInterestByRegion(self):
        data = request.get_json()
        keyword = data.get('keyword')
        return self.service.getInterestByRegion(keyword)

    def getInterestOverTime(self):
        data = request.get_json()
        keyword = data.get('keyword')
        return self.service.getInterestOverTime(keyword)