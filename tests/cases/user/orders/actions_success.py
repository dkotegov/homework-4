import unittest

from tests.default_setup import default_setup
from tests.pages.user.orders import OrdersPage
from tests.pages.chat import ChatPage
from tests.steps.auth_user import auth_setup


class ActionsOrdersSuccessTest(unittest.TestCase):

    def setUp(self):
        default_setup(self)
        auth_setup(self)
        self.orders_page = OrdersPage(self.driver)
        self.chat_page = ChatPage(self.driver, 1)
        self.orders_page.open()

    def tearDown(self):
        self.driver.quit()

    def test_go_to_chat_success(self):
        restaurant_name = self.orders_page.get_first_restaurant_name()
        self.orders_page.click_first_restaurant_go_to_chat()
        self.assertEqual(restaurant_name, self.chat_page.get_restaurant_name())
