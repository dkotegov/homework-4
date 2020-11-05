import os
import unittest

from pages.chat import Chat
from selenium.webdriver import DesiredCapabilities, Remote


class OpenChatNoLogin(unittest.TestCase):

    NO_CONTACTS_LABEL = 'Для использования чата необходимо авторизоваться.'

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test(self):

        chat_page = Chat(self.driver)
        chat_page.open()

        chat_contacts = chat_page.contacts

        contacts_html = chat_contacts.get_contacts_html()

        self.assert_(self.NO_CONTACTS_LABEL in contacts_html)
