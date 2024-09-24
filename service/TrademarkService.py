import requests
import json
from urllib.parse import quote
from config import RAPIDAPI_API_KEY, TESS_BASE_URL

class TrademarkService:
  def fetchAndFilterResponse(self, prompt):
      return self.filterJson(self.fetchTrademarks(prompt))

  def fetchTrademarks(self, prompt):
      headers = {
        "X-RapidAPI-Key": RAPIDAPI_API_KEY,
        "X-RapidAPI-Host": "uspto-trademark.p.rapidapi.com"
      }

      encodedPrompt = quote(prompt)
      url = TESS_BASE_URL + f"v1/trademarkSearch/{encodedPrompt}/active"

      try:
        response = requests.get(url, headers=headers)

      except Exception as e:
        print(e)
        return json.dumps({"Exception": e})
      
      return response.json()

  def filterJson(self, data):
    transformedData = {}
    transformedData["count"] = data["count"]
    transformedData["items"] = []

    for item in data["items"]:
      newItem = {}
      newItem["description"] = item["description"]
      newItem["keyword"] = item["keyword"]
      newItem["owners"] = []

      for owner in item["owners"]:
        ownerData = {
            "address1": owner.get("address1"),
            "city": owner.get("city"),
            "country": owner.get("country"),
            "name": owner.get("name"),
        }
        newItem["owners"].append(ownerData)

      newItem["status_label"] = item["status_label"]
      transformedData["items"].append(newItem)
      
    return transformedData