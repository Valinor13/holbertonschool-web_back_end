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

    def destroy_session(self, request=None):
        """ Deletes session id from dictionary """
        if not request or not self.session_cookie(request):
            return False
        id_ = self.session_cookie(request)
        if not self.user_id_for_session_id(id_):
            return False
        del self.user_id_by_session_id[id_]
        return True

    def create_session(self, user_id: str = None) -> str:
        """ Creates a session id and assigns it to the user id """
        if not user_id or not isinstance(user_id, str):
            return None
        id_ = str(uuid.uuid4())
        self.user_id_by_session_id[id_] = user_id
        return id_

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ Getter method for user id based on session id """
        if not session_id or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None) -> TypeVar('User'):
        """ Returns user object based on session id """
        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)
        return User.get(user_id)
