#!/usr/bin/env python3
from flask import Flask, render_template, session, request
from pymongo import MongoClient

#extra import
import email, smtplib, ssl
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#from pymongo import MongoClient
#leroy is tremendously cute


app = Flask(__name__)
app.secret_key = "thasasp1cymeatball"

email_test = "leshaigor@gmail.com"
#messages = []

client = MongoClient("mongodb+srv://joeyDB:GPdPS7Jk8jKGjXf@cluster0-exgbo.mongodb.net/test?retryWrites=true&w=majority")
db = client['blueprint']

geotags = db['geotags']
#emails = db['emails']

@app.route('/', methods=['GET'])
def home():
    #print(request.form)
    email_test = session.get('email', 'test')
    loggedIn=('email' in session)
    return render_template('index.html',
        loggedIn=loggedIn
        #message = request.form.get('Email', "test"), 
    )   
#test
        
@app.route('/register', methods=['POST'])
def register():
    print('request.form is: ', request.form)
    session['email'] = request.form.get('email', 'leshaigor@gmail.com')
    print(session['email'])
    email_test = session['email']
    print('Email went through')
    return 'success'

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('email', None)
    return 'success'

@app.route('/submit', methods=['POST'])
def submit():
    #geotags = request.form.get('geotags', '')
    theRequest = request.form.get('request', 'default request')
    geotag = '12.345, 67.8910'
    the_email = session['email']
    print("we got here!")
    geotags.insert_one({'email': the_email, 'geotag': geotag, 'request': theRequest})

    print("got here")
    print('The test is running succesfully')
    #print('Mail Sent')
    # assign key email aspects to variables for easier future editing
    subject = "Your Suggestion"
    message = request.form.get("message", "default value")
    print(message)
    body = "Hi there dear user,\n\nWe heard that you expressed interest in someone opening a(n)" + message + "! We'll send another email to update you if any " + message + " opens nearby."
    sender_email = "SupinDemand@gmail.com"
    #session['email'] = session['email']
    print('session[email] is: ', session['email'])
    email_test = session['email']
    print('email_test is: ', email_test)
    receiver_email = email_test
    password = "MITBlueprint3P"
    # Create the email head (sender, receiver, and subject)
    email = MIMEMultipart()
    email["From"] = sender_email
    email["To"] = receiver_email 
    email["Subject"] = subject
    email.attach(MIMEText(body, "plain"))
    #Create SMTP session for sending the mail
    session1 = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session1.starttls() #enable security
    session1.login(sender_email, password) #login with mail_id and password
    text = email.as_string()
    session1.sendmail(sender_email, receiver_email, text)
    session1.quit()
    return 'success'
    
app.run(port=3000, debug=True)