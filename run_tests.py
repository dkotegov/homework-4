# -*- coding: utf-8 -*-

import sys
import unittest
from tests.cases.user.restaurant_page.add_dish_to_basket import AddDishToBasketTest
from tests.cases.user.auth.auth_success import AuthTest
from tests.cases.user.auth.auth_failed import AuthFailedTest

if __name__ == '__main__':
    suite = unittest.TestSuite((
        # unittest.makeSuite(AddDishToBasketTest),
        unittest.makeSuite(AuthTest),
        unittest.makeSuite(AuthFailedTest),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
