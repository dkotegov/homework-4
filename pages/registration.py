from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from helpers import Page, Component


class RegistrationForm(Component):
    ERROR = "input-error"

    REGISTRATION_ERROR = "#reg-error"
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
        self.helpers.clear_input(self.NAME)
        self.helpers.input_value(self.NAME, text)

    def is_error_name(self):
        return self.helpers.is_contains_class(self.NAME, self.ERROR)

    def input_surname_value(self, text):
        self.helpers.clear_input(self.SURNAME)
        self.helpers.input_value(self.SURNAME, text)

    def is_error_surname(self):
        return self.helpers.is_contains_class(self.SURNAME, self.ERROR)

    def input_telephone_value(self, text):
        self.helpers.clear_input(self.TELEPHONE)
        self.helpers.input_value(self.TELEPHONE, text)

    def is_error_telephone(self):
        return self.helpers.is_contains_class(self.TELEPHONE, self.ERROR)

    def input_password_value(self, text):
        self.helpers.clear_input(self.PASSWORD)
        self.helpers.input_value(self.PASSWORD, text)

    def is_error_password(self):
        return self.helpers.is_contains_class(self.PASSWORD, self.ERROR)

    def input_confirm_password_value(self, text):
        self.helpers.clear_input(self.CONFIRM_PASSWORD)
        self.helpers.input_value(self.CONFIRM_PASSWORD, text)

    def is_error_confirm_password(self):
        return self.helpers.is_contains_class(self.CONFIRM_PASSWORD, self.ERROR)

    def input_email_value(self, text):
        self.helpers.clear_input(self.EMAIL)
        self.helpers.input_value(self.EMAIL, text)

    def is_error_email(self):
        return self.helpers.is_contains_class(self.EMAIL, self.ERROR)

    def input_date_value(self, text):
        self.helpers.clear_input(self.DATE)
        self.helpers.input_value(self.DATE, text)

    def is_error_date(self):
        return self.helpers.is_contains_class(self.DATE, self.ERROR)

    def input_sex_value(self, text):
        self.helpers.input_value(self.SEX, text)

    def is_error_sex(self):
        return self.helpers.is_contains_class(self.SEX, self.ERROR)

    def is_error_form(self):
        self.helpers.wait(until=EC.presence_of_element_located((By.CSS_SELECTOR, self.REGISTRATION_ERROR)))
        return self.helpers.is_contains(self.REGISTRATION_ERROR)

    def enter_submit(self):
        self.helpers.click_element(self.SUBMIT)


class RegistrationPage(Page):
    PATH = "/signup"

    BOARD = ".board"

    def wait_page(self):
        self.helpers.wait(until=EC.presence_of_element_located((By.CSS_SELECTOR, self.BOARD)))

    def delete_user(self, user_id):
        url = self.BASE_URL + self.BACK_URL + "/user/{}/delete".format(user_id)
        self.helpers.fetch(url)

    @property
    def form(self):
        return RegistrationForm(self.driver)
