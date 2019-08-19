from datetime import datetime

from flask import render_template
from HelloFlask import app

@app.route('/')
@app.route('/home')
#@app.route('/api/data')


def home():
    now =datetime.now()
    formatted_now = now.strftime ("%A, %d %B, %Y at %X")

    #html_content="<html><head><title>Hello Shishu this Python code</title></head><body>"
    #html_content +="<strong> Hello Flask!</strong> on " + formatted_now
    #html_content += "</body></html>"
    return render_template("index.html", 
                           title="Hello Flask",
                           message = "Hello, Shishu",
                           content =" on " + formatted_now)
@app.route('/about')

def about():
    return render_template("about.html",
                           title=" About Shishu Flask",
                           content="Example of app for flask app")

