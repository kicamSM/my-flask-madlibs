from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY'] = "iloverollerderby12"
debug = DebugToolbarExtension(app)

@app.route("/")
def home_page():
     return render_template('home.html')