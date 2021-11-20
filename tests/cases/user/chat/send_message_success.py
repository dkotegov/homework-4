import unittest

from faker import Faker
from tests.default_setup import default_setup
from tests.steps.auth_user import auth_setup
from tests.pages.chat import ChatPage


class SendMessageSuccessTest(unittest.TestCase):
    chat_id = 4
    smiley = "🙃"

    def setUp(self):
        self.fake = Faker()
        default_setup(self)
        auth_setup(self)
        self.chat_page = ChatPage(self.driver, self.chat_id)
        self.chat_page.open()

    def tearDown(self):
        self.driver.quit()

    def test_send_message_at_click_button(self):
        message = self.fake.name()
        self.chat_page.set_new_message(message)
        self.chat_page.click_submit()
        messages = self.chat_page.get_all_messages()
        self.assertIn(message, messages)

    def test_send_message_at_enter_button(self):
        message = self.fake.name()
        self.chat_page.set_new_message(message)
        self.chat_page.click_enter()
        messages = self.chat_page.get_all_messages()
        self.assertIn(message, messages)

    def test_send_message_with_smiley_at_click_button(self):
        message = self.fake.name() + self.smiley
        self.chat_page.set_new_message(message)
        self.chat_page.click_submit()
        messages = self.chat_page.get_all_messages()
        self.assertIn(message, messages)
