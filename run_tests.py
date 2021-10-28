# -*- coding: utf-8 -*-

import unittest
from tests import ProductTest, AllSellerProductsTest, SearchTest, UserProductsTest, HeaderTest, FooterTest, ThemeTest

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(ProductTest),
        unittest.makeSuite(AllSellerProductsTest),
        unittest.makeSuite(SearchTest),
        unittest.makeSuite(UserProductsTest),
        unittest.makeSuite(HeaderTest),
        unittest.makeSuite(FooterTest),
        unittest.makeSuite(ThemeTest)
    ))

    unittest.TextTestRunner().run(suite)
