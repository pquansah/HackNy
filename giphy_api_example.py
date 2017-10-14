import urllib
import json


api_key = 'MXumeVsEgV4ncwe7aHDAdmwnNM4UkI92'

emotion_list = ['happy', 'sad', 'scared', 'angry', 'suprised', 'confused', 'excited', 'disgust']
emo = emotion_list[4]
subject = input('Subject : ')
concept = '{} {}'.format(emo, subject).replace(' ', '+')

data = json.loads(urllib.request.urlopen("http://api.giphy.com/v1/gifs/search?q={}&api_key={}&limit=5".format(concept,api_key)).read())
print(json.dumps(data, sort_keys=True, indent=4))

				
