# -*- coding: utf-8 -*-

import unittest
from tests import ProductTest, SellerProductsTest, SearchTest, UserProductsTest, \
    HeaderTest, FooterTest, ThemeTest, RegistrationTest, LoginTest, MainTest, FavoritesTest, \
    MessagesTest, AwaitReviewsTest, ReviewsTest

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(ProductTest),
        unittest.makeSuite(SellerProductsTest),
        unittest.makeSuite(SearchTest),
        unittest.makeSuite(UserProductsTest),
        unittest.makeSuite(HeaderTest),
        unittest.makeSuite(FooterTest),
        unittest.makeSuite(ThemeTest),
        unittest.makeSuite(RegistrationTest),
        unittest.makeSuite(LoginTest),
        unittest.makeSuite(MainTest),
        unittest.makeSuite(FavoritesTest),
        unittest.makeSuite(MessagesTest),
        unittest.makeSuite(ReviewsTest),
        unittest.makeSuite(AwaitReviewsTest)
    ))

    unittest.TextTestRunner().run(suite)
