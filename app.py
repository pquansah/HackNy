from flask import Flask, render_template, request
import requests 
import urllib

from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
#from imgurpython import ImgurClient
import json

app = Flask(__name__)
emotion_list = ['happy', 'sad', 'scared', 'angry', 'surprised', 'confused', 'disgust']

def clarifai_prediction():
    return "disgust"
    #paak put your stuff here

@app.route('/')
def send_emotion_gif():
    emo = clarifai_prediction()
    
    return render_template('index.html', )


@app.route('/gif-urls', methods=['POST'])
def hello():
    emo = clarifai_prediction()
    name = request.form.get("name")
    concept = '{} {}'.format(subject, emo).replace(' ', '+')

    data = json.loads(urllib.urlopen("http://api.giphy.com/v1/gifs/search?q={}&api_key={}&limit=5".format(concept,api_key)).read())
    embed_urls_list = []
    for gif in data['data']:
        embed_urls_list.append(gif['embed_url'])
    return render_template('hello.html', urls=embed_urls_li)
'''
# using an api call to get data
@app.route('/weather/', methods=['GET'])
'''