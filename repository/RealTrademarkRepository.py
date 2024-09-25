from interface.Repository import Repository
import requests
import json
from urllib.parse import quote
from config import RAPIDAPI_API_KEY, TESS_BASE_URL

class RealTrademarkRepository(Repository):
    def fetchData(self, prompt):
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