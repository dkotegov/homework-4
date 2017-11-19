# -*- coding: utf-8 -*-


import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote
from like_tests.elements.user.pages import UserPage


class LoginTest(unittest.TestCase):
    USERNAME = u'Имярек Человекович'

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test(self):
        user_name = UserPage(self.driver).login()
        self.assertEqual(self.USERNAME, user_name)
