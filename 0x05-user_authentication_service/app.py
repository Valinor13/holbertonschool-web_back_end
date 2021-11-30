#!/usr/bin/env python3
""" Appy flask navigator module """
from flask import Flask, jsonify, request
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
