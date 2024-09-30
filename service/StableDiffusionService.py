from interface.repositoryInterface.ImageGenerationRepository import ImageGenerationRepository
from interface.serviceInterface.ImageGenerationService import ImageGenerationService
from constants import SD_TXT2IMG_URL, SD_IMG2IMG_URL

class StableDiffusionService(ImageGenerationService):
  def __init__(self, repository: ImageGenerationRepository):
    super().__init__(repository)

  async def textToImage(self, payload):
    return await self.repository.generateImage(SD_TXT2IMG_URL, payload)

  async def imageToImage(self, payload):
    return await self.repository.generateImage(SD_IMG2IMG_URL, payload)