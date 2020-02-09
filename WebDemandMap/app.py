#!/usr/bin/env python3
from flask import Flask, render_template, session, request

#extra import
import email, smtplib, ssl
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#from pymongo import MongoClient
#leroy is tremendously cute
app = Flask(__name__)
app.secret_key = "thasasp1cymeatball"

#messages = []

@app.route('/', methods=['GET'])
def home():
    print(request.form)
    return render_template('index.html',
        message = request.form.get('Email', "test"), 
        loggedIn=('Email' in session),
        email=session.get('Email', '')
        ) 

        
@app.route('/register', methods=['POST'])
def register():
    session['Email'] = request.form.get('Email', '')
    print('Email went through')
    return 'success'

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('Email', None)
    return 'success'

@app.route('/submit', methods=['POST'])
def submit():
    message = reguest.form.get('message', '')
    return 'success'


@app.route('/sendemail', methods=['POST'])
def sendemail():
    print('Mail Sent')
    # assign key email aspects to variables for easier future editing

    subject = "Interest in further services"
    message = request.form.get("message", "default value")
    body = "Hi there dear user, \n we heard that you expressed in " + message + " ! We'll let you know any updates when they come around"
    sender_email = "SupinDemand@gmail.com"
    receiver_email = request.form.get('Email', 'leshaigor@gmail.com')
    password = "MITBlueprint3P"
    # Create the email head (sender, receiver, and subject)
    email = MIMEMultipart()
    email["From"] = sender_email
    email["To"] = receiver_email 
    email["Subject"] = subject
    email.attach(MIMEText(body, "plain"))
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_email, password) #login with mail_id and password
    text = email.as_string()
    session.sendmail(sender_email, receiver_email, text)
    session.quit()
    return 'success'
    
app.run(port=3000, debug=True)