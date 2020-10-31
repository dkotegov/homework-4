import sys
import unittest
from tests.tests_postnikov.test import FirstTest


if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(FirstTest)
    ))

    result = unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit(not result.wasSuccessful)
