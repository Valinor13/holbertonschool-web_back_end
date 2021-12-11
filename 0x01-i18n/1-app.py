#!/usr/bin/env python3
""" This is the basic flask appy """

from flask import Flask, request
from flask_babel import Babel
from flask.templating import render_template
app = Flask(__name__)
app.config.from_object('app.Config.settings')
babel = Babel(app)


class Config:
    """ Config settings for babel app """
    LANGUAGES = ['en', 'fr']

    @babel.localeselector
    def get_locale(self):
        """ returns the location for the g11n app """
        return request.accept_languages.best_match(self.LANGUAGES), 200


@app.route('/')
def index():
    """ calls the index from templates """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run()
