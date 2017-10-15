import urllib
import json

api_key = 'MXumeVsEgV4ncwe7aHDAdmwnNM4UkI92'

def clarifai_prediction():
    return 'happy'

emotion_list = ['happy', 'sad', 'scared', 'angry', 'surprised', 'confused', 'excited', 'disgust']
emo = clarifai_prediction()
subject = "moon"
concept = '{} {}'.format(subject, emo).replace(' ', '+')

data_search_gif = json.loads(urllib.urlopen("http://api.giphy.com/v1/gifs/search?q={}&api_key={}&limit=5".format(concept,api_key)).read())
data_search_sticker = json.loads(urllib.urlopen("http://api.giphy.com/v1/stickers/search?q={}&api_key={}&limit=5".format(concept,api_key)).read())

def first():
    gif_list = []
    for gif in data_search_gif['data']:
        gif_list.append(gif['images']['original']['url'])
    
    for gif in gif_list:
        print(json.dumps(gif))

def firsthalf():

def second():
    sticker_list = []
    for sticker in data_search_sticker['data']:
        sticker_list.append(sticker['images']['original']['url'])
    print(json.dumps(sticker_list, indent=1))

def second half():

if __name__ == "__main__": 
    #first()
    second()