from interface.repositoryInterface.TrademarkCheckRepository import TrademarkCheckRepository
import requests, json
from urllib.parse import quote
from constants import RAPIDAPI_API_KEY, TESS_BASE_URL

class RealTrademarkRepository(TrademarkCheckRepository):
    def __init__(self):
        pass
    
    def getTrademarks(self, prompt):
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