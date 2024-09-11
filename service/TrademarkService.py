import requests
import json
from urllib.parse import quote
from config import RAPIDAPI_API_KEY, TESS_BASE_URL

def fetchAndFilterResponse(prompt):
    return filterJson(fetchTrademarks(prompt))

def fetchTrademarks(prompt):
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


def filterJson(data):
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


def testFilterJson():
	original_data = json.loads("""{ 
    "count": 27,
    "items": [
      {
        "abandonment_date": null,
        "description": "Hair accessories, namely, hair ties, hair bands, ponytail holders",
        "expiration_date": "2026-10-27",
        "filing_date": "2020-04-17",
        "keyword": "JUST DO IT",
        "owners": [
          {
            "address1": "1 Bowerman Dr.",
            "address2": null,
            "city": "Beaverton",
            "country": "US",
            "index": 1,
            "legal_entity_type": "03",
            "legal_entity_type_label": "Corporation",
            "name": "Nike, Inc.",
            "owner_label": "Original Registrant",
            "owner_type": "30",
            "postcode": "97005",
            "state": "OR"
          }
        ],
        "registration_date": "2020-10-27",
        "registration_number": "6185209",
        "serial_number": "88876918",
        "status_code": "700",
        "status_date": "2020-10-27",
        "status_definition": "REGISTERED",
        "status_label": "Live/Registered"
      },
      {
        "abandonment_date": null,
        "description": "Retail store services and on-line retail store services featuring apparel, apparel accessories, footwear, footwear accessories, headwear, eyewear and accessories, sporting goods and equipment, bags, sports bags, sports and fitness products and accessories",
        "expiration_date": "2025-04-16",
        "filing_date": "2018-10-26",
        "keyword": "JUST DO IT",
        "owners": [
          {
            "address1": "One Bowerman Drive",
            "address2": null,
            "city": "Beaverton",
            "country": "US",
            "index": 1,
            "legal_entity_type": "03",
            "legal_entity_type_label": "Corporation",
            "name": "Nike, Inc.",
            "owner_label": "Original Registrant",
            "owner_type": "30",
            "postcode": "97005",
            "state": "OR"
          }
        ],
        "registration_date": "2019-04-16",
        "registration_number": "5727940",
        "serial_number": "88170627",
        "status_code": "700",
        "status_date": "2019-04-16",
        "status_definition": "REGISTERED",
        "status_label": "Live/Registered"
      },
      {
        "abandonment_date": null,
        "description": "Bottles, sold empty",
        "expiration_date": "2022-02-16",
        "filing_date": "2015-09-21",
        "keyword": "JUST DO IT",
        "owners": [
          {
            "address1": null,
            "address2": "One Bowerman Drive",
            "city": "Beaverton",
            "country": "US",
            "index": 1,
            "legal_entity_type": "03",
            "legal_entity_type_label": "Corporation",
            "name": "Nike, Inc.",
            "owner_label": "Original Registrant",
            "owner_type": "30",
            "postcode": "97005",
            "state": "OR"
          }
        ],
        "registration_date": "2016-02-16",
        "registration_number": "4902036",
        "serial_number": "86762618",
        "status_code": "700",
        "status_date": "2016-02-16",
        "status_definition": "REGISTERED",
        "status_label": "Live/Registered"
      }]
}
      """)

	transformedData = filterJson(original_data)
	print(json.dumps(transformedData, indent=4))