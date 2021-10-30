from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from helpers import Page, Component


class RegistrationForm(Component):
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
        self.helpers.input_value(self.NAME, text)

    def clear_name_value(self):
        self.helpers.clear_input(self.NAME)

    def is_error_name(self):
        return self.helpers.is_contains_class(self.NAME, self.ERROR)

    def input_surname_value(self, text):
        self.helpers.input_value(self.SURNAME, text)

    def clear_surname_value(self):
        self.helpers.clear_input(self.SURNAME)

    def is_error_surname(self):
        return self.helpers.is_contains_class(self.SURNAME, self.ERROR)

    def input_telephone_value(self, text):
        self.helpers.input_value(self.TELEPHONE, text)

    def clear_telephone_value(self):
        self.helpers.clear_input(self.TELEPHONE)

    def is_error_telephone(self):
        return self.helpers.is_contains_class(self.TELEPHONE, self.ERROR)

    def input_password_value(self, text):
        self.helpers.input_value(self.PASSWORD, text)

    def clear_password_value(self):
        self.helpers.clear_input(self.PASSWORD)

    def is_error_password(self):
        return self.helpers.is_contains_class(self.PASSWORD, self.ERROR)

    def input_confirm_password_value(self, text):
        self.helpers.input_value(self.CONFIRM_PASSWORD, text)

    def clear_confirm_password_value(self):
        self.helpers.clear_input(self.CONFIRM_PASSWORD)

    def is_error_confirm_password(self):
        return self.helpers.is_contains_class(self.CONFIRM_PASSWORD, self.ERROR)

    def input_email_value(self, text):
        self.helpers.input_value(self.EMAIL, text)

    def clear_email_value(self):
        self.helpers.clear_input(self.EMAIL)

    def is_error_email(self):
        return self.helpers.is_contains_class(self.EMAIL, self.ERROR)

    def get_registration_error(self):
        return self.helpers.get_element(self.REGISTRATION_ERROR, self.helpers.SELECTOR.XPATH).text

    def enter_submit(self):
        self.helpers.click_button(self.SUBMIT)


class RegistrationPage(Page):
    PATH = "signup"

    TITLE = ".reg-panel-title__product-name"

    @property
    def form(self):
        return RegistrationForm(self.driver)

    def get_title(self):
        self.helpers.wait(until=EC.presence_of_element_located((By.CSS_SELECTOR, self.TITLE)))
        return self.driver.find_element(By.CSS_SELECTOR, self.TITLE).text
