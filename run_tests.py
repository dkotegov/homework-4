# -*- coding: utf-8 -*-

import unittest
import sys

from test_names_page import NamesTest
from test_calc_page import CalcTest

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(NamesTest),
        unittest.makeSuite(CalcTest),

    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
