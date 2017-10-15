from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
from imgurpython import ImgurClient
import json
client = ImgurClient('3f50136dbb425b8', '15567e9f23b8d117b4ff3b2cfd5a5195f0def36d')

# Example request
items = client.gallery()
for item in items:
    print(item.link)

client_id = '3f50136dbb425b8'
client_secret = '15567e9f23b8d117b4ff3b2cfd5a5195f0def36d'

app = ClarifaiApp(api_key='f789eaa60ab04869a2b80c752daa3484')

# get the general model
model = app.workflows.get('mood-flow')

image = ClImage(url='https://sslg.ulximg.com/image/405x405/artist/1392767353_217f16228baaa5dc18c82925ac76edf6.jpg/9e89e114db44f266e044addd06e88d69/1392767353_kanye_west_wall_40.jpg')
hello = model.predict([image])
# predict with the model

##print(json.dumps(hello, indent=1))