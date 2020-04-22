# -*- coding: utf-8 -*-

import sys
import unittest
import tests.cases.user_test as signup


if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(signup.Test),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
