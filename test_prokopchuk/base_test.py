# -*- coding: utf-8 -*-

import os
import unittest

from test_prokopchuk.page import AuthPage, GroupsPage
from selenium.webdriver import DesiredCapabilities, Remote

LOGIN = 'technopark27'
PASSWORD = 'testQA1'


class BaseTest(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.driver.implicitly_wait(5)
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = auth_page.form
        auth_form.set_login(LOGIN)
        auth_form.set_password(PASSWORD)
        auth_form.submit()
        GroupsPage(self.driver).open()

    def tearDown(self):
        self.driver.quit()
