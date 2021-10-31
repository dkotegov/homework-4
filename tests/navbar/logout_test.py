from pages.main import MainPage
from tests.default_authorized import TestAuthorized


class LogoutTest(TestAuthorized):
    def test(self):
        main_page = MainPage(self.driver)
        main_page.open()
        main_page.click_on_logout()
        self.assertFalse(main_page.check_dropdown())
