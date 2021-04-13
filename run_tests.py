#!/usr/bin/env python2

import sys
import unittest
from tests.auth_tests import AuthTests
from tests.setting_test import SettingsTests
from tests.signup_tests import SignupTests
from tests.subscribe_tests import SubscribeTests


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(AuthTests))
    suite.addTest(unittest.makeSuite(SettingsTests))
    suite.addTest(unittest.makeSuite(SignupTests))
    suite.addTest(unittest.makeSuite(SubscribeTests))
    result = unittest.TextTestRunner().run(suite)
    successfulRes = result.wasSuccessful()
    if not successfulRes:
        sys.exit(not successfulRes)
