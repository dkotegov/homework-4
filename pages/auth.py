from default import *


class AuthPage(Page):
    PATH = ''

    @property
    def form(self):
        return AuthForm(self.driver)


class AuthForm(Component, Page):
    LOGIN = '//input[@name="Login"]'
    PASSWORD = '//input[@name="Password"]'
    SUBMIT = '//button[@data-test-id="submit-button"]'
    SUBMIT_ACCOUNT_NAME = '//button[@data-test-id="next-button"]'

    def set_login(self, login):
        self.wait_for_clickable(self.LOGIN)
        self.driver.find_element_by_xpath(self.LOGIN).send_keys(login)

    def set_password(self, pwd):
        self.wait_for_clickable(self.PASSWORD)
        self.driver.find_element_by_xpath(self.PASSWORD).send_keys(pwd)

    def submit_account_name(self):
        self.wait_for_clickable(self.SUBMIT_ACCOUNT_NAME)
        self.driver.find_element_by_xpath(self.SUBMIT_ACCOUNT_NAME).click()

    def submit(self):
        self.wait_for_clickable(self.SUBMIT)
        self.driver.find_element_by_xpath(self.SUBMIT).click()
