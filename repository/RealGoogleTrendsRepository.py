from interface.Repository import Repository
import serpapi, json
from datetime import datetime, timedelta
from flask import jsonify
from constants import SERPAPI_API_KEY

class RealGoogleTrendsRepository(Repository):
    def fetchTrends(self, date, country_code):
        params = {
                "engine": "google_trends_trending_now",
                "frequency": "daily",
                "geo": country_code,
                "date": date,
                "api_key": SERPAPI_API_KEY
            }
            
        try:
            search = serpapi.search(params)
            results = search.as_dict()
            return results
        except Exception as e:
            if e.status_code == 429:
                return json.dumps({"message": "API limit of 100 searches per month exceeded."}), 429
            else:
                print(e)
                return json.dumps({"Exception": e})
            
    def fetchRelatedQueries(self, keyword):
        params = {
                "engine": "google_trends",
                "q": keyword,
                "data_type": "RELATED_QUERIES",
                "api_key": SERPAPI_API_KEY
            }
            
        try:
            search = serpapi.search(params)
            results = search.as_dict()
            return results
        except Exception as e:
            if e.status_code == 429:
                return json.dumps({"message": "API limit of 100 searches per month exceeded."}), 429
            else:
                print(e)
                return json.dumps({"Exception": e})
            
    def fetchInterestByRegion(self, keyword):
        params = {
                "engine": "google_trends",
                "q": keyword,
                "data_type": "GEO_MAP_0",
                "api_key": SERPAPI_API_KEY
            }
            
        try:
            search = serpapi.search(params)
            results = search.as_dict()
            return results
        except Exception as e:
            if e.status_code == 429:
                return json.dumps({"message": "API limit of 100 searches per month exceeded."}), 429
            else:
                print(e)
                return json.dumps({"Exception": e})
            
    def fetchInterestOverTime(self, keyword):
        if not keyword:
            return jsonify({'error': 'Keyword is required'}), 400
                
        endDate = datetime.now().strftime('%Y-%m-%d')
        startDate = (datetime.now() - timedelta(days=5*365)).strftime('%Y-%m-%d')

        params = {
            "engine": "google_trends",
            "q": keyword,
            "data_type": "TIMESERIES",
            "api_key": SERPAPI_API_KEY,
            "date": f"{startDate} {endDate}"
        }
        try:
            search = serpapi.search(params)
            data = search.as_dict()
            return data
        except Exception as e:
            print(e)
            return json.dumps({"Exception": e})
        