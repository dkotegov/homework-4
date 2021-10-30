import unittest
import sys
from tests.login.login_success_test import LoginSuccessTest


def main():
    suite = unittest.TestSuite((
        unittest.makeSuite(LoginSuccessTest)
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())


if __name__ == '__main__':
    main()
