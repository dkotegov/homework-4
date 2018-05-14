import unittest

import os
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities, Remote

from auth.auth import AuthPage


class Tests(unittest.TestCase):
    PROFILE_ONE_LOGIN = 'technopark43'
    PROFILE_PASSWORD = os.environ['PROFILE_PASSWORD']
    print(os.environ.get('PROFILE_PASSWORD'))
    PROFILE_SECOND_LOGIN = 'technopark46'

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test_add_profile_to_black_list(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = auth_page.form
        auth_form.full_auth(self.PROFILE_ONE_LOGIN, self.PROFILE_PASSWORD)