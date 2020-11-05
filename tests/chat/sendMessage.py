import os
import unittest

from pages.chat import Chat
from selenium.webdriver import DesiredCapabilities, Remote

from tests.login import LoginTest


class SendMessage(unittest.TestCase):

    MSG = 'Hello'

    MSG_10_CHAR = '0123456789'

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

        # self.MSG = self.MSG_10_CHAR * 60  # for test 50 and 150 msg char

        chat_messages = chat_page.messages
        chat_messages.set_msg(self.MSG)
        chat_messages.send_msg()
        chat_messages.wait_new_msg()
        new_msg = chat_messages.get_last_msg()

        self.assertEqual(new_msg, self.MSG)

        date_and_time_last_msg = chat_messages.get_last_msg()
        time = date_and_time_last_msg.split(' ')

        self.assert_(len(time) < 4, 'not enough numbers for date')  # replace '<' to '>' for true test

