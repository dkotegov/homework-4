# -*- coding: utf-8 -*-

import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from tests.pages.auth import AuthPage


class MessagesTest(unittest.TestCase):
    BROWSER = os.environ.get('BROWSER', 'CHROME')
    LOGIN = unicode(os.environ['LOGIN'], 'utf-8')
    PASSWORD = unicode(os.environ['PASSWORD'], 'utf-8')

    def setUp(self):
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, self.BROWSER)
        )
        auth_page = AuthPage(self.driver)
        auth_page.sign_in(self.LOGIN, self.PASSWORD)

    def tearDown(self):
        self.driver.quit()
