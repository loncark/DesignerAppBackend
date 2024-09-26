from interface.Repository import Repository
import google.generativeai as genai
from config import GEMINI_API_KEY

class RealGeminiRepository(Repository):
    def __init__(self):
        genai.configure(api_key=GEMINI_API_KEY) 
        self.model = genai.GenerativeModel('gemini-pro')

    def fetchData(self, prompt):
        response = self.model.generate_content(prompt)

        return response.text