'''
Quizzicle App 
Written by Mandy Kopelke and Anne Holman for CSB2019

API & Flask Team Project, Term 2
Uses the Open Trivia Database API, more info at: https://opentdb.com/

This module defines the routes required to control the app. 

'''
from flask import Flask, render_template
import classes

## Initialise Flask app
app = Flask(__name__)

## Route that displays the Quizzicle landing page
@app.route("/index/")
@app.route("/")
def start_app():
    '''
    Delivers the application index HTML page to the calling browser
    '''
    
    return render_template("index.html")
