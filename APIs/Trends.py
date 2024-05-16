import serpapi
from config import SERPAPI_API_KEY

params = {
  "engine": "google_trends_trending_now",
  "frequency": "realtime",
  "geo": "US",
  "cat": "all",
  "api_key": SERPAPI_API_KEY
}

search = serpapi.search(params)
results = search.as_dict()
realtime_searches = results["realtime_searches"]

print(results)