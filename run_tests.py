# -*- coding: utf-8 -*-

import sys
import unittest
# from tests.cases.user.restaurant_page.add_dish_to_basket import AddDishToBasketTest
from tests.cases.user.profile.change_password_failed import ChangePasswordFailedTests
from tests.cases.user.profile.change_name_failed import ChangeNameFailedTests
from tests.cases.user.profile.change_email_failed import ChangeEmailFailedTests
from tests.cases.user.profile.change_phone_failed import ChangePhoneFailedTests
from tests.cases.user.profile.change_data_success import ChangeDataSuccessTests
from tests.cases.user.auth.auth_success import AuthTest

if __name__ == '__main__':
    suite = unittest.TestSuite((
        # unittest.makeSuite(AddDishToBasketTest),
        # unittest.makeSuite(AuthTest),
        # unittest.makeSuite(ChangePasswordFailedTests),
        # unittest.makeSuite(ChangeNameFailedTests),
        # unittest.makeSuite(ChangeEmailFailedTests),
        # unittest.makeSuite(ChangePhoneFailedTests),
        unittest.makeSuite(ChangeDataSuccessTests),
    ))

    result = unittest.TextTestRunner().run(suite)
    successfulRes = result.wasSuccessful()
    if not successfulRes:
        sys.exit(not successfulRes)
