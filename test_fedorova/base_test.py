# -*- coding: utf-8 -*-

import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from page import AuthPage, GroupsPage

LOGIN = os.environ['LOGIN']
PASSWORD = os.environ['PASSWORD']

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
        auth_form.set_login('technopark36')
        auth_form.set_password('testQA1')
        auth_form.submit()
	groups_page = GroupsPage(self.driver)		
	groups_page.open()

    def tearDown(self):
        self.driver.quit()

