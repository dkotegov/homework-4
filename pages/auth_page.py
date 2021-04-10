import components
from pages.base_page import BasePage
from components.auth_form import AuthForm


class AuthPage(BasePage):
    PATH = 'auth'

    def __init__(self, driver):
        self.auth_form = AuthForm(self.driver)
        super(AuthPage, self).__init__(driver, self.auth_form.locators.root)

    def check_open_page(self):
        return self.auth_form.is_open()

