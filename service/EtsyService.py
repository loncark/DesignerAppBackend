from config import RAPIDAPI_ETSY_URL, RAPIDAPI_API_KEY

import requests, os, json

def fetchProducts(keyword, page):

    querystring = {"query": keyword, "page" : page}

    headers = {
        "x-rapidapi-key": RAPIDAPI_API_KEY,
        "x-rapidapi-host": "etsy-api2.p.rapidapi.com"
    }

    response = requests.get(RAPIDAPI_ETSY_URL, headers=headers, params=querystring)

    return response.json()

def fetchProducts2(keyword, page):
    file_path = r"C:\Users\Kristina\Documents\Diplomski rad\DesignerAppBackend\sample JSONs\EtsyPage1.json"
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    return data


