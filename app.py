#import libraries
import numpy as np
import pandas as pd
from flask import Flask, render_template,request
from flask_cors import CORS, cross_origin
import joblib


app = Flask(__name__)
# cors = CORS(app, resources={r'/*': {'origins': '*'}})
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
model = joblib.load('pipeline.pkl')
# #To use the predict button in our web-app
@app.route('/predict',methods=['GET'])
#@cross_origin(app, support_credentials= True, origins=['*'])
@cross_origin()
def predict():
   args = request.args
   text = args.get('textbody')
   prediction = model.predict([text])
   
   if (prediction==1):
      prediction = {'Prediction' : "Meeting"}
   else:
      prediction = {'Prediction' : "Normal"}
   return prediction

@app.route('/')
def my_form():
    return render_template('entry.html')

@app.route('/', methods=['POST'])
def textentry():
   text = request.form['text']
   prediction = model.predict([text])
   
   if (prediction==1):
      prediction = 1
   else:
      prediction = 0
   return prediction


if __name__ == "__main__":
   app.run(debug=True)
