from flask import Flask
from flask_cors import CORS
from controller.FirebaseController import FirebaseController
from controller.GeminiController import GeminiController
from controller.TrademarkController import TrademarkController
from controller.StableDiffusionController import StableDiffusionController
from controller.GoogleTrendsController import GoogleTrendsController
from controller.EtsyController import EtsyController

def createApp():
    app = Flask(__name__)
    CORS(app)

    controllers = [
        FirebaseController(),
        GeminiController(),
        TrademarkController(),
        StableDiffusionController(),
        GoogleTrendsController(),
        EtsyController(),
    ]

    for controller in controllers:
        app.register_blueprint(controller.blueprint)

    return app

if __name__ == '__main__':
    app = createApp()
    app.run(debug=True)
