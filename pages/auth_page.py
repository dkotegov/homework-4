import components
from pages.base_page import BasePage
from components.auth_form import AuthForm


class AuthPage(BasePage):
    PATH = 'auth'

    def __init__(self, driver):
        self.resume_create_form = AuthForm(driver)
        super(AuthPage, self).__init__(driver, self.resume_create_form.ROOT)

    @property
    def form(self) -> components.auth_form:
        return AuthForm(self.driver)
