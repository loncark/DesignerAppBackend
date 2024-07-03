from config import SERPAPI_ETSY_URL, TESS_API_KEY

import requests

def fetchProducts(keyword, page):

    querystring = {"query": keyword, "page" : page}

    headers = {
        "x-rapidapi-key": TESS_API_KEY,
        "x-rapidapi-host": "etsy-api2.p.rapidapi.com"
    }

    response = requests.get(SERPAPI_ETSY_URL, headers=headers, params=querystring)

    return response.json()


