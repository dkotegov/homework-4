import constants
import utils
from pages.main import MainPage
from tests.default_authorized import TestAuthorized


class LogoutTest(TestAuthorized):
    def test(self):
        main_page = MainPage(self.driver)
        main_page.open()
        main_page.set_navbar()
        main_page.navbar.click_on_logout()
        self.assertFalse(main_page.navbar.has_dropdown())
