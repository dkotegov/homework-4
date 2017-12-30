import random
import string


class Utils(object):

    @staticmethod
    def random_str(length):
        return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))