from random import choice
from string import ascii_letters


def _randomString(length):
    return ''.join(choice(ascii_letters) for _ in range(length))


def _randomMail(length, endsWith=None):
    mail = _randomString(length)
    if endsWith is not None:
        return mail + "@" + endsWith
    return mail + "@" + _randomString(4) + "." + _randomString(3)
