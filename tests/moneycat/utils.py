import os
from testutils import SeleniumTest

from .pages.auth import AuthPage
from .pages.main import MainPage


class TestCase(SeleniumTest):
    def setUp(self):
        super().setUp()
        account = AuthPage(self.driver)
        account.open()
        login_form = account.form
        account.Actions.sign_in(login_form, os.environ.get("LOGIN"), os.environ.get("PASS"))
        MainPage(self.driver).currency_list.wait_self()

    def tearDown(self) -> None:
        self.driver.quit()
