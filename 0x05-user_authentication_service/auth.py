#!/usr/bin/env python3
""" This module hashes a password and returns it in bytes """
import bcrypt


def _hash_password(password: str) -> bytes:
    """ salt & pepper the hash browns """
    pdub = bytes(password, 'utf-8')
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(pdub, salt)
