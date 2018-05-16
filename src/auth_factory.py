import os

from .auth import Auth


class AuthFactory(object):

    @staticmethod
    def create():
        username = os.environ['LOGIN']
        password = os.environ['PASSWORD']
        return Auth(username=username, password=password)