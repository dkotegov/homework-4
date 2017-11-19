#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import unittest
from like_tests.tests.auth import LoginTest, LogoutTest


if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(LoginTest),
        unittest.makeSuite(LogoutTest)
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
