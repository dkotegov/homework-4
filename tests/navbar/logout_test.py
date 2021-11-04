import constants
from pages.main import MainPage
from tests.default_authorized import TestAuthorized


class LogoutTest(TestAuthorized):
    def test(self):
        main_page = MainPage(self.driver)
        main_page.open()
        main_page.set_navbar()
        main_page.navbar.click_on_logout()
        main_page.open()
        self.assertTrue(main_page.navbar.is_visible_login())
