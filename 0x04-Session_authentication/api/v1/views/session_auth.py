#!/usr/bin/env python3
""" Module of Session User views
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> str:
    """ POST /api/v1/users/
    JSON body:
      - email
      - password
      - last_name (optional)
      - first_name (optional)
    Return:
      - User object JSON represented
      - 400 if can't create the new User
    """
    email = request.form.get('email')
    if not email or len(email) == 0:
        return jsonify({'error': 'email missing'}), 400
    password = request.form.get('password')
    if not password or len(password) == 0:
        return jsonify({'error': 'password missing'}), 400
    try:
        user_list = User.search({'email': email})
        for user in user_list:
            if user.is_valid_password(password):
                from api.v1.app import auth
                id_ = auth.create_session(user.id)
                response = jsonify(user.to_json())
                response.set_cookie(getenv('SESSION_NAME'), id_)
                return response
        return jsonify({ "error": "wrong password" }), 401
    except Exception:
        return jsonify({ "error": "no user found for this email" }), 404
