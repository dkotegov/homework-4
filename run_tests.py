# -*- coding: utf-8 -*-

import sys
import unittest
from tests.Tests import MyTest

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(MyTest)
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
