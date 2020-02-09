from pymongo import MongoClient
from flask import Flask, render_template, request, session
import datetime

app = Flask(__name__)
app.secret_key = 'thatsasp1cymeatball'

#client = MongoClient("mongodb://localhost:27017")
client = MongoClient("mongodb+srv://Admin:adminADMIN@cluster0-b80xk.mongodb.net/test?retryWrites=true&w=majority")
db = client['blueprint']

messages = []

messages2 = db['messages']

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html', 
        messages=messages2.find({}),
        loggedIn=('username' in session),
        username=session.get('username', '')
    )

@app.route('/login', methods=['POST'])
def login():
    session['username'] = request.form['username']
    return 'success'

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('username', None)
    return 'success'

@app.route('/message', methods=['POST'])
def message():
    message = session['username'] + ": " + request.form['message']
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_object = {'message': message, 'ts': now}
    messages2.insert_one(new_object)
    messages.append(new_object)
    return 'success'

app.run(port=3000, debug=True, host="0.0.0.0")