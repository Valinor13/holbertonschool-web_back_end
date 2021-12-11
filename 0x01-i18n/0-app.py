#!/usr/bin/env python3
""" This is the basic flask appy """

from flask import Flask
from flask.templating import render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('templates/0-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
