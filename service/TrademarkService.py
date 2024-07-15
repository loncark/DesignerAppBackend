import requests
import sys, os
import json
from urllib.parse import quote
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import RAPIDAPI_API_KEY, TESS_BASE_URL

def fetchAndFilterResponse(prompt):
    return filterJson(fetchResponse(prompt))

def fetchResponse(prompt):
    headers = {
      "X-RapidAPI-Key": RAPIDAPI_API_KEY,
      "X-RapidAPI-Host": "uspto-trademark.p.rapidapi.com"
    }

    encoded_prompt = quote(prompt)
    url = TESS_BASE_URL + f"v1/trademarkSearch/{encoded_prompt}/active"

    response = requests.get(url, headers=headers)

    return response.json()


def filterJson(data):
  transformed_data = {}
  transformed_data["count"] = data["count"]
  transformed_data["items"] = []

  for item in data["items"]:
    new_item = {}
    new_item["description"] = item["description"]
    new_item["keyword"] = item["keyword"]
    new_item["owners"] = []

    for owner in item["owners"]:
      owner_data = {
          "address1": owner.get("address1"),
          "city": owner.get("city"),
          "country": owner.get("country"),
          "name": owner.get("name"),
      }
      new_item["owners"].append(owner_data)

    new_item["status_label"] = item["status_label"]
    transformed_data["items"].append(new_item)
    
  return transformed_data


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

	# Transform the data
	transformed_data = filterJson(original_data)

	# Print the transformed JSON (optional)
	print(json.dumps(transformed_data, indent=4))