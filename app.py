from flask import Flask
import Controller
app = Flask(__name__)

app.route('/gemini')(Controller.queryGemini)
app.route('/trends')(Controller.queryGoogleTrends)
app.route('/db')(Controller.saveToRealtimeDb)
app.route('/storage')(Controller.saveToStorage)
app.route('/tess')(Controller.queryTESS)
app.route('/sd')(Controller.SDtextToImage)

if __name__ == '__main__':
    app.run(debug=True)
