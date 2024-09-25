from interface.Repository import Repository

class RealGeminiRepository(Repository):
    def fetchData(self, model, prompt):
        response = model.generate_content(prompt)

        return response.text