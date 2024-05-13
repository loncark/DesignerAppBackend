# START VPN ON US SERVER BEFORE RUNNING

import google.generativeai as genai
from config import API_KEY

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel('gemini-pro')
response = model.generate_content('Tell me what cats are in one sentence.')

print(response.text)
