import serpapi, json
from config import SERPAPI_API_KEY

# change frequency to realtime for realtime searches,
# delete the date field and add "cat": "all",

def fetchTrends(date, country_code):
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
    except serpapi.SerpApiClientException as e:
        if e.status_code == 429:
            error_response = {
                "message": "API limit of 100 searches per month exceeded."
            }
            return json.dumps(error_response), 429
        else:
            raise

def fetchRelatedQueries(keyword):
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
    except serpapi.SerpApiClientException as e:
        if e.status_code == 429:
            error_response = {
                "message": "API limit of 100 searches per month exceeded."
            }
            return json.dumps(error_response), 429
        else:
            raise

def fetchInterestByRegion(keyword):
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
    except serpapi.SerpApiClientException as e:
        if e.status_code == 429:
            error_response = {
                "message": "API limit of 100 searches per month exceeded."
            }
            return json.dumps(error_response), 429
        else:
            raise