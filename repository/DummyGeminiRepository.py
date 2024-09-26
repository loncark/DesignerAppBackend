from interface.Repository import Repository

class DummyGeminiRepository(Repository):
    def fetchData(self, prompt):
        return "Some dummy text for testing purposes."