# START VPN ON US OR JAPAN SERVER BEFORE RUNNING

import google.generativeai as genai
from config import GEMINI_API_KEY

class GeminiService:
    def __init__(self):
        genai.configure(api_key=GEMINI_API_KEY) 
        self.model = genai.GenerativeModel('gemini-pro')

    def fetchResponse(self, prompt):
        
        response = self.model.generate_content(prompt)

        return response.text