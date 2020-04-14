import os
import unittest
from selenium.webdriver import DesiredCapabilities, Remote

from pages.account import AccountPage
from pages.profile import ProfilePage


class AutoCompleteCityTest(unittest.TestCase):
    CITY_PREFIX = 'Сан'
    SUGGESTION = 'Санок, Польша'

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test(self):
        driver = self.driver
        auth_page = AccountPage(driver)
        auth_page.open()
        auth_page.auth()

        profile_page = ProfilePage(driver)
        profile_page.open()
        profile_steps = profile_page.steps

        profile_steps.set_city(self.CITY_PREFIX)
        profile_steps.suggest_city()
        profile_steps.save()
        self.assertEqual(self.SUGGESTION, profile_steps.get_city())