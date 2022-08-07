#import libraries
import numpy as np
import pandas as pd
from flask import Flask, render_template,request
import joblib


app = Flask(__name__)
model = joblib.load('pipeline.pkl')

# #To use the predict button in our web-app
@app.route('/predict',methods=['GET'])
def magic():
   args = request.args
   text = args.get('textbody')
   prediction = model.predict([text])
   
   if (prediction==1):
      prediction = 1
   else:
      prediction = 0
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
