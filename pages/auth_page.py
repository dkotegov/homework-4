from pages.base_page import BasePage
from pages.main_page import MainPage

import settings as s


class AuthPage(BasePage):
    PATH = '/auth'
    USERNAME_INPUT = 'input[name="username"]'
    PASSWORD_INPUT = 'input[name="password"]'
    LOGIN_BTN = 'input[type="submit"]'
    USERNAME_ERROR = '#usernameErrorText'
    PASSWORD_ERROR = '#passwordErrorText'
    SIGNUP_BTN = 'div.muted > linkbutton'

    def __init__(self, driver):
        super().__init__(driver, 'div.auth')

    def auth(self):
        self.open()
        self.set_username()
        self.set_password()
        self.click_login_btn()

        # we need to wait for login to succeed
        main_page = MainPage(self.driver)
        return main_page.get_authenticated_user_email()

    def set_username(self, username=s.USERNAME):
        el = self.locate_el(self.USERNAME_INPUT)
        el.clear()
        el.send_keys(username)

    def set_password(self, password=s.PASSWORD):
        el = self.locate_el(self.PASSWORD_INPUT)
        el.clear()
        el.send_keys(password)

    def get_username_error(self):
        return self.locate_el(self.USERNAME_ERROR).text

    def get_password_error(self):
        return self.locate_el(self.PASSWORD_ERROR).text

    def click_login_btn(self):
        self.locate_el(self.LOGIN_BTN).click()

    def click_signup_btn(self):
        self.locate_el(self.SIGNUP_BTN).click()
