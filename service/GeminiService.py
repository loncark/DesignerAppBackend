# START VPN ON US OR JAPAN SERVER BEFORE RUNNING LIVE

import google.generativeai as genai
from config import GEMINI_API_KEY
from repository.DummyGeminiRepository import DummyGeminiRepository
from repository.RealGeminiRepository import RealGeminiRepository

class GeminiService:
    def __init__(self, global_test=False):
        genai.configure(api_key=GEMINI_API_KEY) 
        self.model = genai.GenerativeModel('gemini-pro')
        
        if global_test:
            self.repository = DummyGeminiRepository()
        else:
            self.repository = RealGeminiRepository()

    def fetchResponse(self, prompt):
        return self.repository.fetchData(self.model, prompt)