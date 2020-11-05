import os
import unittest

from pages.chat import Chat
from selenium.webdriver import DesiredCapabilities, Remote

from tests.login import LoginTest


class SendSticker(unittest.TestCase):
    STICKER_PATH = 'cat_1.png'

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
        chat_messages.open_sticker_menu()
        msg_count = chat_messages.get_msg_count()
        chat_messages.click_first_sticker()
        chat_messages.wait_new_msg(msg_count + 1)
        sticker_path = chat_messages.get_sticker_path()

        self.assertEqual(sticker_path, self.STICKER_PATH)
