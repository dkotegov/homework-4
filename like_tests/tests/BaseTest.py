# -*- coding: utf-8 -*-

import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote
from like_tests.components.html import AuthPage


class BaseTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser = \
            os.environ.get('BROWSER', 'CHROME')

        cls.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        cls.auth_page = AuthPage(cls.driver)
        cls.auth_page.login()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
