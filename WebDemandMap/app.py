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
    session['Email'] = request.form.get('Email', 'test')
    print('Email went through')
    return 'success'

@app.route('/')

@app.route('/sendemail', methods=['POST'])
def sendemail():
    # assign key email aspects to variables for easier future editing
    subject = "Interest in further services"
    message = request.form.get
    body = "Hi there dear user, /n we heard that you expressed in "
    sender_email = "connerleavitt@gmail.com"
    receiver_email = "connerleavitt@icloud.com"
    password = "abc123"
    # Create the email head (sender, receiver, and subject)
    email = MIMEMultipart()
    email["From"] = 'demandmap@gmail.com'
    email["To"] = receiver_email 
    email["Subject"] = subject
        # Add body and attachment to email
        #email.attach(MIMEText(body, "plain"))
        #attach_file = open(file, "rb") # open the file
        #report = MIMEBase("application", "octate-stream")
        #report.set_payload((attach_file).read())
        #encoders.encode_base64(report)
        #add report header with the file name
        #report.add_header("Content-Decomposition", "attachment", filename = file)
        #email.attach(report)
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_email, password) #login with mail_id and password
    text = email.as_string()
    session.sendmail(sender_email, receiver_email, text)
    session.quit()
    print('Mail Sent')
    
app.run(port=3000, debug=True)