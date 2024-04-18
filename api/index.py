from flask import *

app = Flask(__name__)

@app.route('/')
def home():
    return send_file("api/static/StoryMe_Website.html")