from interface.controllerInterface.ProductResearchController import ProductResearchController
from interface.Service import Service
from flask import Blueprint, request

class EtsyController(ProductResearchController):
    def __init__(self, service: Service):
        self.service = service
        self.blueprint = Blueprint('etsyBp', __name__)
        self.blueprint.route('/etsy', methods=['POST'])(self.getProducts)

    def getProducts(self):
        data = request.get_json()
        return self.service.fetchProducts(**data)