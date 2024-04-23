#/usr/bin/env python3
from flask import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('StoryMe_Website.html')

@app.route('/SobreNosotros')
def about():
    return render_template('SobreNosotros.html')

if __name__ == "__main__":
    app.run(debug=True)
