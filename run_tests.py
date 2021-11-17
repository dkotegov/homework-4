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
from tests.cases.restaurant.menu.change_section_success import ChangeSectionSuccessTest
from tests.cases.restaurant.menu.change_section_failed import ChangeSectionFailedTest
from tests.cases.restaurant.menu.add_dish_failed import AddDishFailedTest
from tests.cases.restaurant.menu.add_dish_success import AddDishSuccessTest
from tests.cases.restaurant.menu.change_dish_success import ChangeDishSuccessTest
from tests.cases.restaurant.menu.delete_dish_success import DeleteDishSuccessTest
from tests.cases.user.basket.actions_success import ActionsBasketSuccessTest
from tests.cases.user.chat.send_message_success import SendMessageSuccessTest
from tests.cases.user.chat.send_message_failed import SendMessageFailedTest
from tests.cases.user.chat.select_chat_success import SelectChatSuccessTest
from tests.cases.user.ordering.make_order_success import MakeOrderSuccessTest
from tests.cases.user.ordering.make_order_failed import MakeOrderFailedTest
from tests.cases.user.orders.actions_success import ActionsOrdersSuccessTest
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
        # unittest.makeSuite(ChangeUserAvatarSuccessTests),
        # unittest.makeSuite(ChangeRestaurantPhoneFailedTests),
        # unittest.makeSuite(ChangeRestaurantPasswordFailedTests),
        # unittest.makeSuite(ChangeRestaurantEmailFailedTests),
        # unittest.makeSuite(ChangeRestaurantDataSuccessTests),
        # unittest.makeSuite(ChangeRestaurantCostFailedTests),
        # unittest.makeSuite(ChangeSectionSuccessTest),
        # unittest.makeSuite(ChangeSectionFailedTest),
        # unittest.makeSuite(AddDishFailedTest),
        # unittest.makeSuite(AddDishSuccessTest),
        # unittest.makeSuite(ChangeDishSuccessTest),
        # unittest.makeSuite(DeleteDishSuccessTest),
        # unittest.makeSuite(ActionsBasketSuccessTest),
        # unittest.makeSuite(SendMessageSuccessTest),
        # unittest.makeSuite(SendMessageFailedTest),
        # unittest.makeSuite(SelectChatSuccessTest),
        # unittest.makeSuite(MakeOrderSuccessTest),
        # unittest.makeSuite(MakeOrderFailedTest),
        unittest.makeSuite(ActionsOrdersSuccessTest),
    ))

    result = unittest.TextTestRunner().run(suite)
    successfulRes = result.wasSuccessful()
    if not successfulRes:
        sys.exit(not successfulRes)
