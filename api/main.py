from flask import Flask
app = Flask (__name__)

@app.route("/")
def home():
    return "HELLO from vercel use Flask"

@app.route("/about")
def about():
    return "HELLO about"