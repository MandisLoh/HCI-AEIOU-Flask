from flask import Flask
from flask import render_template
from datetime import datetime
import re
#import libraries
import numpy as np
import pandas as pd
from flask import Flask, render_template,request
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA

from model import X_test_pca
from html_to_text import html2text

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

# #To use the predict button in our web-app
@app.route('/predict.html',methods=['GET'])
def predict():
   html = './templates/inbox-faith-email.html'
   model = pickle.load(open('model.pkl', 'rb'))
   count_vect = CountVectorizer()
   final_features = html2text(html)
   prediction = model.predict(count_vect.fit_transform([final_features]))
   return render_template('predict.html', prediction_text='Predicted category is {}'.format(prediction))

@app.route('/')
def inbox_main_unread():
   return render_template('inbox-main-unread.html')

@app.route('/inbox-faith-email.html/')
def inbox_faith_email():
   return render_template('inbox-faith-email.html')

@app.route('/inbox-faith-email.html/inbox-faith-email-w-pop-up.html')
def inbox_faith_email_w_pop_up():
   return render_template('inbox-faith-email-w-pop-up.html')

@app.route('/inbox-faith-email.html/calendar-event-2.html')
def calendar_event_2():
   return render_template('calendar-event-2.html')

@app.route('/inbox-new-email.html')
def inbox_new_email():
   return render_template('inbox-new-email.html')

@app.route('/new-e-mail-message-empty.html')
def new_e_mail_message_empty():
   return render_template('new-e-mail-message-empty.html')

@app.route('/new-e-mail-message.html')
def new_e_mail_message():
   return render_template('new-e-mail-message.html')

@app.route('/new-e-mail-message-w-pop-up.html')
def new_e_mail_message_w_pop_up():
   return render_template('new-e-mail-message-w-pop-up.html')

@app.route('/new-appointment.html')
def new_appointment():
   return render_template('new-appointment.html')

@app.route('/calendar-event-1.html')
def calendar_event_1():
   return render_template('calendar-event-1.html')

@app.route('/calendar-event-12.html')
def calendar_event_12():
   return render_template('calendar-event-12.html')

@app.route('/calendar-main.html')
def calendar_main():
   return render_template('calendar-main.html')

@app.route('/inbox-faith-email.html/calendar-event-12.html')
def calendar_event_12_1():
   return render_template('calendar-event-12.html')

if __name__ == "__main__":
   app.run(debug=True)