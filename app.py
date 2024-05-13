from flask import Flask
from Controller import hello

app = Flask(__name__)

app.route('/api/hello')(hello)

if __name__ == '__main__':
    app.run(debug=True)
