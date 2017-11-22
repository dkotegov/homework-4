from selenium.webdriver.common.by import By

from base import BaseElement


class LoginForm(BaseElement):
    SUBMIT_BUTTON = '//input[@data-l="t,loginButton"]'
    PASSWORD_INPUT = '//input[@name="st.password"]'
    LOGIN_INPUT = '//input[@name="st.email"]'

    def __init__(self, driver):
        super(LoginForm, self).__init__(driver)

        self.locator = None

    def login_input(self):
        self.locator = (By.XPATH, self.LOGIN_INPUT)
        return self

    def password_input(self):
        self.locator = (By.XPATH, self.PASSWORD_INPUT)
        return self

    def submit_button(self):
        self.locator = (By.XPATH, self.SUBMIT_BUTTON)
        return self
