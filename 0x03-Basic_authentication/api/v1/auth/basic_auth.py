#!/usr/bin/env python3
""" Basic Auth module with inherited class """


from typing import List, Tuple, TypeVar
from models.user import User
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """ Basic Auth class inheriting from Auth base """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ Req check for base64 extraction """

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
                                 str) -> Tuple[str, str]:
        """ Get user credentials if string is correctly formatted """

        if decoded_base64_authorization_header is None:
            return None, None
        if isinstance(decoded_base64_authorization_header, str) is False:
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        return decoded_base64_authorization_header.split(':')

    def user_object_from_credentials(self,
                                     user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """ Create object of user from credential """

        if user_email is None or user_pwd is None:
            return None
        if isinstance(user_email,
                      str) is False or isinstance(user_pwd, str) is False:
            return None

        try:
            user_list = User.search({'email': user_email})
            for user in user_list:
                if user.is_valid_password(user_pwd):
                    return user
        except Exception:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ returns current user from user_db """

        auth = request.headers.get('Authorization')
        header = self.extract_base64_authorization_header(auth)
        header_decoded = self.decode_base64_authorization_header(header)
        return self.user_object_from_credentials(
                self.extract_user_credentials(header_decoded))
