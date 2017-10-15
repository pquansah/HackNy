from flask import Flask, render_template, request
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
import requests 
import urllib, json

app = Flask(__name__)
emotion_list = ['happy', 'sad', 'scared', 'angry', 'surprised', 'confused', 'disgust']
giphy_api_key = 'MXumeVsEgV4ncwe7aHDAdmwnNM4UkI92'
client_id = '3f50136dbb425b8'
client_secret = '15567e9f23b8d117b4ff3b2cfd5a5195f0def36d'

def clarifai_prediction(image):
    app = ClarifaiApp(api_key='f789eaa60ab04869a2b80c752daa3484')
    model = app.workflows.get('mood-flow')
    climage = ClImage(filename=image)
    hello = model.predict([climage])
    test = hello['results'][0]['outputs'][0]['data']['concepts'][0]['id']
    return test

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/gif-urls', methods=['POST'])
def hello():
    img = request.form.get("image")
    emo = clarifai_prediction(img)
    try:
        subject = request.form.get("name")
    except:
        subject = ""
    concept = '{} {}'.format(subject, emo).replace(' ', '+')

    data = json.loads(urllib.urlopen("http://api.giphy.com/v1/gifs/search?q={}&api_key={}&limit=5".format(concept,giphy_api_key)).read())
    gif_list = []
    for gif in data['data']:
        gif_list.append(gif['images']['original']['url'])
    
    fixed_concept = concept.replace('+{}'.format(emo),'')

    data_search_sticker = json.loads(urllib.urlopen("http://api.giphy.com/v1/stickers/search?q={}&api_key={}&limit=5".format(concept,giphy_api_key)).read())
    sticker_list = []
    for sticker in data_search_sticker['data']:
        sticker_list.append(sticker['images']['original']['url'])

    return render_template('hello.html', concept=fixed_concept, gif_urls=gif_list, sticker_urls=sticker_list, emotion=emo)
'''
# using an api call to get data
@app.route('/weather/', methods=['GET'])
'''

if __name__ == '__main__':
    app.debug = True
    app.run()