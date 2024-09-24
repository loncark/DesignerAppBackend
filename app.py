from flask import Flask
from flask_cors import CORS
from controller.GeminiController import gemini_bp
from controller.TrademarkController import trademark_bp
from controller.StableDiffusionController import sd_bp
from controller.GoogleTrendsController import gt_bp
from controller.FirebaseController import FirebaseController
from controller.EtsyController import etsy_bp

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.register_blueprint(gemini_bp)
    app.register_blueprint(trademark_bp)
    app.register_blueprint(sd_bp)
    app.register_blueprint(gt_bp)
    app.register_blueprint(etsy_bp)

    firebaseController = FirebaseController()
    app.register_blueprint(firebaseController.firebaseBp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
