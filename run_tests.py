# -*- coding: utf-8 -*-

import unittest
from tests import ProductTest, AllSellerProductsTest

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(ProductTest),
        unittest.makeSuite(AllSellerProductsTest)
    ))

    unittest.TextTestRunner().run(suite)
