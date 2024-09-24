from config import RAPIDAPI_ETSY_URL, RAPIDAPI_API_KEY
import requests, json

class EtsyService:
    def __init__(self, global_test=True) -> None:
        self.global_test = global_test

    def fetchProducts(self, keyword, page):
        if self.global_test:
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

            try:
                response = requests.get(RAPIDAPI_ETSY_URL, headers=headers, params=queryString)
            
            except Exception as e:
                print(e)
                return json.dumps({"Exception": e})

            return response.json()
    


