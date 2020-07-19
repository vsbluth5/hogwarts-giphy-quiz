from flask import render_template
from flask import request
from app import app
from app.models import model
import os

app.config['GIPHY_KEY'] = os.getenv("GIPHY_KEY")

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', pagetitle='Home')
    
@app.route('/results')
def displayResults():
    return render_template("results.html")

@app.route('/getChoices', methods=['GET', 'POST'])
def handleChoices():
    if request.method == 'GET':
        return "This is what happens when the form is not posted"
    else:
        userdata = dict(request.form)
        print(userdata)
        nickname = model.shout(userdata['nname'])
        faveColor= model.shout(userdata['breakfast'])
        age= userdata['age']
        return render_template("choices.html", nickname=nickname, faveColor=faveColor, age=age)

@app.route('/getGifs', methods=['GET', 'POST'])
def makeDecision():
    if request.method == 'GET':
        return "This is what happens when the radiobuttons are not posted"
    else:
        userdata = dict(request.form)
        print(userdata)
        urlList = model.getURL(userdata['animal'], userdata['hogwarts'], userdata['colors'], app.config['GIPHY_KEY'])
        return render_template("results.html", ch1=userdata['animal'], ch2=userdata['hogwarts'], ch3=userdata['colors'], photos=urlList)
        #return render_template("results.html", photo="static/micropig.jpg")