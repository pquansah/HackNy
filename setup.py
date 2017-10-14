from clarifai.rest import ClarifaiApp
import json
app = ClarifaiApp(api_key='f789eaa60ab04869a2b80c752daa3484')

# get the general model
model = app.models.get("general-v1.3")

# predict with the model
hello = model.predict_by_url(url='https://peopledotcom.files.wordpress.com/2016/12/kanye-west-660x450.jpg?w=660')

print(json.dumps(hello, indent=1))