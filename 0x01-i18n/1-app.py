#!/usr/bin/env python3
""" This is the basic flask appy """

from flask import Flask, request
from flask_babel import Babel
from flask.templating import render_template
app = Flask(__name__)
babel = Babel(app)


class Config:
    """ Config settings for babel app """
    LANGUAGES = ['en', 'fr']


app.config.from_object(Config)


@app.route('/')
def index():
    """ calls the index from templates """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run()
