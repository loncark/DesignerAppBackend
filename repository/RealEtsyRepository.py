from interface.repositoryInterface.ProductResearchRepository import ProductResearchRepository
from constants import RAPIDAPI_ETSY_URL, RAPIDAPI_API_KEY
import requests, json

class RealEtsyRepository(ProductResearchRepository):
    def __init__(self):
        pass
    
    def getProducts(self, keyword, page):
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