from config import RAPIDAPI_ETSY_URL, RAPIDAPI_API_KEY

import requests

def fetchProducts(keyword, page):

    querystring = {"query": keyword, "page" : page}

    headers = {
        "x-rapidapi-key": RAPIDAPI_API_KEY,
        "x-rapidapi-host": "etsy-api2.p.rapidapi.com"
    }

    response = requests.get(RAPIDAPI_ETSY_URL, headers=headers, params=querystring)

    return response.json()


