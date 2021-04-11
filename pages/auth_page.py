import components
from pages.base_page import BasePage
from components.auth_form import AuthForm


class AuthPage(BasePage):
    PATH = 'auth'

    def __init__(self, driver):
        self.auth_form = AuthForm(driver)
        super(AuthPage, self).__init__(driver, self.auth_form.locators.root)

    def check_open_page(self):
        return self.auth_form.is_open()

    def top_error(self):
        return self.auth_form.top_error()

    def password_error(self, error_text):
        elements = self.auth_form.check_any_error()
        return elements[0].size['width'] == 0 and elements[1].text == error_text

    def email_error(self, error_text):
        elements = self.auth_form.check_any_error()
        return elements[0].text == error_text and elements[1].size['width'] == 0

    def empty_fields(self):
        elements = self.auth_form.check_any_error()
        return elements[0].text == 'Укажите email.' and elements[1].text == 'Укажите пароль.'

    def go_to_reg(self):
        self.auth_form.click_href_reg()

    def is_open(self) -> bool:
        self.auth_form.wait_for_mainpage()
