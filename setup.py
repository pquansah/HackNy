from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
import json
app = ClarifaiApp(api_key='f789eaa60ab04869a2b80c752daa3484')

# get the general model
model = app.models.get('{model_id}')

image = ClImage(url='https://samples.clarifai.com/puppy.jpeg')
hello = model.predict([image])
# predict with the model

print(json.dumps(hello, indent=1))