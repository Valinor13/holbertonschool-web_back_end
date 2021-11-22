#!/usr/bin/env python3
""" Basic Auth module """
from flask import request
from typing import TypeVar, List
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """ Basic Auth class """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ Extract Base64 method """
        if authorization_header is None:
            return None
        if isinstance(authorization_header, str) is False:
            return None
        auth_str = base64.b64decode(authorization_header)
        if auth_str.startswith('Basic ') is False:
            return None
        return (auth_str[5:])
