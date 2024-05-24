from flask import Flask
import controller.GeminiController as GeminiController
import controller.TrademarkController as TrademarkController
import controller.StableDiffusionController as SDController
import controller.GoogleTrendsController as GTController
import controller.FirebaseController as FirebaseController

app = Flask(__name__)

app.route('/gemini')(GeminiController.queryGemini)
app.route('/trends')(GTController.queryGoogleTrends)
app.route('/db')(FirebaseController.saveToRealtimeDb)
app.route('/storage')(FirebaseController.saveToStorage)
app.route('/tess')(TrademarkController.queryTESS)
app.route('/sd')(SDController.SDtextToImage)

if __name__ == '__main__':
    app.run(debug=True)
