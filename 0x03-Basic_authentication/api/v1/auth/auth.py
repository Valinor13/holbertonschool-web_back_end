#!/usr/bin/env python3
""" Auth module
"""
from flask import request
from typing import TypeVar, List


class Auth():
    """ Auth class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Require authentication check """
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        for item in excluded_paths:
            if path in item or (path + '/') in item:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """ Authorized header req check """
        if request is None:
            return None
        if not request.headers.get('Authorization'):
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """ Returns current user """
        return None
