from interface.Repository import Repository

class DummyGeminiRepository(Repository):
    def fetchData(self, model, prompt):
        return "Some dummy text for testing purposes"