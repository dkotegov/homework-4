# -*- coding: utf-8 -*-

import unittest
from tests import ProductTest, AllSellerProductsTest, SearchTest

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(ProductTest),
        unittest.makeSuite(AllSellerProductsTest),
        unittest.makeSuite(SearchTest)
    ))

    unittest.TextTestRunner().run(suite)
