import service.StableDiffusionService

async def SDtextToImage():
    return await service.StableDiffusionService.fetch_and_save_image('')
