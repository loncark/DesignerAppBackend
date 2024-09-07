from config import RAPIDAPI_ETSY_URL, RAPIDAPI_API_KEY

import requests, json

global_test = True

def fetchProducts(keyword, page, test=global_test):
    if test:
        if keyword == '':
            filePath = r"C:\Users\Kristina\Documents\Diplomski rad\DesignerAppBackend\sample JSONs\EtsyPage1.json"
        elif keyword == 'cat shirt':
            filePath = r"C:\Users\Kristina\Documents\Diplomski rad\DesignerAppBackend\sample JSONs\EtsyPage2.json"
        elif keyword == 'christmas':
            filePath = r"C:\Users\Kristina\Documents\Diplomski rad\DesignerAppBackend\sample JSONs\EtsyPage3.json"
        
        with open(filePath, 'r') as file:
            data = json.load(file)
        
        return data

    else:
        queryString = {"query": keyword, "page" : page}

        headers = {
            "x-rapidapi-key": RAPIDAPI_API_KEY,
            "x-rapidapi-host": "etsy-api2.p.rapidapi.com"
        }

        response = requests.get(RAPIDAPI_ETSY_URL, headers=headers, params=queryString)

        return response.json()
    


