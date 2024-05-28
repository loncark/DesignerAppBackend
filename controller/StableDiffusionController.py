import service.StableDiffusionService

from flask import Blueprint, request

sd_bp = Blueprint('sd_bp', __name__)

@sd_bp.route('/sd/txt2img', methods=['POST'])
async def SDtextToImage():
    data = request.get_json()
    return await service.StableDiffusionService.txt2img(data)

@sd_bp.route('/sd/img2img', methods=['POST'])
async def SDimageToImage():
    data = request.get_json()
    return await service.StableDiffusionService.img2img(data)
