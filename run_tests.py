# -*- coding: utf-8 -*-

import sys
import unittest
import tests.cases.user_test as signup
from tests.cases import auth_test

if __name__ == '__main__':
    suite = unittest.TestSuite((
        # unittest.makeSuite(signup.Test),
        unittest.makeSuite(auth_test.AuthTest),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
