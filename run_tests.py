# -*- coding: utf-8 -*-

import sys
import unittest
from tests.car_showrooms.search_showroom_tests import ExampleTest

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(ExampleTest),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
