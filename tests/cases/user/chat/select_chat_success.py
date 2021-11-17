import unittest

from faker import Faker
from tests.default_setup import default_setup
from tests.steps.auth_user import auth_setup
from tests.pages.chat_list import ChatListPage


class SelectChatSuccessTest(unittest.TestCase):

    def setUp(self):
        default_setup(self)
        auth_setup(self)
        self.chat_list_page = ChatListPage(self.driver)
        self.chat_list_page.open()

    def tearDown(self):
        self.driver.quit()

    def test_select_chat_success(self):
        chats = self.chat_list_page.get_all_chats()
        self.assertLess(0, len(chats))
        self.chat_list_page.click_chat(chats[0])
        self.assertEqual(chats[0], self.chat_list_page.get_restaurant_name())
