from flask import Flask, render_template, request
import requests 
import urllib, json

app = Flask(__name__)
emotion_list = ['happy', 'sad', 'scared', 'angry', 'surprised', 'confused', 'disgust']
giphy_api_key = 'MXumeVsEgV4ncwe7aHDAdmwnNM4UkI92'
def clarifai_prediction():
    return "disgust"
    #paak put your stuff here

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/gif-urls', methods=['POST'])
def hello():
    emo = clarifai_prediction()
    subject = request.form.get("name")
    concept = '{} {}'.format(subject, emo).replace(' ', '+')

    data = json.loads(urllib.urlopen("http://api.giphy.com/v1/gifs/search?q={}&api_key={}&limit=5".format(concept,giphy_api_key)).read())
    gif_list = []
    for gif in data['data']:
        gif_list.append(gif['images']['original']['url'])
    return render_template('hello.html', image_urls=gif_list)
'''
# using an api call to get data
@app.route('/weather/', methods=['GET'])
'''

if __name__ == '__main__':
    app.debug = True
    app.run()