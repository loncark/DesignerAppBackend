import service.StableDiffusionService

from flask import Blueprint

sd_bp = Blueprint('sd_bp', __name__)

@sd_bp.route('/sd')
async def SDtextToImage():
    return await service.StableDiffusionService.fetch_and_save_image('')
