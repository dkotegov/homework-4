from os import environ
from helpers.wait_for_visible import wait_for_visible
from pages.default import DefaultPage, Component


class SignupPage(DefaultPage):
    USER_NAME_HEADER = '#user-full-name'
    BUTTON_BOX_LOGIN = '#login-button'
    LOGIN_LINK = '[href$="/login"]'

    def __init__(self, driver):
        super().__init__(driver, '/signup')
        self.signup_form = SignupForm(self.driver)

    def sign_up(self, login=environ['LOGIN'], email=environ['EMAIL'], password=environ['PASSWORD']):
        self.signup_form.fill_login_input(login)
        self.signup_form.fill_email_input(email)
        self.signup_form.fill_password_input(password)
        self.signup_form.submit()

    @property
    def validation_hint_login(self):
        return self.signup_form.get_validation_hint_login()

    @property
    def validation_hint_email(self):
        return self.signup_form.get_validation_hint_email()

    @property
    def validation_hint_password(self):
        return self.signup_form.get_validation_hint_password()

    def go_to_login_from_form(self):
        wait_for_visible(self.driver, self.BUTTON_BOX_LOGIN)
        self.driver.find_element_by_css_selector(self.BUTTON_BOX_LOGIN).click()

    def go_to_login_from_header(self):
        wait_for_visible(self.driver, self.LOGIN_LINK)
        self.driver.find_element_by_css_selector(self.LOGIN_LINK).click()


class SignupForm(Component):
    LOGIN = 'input[name="username"]'
    EMAIL = 'input[name="email"]'
    PASSWORD = 'input[name="password"]'
    SUBMIT = '#signup-submit'
    VALIDATION_HINT_LOGIN = '#validation-hint-login'
    VALIDATION_HINT_EMAIL = '#validation-hint-email'
    VALIDATION_HINT_PASSWORD = '#validation-hint-password'

    def fill_login_input(self, username):
        wait_for_visible(self.driver, self.LOGIN)
        self.driver.find_element_by_css_selector(self.LOGIN).click()
        self.driver.find_element_by_css_selector(self.LOGIN).send_keys(username)

    def fill_email_input(self, email):
        wait_for_visible(self.driver, self.EMAIL)
        self.driver.find_element_by_css_selector(self.EMAIL).click()
        self.driver.find_element_by_css_selector(self.EMAIL).send_keys(email)

    def fill_password_input(self, password):
        wait_for_visible(self.driver, self.PASSWORD)
        self.driver.find_element_by_css_selector(self.PASSWORD).click()
        self.driver.find_element_by_css_selector(self.PASSWORD).send_keys(password)

    def submit(self):
        wait_for_visible(self.driver, self.SUBMIT)
        self.driver.find_element_by_css_selector(self.SUBMIT).click()

    def get_validation_hint_login(self):
        wait_for_visible(self.driver, self.VALIDATION_HINT_LOGIN)
        return self.driver.find_element_by_css_selector(self.VALIDATION_HINT_LOGIN).text

    def get_validation_hint_email(self):
        wait_for_visible(self.driver, self.VALIDATION_HINT_EMAIL)
        return self.driver.find_element_by_css_selector(self.VALIDATION_HINT_EMAIL).text

    def get_validation_hint_password(self):
        wait_for_visible(self.driver, self.VALIDATION_HINT_PASSWORD)
        return self.driver.find_element_by_css_selector(self.VALIDATION_HINT_PASSWORD).text
