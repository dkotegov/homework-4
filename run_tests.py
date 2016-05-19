# -*- coding: utf-8 -*-

import unittest

from test_names_page import NamesTest

if __name__ == '__main__':
    suite = unittest.TestSuite(unittest.makeSuite(NamesTest))
    unittest.main()
