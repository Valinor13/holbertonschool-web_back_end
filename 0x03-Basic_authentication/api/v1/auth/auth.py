#!/usr/bin/env python3
""" Auth module
"""
from flask import request
from typing import TypeVar, List


TIMESTAMP_FORMAT = "%Y-%m-%dT%H:%M:%S"
DATA = {}


class Auth():
    """ Auth class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Require authentication check """
        return False

    def authorization_header(self, request=None) -> str:
        """ Authorized header req check """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Returns current user """
        return None
