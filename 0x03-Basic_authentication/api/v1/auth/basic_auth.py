#!/usr/bin/env python3
""" Basic Auth module
"""
from flask import request
from typing import TypeVar, List
from auth import Auth


class BasicAuth(Auth):
    """ Basic Auth class
    """
