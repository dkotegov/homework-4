# -*- coding: utf-8 -*-

import sys
import unittest
from tests.cases.user.restaurant_page.add_dish_to_basket import AddDishToBasketTest
from tests.cases.user.auth.auth_success import AuthTest
from tests.cases.user.auth.auth_failed import AuthFailedTest
from tests.cases.restaurant.auth.auth_success import RestaurantAuthTest
from tests.cases.restaurant.auth.auth_failed import RestaurantAuthFailedTest

if __name__ == '__main__':
    suite = unittest.TestSuite((
        # unittest.makeSuite(AddDishToBasketTest),
        unittest.makeSuite(AuthTest),
        unittest.makeSuite(AuthFailedTest),
        unittest.makeSuite(RestaurantAuthTest),
        unittest.makeSuite(RestaurantAuthFailedTest),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
