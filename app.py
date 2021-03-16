import tensorflow as tf
import numpy as np
import os
from tensorflow.keras.models import load_model
from flask import Flask, request
app = Flask(__name__)

img_height=48
img_width=48
batch_size=64

def model_predict(img_path, model):
    img = image.load_img(img_path)
    img = image.load_img(img_path, target_size=(img_height,img_width))
    img = image.img_to_array(img)
    img = np.expand_dims(img,axis=0)
    prediction = model.predict(img)
    return prediction
    
@app.route('/predict',methods=['GET','POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath=os.path.dir_name(__file__)
        file_path=os.path.join(
            basepath,'uploads',secure_filename(f.filename))
        f.save(file_path)

        # Load model
        model=load_model('tomato.h5',compile=False)
        disease_class = ['Tomato_Bacterial_spot', 'Tomato_Early_blight','Tomato_Late_blight', 'Tomato_Leaf_Mold', 'Tomato_Septoria_leaf_spot','Tomato_Spider_mites_Two_spotted_spider_mite', 'Tomato__Target_Spot','Tomato__Tomato_YellowLeaf__Curl_Virus', 'Tomato__Tomato_mosaic_virus', 'Tomato_healthy']
        
        print('Model loaded. Check http://127.0.0.1:5000/')

        # Make prediction
        prediction=model_predict(file_path,model)
        a=prediction[0]
        i=np.argmax(a)
        result=disease_class[i]
        print(result)
        return result
    return None


@app.route('/')
def hello_world():
    return 'Hello, World!'
