from datetime import datetime
from flask import jsonify

from repository.RealGoogleTrendsRepository import RealGoogleTrendsRepository
from repository.DummyGoogleTrendsRepository import DummyGoogleTrendsRepository

# LEAVE global_test=True TO NOT DRAIN THE API LIMIT (45/mo for etsy, a lot for trademark, 100/mo for Trends, interest and related together)

class GoogleTrendsService:
    def __init__(self, global_test=True):
        if global_test:
            self.repository = DummyGoogleTrendsRepository()
        else:
            self.repository = RealGoogleTrendsRepository()

    def fetchTrends(self, date, country_code):
        return self.repository.fetchData(date, country_code)
            
    def fetchRelatedQueries(self, keyword):
        return self.repository.fetchRelatedQueries(keyword)
            
    def fetchInterestByRegion(self, keyword):
        return self.repository.fetchInterestByRegion(keyword)
            
    def fetchInterestOverTime(self, keyword):
        data = self.repository.fetchInterestOverTime(keyword)     
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
