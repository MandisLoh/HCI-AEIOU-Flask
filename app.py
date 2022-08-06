#import libraries
import numpy as np
import pandas as pd
from flask import Flask, render_template,request
import joblib


app = Flask(__name__)
model = joblib.load('pipeline.pkl')

# #To use the predict button in our web-app
@app.route('/predict',methods=['GET'])
def predict(text):
   prediction = prediction = model.predict([text])
   
   if (prediction==1):
      prediction = "Meeting"
   else:
      prediction = "Normal"
   return prediction

@app.route('/')
def my_form():
    return render_template('entry.html')

@app.route('/', methods=['POST'])
def textentry():
    text = request.form['text']
    return text


if __name__ == "__main__":
   app.run(debug=True)
