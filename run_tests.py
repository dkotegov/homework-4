import sys
import unittest

from anonimazer import tests


def run_tests():
    suite = unittest.TestSuite((
        unittest.makeSuite(tests.TestAnonimazer),
    ))
    result = unittest.TextTestRunner().run(suite)
    if not result.wasSuccessful():
        sys.exit(not result.wasSuccessful())


if __name__ == '__main__':
    run_tests()