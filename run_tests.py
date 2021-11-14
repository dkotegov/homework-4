# -*- coding: utf-8 -*-

import sys
import unittest
from tests.cases.user.restaurant.add_dish_success import AddDishToBasketSuccessTest
from tests.cases.user.restaurant.condition_success import ConditionSuccessTest
from tests.cases.user.profile.change_password_failed import ChangeUserPasswordFailedTests
from tests.cases.user.profile.change_name_failed import ChangeUserNameFailedTests
from tests.cases.user.profile.change_email_failed import ChangeUserEmailFailedTests
from tests.cases.user.profile.change_phone_failed import ChangeUserPhoneFailedTests
from tests.cases.user.profile.change_data_success import ChangeUserDataSuccessTests
from tests.cases.user.profile.change_avatar_success import ChangeUserAvatarSuccessTests
from tests.cases.restaurant.profile.change_password_failed import ChangeRestaurantPasswordFailedTests
from tests.cases.restaurant.profile.change_cost_failed import ChangeRestaurantCostFailedTests
from tests.cases.restaurant.profile.change_email_failed import ChangeRestaurantEmailFailedTests
from tests.cases.restaurant.profile.change_phone_failed import ChangeRestaurantPhoneFailedTests
from tests.cases.restaurant.profile.change_data_success import ChangeRestaurantDataSuccessTests
from tests.cases.user.auth.auth_success import AuthTest

if __name__ == '__main__':
    suite = unittest.TestSuite((
        # unittest.makeSuite(AddDishToBasketSuccessTest),
        # unittest.makeSuite(ConditionSuccessTest),
        # unittest.makeSuite(AuthTest),
        # unittest.makeSuite(ChangeUserPasswordFailedTests),
        # unittest.makeSuite(ChangeUserNameFailedTests),
        # unittest.makeSuite(ChangeUserEmailFailedTests),
        # unittest.makeSuite(ChangeUserPhoneFailedTests),
        # unittest.makeSuite(ChangeUserDataSuccessTests),
        unittest.makeSuite(ChangeUserAvatarSuccessTests),
        # unittest.makeSuite(ChangeRestaurantPhoneFailedTests),
        # unittest.makeSuite(ChangeRestaurantPasswordFailedTests),
        # unittest.makeSuite(ChangeRestaurantEmailFailedTests),
        # unittest.makeSuite(ChangeRestaurantDataSuccessTests),
        # unittest.makeSuite(ChangeRestaurantCostFailedTests),
    ))

    result = unittest.TextTestRunner().run(suite)
    successfulRes = result.wasSuccessful()
    if not successfulRes:
        sys.exit(not successfulRes)
