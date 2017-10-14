from clarifai.rest import ClarifaiApp

app = ClarifaiApp(api_key='f789eaa60ab04869a2b80c752daa3484')

# get the general model
model = app.models.get("general-v1.3")

# predict with the model
hello = model.predict_by_url(url='https://samples.clarifai.com/metro-north.jpg')

print(json.dumps(hello, indent=1))