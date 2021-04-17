import tensorflow as tf
import numpy as np
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
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
        type_of_plant=int(request.form['plant'])
        # Save the file to ./uploads
        basepath=os.path.dirname(__file__)
        file_path=os.path.join(
            basepath,'uploads',f.filename)
        f.save(file_path)

        # Load model
        if(type_of_plant==1):
            disease_class=['Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold', 'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite', 'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus', 'Tomato___healthy']
            model = load_model('tomato.h5')
        elif(type_of_plant==2):
            disease_class=['Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy']
            model=load_model('potato.h5')
        elif(type_of_plant==3):
            disease_class=['Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 'Grape___healthy']
            model=load_model('grape.h5')
        elif(type_of_plant==4):
            disease_class=['Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy']
            model=load_model('corn(maize).h5')
        elif(type_of_plant==5):
            disease_class=['Strawberry___Leaf_scorch', 'Strawberry___healthy']
            model=load_model('strawberry.h5')
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
