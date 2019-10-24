import sys
import unittest

from tests.test_auth import TestAuth


def run_tests():
    suite = unittest.TestSuite((
        unittest.makeSuite(TestAuth),
    ))
    result = unittest.TextTestRunner().run(suite)
    if not result.wasSuccessful():
        sys.exit(not result.wasSuccessful())


if __name__ == '__main__':
    run_tests()
