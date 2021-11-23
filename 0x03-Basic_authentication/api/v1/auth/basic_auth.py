#!/usr/bin/env python3
""" Basic Auth module """
from flask import request
from typing import TypeVar, List, tuple
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
        if authorization_header.startswith('Basic ') is False:
            return None
        return (authorization_header[6:])

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """ decode base64 encoded string """
        if base64_authorization_header is None:
            return None
        if isinstance(base64_authorization_header, str) is False:
            return None
        try:
            b = base64.b64decode(base64_authorization_header)
            return b.decode("utf-8")
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                 str) -> tuple(str, str):
        """ Get user credentials """
        if decoded_base64_authorization_header is None:
            return None, None
        if isinstance(decoded_base64_authorization_header, str) is False:
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        return decoded_base64_authorization_header.split(':')
