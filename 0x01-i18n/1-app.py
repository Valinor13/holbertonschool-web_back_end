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

@babel.localeselector
def get_locale():
    """ returns the location for the g11n app """
    return request.accept_languages.best_match(app.config(Config.LANGUAGES))

@babel.timezoneselector
def get_timezone(self):
    """ returns the timezone default = UTC """
    return 'UTC'

@app.route('/')
def index():
    """ calls the index from templates """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run()
