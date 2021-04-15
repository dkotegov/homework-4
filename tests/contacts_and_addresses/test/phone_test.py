import os
import time
import unittest
from selenium.webdriver import DesiredCapabilities, Remote

from tests.contacts_and_addresses.src.auth_page import AuthPage
from tests.contacts_and_addresses.src.phone_page import PhonePage


class PhoneTest(unittest.TestCase):
    LOGIN = os.environ['LOGIN']
    PASSWORD = os.environ['PASSWORD']

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')
        # browser = os.environ.get('BROWSER', 'FIREFOX')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_form = auth_page.form
        auth_form.authorize(self.LOGIN, self.PASSWORD)

        auth_page.top_menu.get_username()

        phone_page = PhonePage(self.driver)
        phone_page.open()

        phone_page.form.add_number()

