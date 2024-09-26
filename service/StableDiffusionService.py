from constants import SD_TXT2IMG_URL, SD_IMG2IMG_URL
from repository.RealStableDiffusionRepository import RealStableDiffusionRepository
from repository.DummyStableDiffusionRepository import DummyStableDiffusionRepository

class StableDiffusionService:
  def __init__(self, global_test=True) -> None:
    if global_test:
      self.repository = DummyStableDiffusionRepository()
    else:
      self.repository = RealStableDiffusionRepository()

  async def txt2img(self, payload):
    return await self.repository.fetchData(SD_TXT2IMG_URL, payload)

  async def img2img(self, payload):
    return await self.repository.fetchData(SD_IMG2IMG_URL, payload)