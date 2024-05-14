# START VPN ON US OR JAPAN SERVER BEFORE RUNNING

import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel('gemini-pro')
response = model.generate_content('Tell me what cats are in one sentence.')

print(response.text)
