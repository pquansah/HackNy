from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
import json

client_id = '3f50136dbb425b8'
client_secret = '15567e9f23b8d117b4ff3b2cfd5a5195f0def36d'

app = ClarifaiApp(api_key='f789eaa60ab04869a2b80c752daa3484')

# get the general model
model = app.workflows.get('mood-flow')

image = ClImage(filename='/Users/GeriElise/Desktop/face5.png')
hello = model.predict([image])
test = hello['results'][0]['outputs'][0]['data']['concepts'][0]['id']
# predict with the model

print(json.dumps(test, indent=1))
#print ()