#!/usr/bin/env python3
""" This is the basic flask appy """

from flask import Flask, request, g
from flask_babel import Babel, gettext
from flask.templating import render_template
app = Flask(__name__)
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """ Config settings for babel app """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """ returns the location for the g11n app """
    locale = request.args.get('locale')
    if locale and locale in Config.LANGUAGES:
        return locale
    t10s = [str(translation) for translation in babel.list_translations()]
    return request.accept_languages.best_match(t10s)


def get_user():
    """ gets a user from the browser input """
    login_id = request.args.get('login_as')
    if not login_id or not users[login_id]:
        return None
    return users[login_id]


@app.before_request
def before_request():
    """ assigns user before page loads """
    user = get_user()
    if user:
        g.user = user
        return render_template('5-index.html', logger=gettext('logged_in_as'))
    else:
        return render_template('5-index.html', logger=gettext('not_logged_in'))


@app.route('/')
def index():
    """ calls the index from templates """
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run()
