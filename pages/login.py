import os

from pages.default import DefaultPage, Component
from helpers.wait_for_visible import wait_for_visible


class LoginPage(DefaultPage):
    def __init__(self, driver):
        super().__init__(driver, '/login')
        self.login_form = LoginForm(self.driver)

    def sign_in(self, login=os.environ['LOGIN'], password=os.environ['PASSWORD']):
        self.login_form.fill_login_input(login)
        self.login_form.fill_password_input(password)
        self.login_form.submit()

    @property
    def username_in_profile(self):
        return self.login_form.get_username_from_profile()

    @property
    def validation_hint(self):
        return self.login_form.get_validation_hint()


class LoginForm(Component):
    LOGIN = 'input[name="username"]'
    PASSWORD = 'input[name="password"]'
    SUBMIT = '#login-submit'
    USER_NAME_HEADER = '#user-full-name'
    VALIDATION_HINT = '#validation-hint-login'

    def fill_login_input(self, username):
        wait_for_visible(self.driver, self.LOGIN)
        self.driver.find_element_by_css_selector(self.LOGIN).click()
        self.driver.find_element_by_css_selector(self.LOGIN).send_keys(username)

    def fill_password_input(self, password):
        wait_for_visible(self.driver, self.PASSWORD)
        self.driver.find_element_by_css_selector(self.PASSWORD).click()
        self.driver.find_element_by_css_selector(self.PASSWORD).send_keys(password)

    def submit(self):
        wait_for_visible(self.driver, self.SUBMIT)
        self.driver.find_element_by_css_selector(self.SUBMIT).click()

    def get_username_from_profile(self):
        wait_for_visible(self.driver, self.USER_NAME_HEADER)
        return self.driver.find_element_by_css_selector(self.USER_NAME_HEADER).text

    def get_validation_hint(self):
        wait_for_visible(self.driver, self.VALIDATION_HINT)
        return self.driver.find_element_by_css_selector(self.VALIDATION_HINT).text
