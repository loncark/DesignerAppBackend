from interface.repositoryInterface.TextGenerationRepository import TextGenerationRepository

class DummyGeminiRepository(TextGenerationRepository):
    def __init__(self):
        pass
    
    def generateText(self, prompt):
        return "Some dummy text for testing purposes."