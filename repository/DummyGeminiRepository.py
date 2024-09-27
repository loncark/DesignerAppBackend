from interface.Repository import Repository

class DummyGeminiRepository(Repository):
    def __init__(self):
        pass
    
    def fetchResponse(self, prompt):
        return "Some dummy text for testing purposes."