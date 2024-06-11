from flask import Flask
from flask_cors import CORS
from controller.GeminiController import gemini_bp
from controller.TrademarkController import trademark_bp
from controller.StableDiffusionController import sd_bp
from controller.GoogleTrendsController import gt_bp
from controller.FirebaseController import firebase_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(gemini_bp)
app.register_blueprint(trademark_bp)
app.register_blueprint(sd_bp)
app.register_blueprint(gt_bp)
app.register_blueprint(firebase_bp)

if __name__ == '__main__':
    app.run(debug=True)
