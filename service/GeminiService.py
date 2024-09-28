# START VPN ON US OR JAPAN SERVER BEFORE RUNNING LIVE

from interface.repositoryInterface.TextGenerationRepository import TextGenerationRepository

class GeminiService:
    def __init__(self, repository: TextGenerationRepository):
        self.repository = repository

    def generateText(self, prompt):
        return self.repository.generateText(prompt)