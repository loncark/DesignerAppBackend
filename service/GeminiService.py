# START VPN ON US OR JAPAN SERVER BEFORE RUNNING LIVE

from interface.Repository import Repository

class GeminiService:
    def __init__(self, repository: Repository):
        self.repository = repository

    def fetchResponse(self, prompt):
        return self.repository.fetchResponse(prompt)