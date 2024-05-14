import requests
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import TESS_API_KEY

url = "https://uspto-trademark.p.rapidapi.com/v1/trademarkSearch/just%20do%20it/active"

headers = {
	"X-RapidAPI-Key": TESS_API_KEY,
	"X-RapidAPI-Host": "uspto-trademark.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())