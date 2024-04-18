from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("StoryMe_Website.html")


if __name__ == "__main__":
    app.run(host="https://story-me-web.vercel.app/")