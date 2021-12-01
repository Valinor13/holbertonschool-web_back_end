#!/usr/bin/env python3
""" Appy flask navigator module """
from flask import Flask, jsonify, request, make_response, abort
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def welcome_message() -> str:
    """ GET home dir
    Return:
      - welcome message
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    """ POST users
    Return:
      - returns json with new email or already registered message
    """
    pw = request.form.get('password')
    email = request.form.get('email')

    try:
        AUTH.register_user(email, pw)
        return jsonify({'email': email, 'message': 'user created'})
    except ValueError:
        return jsonify({'message': 'email already registered'}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """ POST sessions
    Return:
      - returns json with email and logging confirmation
    """
    pw = request.form.get('password')
    email = request.form.get('email')
    if AUTH.valid_login(email, pw):
        sesh_id = AUTH.create_session(email)
        cookie(sesh_id)
        return jsonify({'email': email, 'message': 'logged in'})
    else:
        abort(401)


@app.route('/cookie')
def cookie(sesh_id: str):
    """ makes a cookie in response """
    if not request.cookies.get('session_id'):
        res = make_response('Setting a cookie')
        res.set_cookie('session_id', sesh_id)
    else:
        res = make_response(
            'Value of cookie session_id is {}'.format(
                request.cookies.get('session_id')))
    return res


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
