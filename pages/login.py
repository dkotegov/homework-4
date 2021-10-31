from os import environ
from pages.default import DefaultPage, Component
from helpers.wait_for_visible import wait_for_visible


class LoginPage(DefaultPage):
    USER_NAME_HEADER = '#user-full-name'
    BUTTON_BOX_SIGNUP = '#signup-button'
    SIGNUP_LINK = '[href$="/signup"]'

    def __init__(self, driver):
        super().__init__(driver, '/login')
        self.login_form = LoginForm(self.driver)

    def sign_in(self, login=environ['LOGIN'], password=environ['PASSWORD']):
        self.login_form.fill_login_input(login)
        self.login_form.fill_password_input(password)
        self.login_form.submit()

    @property
    def validation_hint(self):
        return self.login_form.get_validation_hint()

    def get_username_from_profile(self):
        wait_for_visible(self.driver, self.USER_NAME_HEADER)
        return self.driver.find_element_by_css_selector(self.USER_NAME_HEADER).text

    def go_to_signup_from_form(self):
        wait_for_visible(self.driver, self.BUTTON_BOX_SIGNUP)
        self.driver.find_element_by_css_selector(self.BUTTON_BOX_SIGNUP).click()

    def go_to_signup_from_header(self):
        wait_for_visible(self.driver, self.SIGNUP_LINK)
        self.driver.find_element_by_css_selector(self.SIGNUP_LINK).click()


class LoginForm(Component):
    LOGIN = 'input[name="username"]'
    PASSWORD = 'input[name="password"]'
    SUBMIT = '#login-submit'
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

    def get_validation_hint(self):
        wait_for_visible(self.driver, self.VALIDATION_HINT)
        return self.driver.find_element_by_css_selector(self.VALIDATION_HINT).text
