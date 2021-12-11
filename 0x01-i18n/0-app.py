#!/usr/bin/env python3
""" This is the basic flask appy """

from flask import Flask
from flask.templating import render_template
app = Flask(__name__)


@app.route('/')
def index():
    """ calls the index from templates """
    return render_template('0-index.html')
