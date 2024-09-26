# START VPN ON US OR JAPAN SERVER BEFORE RUNNING LIVE

from repository.DummyGeminiRepository import DummyGeminiRepository
from repository.RealGeminiRepository import RealGeminiRepository

class GeminiService:
    def __init__(self, global_test=False):      
        if global_test:
            self.repository = DummyGeminiRepository()
        else:
            self.repository = RealGeminiRepository()

    def fetchResponse(self, prompt):
        return self.repository.fetchData(prompt)