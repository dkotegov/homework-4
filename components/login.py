from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from helpers import Component


class Login(Component):
    OUTSIDE = ".auth"
    POPUP = ".auth-content"
    TITLE = ".auth-content-inner__title"
    LOGIN = ".auth-content-form__tel"
    PASSWORD = ".auth-content-form__password"
    SUBMIT = ".auth-content-form__button"
    REGISTRATION_BUTTON = ".auth-content-form-registration__link"
    CLOSE_BUTTON = ".auth-content-inner__close"

    LOGIN_BUTTON = ".header-right__account"
    LOGINED = ".header-right-avatar__img"
    LOGOUT = "[data-action = \"logoutClick\"]"
    AUTH_ERROR = "#auth-error"

    def click_registration(self):
        self.helpers.click_button(self.REGISTRATION_BUTTON)

    def click_close(self):
        self.helpers.click_button(self.CLOSE_BUTTON)

    def click_outside(self):
        self.helpers.wait(until=EC.presence_of_element_located((By.CSS_SELECTOR, self.OUTSIDE)))
        self.driver.execute_script("document.querySelector(\"{}\").click()".format(self.OUTSIDE))

    def is_logined(self):
        self.helpers.wait(until=EC.presence_of_element_located((By.CSS_SELECTOR, self.LOGINED)))
        return self.helpers.is_contains(self.LOGINED)

    def is_error(self):
        self.helpers.wait(until=EC.presence_of_element_located((By.CSS_SELECTOR, self.AUTH_ERROR)))
        return self.helpers.is_contains(self.AUTH_ERROR)

    def open_auth(self):
        self.helpers.click_button(self.LOGIN_BUTTON)

    def is_opened(self):
        return self.helpers.is_contains(self.POPUP)

    def input_telephone_value(self, text):
        self.helpers.input_value(self.LOGIN, text)

    def clear_telephone_value(self):
        self.helpers.clear_input(self.LOGIN)

    def input_password_value(self, text):
        self.helpers.input_value(self.PASSWORD, text)

    def clear_password_value(self):
        self.helpers.clear_input(self.PASSWORD)

    def enter_submit(self):
        self.helpers.click_button(self.SUBMIT)

    def auth(self):
        self.open_auth()

        self.input_telephone_value("4444444444")
        self.input_password_value("Qwerty123")

        self.enter_submit()

        self.helpers.wait(until=EC.presence_of_element_located((By.CSS_SELECTOR, self.LOGINED)))

    def logout(self):
        self.helpers.click_button(self.LOGINED)
        self.helpers.click_button(self.LOGOUT)

        self.helpers.wait(until=EC.presence_of_element_located((By.CSS_SELECTOR, self.LOGIN_BUTTON)))
