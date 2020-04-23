# -*- coding: utf-8 -*-

import sys
import unittest

from tests.cases import board_test
from tests.cases import pin_test

if __name__ == '__main__':
    suite = unittest.TestSuite((
        # unittest.makeSuite(signup.Test),
        unittest.makeSuite(pin_test.Test),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
