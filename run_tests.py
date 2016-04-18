# -*- coding: utf-8 -*-

import unittest

from test_currency_page import TestCurrencyPage

if __name__ == '__main__':
    # suite = unittest.TestSuite((unittest.makeSuite(UploadAnySizes),))
    # result = unittest.TextTestRunner().run(suite)
    # sys.exit(not result.wasSuccessful())
    suite = unittest.TestSuite(unittest.makeSuite(TestCurrencyPage))
    unittest.main()
