#!/usr/bin/env python3
""" Basic Auth module """
from flask import request
from typing import TypeVar, List
from auth import Auth


class BasicAuth(Auth):
    """ Basic Auth class """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ Extract Base64 method """
        if authorization_header is None:
            return None
