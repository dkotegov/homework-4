import sys
import unittest

from tests.test_settings import TestsAddApp

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(TestsAddApp),
    ))
    result = unittest.TextTestRunner(failfast=True).run(suite)
    sys.exit(not result.wasSuccessful())
