#!/usr/bin/env python2

import sys
import unittest
from tests.example_test import ExampleTest
from tests.setting_test import PasswordChangeTest


if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(ExampleTest),
        unittest.makeSuite(PasswordChangeTest),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
