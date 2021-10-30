from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.default_page import DefaultPage, SELECTOR


class RegistrationPage(DefaultPage):
    PATH = "signup"

    TITLE = ".reg-panel-title__product-name"

    ERROR = "input-error"

    REGISTRATION_ERROR = "//div[@id=\"reg-error\"][contains(string(), \"Пользователь уже существует\")]"
    NAME = "#name"
    SURNAME = "#surname"
    TELEPHONE = "#phone"
    PASSWORD = "#password"
    CONFIRM_PASSWORD = "#passwordConfirm"
    EMAIL = "#mail"
    DATE = "#date"
    SEX = "#sex"
    SUBMIT = "#submitBtn"

    def input_name_value(self, text):
        self.__input_value__(self.NAME, text)

    def clear_name_value(self):
        self.__clear_input__(self.NAME)

    def is_error_name(self):
        return self.__element_contains_class__(self.NAME, self.ERROR)

    def input_surname_value(self, text):
        self.__input_value__(self.SURNAME, text)

    def clear_surname_value(self):
        self.__clear_input__(self.SURNAME)

    def is_error_surname(self):
        return self.__element_contains_class__(self.SURNAME, self.ERROR)

    def input_telephone_value(self, text):
        self.__input_value__(self.TELEPHONE, text)

    def clear_telephone_value(self):
        self.__clear_input__(self.TELEPHONE)

    def is_error_telephone(self):
        return self.__element_contains_class__(self.TELEPHONE, self.ERROR)

    def input_password_value(self, text):
        self.__input_value__(self.PASSWORD, text)

    def clear_password_value(self):
        self.__clear_input__(self.PASSWORD)

    def is_error_password(self):
        return self.__element_contains_class__(self.PASSWORD, self.ERROR)

    def input_confirm_password_value(self, text):
        self.__input_value__(self.CONFIRM_PASSWORD, text)

    def clear_confirm_password_value(self):
        self.__clear_input__(self.CONFIRM_PASSWORD)

    def is_error_confirm_password(self):
        return self.__element_contains_class__(self.CONFIRM_PASSWORD, self.ERROR)

    def input_email_value(self, text):
        self.__input_value__(self.EMAIL, text)

    def clear_email_value(self):
        self.__clear_input__(self.EMAIL)

    def is_error_email(self):
        return self.__element_contains_class__(self.EMAIL, self.ERROR)

    def get_registration_error(self):
        return self.__get_element__(self.REGISTRATION_ERROR, by=SELECTOR.XPATH).text

    def enter_submit(self):
        self.__click_button__(self.SUBMIT)

    def get_title(self):
        self.wait(until=EC.presence_of_element_located((By.CSS_SELECTOR, self.TITLE)))
        return self.driver.find_element(By.CSS_SELECTOR, self.TITLE).text
