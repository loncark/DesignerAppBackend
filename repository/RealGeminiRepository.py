from interface.Repository import Repository
import google.generativeai as genai
from constants import GEMINI_API_KEY

class RealGeminiRepository(Repository):
    def __init__(self):
        genai.configure(api_key=GEMINI_API_KEY) 
        self.model = genai.GenerativeModel('gemini-pro')

    def fetchResponse(self, prompt):
        response = self.model.generate_content(prompt)

        return response.text