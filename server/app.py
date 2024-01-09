#!/usr/bin/env python3

# import Flask
from flask import Flask

app = Flask(__name__) # flask class contructor only requires name of the module to be interprated as the application
# flask uses it to figure out where the application is and where important files will be

@app.route('/') # to map urls to python functions we use routes
def index():
    return '<h1>Programming with Flask</h1>'

# working with dynamic routes. Anything with the "<>" will be passed to decorated function as a parameter
@app.route('/<string:username>')
def user(username):
    return f'<h1>Profile for {username}</h1>'

if __name__ == '__main__':
    app.run(port=5555)