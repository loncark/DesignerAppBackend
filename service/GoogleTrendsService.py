from interface.repositoryInterface.TrendResearchRepository import TrendResearchRepository
from datetime import datetime
from flask import jsonify

class GoogleTrendsService:
    def __init__(self, repository: TrendResearchRepository):
        self.repository = repository

    def getTrends(self, date, country_code):
        return self.repository.getTrends(date, country_code)
            
    def getRelatedQueries(self, keyword):
        return self.repository.getRelatedQueries(keyword)
            
    def getInterestByRegion(self, keyword):
        return self.repository.getInterestByRegion(keyword)
            
    def getInterestOverTime(self, keyword):
        data = self.repository.getInterestOverTime(keyword)     
        processed_data = self.extractDatesAndValues(data)

        return jsonify({'data': processed_data})

    def extractDatesAndValues(self, data):
        timeline_data = data['interest_over_time']['timeline_data']
            
        processed_data = []
        for item in timeline_data:
            date = datetime.fromtimestamp(int(item['timestamp']))
            value = item['values'][0]['extracted_value']
            processed_data.append({
                'date': date.strftime('%Y-%m-%d'),
                'value': value
            })

        return processed_data
