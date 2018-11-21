#!/usr/bin/python

from os import environ


ENV_LOGIN = "LOGIN"
ENV_PASSWORD = "PASSWORD"
ENV_BROWSER = "BROWSER"

CHROME_NAME = "CHROME"
FIREFOX_NAME = "FIREFOX"
ENV_BROWSER_EXPECTED = (CHROME_NAME, FIREFOX_NAME)


class EnvKeyNotFound(Exception):
    def __init__(self, key_name):
        message = "Key '{}' not found in environment".format(key_name)
        super(EnvKeyNotFound, self).__init__(message)


class EnvValueUnexpected(Exception):
    def __init__(self, key_name, value_name):
        message = "Value {v} by key '{k}' is unexpected".format(k=key_name, v=value_name)
        super(EnvValueUnexpected, self).__init__(message)


def get_credentials():
    if ENV_LOGIN not in environ:
        raise EnvKeyNotFound(ENV_LOGIN)
    if ENV_PASSWORD not in environ:
        raise EnvKeyNotFound(ENV_PASSWORD)
    
    return environ[ENV_LOGIN], environ[ENV_PASSWORD]


def get_browser_name():
    if ENV_BROWSER not in environ:
        raise EnvKeyNotFound(ENV_BROWSER)

    browser_name = environ[ENV_BROWSER]

    if browser_name not in ENV_BROWSER_EXPECTED:
        raise EnvValueUnexpected(ENV_BROWSER, browser_name)
    
    return browser_name
    

