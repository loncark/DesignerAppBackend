from service.StableDiffusionService import StableDiffusionService
from flask import Blueprint, request

class StableDiffusionController:
    def __init__(self):
        self.service = StableDiffusionService()
        self.blueprint = Blueprint('sdBp', __name__)
        self.registerRoutes()

    def registerRoutes(self):
        self.blueprint.route('/sd/txt2img', methods=['POST'])(self.SDtextToImage)
        self.blueprint.route('/sd/img2img', methods=['POST'])(self.SDimageToImage)

    async def SDtextToImage(self):
        data = request.get_json()
        return await self.service.txt2img(data)

    async def SDimageToImage(self):
        data = request.get_json()
        return await self.service.img2img(data)
