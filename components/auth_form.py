from components.default import Component

from utils import wait_for_element_by_selector


class AuthForm(Component):
    LOGIN = '#email'
    PASSWORD = '#password'
    SUBMIT = '.form-content__button'

    def set_login(self, login):
        wait_for_element_by_selector(self.driver, self.LOGIN)
        self.driver.find_element_by_css_selector(self.LOGIN).send_keys(login)

    def set_password(self, password):
        wait_for_element_by_selector(self.driver, self.PASSWORD)
        self.driver.find_element_by_css_selector(self.PASSWORD).send_keys(password)

    def submit(self):
        wait_for_element_by_selector(self.driver, self.SUBMIT)
        self.driver.find_element_by_css_selector(self.SUBMIT).click()
