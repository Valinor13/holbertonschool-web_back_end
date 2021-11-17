#!/usr/bin/env python3
""" Password encryption module """


import bcrypt


def hash_password(password: str) -> bytes:
    """ Salt & Pepper a hashpass """
    pdub = bytes(password, 'ascii')
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(pdub, salt)


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Checks Seasoning """
    if bcrypt.checkpw(bytes(password, 'ascii'), hashed_password):
        return True
    return False
