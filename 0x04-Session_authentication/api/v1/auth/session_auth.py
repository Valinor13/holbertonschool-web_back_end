#!/usr/bin/env python3
""" Session Auth module with inherited class """


from typing import List, Tuple, TypeVar
from models.user import User
from api.v1.auth.auth import Auth
import base64


class SessionAuth(Auth):
    """ Session Auth class inheriting from Auth base """
