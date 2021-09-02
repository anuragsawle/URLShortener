from flask import Flask,jsonify
from flask_restful import Api
import requests

app = Flask(__name__)
api = Api(app)


@app.route('/')
def getURL():
    return "Pass URL in address bar"


@app.route('/<string:URL>/')
def URLShortener(URL):
        cuttly = "https://cutt.ly/scripts/shortenUrl.php"
        data = {"url": URL}
        short = requests.post(cuttly, data=data).text
        shortenURL = short
        return jsonify({'URL': URL,
                        'Shortener URL': shortenURL})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
