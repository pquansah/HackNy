import urllib.request, json

emotion_list = ['happy', 'sad', 'scared', 'angry', 'suprised', 'confused', 'excited', 'disgust']
api_key = 'MXumeVsEgV4ncwe7aHDAdmwnNM4UkI92'
concept = 'ryan gosling'.replace(' ', '+')

data = json.loads(urllib.request.urlopen("http://api.giphy.com/v1/gifs/search?q={}&api_key={}&limit=5".format(concept,api_key)).read())
print(json.dumps(data, sort_keys=True, indent=4))

				
