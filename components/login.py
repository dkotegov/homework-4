import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from helpers import Component


class Login(Component):
    OUTSIDE = ".auth"

    POPUP = ".auth-content"
    CLOSE_BUTTON = ".auth-content-inner__close"
    TELEPHONE_INPUT = ".auth-content-form__tel"
    PASSWORD_INPUT = ".auth-content-form__password"
    SUBMIT_BUTTON = ".auth-content-form__button"
    REGISTRATION_BUTTON = ".auth-content-form-registration__link"

    LOGIN_BUTTON = ".header-right__account"
    LOGINED = ".header-right-avatar__img"
    LOGOUT_BUTTON = "[data-action = \"logoutClick\"]"
    AUTH_ERROR = "#auth-error"

    def open_auth(self):
        self.helpers.click_element(self.LOGIN_BUTTON)

    def is_opened(self):
        return self.helpers.is_contains(self.POPUP)

    def click_registration(self):
        self.helpers.click_element(self.REGISTRATION_BUTTON)

    def click_close(self):
        self.helpers.click_element(self.CLOSE_BUTTON)

    def click_outside(self):
        self.helpers.wait(until=EC.presence_of_element_located((By.CSS_SELECTOR, self.OUTSIDE)))
        self.driver.execute_script("document.querySelector(\"{}\").click()".format(self.OUTSIDE))

    def is_logined(self):
        self.helpers.wait(until=EC.presence_of_element_located((By.CSS_SELECTOR, self.LOGINED)))
        return self.helpers.is_contains(self.LOGINED)

    def input_telephone_value(self, text):
        self.helpers.clear_input(self.TELEPHONE_INPUT)
        self.helpers.input_value(self.TELEPHONE_INPUT, text)

    def is_error_telephone(self):
        element = self.helpers.get_element(self.TELEPHONE_INPUT)
        return element.get_attribute("validationMessage") is not None

    def input_password_value(self, text):
        self.helpers.clear_input(self.PASSWORD_INPUT)
        self.helpers.input_value(self.PASSWORD_INPUT, text)

    def is_error_password(self):
        element = self.helpers.get_element(self.PASSWORD_INPUT)
        return element.get_attribute("validationMessage") is not None

    def is_error_form(self):
        self.helpers.wait(until=EC.presence_of_element_located((By.CSS_SELECTOR, self.AUTH_ERROR)))
        return self.helpers.is_contains(self.AUTH_ERROR)

    def enter_submit(self):
        self.helpers.click_element(self.SUBMIT_BUTTON)

    def auth(self):
        login = os.environ.get("LOGIN")
        password = os.environ.get("PASSWORD")

        self.open_auth()

        self.input_telephone_value(login)
        self.input_password_value(password)

        self.enter_submit()

        self.helpers.wait(until=EC.presence_of_element_located((By.CSS_SELECTOR, self.LOGINED)))

    def logout(self):
        self.helpers.click_element(self.LOGINED)
        self.helpers.click_element(self.LOGOUT_BUTTON)

        self.helpers.wait(until=EC.presence_of_element_located((By.CSS_SELECTOR, self.LOGIN_BUTTON)))
