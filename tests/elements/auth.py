from selenium.webdriver.common.by import By

from base import BaseElement


class LoginForm(BaseElement):
    SUBMIT_BUTTON = (By.XPATH, '//input[@data-l="t,loginButton"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@name="st.password"]')
    LOGIN_INPUT = (By.XPATH, '//input[@name="st.email"]')

    def __init__(self, driver):
        super(LoginForm, self).__init__(driver)

        self.locator = None

    def login_input(self):
        self.locator = self.LOGIN_INPUT
        return self

    def password_input(self):
        self.locator = self.PASSWORD_INPUT
        return self

    def submit_button(self):
        self.locator = self.SUBMIT_BUTTON
        return self
