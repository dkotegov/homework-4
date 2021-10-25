# -*- coding: utf-8 -*-

import unittest
from tests import ProductTest, AllSellerProductsTest, SearchTest, UserProductsTest

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(ProductTest),
        unittest.makeSuite(AllSellerProductsTest),
        unittest.makeSuite(SearchTest),
        unittest.makeSuite(UserProductsTest)
    ))

    unittest.TextTestRunner().run(suite)
