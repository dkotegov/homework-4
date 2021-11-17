import unittest

from faker import Faker
from tests.default_setup import default_setup
from tests.steps.auth_user import auth_setup
from tests.pages.chat import ChatPage


class SendMessageFailedTest(unittest.TestCase):
    chat_id = 4
    message_empty = ''

    def setUp(self):
        self.fake = Faker()
        default_setup(self)
        auth_setup(self)
        self.chat_page = ChatPage(self.driver, self.chat_id)
        self.chat_page.open()

    def tearDown(self):
        self.driver.quit()

    def test_send_empty_message_at_click_button(self):
        self.chat_page.set_new_message(self.message_empty)
        self.chat_page.click_submit()
        messages = self.chat_page.get_all_messages()
        self.assertNotIn(self.message_empty, messages)

    def test_send_empty_message_at_enter_button(self):
        self.chat_page.set_new_message(self.message_empty)
        self.chat_page.click_enter()
        messages = self.chat_page.get_all_messages()
        self.assertNotIn(self.message_empty, messages)
