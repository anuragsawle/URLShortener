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
    textFile = open('Previously_searched_urls.txt', 'r')
    previous_urls = textFile.readlines()
    found = False
    givenURL = URL
    for url in previous_urls:
        foundUrls = url.split(':::')
        foundUrl = foundUrls[0]
        if foundUrl == givenURL:
            shortenURL = foundUrls[1]
            shortenURL = shortenURL.split('\n')[0]
            found = True
    if found:
        return jsonify({'URL': URL,
                        'Shortener URL': shortenURL})
    else:
        cuttly = "https://cutt.ly/scripts/shortenUrl.php"
        data = {"url": URL}
        short = requests.post(cuttly, data=data).text
        shortenURL = short
        urlsToAdd = givenURL + ':::' + shortenURL + '\n'
        if urlsToAdd[0] != 'f':
            textFile = open('Previously_searched_urls.txt', 'a')
            textFile.write(urlsToAdd)
            textFile.close()
        return jsonify({'URL': URL,
                        'Shortener URL': shortenURL})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
