# -*- coding: utf-8 -*-

import unittest

from test_names_page import NamesTest
from test_calc_page import CalcTest

if __name__ == '__main__':
    suite = unittest.TestSuite(unittest.makeSuite(NamesTest))
    suite2 = unittest.TestSuite(unittest.makeSuite(CalcTest))
    unittest.main()
