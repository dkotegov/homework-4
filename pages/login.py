from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.default_page import DefaultPage


class LoginPage(DefaultPage):
    PATH = ""

    OUTSIDE = ".auth"
    POPUP = ".auth-content"
    TITLE = ".auth-content-inner__title"
    LOGIN = ".auth-content-form__tel"
    PASSWORD = ".auth-content-form__password"
    SUBMIT = ".auth-content-form__button"
    LOGIN_BUTTON = ".header-right__account"
    REGISTRATION_BUTTON = ".auth-content-form-registration__link"
    CLOSE_BUTTON = ".auth-content-inner__close"

    LOGINED = ".header-right-avatar__img"
    LOGOUT = "[data-action = \"logoutClick\"]"
    AUTH_ERROR = "#auth-error"

    def click_registration(self):
        self.__click_button__(self.REGISTRATION_BUTTON)

    def click_close(self):
        self.__click_button__(self.CLOSE_BUTTON)

    def click_outside(self):
        self.__click_button__(self.OUTSIDE)

    def is_logined(self):
        self.wait(until=EC.presence_of_element_located((By.CSS_SELECTOR, self.LOGINED)))
        return self.is_contains(self.LOGINED)

    def is_error(self):
        self.wait(until=EC.presence_of_element_located((By.CSS_SELECTOR, self.AUTH_ERROR)))
        return self.is_contains(self.AUTH_ERROR)

    def open_auth(self):
        self.__click_button__(self.LOGIN_BUTTON)

    def is_opened(self):
        return self.is_contains(self.POPUP)

    def input_telephone_value(self, text):
        self.__input_value__(self.LOGIN, text)

    def clear_telephone_value(self):
        self.__clear_input__(self.LOGIN)

    def input_password_value(self, text):
        self.__input_value__(self.PASSWORD, text)

    def clear_password_value(self):
        self.__clear_input__(self.PASSWORD)

    def enter_submit(self):
        self.__click_button__(self.SUBMIT)

    def auth(self):
        self.open_auth()

        self.input_telephone_value("4444444444")
        self.input_password_value("Qwerty123")

        self.enter_submit()

        self.wait(until=EC.presence_of_element_located((By.CSS_SELECTOR, self.LOGINED)))

    def logout(self):
        self.__click_button__(self.LOGINED)
        self.__click_button__(self.LOGOUT)

        self.wait(until=EC.presence_of_element_located((By.CSS_SELECTOR, self.LOGIN_BUTTON)))

    def get_title(self):
        self.wait(until=EC.presence_of_element_located((By.CSS_SELECTOR, self.TITLE)))
        return self.driver.find_element(By.CSS_SELECTOR, self.TITLE).text
