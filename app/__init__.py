from flask import Flask #import the flask library

app = Flask(__name__) #app is the name of the Flask object, _name_ is the name of the current module running

from app import routes  #now run routes.py