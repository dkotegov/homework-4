import unittest
import sys
from tests.login import LoginTestSuite
from tests.signup import SignupTestSuite


def main():
    suite = unittest.TestSuite((
        unittest.makeSuite(LoginTestSuite),
        unittest.makeSuite(SignupTestSuite)
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())


if __name__ == '__main__':
    main()
