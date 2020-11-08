import sys
import unittest

from tests.pages.manage_orders_page import ManageOrderPage
from tests.tests_potapchuk.feedback_tests import FeedbackTest
from tests.tests_potapchuk.map_tests import MapTest
from tests.tests_potapchuk.notification_tests import NotificationTest
from tests.tests_potapchuk.order_approve_tests import OrderApproveTest
from tests.tests_potapchuk.order_history_tests import OrderHistoryTest
from tests.tests_potapchuk.restaurant_tests import RestaurantTest
from tests.tests_potapchuk.support_chat_list_tests import ChatListTest
from tests.tests_yakovidis.authentication import AuthenticationTest
from tests.tests_yakovidis.profile import ProfileTest
from tests.tests_yakovidis.registration import RegistrationTest
from tests.tests_yakovidis.change_address import AddressTest
from tests.tests_yakovidis.main_page import MainPageTest

from tests.tests_postnikov.add_restaurants import AddRestaurantTest
from tests.tests_postnikov.add_rest_point import AddPointTest
from tests.tests_postnikov.add_products import AddProductTest
from tests.tests_postnikov.manage_orders import ManageOrdersTest
from tests.tests_postnikov.rest_tags import ManageRestaurantTagsTest

from tests.tests_potapchuk.support_chat_tests import ChatTest


if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(AuthenticationTest),
        unittest.makeSuite(ProfileTest),
        unittest.makeSuite(RegistrationTest),
        unittest.makeSuite(AddressTest),
        unittest.makeSuite(MainPageTest),

        unittest.makeSuite(AddRestaurantTest),
        unittest.makeSuite(AddPointTest),
        unittest.makeSuite(AddProductTest),
        unittest.makeSuite(ManageRestaurantTagsTest),
        unittest.makeSuite(ManageOrdersTest),

        # unittest.makeSuite(MapTest),

        unittest.makeSuite(NotificationTest),
        unittest.makeSuite(OrderHistoryTest),
        unittest.makeSuite(OrderApproveTest),
        unittest.makeSuite(RestaurantTest),
        unittest.makeSuite(FeedbackTest),
        unittest.makeSuite(ChatTest),
        unittest.makeSuite(ChatListTest),

    ))

    result = unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit(not result.wasSuccessful)
