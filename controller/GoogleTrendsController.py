from interface.Service import Service
from flask import Blueprint, request

class GoogleTrendsController:
    def __init__(self, service: Service):
        self.service = service
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
        return self.service.fetchTrends(date, country_code)

    def getRelatedQueries(self):
        data = request.get_json()
        keyword = data.get('keyword')
        return self.service.fetchRelatedQueries(keyword)

    def getInterestByRegion(self):
        data = request.get_json()
        keyword = data.get('keyword')
        return self.service.fetchInterestByRegion(keyword)

    def getInterestOverTime(self):
        data = request.get_json()
        keyword = data.get('keyword')
        return self.service.fetchInterestOverTime(keyword)