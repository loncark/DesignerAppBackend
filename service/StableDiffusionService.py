from interface.repositoryInterface.ImageGenerationRepository import ImageGenerationRepository
from constants import SD_TXT2IMG_URL, SD_IMG2IMG_URL

class StableDiffusionService:
  def __init__(self, repository: ImageGenerationRepository):
    self.repository = repository

  async def txt2img(self, payload):
    return await self.repository.generateImage(SD_TXT2IMG_URL, payload)

  async def img2img(self, payload):
    return await self.repository.generateImage(SD_IMG2IMG_URL, payload)