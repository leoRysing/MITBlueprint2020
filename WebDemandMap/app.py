#!/usr/bin/env python3
from flask import Flask, render_template, session, request
#from pymongo import MongoClient
#leroy is tremendously cute
app = Flask(__name__)

#messages = []

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html',
        #message = request.form['message'], 
        loggedIn=('email' in session),
        email=session.get('email', '')
        ) 

        
@app.route('/register', methods=['POST'])
def register():
    session['email'] = request.form['email']
    print('email went through')
    return 'success'

app.run(port=3000, debug=True)