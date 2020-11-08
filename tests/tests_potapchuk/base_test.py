import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from tests.helpers.database import DatabaseFiller
from tests.pages.address_page import AddressPage
from tests.pages.auth_page import AuthPage
from tests.pages.order_page import OrderPage
from tests.pages.restaurant_page import RestaurantPage


class BaseTest(unittest.TestCase):
    DEFAULT_REST_NAME = 'default====-+'
    DEFAULT_PROD_NAME = 'product%s'
    DEFAULT_PROD_PRICE = 100

    def setUp(self, auth=None, with_address=False):
        super().__init__()

        if not hasattr(self, 'driver'):
            browser = os.environ.get('BROWSER', 'CHROME')
            self.driver = Remote(
                command_executor='http://127.0.0.1:4444/wd/hub',
                desired_capabilities=getattr(DesiredCapabilities, browser).copy()
            )

        if auth == 'user':
            self.login = os.environ.get('LOGIN')
            self.password = os.environ.get('PASSWORD')
        elif auth == 'admin':
            self.login = os.environ.get('ADMIN_LOGIN')
            self.password = os.environ.get('ADMIN_PASSWORD')
        elif auth == 'support':
            self.login = os.environ.get('SUP_LOGIN')
            self.password = os.environ.get('SUP_PASSWORD')

        if auth is not None:
            auth_page = AuthPage(self.driver)
            auth_page.open()
            auth_page.wait_open()
            auth_page.auth(self.login, self.password)
            self.isAuthenticated = True

        if with_address:
            address_page = AddressPage(self.driver)
            address_page.open()
            address_page.start_address(DatabaseFiller().ADDRESS)

    def tearDown(self):
        self.driver.quit()

    def create_restaurant(self):
        self.filler = DatabaseFiller()
        self.filler.admin_auth()
        self.filler.create_restaurant(self.DEFAULT_REST_NAME)
        self.rest_id = self.filler.get_restaurant_id_by_name(
            self.DEFAULT_REST_NAME
        )

    def create_restaurant_with_products(self, prod_num):
        self.prod_num = prod_num
        self.create_restaurant()

        for i in range(prod_num):
            self.filler.create_product(
                self.rest_id,
                self.DEFAULT_PROD_NAME % i,
                self.DEFAULT_PROD_PRICE,
            )

    def clear_restaurant(self):
        self.filler.delete_restaurant(self.rest_id)

    def order_product(self, rest_id):
        rest = RestaurantPage(self.driver, rest_id, 1)
        rest.open()
        rest.wait_visible()
        rest.add_product(0)

    def checkout_order(self, rest_id):
        self.order_product(rest_id)

        order = OrderPage(self.driver)
        order.open()
        order.wait_visible()
        order.click_checkout_button()
