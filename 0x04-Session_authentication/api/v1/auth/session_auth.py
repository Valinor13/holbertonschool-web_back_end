#!/usr/bin/env python3
""" Session Auth module with inherited class """


from typing import List, Tuple, TypeVar
from models.user import User
from api.v1.auth.auth import Auth
import base64
import uuid


class SessionAuth(Auth):
    """ Session Auth class inheriting from Auth base """

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ Creates a session id and assigns it to the user id """
        if not user_id or not isinstance(user_id, str):
            return None
        self.user_id_by_session_id[str(uuid.uuid4())] = user_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ Getter method for user id based on session id """
        if not session_id or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)
