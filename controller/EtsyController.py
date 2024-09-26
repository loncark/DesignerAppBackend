from interface.Service import Service
from flask import Blueprint, request

class EtsyController:
    def __init__(self, service: Service):
        self.service = service
        self.blueprint = Blueprint('etsyBp', __name__)
        self.blueprint.route('/etsy', methods=['POST'])(self.queryEtsy)

    def queryEtsy(self):
        data = request.get_json()
        return self.service.fetchProducts(**data)