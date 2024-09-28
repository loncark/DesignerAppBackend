from interface.repositoryInterface.TextGenerationRepository import TextGenerationRepository
import google.generativeai as genai
from constants import GEMINI_API_KEY

class RealGeminiRepository(TextGenerationRepository):
    def __init__(self):
        genai.configure(api_key=GEMINI_API_KEY) 
        self.model = genai.GenerativeModel('gemini-pro')

    def generateText(self, prompt):
        response = self.model.generate_content(prompt)

        return response.text