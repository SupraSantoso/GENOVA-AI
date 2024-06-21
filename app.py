from flask import Flask, render_template, request, redirect, url_for, flash
import os
import tensorflow as tf 
from tensorflow import keras
from keras import layers, models, optimizers, losses, metrics, preprocessing
import numpy as np
from werkzeug.utils import secure_filename
import time 

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "static/uploads/"
model = models.load_model("model/CNN50_Brain_Tumor.h5")

current_time = time.time() 

def predict_image(img_path):
    img = preprocessing.image.load_img(img_path, target_size=(224, 224))
    img_array = preprocessing.image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0

    predictions = model.predict(img_array)
    return predictions

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            prediction = predict_image(filepath)
            result = np.argmax(prediction, axis=1)
            confidence = int(np.max(prediction) * 100)

            class_names = ['Glioma', 'Meningioma', 'No Tumor', 'Pituitary']
            predicted_class = class_names[result[0]]

            print(f'Predicted Class: {predicted_class}, Confidence: {confidence}')
            local_time = time.localtime(current_time)
            data_date = time.strftime("%d-%m-%Y", local_time)
            data_time = time.strftime("%H:%M:%S", local_time)

            return render_template("predict.html", img_path=filename, predicted_class=predicted_class, confidence=confidence, data_date=data_date, data_time=data_time)

    return render_template("predict.html")

@app.route("/more")
def more():
    return render_template("more.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/glioma")
def glioma():
    return render_template("galery_glioma.html")

@app.route("/meningioma")
def meningioma():
    return render_template("galery_meningioma.html")

@app.route("/no tumor")
def no_tumor():
    return render_template("galery_notumor.html")

@app.route("/pituitary")
def pituitary():
    return render_template("galery_pituitary.html")

@app.route("/faq")
def faq():
    return render_template("faq.html")

if __name__ == '__main__':
    app.run(debug=True)
