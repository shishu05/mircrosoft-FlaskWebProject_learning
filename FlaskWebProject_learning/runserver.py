"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

import os
from HelloFlask import app


if __name__ == '__main__':

    HOST = os.environ.get('SERVER_HOST','localhost')

    try:
        PORT = int(os.environ.get('SERVER_PORT','5555'))

    except ValueError:
            PORT:5555

app.run(HOST,PORT)


#from flask import Flask
##import flask
#app = Flask(__name__)

## Make the WSGI interface available at the top level so wfastcgi can get it.
#wsgi_app = app.wsgi_app


#@app.route('/')
#@app.route('/hello/<name>?message=<msg>')
#def hello(name,msg):
#    """Renders a sample page."""
#    return "Hello World!" +name + "! Message is " + msg + "."

#if __name__ == '__main__':
#    import os
#    HOST = os.environ.get('SERVER_HOST', 'localhost')
#    try:
#        PORT = int(os.environ.get('SERVER_PORT', '5555'))
#    except ValueError:
#        PORT = 5555
#    app.run(HOST, PORT)
