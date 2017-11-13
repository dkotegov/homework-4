# -*- coding: utf-8 -*-


import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from page import *


class Test(unittest.TestCase):

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def login(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_form = auth_page.form
        auth_form.set_login(USERNAME)
        auth_form.set_password(PASSWORD)
        auth_form.submit()

    def logout(self):
        page = Page(self.driver)
        page.open()
        page.top_menu.open()
        page.top_menu.logout()