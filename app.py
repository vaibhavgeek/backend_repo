from flask import Flask, request
import gensim
import gensim.downloader

app = Flask(__name__)

glove_vectors = gensim.downloader.load('glove-twitter-25')

@app.route("/", methods=['POST'])
def hello_world():
    titles = request.json["text"]
    json = {}
    for title in titles:
        try:
            vec = glove_vectors[title]
            json[title] = vec.tolist()
        except:
            pass
    return json

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=8001)
