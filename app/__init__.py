import os
from flask import Flask, render_template, send_from_directory
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html',  url=os.getenv("URL"))

@app.route('/health')
def all_good():
    status = flask.Response(status=200)
    return status
