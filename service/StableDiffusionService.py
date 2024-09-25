from config import SD_TXT2IMG_URL, SD_IMG2IMG_URL
from repository.RealSDRepository import RealSDRepository
from repository.DummySDRepository import DummySDRepository

class StableDiffusionService:
  def __init__(self, global_test=True) -> None:
    if global_test:
      self.repository = DummySDRepository()
    else:
      self.repository = RealSDRepository()

  async def txt2img(self, payload):
    return await self.repository.fetchData(SD_TXT2IMG_URL, payload)

  async def img2img(self, payload):
    return await self.repository.fetchData(SD_IMG2IMG_URL, payload)