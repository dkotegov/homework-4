from tests.components.component import Component

from selenium.webdriver.support.ui import WebDriverWait


class LoginForm(Component):
    LOGIN = '//input[contains(@class,"icon-bar__profile-image")]'
    INPUT_PHONE = '//input[@id="login-field__phone-input"]'
    INPUT_PHONE_ERROR = '//div[@id="login-field__phone-input-wrapper_err"]'
    INPUT_PASSWORD = '//input[@id="login-field__password-input"]'
    INPUT_PASSWORD_ERROR = '//div[@id="login-field__password-input-wrapper_err"]'
    SUBMIT = '//button[contains(@class,"login-field__submit")]'
    REGISTRATION = '//button[@class="neon-button login-field__goto-signup"]'

    def wait_open(self):
        return WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.SUBMIT).is_displayed()
        )

    def registration(self):
        self.driver.find_element_by_xpath(self.REGISTRATION).click()

    def open(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()

    def set_phone(self, phone):
        self.driver.find_element_by_xpath(self.INPUT_PHONE).send_keys(phone)

    def get_phone_error(self):
        WebDriverWait(self.driver, 30, 1).until(
            lambda d: d.find_element_by_xpath(self.INPUT_PHONE_ERROR).text != ''
        )
        return self.driver.find_element_by_xpath(self.INPUT_PHONE_ERROR).text

    def set_password(self, password):
        self.driver.find_element_by_xpath(self.INPUT_PASSWORD).send_keys(password)

    def get_password_error(self):
        WebDriverWait(self.driver, 30, 1).until(
            lambda d: d.find_element_by_xpath(self.INPUT_PASSWORD_ERROR).text != ''
        )
        return self.driver.find_element_by_xpath(self.INPUT_PASSWORD_ERROR).text

    def clean_password(self):
        self.driver.find_element_by_xpath(self.INPUT_PASSWORD).clear()

    def clean_phone(self):
        self.driver.find_element_by_xpath(self.INPUT_PHONE).clear()

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()
