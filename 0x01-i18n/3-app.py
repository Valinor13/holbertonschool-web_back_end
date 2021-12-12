#!/usr/bin/env python3
""" This is the basic flask appy """

from flask import Flask, request
from flask_babel import Babel, gettext
from flask.templating import render_template
app = Flask(__name__)
babel = Babel(app)


class Config:
    """ Config settings for babel app """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


@babel.localeselector
def get_locale():
    """ returns the location for the g11n app """
    translations = [str(translation) for translation in babel.list_translations()]
    return request.accept_languages.best_match(translations)


app.config.from_object(Config)


@app.route('/')
def index():
    """ calls the index from templates """
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run()
