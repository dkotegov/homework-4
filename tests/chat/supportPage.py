import os
import unittest

from pages.chat import Chat
from selenium.webdriver import DesiredCapabilities, Remote

from tests.login import LoginTest


class OpenSupportPage(unittest.TestCase):
    SUPPORT_NAME = 'Support'

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

        messages_window = chat_page.messages
        chat_with_name = messages_window.get_companion_name()

        self.assertEqual(chat_with_name, self.SUPPORT_NAME)
