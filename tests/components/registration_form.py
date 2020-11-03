from tests.components.component import Component

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class RegistrationForm(Component):
    NAME_INPUT = '//input[@id="signup-field__fname-input"]'
    NAME_ERROR = '//div[@id="signup-field__fname-input-wrapper_err"]'
    SURNAME_INPUT = '//input[@id="signup-field__lname-input"]'
    SURNAME_ERROR = '//div[@id="signup-field__lname-input-wrapper_err"]'
    PHONE_INPUT = '//input[@id="signup-field__phone-input"]'
    PHONE_ERROR = '//div[@id="signup-field__phone-input-wrapper_err"]'
    PASSWORD1_INPUT = '//input[@id="signup-field__password-input1"]'
    PASSWORD1_ERROR = '//div[@id="signup-field__password-input1-wrapper_err"]'
    PASSWORD2_INPUT = '//input[@id="signup-field__password-input2"]'
    PASSWORD2_ERROR = '//div[@id="signup-field__password-input2-wrapper_err"]'
    REGISTER_BUTTON = '//button[@class="neon-button signup-field__submit"]'
    CONFIRM_ERROR = '//div[@id="signup-general-error"]'

    def wait_open(self):
        return WebDriverWait(self.driver, 30, 1).until(
            ec.element_to_be_clickable((By.XPATH, self.REGISTER_BUTTON))
        )

    def set_name(self, name):
        self.driver.find_element_by_xpath(self.NAME_INPUT).send_keys(name)

    def get_name_error(self):
        curr_error = self.driver.find_element_by_xpath(self.NAME_ERROR).text
        WebDriverWait(self.driver, 30, 1).until(
            lambda d: d.find_element_by_xpath(self.NAME_ERROR).text == curr_error
                      and
                      d.find_element_by_xpath(self.NAME_ERROR).text != ''
        )
        return self.driver.find_element_by_xpath(self.NAME_ERROR).text

    def get_name(self):
        return self.driver.find_element_by_xpath(self.NAME_INPUT).get_attribute('value')

    def set_surname(self, surname):
        self.driver.find_element_by_xpath(self.SURNAME_INPUT).send_keys(surname)

    def get_surname_error(self):
        curr_error = self.driver.find_element_by_xpath(self.SURNAME_ERROR).text
        WebDriverWait(self.driver, 30, 1).until(
            lambda d: d.find_element_by_xpath(self.SURNAME_ERROR).text != curr_error
                      and
                      d.find_element_by_xpath(self.SURNAME_ERROR).text != ''
        )
        return self.driver.find_element_by_xpath(self.SURNAME_ERROR).text

    def get_surname(self):
        return self.driver.find_element_by_xpath(self.SURNAME_INPUT).get_attribute('value')

    def set_phone(self, email):
        self.driver.find_element_by_xpath(self.PHONE_INPUT).send_keys(email)

    def get_phone_error(self):
        WebDriverWait(self.driver, 30, 1).until(
            lambda d: d.find_element_by_xpath(self.PHONE_ERROR).text != ''
        )
        return self.driver.find_element_by_xpath(self.PHONE_ERROR).text

    def get_phone(self):
        return self.driver.find_element_by_xpath(self.PHONE_INPUT).get_attribute('value')

    def set_password1(self, email):
        self.driver.find_element_by_xpath(self.PASSWORD1_INPUT).send_keys(email)

    def get_password1_error(self):
        WebDriverWait(self.driver, 30, 1).until(
            lambda d: d.find_element_by_xpath(self.PASSWORD1_ERROR).text != ''
        )
        return self.driver.find_element_by_xpath(self.PASSWORD1_ERROR).text

    def get_password1(self):
        return self.driver.find_element_by_xpath(self.PASSWORD1_INPUT).get_attribute('value')

    def set_password2(self, email):
        self.driver.find_element_by_xpath(self.PASSWORD2_INPUT).send_keys(email)

    def get_password2_error(self):
        WebDriverWait(self.driver, 30, 1).until(
            lambda d: d.find_element_by_xpath(self.PASSWORD2_ERROR).text != ''
        )
        return self.driver.find_element_by_xpath(self.PASSWORD2_ERROR).text

    def get_password2(self):
        return self.driver.find_element_by_xpath(self.PASSWORD2_INPUT).get_attribute('value')

    def get_confirm_error(self):
        WebDriverWait(self.driver, 30, 1).until(
            lambda d: d.find_element_by_xpath(self.CONFIRM_ERROR).text != ''
        )
        return self.driver.find_element_by_xpath(self.CONFIRM_ERROR).text

    def register(self):
        self.driver.find_element_by_xpath(self.REGISTER_BUTTON).click()
