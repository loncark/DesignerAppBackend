from constants import SD_TXT2IMG_URL, SD_IMG2IMG_URL
from interface.Repository import Repository

class StableDiffusionService:
  def __init__(self, repository: Repository):
    self.repository = repository

  async def txt2img(self, payload):
    return await self.repository.fetchData(SD_TXT2IMG_URL, payload)

  async def img2img(self, payload):
    return await self.repository.fetchData(SD_IMG2IMG_URL, payload)