import flask
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()

#how to pass different ports to it?
#pass the port = port# in the app.run() method>>

#didnt work 
