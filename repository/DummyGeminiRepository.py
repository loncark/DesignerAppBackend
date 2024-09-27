from interface.Repository import Repository

class DummyGeminiRepository(Repository):
    def fetchResponse(self, prompt):
        return "Some dummy text for testing purposes."