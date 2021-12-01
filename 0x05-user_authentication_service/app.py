#!/usr/bin/env python3
""" Appy flask navigator module """
from flask import Flask, jsonify, request, abort
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
    if email and AUTH.valid_login(email, pw):
        sesh_id = AUTH.create_session(email)
        resp = jsonify({'email': email, 'message': 'logged in'})
        resp.set_cookie('session_id', sesh_id)
        return resp
    else:
        abort(401)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
