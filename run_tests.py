# -*- coding: utf-8 -*-

import sys
import unittest
from tests.shop_tests import ShopTests

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(ShopTests),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
