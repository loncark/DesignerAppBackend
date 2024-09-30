# START VPN ON US OR JAPAN SERVER BEFORE RUNNING LIVE

from interface.repositoryInterface.TextGenerationRepository import TextGenerationRepository
from interface.serviceInterface.TextGenerationService import TextGenerationService

class GeminiService(TextGenerationService):
    def __init__(self, repository: TextGenerationRepository):
        super().__init__(repository)

    def generateText(self, prompt):
        return self.repository.generateText(prompt)