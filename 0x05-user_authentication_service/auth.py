#!/usr/bin/env python3
""" This module hashes a password and returns it in bytes """
import bcrypt
from sqlalchemy.orm.exc import NoResultFound
from db import DB
from user import User


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Verifies new user to be stored in database prior to auth """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f'User <{email}> already exists')
        except NoResultFound:
            hp = _hash_password(password)
            return self._db.add_user(email, hp)


def _hash_password(password: str) -> bytes:
    """ salt & pepper the hash browns """
    pdub = bytes(password, 'utf-8')
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(pdub, salt)
