import serpapi
from config import SERPAPI_API_KEY

# change frequency to realtime for realtime searches,
# delete the date field and add "cat": "all",

def fetchTrends(date, country_code):
  params = {
        "engine": "google_trends_trending_now",
        "frequency": "daily",
        "geo": {country_code}, # "US",
        "date": {date}, # "20240505",
        "api_key": SERPAPI_API_KEY
      }

  search = serpapi.search(params)
  results = search.as_dict()

  return results

def fetchRelatedQueries(keyword):
  params = {
  "engine": "google_trends",
  "q": {keyword},
  "data_type": "RELATED_QUERIES",
  "api_key": SERPAPI_API_KEY
}

  search = serpapi.search(params)
  results = search.as_dict()
  
  return results

def fetchInterestByRegion(keyword):
  params = {
  "engine": "google_trends",
  "q": {keyword},
  "data_type": "GEO_MAP_0",
  "api_key": SERPAPI_API_KEY
}

  search = serpapi.search(params)
  results = search.as_dict()
  
  return results