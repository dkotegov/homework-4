import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from tests.helpers.database import DatabaseFiller
from tests.pages.auth_page import AuthPage


class BaseTest(unittest.TestCase):
    def setUp(self, auth=None):
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

    def tearDown(self):
        self.driver.quit()

    def create_restaurant(self):
        self.DEFAULT_REST_NAME = self.clear_restaurant.__name__
        self.filler = DatabaseFiller()
        self.filler.admin_auth()
        self.filler.create_restaurant(self.DEFAULT_REST_NAME)
        self.rest_id = self.filler.get_restaurant_id_by_name(
            self.DEFAULT_REST_NAME
        )

    def clear_restaurant(self):
        self.filler.delete_restaurant(self.rest_id)
