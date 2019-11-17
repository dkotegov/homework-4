import sys
import unittest
from tests.userinfo_test import UserInfoTest


if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(UserInfoTest),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())

