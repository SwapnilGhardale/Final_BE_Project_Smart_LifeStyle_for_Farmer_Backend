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
       
        return result
    return None


@app.route('/')
def hello_world():
    return 'Hello, World!'
