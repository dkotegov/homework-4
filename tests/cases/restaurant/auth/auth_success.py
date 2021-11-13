import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote
from tests.pages.auth_restaurant import RestaurantAuthPage


class RestaurantAuthTest(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.auth_page = RestaurantAuthPage(self.driver)
        self.auth_page.open()
        self.USERNAME = os.environ['USERNAME_RESTAURANT']
        self.LOGIN = os.environ['LOGIN_RESTAURANT']
        self.PASSWORD = os.environ['PASSWORD']

    def tearDown(self):
        self.driver.quit()

    def test_auth_success(self):
        self.auth_page.set_login(self.LOGIN)
        self.auth_page.set_password(self.PASSWORD)
        self.auth_page.submit()
        self.auth_page.wait_until_login()
        is_logged = self.auth_page.navbar.check_if_restaurant_logged()
        self.assertEqual(is_logged, True)

    def test_go_to_sighup_success(self):
        self.auth_page.go_to_registration()
        url = self.driver.current_url
        self.assertEqual(url, "https://delivery-borscht.ru/restaurants/signup")

    def test_go_to_customer_auth_success(self):
        self.auth_page.go_to_customer_auth()
        url = self.driver.current_url
        self.assertEqual(url, "https://delivery-borscht.ru/signin")

    # def test_password_quotes_arent_cut(self):
