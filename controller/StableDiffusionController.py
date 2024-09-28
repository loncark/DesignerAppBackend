from interface.controllerInterface.ImageGenerationController import ImageGenerationController
from interface.serviceInterface.ImageGenerationService import ImageGenerationService
from flask import Blueprint, request

class StableDiffusionController(ImageGenerationController):
    def __init__(self, service: ImageGenerationService):
        self.service = service
        self.blueprint = Blueprint('sdBp', __name__)
        self.registerRoutes()

    def registerRoutes(self):
        self.blueprint.route('/sd/txt2img', methods=['POST'])(self.textToImage)
        self.blueprint.route('/sd/img2img', methods=['POST'])(self.imageToImage)

    async def textToImage(self):
        data = request.get_json()
        return await self.service.textToImage(data)

    async def imageToImage(self):
        data = request.get_json()
        return await self.service.imageToImage(data)
