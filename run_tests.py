# -*- coding: utf-8 -*-

import unittest

from test_currency_page import TestCurrencyPage
from test_picture_day import DayTest
from test_toolbar import ToolbarTestCase

if __name__ == '__main__':
    suite = unittest.TestSuite(unittest.makeSuite(TestCurrencyPage))
    suite2 = unittest.TestSuite(unittest.makeSuite(ToolbarTestCase))
    suite3 = unittest.TestSuite(unittest.makeSuite(DayTest))
    unittest.main()
