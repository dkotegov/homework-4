import os
import unittest

from pages.chat import Chat
from selenium.webdriver import DesiredCapabilities, Remote

from tests.login import LoginTest


class SendEmoji(unittest.TestCase):
    EMOJI = '🍕'

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test(self):
        login_act = LoginTest()
        login_act.driver = self.driver
        login_act.loginBeforeAllTests()

        chat_page = Chat(self.driver)
        chat_page.open()

        chat_contacts = chat_page.contacts
        chat_contacts.go_support()

        chat_messages = chat_page.messages
        chat_messages.open_emoji_menu()
        chat_messages.click_emoji_pizza()
        msg_count = chat_messages.get_msg_count()
        chat_messages.send_msg()
        chat_messages.wait_new_msg(msg_count + 1)
        new_msg = chat_messages.get_last_msg()

        self.assertEqual(new_msg, self.EMOJI)
