from tests.components.component import Component

from selenium.webdriver.support.ui import WebDriverWait


class LoginForm(Component):
    LOGIN = '//input[contains(@class,"icon-bar__profile-image")]'
    INPUT_PHONE = '//input[@id="login-field__phone-input"]'
    INPUT_PASSWORD = '//input[@id="login-field__password-input"]'
    SUBMIT = '//button[contains(@class,"login-field__submit")]'

    def wait_open(self):
        return WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.SUBMIT).is_displayed()
        )

    def open(self):
        self.driver.find_element_by_xpath(self.LOGIN).click()

    def set_phone(self, phone):
        self.driver.find_element_by_xpath(self.INPUT_PHONE).send_keys(phone)

    def set_password(self, password):
        self.driver.find_element_by_xpath(self.INPUT_PASSWORD).send_keys(password)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()
