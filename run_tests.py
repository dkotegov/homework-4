# -*- coding: utf-8 -*-

from dotenv import load_dotenv
import unittest

from tests import ProductTest, SellerProductsTest, SearchTest, UserProductsTest, \
    HeaderTest, FooterTest, ThemeTest, RegistrationTest, LoginTest, MainTest, \
    UserMessagesTest, UserReviewsTest, UserAwaitReviewsTest, UserFavoritesTest, \
    UserSideBarTest, SellerSideBarTest

if __name__ == '__main__':
    load_dotenv(".env")

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
        unittest.makeSuite(UserMessagesTest),
        unittest.makeSuite(UserReviewsTest),
        unittest.makeSuite(UserAwaitReviewsTest),
        unittest.makeSuite(UserFavoritesTest),
        unittest.makeSuite(UserSideBarTest),
        unittest.makeSuite(SellerSideBarTest),
    ))

    unittest.TextTestRunner().run(suite)
