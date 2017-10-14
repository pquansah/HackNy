import urllib.request
import json

api_key = 'MXumeVsEgV4ncwe7aHDAdmwnNM4UkI92'

emotion_list = ['happy', 'sad', 'scared', 'angry', 'surprised', 'confused', 'excited', 'disgust']
emo = emotion_list[4]

emo = emotion_list[2]
subject = input('Subject : ')
concept = '{} {}'.format(emo, subject).replace(' ', '+')

data = json.loads(urllib.request.urlopen("http://api.giphy.com/v1/gifs/search?q={}&api_key={}&limit=5".format(concept,api_key)).read())
embed_urls_list = []
for gif in data['data']:
    embed_urls_list.append(gif['embed_url'])
    
for url in embed_urls_list:
    print(json.dumps(url))

