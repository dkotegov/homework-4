import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote
from tests.pages.main import MainPage


class NavbarTest(unittest.TestCase):
    EXISTING_ADDRESS = 'Россия, Москва, улица Ильинка'
    EXISTING_ADDRESS_UPPERCASE = 'Россия, Москва, улица Ильинка'

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.main_page = MainPage(self.driver)
        self.main_page.open()

    def tearDown(self):
        self.driver.quit()

    def test_successful_choosing_address(self):
        self.main_page.address_popup.close_popup()
        self.main_page.navbar.click_address()
        self.main_page.address_popup.set_address(self.EXISTING_ADDRESS)
        self.main_page.address_popup.submit()
        self.main_page.wait_restaurants_displayed()
        is_restaurants_displayed = self.main_page.check_if_restaurants_displayed()
        self.assertEqual(is_restaurants_displayed, True)

    def test_successful_choosing_address_in_uppercase(self):
        self.main_page.address_popup.close_popup()
        self.main_page.navbar.click_address()
        self.main_page.address_popup.set_address(self.EXISTING_ADDRESS_UPPERCASE)
        self.main_page.address_popup.submit()
        self.main_page.wait_restaurants_displayed()
        is_restaurants_displayed = self.main_page.check_if_restaurants_displayed()
        self.assertEqual(is_restaurants_displayed, True)
