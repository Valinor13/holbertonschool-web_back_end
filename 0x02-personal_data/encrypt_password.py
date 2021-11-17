#!/usr/bin/env python3
""" Password encryption module """


import bcrypt


def hash_password(password: str) -> bytes:
    """ Salt & Pepper a hashpass """
    pdub = bytes(password)
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(pdub, salt)
