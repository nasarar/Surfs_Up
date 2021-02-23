from flask import Flask

#creates a Flask app
app = Flask(__name__)


#creates first route
@app.route('/')
def hello_world():
    return('hello_world') 