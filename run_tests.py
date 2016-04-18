#!/usr/bin/env python2

import sys
import unittest

from igor_tests import TopMenuTest
from said_tests import EuroCupsPageTest

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(EuroCupsPageTest),
        unittest.makeSuite(TopMenuTest),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
