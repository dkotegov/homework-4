import sys
import unittest
from tests.userinfo_test import UserinfoTest


if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(UserinfoTest),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())