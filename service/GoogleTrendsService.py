import serpapi
from config import SERPAPI_API_KEY

# change frequency to realtime for realtime searches,
# delete the date field and add "cat": "all",

def fetchResponse(params):
  params = {
        "engine": "google_trends_trending_now",
        "frequency": "daily",
        "geo": "US",
        "date": "20240505",
        "api_key": SERPAPI_API_KEY
      }

  search = serpapi.search(params)
  results = search.as_dict()

  return results