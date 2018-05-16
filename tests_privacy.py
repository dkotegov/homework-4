import unittest

import os

import time
from selenium.webdriver import DesiredCapabilities, Remote

from constants import profiles
from pages.auth_page import AuthPage
from pages.privacy_page import PrivacyPage


class TestsPrivacy(unittest.TestCase):

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test_example(self):
        auth_page = AuthPage(self.driver)
        auth_page.open('')

        auth_page.login(profiles.PROFILE_TECHNOPARK42, profiles.PROFILE_PASSWORD)

        privacy_page = PrivacyPage(self.driver)
        privacy_page.open('/settings/privacy')

        privacy_page.test()

        time.sleep(5)

