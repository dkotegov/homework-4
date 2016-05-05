# -*- coding: utf-8 -*-

import unittest

from test_cases import main_page_test_case
from test_cases import obraz_sna_test_case

if __name__ == '__main__':
    pass

loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(main_page_test_case))
suite.addTests(loader.loadTestsFromModule(obraz_sna_test_case))

unittest.TextTestRunner().run(suite)

