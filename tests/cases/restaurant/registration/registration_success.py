import os
import unittest

from faker import Faker
from selenium.webdriver import DesiredCapabilities, Remote
from tests.pages.registration_restaurant import RestaurantRegistrationPage


class RestaurantRegistrationTest(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.auth_page = RestaurantRegistrationPage(self.driver)
        self.auth_page.open()
        self.EXISTING_EMAIL = os.environ['USERNAME']
        self.EXISTING_PHONE = os.environ['USERNAME_RESTAURANT']
        self.PASSWORD = '111111'
        self.ADDRESS = 'Испания, Мадрид'
        self.RADIUS = 1

    def tearDown(self):
        self.driver.quit()

    def test_registration_success(self):
        f = Faker()
        self.auth_page.set_email(f.email())
        self.auth_page.set_phone(f.phone_number())
        self.auth_page.set_title(f.name())
        self.auth_page.set_radius(self.RADIUS)
        self.auth_page.set_address(self.ADDRESS)
        self.auth_page.set_password(self.PASSWORD)
        self.auth_page.set_repeat_password(self.PASSWORD)
        self.auth_page.submit()
        self.auth_page.wait_until_registered()
        is_logged = self.auth_page.navbar.check_if_restaurant_logged()
        self.assertEqual(is_logged, True)

    def test_go_to_customer_auth_success(self):
        self.auth_page.go_to_customer_auth()
        url = self.driver.current_url
        self.assertEqual(url, "https://delivery-borscht.ru/signin")

    def test_go_to_restaurant_auth_success(self):
        self.auth_page.go_to_restaurant_auth()
        url = self.driver.current_url
        self.assertEqual(url, "https://delivery-borscht.ru/restaurants/signin")

    # def test_password_quotes_arent_cut(self):
