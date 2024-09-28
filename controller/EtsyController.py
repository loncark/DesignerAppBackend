from interface.controllerInterface.ProductResearchController import ProductResearchController
from interface.serviceInterface.ProductResearchService import ProductResearchService
from flask import Blueprint, request

class EtsyController(ProductResearchController):
    def __init__(self, service: ProductResearchService):
        self.service = service
        self.blueprint = Blueprint('etsyBp', __name__)
        self.blueprint.route('/etsy', methods=['POST'])(self.getProducts)

    def getProducts(self):
        data = request.get_json()
        return self.service.getProducts(**data)