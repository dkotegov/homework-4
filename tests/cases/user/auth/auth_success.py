import os
import unittest
from selenium.webdriver import DesiredCapabilities, Remote

from tests.pages.auth_customer import CustomerAuthPage


class AuthTest(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.auth_page = CustomerAuthPage(self.driver)
        self.auth_page.open()
        self.USERNAME = os.environ['USERNAME']
        self.LOGIN = os.environ['LOGIN']
        self.PASSWORD = os.environ['PASSWORD']

    def tearDown(self):
        # todo: logout?
        self.driver.quit()

    def test_auth_success(self):
        self.auth_page.set_login(self.LOGIN)
        self.auth_page.set_password(self.PASSWORD)
        self.auth_page.submit()
        self.auth_page.wait_until_login()
        username = self.auth_page.navbar.get_username()
        self.assertEqual(self.USERNAME, username)

    def test_go_to_sighup_success(self):
        self.auth_page.go_to_registration()
        url = self.driver.current_url
        self.assertEqual(url, "https://delivery-borscht.ru/signup")

    def test_go_to_restaurant_auth_success(self):
        self.auth_page.go_to_restaurant_auth()
        url = self.driver.current_url
        self.assertEqual(url, "https://delivery-borscht.ru/restaurants/signin")
