from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

from base_classes.component import Component


class LoginForm(Component):
    CONTAINER = '//div[@class="auth-form-login"]'

    LOGIN = '//input[@id="inputLogin"]'
    PASSWORD = '//input[@id="inputPassword"]'
    SUBMIT = '//div[@id="submit_button"]'
    JOIN_BUTTON = '//a[text()="Регистрация"]'

    INPUT_ERROR = '//div[@id="inputError"]'

    def set_login(self, login: str):
        self.driver.find_element_by_xpath(self.LOGIN).send_keys(login)

    def set_password(self, password: str):
        self.driver.find_element_by_xpath(self.PASSWORD).send_keys(password)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()

    def open_join(self):
        self.driver.find_element_by_xpath(self.JOIN_BUTTON).click()

    def is_invalid_login(self):
        try:
            return WebDriverWait(self.driver, 2).until(lambda d: len(d.find_element_by_xpath(self.INPUT_ERROR).text) != 0)
        except TimeoutException:
            return False
