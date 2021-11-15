# -*- coding: utf-8 -*-

import sys
import unittest
from tests.cases.user.restaurant_page.add_dish_to_basket import AddDishToBasketTest
from tests.cases.user.auth.auth_success import AuthTest
from tests.cases.user.auth.auth_failed import AuthFailedTest
from tests.cases.restaurant.auth.auth_success import RestaurantAuthTest
from tests.cases.restaurant.auth.auth_failed import RestaurantAuthFailedTest
from tests.cases.user.registration.registration_success import RegistrationTest
from tests.cases.user.registration.registration_failed import RegistrationFailedTest
from tests.cases.restaurant.registration.registration_success import RestaurantRegistrationTest
from tests.cases.restaurant.registration.registration_failed import RestaurantRegistrationFailedTest
from tests.cases.user.main_page.categories_and_filters import CategoriesAndFiltersTest
from tests.cases.user.main_page.navbar import NavbarTest

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(AddDishToBasketTest),
        unittest.makeSuite(AuthTest),
        unittest.makeSuite(AuthFailedTest),
        unittest.makeSuite(RestaurantAuthTest),
        unittest.makeSuite(RestaurantAuthFailedTest),
        unittest.makeSuite(RegistrationTest),
        unittest.makeSuite(RegistrationFailedTest),
        unittest.makeSuite(RestaurantRegistrationTest),
        unittest.makeSuite(RestaurantRegistrationFailedTest),
        unittest.makeSuite(CategoriesAndFiltersTest),
        unittest.makeSuite(NavbarTest)
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
