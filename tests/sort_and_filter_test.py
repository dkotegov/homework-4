import os
import unittest

import utils
from Auth import AuthPage
from Home import HomePage


class SortAndFilterTest(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')
        self.driver = utils.get_remote_driver(browser)

        LOGIN = 'alexersh.testing'
        PASSWORD = os.environ['PASSWORD']

        auth_page = AuthPage(self.driver)
        auth_page.auth(LOGIN, PASSWORD)

    def tearDown(self):
        self.driver.quit()

    def test_buttons(self):
        home_page = HomePage(self.driver)
        home_page.open()

        home_page.utils.close_banner_if_exists()
        home_page.buttons.change_view()

        home_page.buttons.sort_by_alphabet()
        home_page.buttons.sort_by_size()
        home_page.buttons.sort_by_date()

        home_page.buttons.filter_by_image()
        home_page.buttons.filter_by_all()