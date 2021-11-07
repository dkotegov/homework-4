# -*- coding: utf-8 -*-

from dotenv import load_dotenv
import unittest

from tests import ProductTest, SellerProductsTest, SearchTest, RegistrationTest, MainTest, \
    ReviewsTest, UserFavoritesTest, UserSettingsTest, CreateProductTest

if __name__ == '__main__':
    load_dotenv(".env")

    suite = unittest.TestSuite((
        unittest.makeSuite(ProductTest),
        unittest.makeSuite(SellerProductsTest),
        unittest.makeSuite(SearchTest),
        unittest.makeSuite(RegistrationTest),
        unittest.makeSuite(MainTest),
        unittest.makeSuite(ReviewsTest),
        unittest.makeSuite(UserFavoritesTest),
        unittest.makeSuite(UserSettingsTest),
        unittest.makeSuite(CreateProductTest),
    ))

    unittest.TextTestRunner().run(suite)
