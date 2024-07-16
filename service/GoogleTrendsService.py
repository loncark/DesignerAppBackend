import serpapi, json, os
from config import SERPAPI_API_KEY

# change frequency to realtime for realtime searches,
# delete the date field and add "cat": "all",

def fetchTrends2(date, country_code):
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

def fetchRelatedQueries2(keyword):
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

def fetchInterestByRegion2(keyword):
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

# TEST FUNCTIONS TO NOT DRAIN THE API LIMIT (45/mo for etsy, a lot for trademark, 100/mo for Trends, interest and related together)
def fetchTrends(keyword, page):
    file_path = r"C:\Users\Kristina\Documents\Diplomski rad\DesignerAppBackend\sample JSONs\TrendPage1.json"
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    return data

def fetchRelatedQueries(keyword):
    file_path = r"C:\Users\Kristina\Documents\Diplomski rad\DesignerAppBackend\sample JSONs\KeywordsRelated.json"
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    return data

def fetchInterestByRegion(keyword):
    file_path = r"C:\Users\Kristina\Documents\Diplomski rad\DesignerAppBackend\sample JSONs\KeywordsInterest.json"
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    return data