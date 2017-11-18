#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import unittest
from like_tests.tests.LoginTest import LoginTest


if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(LoginTest),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
