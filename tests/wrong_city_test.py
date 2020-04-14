import os
import unittest
from selenium.webdriver import DesiredCapabilities, Remote

from pages.account import AccountPage
from pages.profile import ProfilePage


class WrongCityTest(unittest.TestCase):
    WRONG_CITY = 'QWERTY'
    CITY_ERROR = 'Проверьте название города'

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
        profile_steps.set_city(self.WRONG_CITY)
        profile_steps.save()

        self.assertEqual(self.CITY_ERROR, profile_steps.city_error())