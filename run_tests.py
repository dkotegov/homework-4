import unittest
import sys
from tests.login import LoginTestSuite


def main():
    suite = unittest.TestSuite((
        unittest.makeSuite(LoginTestSuite)
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())


if __name__ == '__main__':
    main()
