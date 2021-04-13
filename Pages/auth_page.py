from Pages.page import Page
import os


class AuthPage(Page):
    USERNAME_INPUT = os.environ['LOGIN']
    PASSWORD_INPUT = os.environ['PASSWORD']
    PATH = '/login'
    LOGIN = '//input[@name="login"]'
    PASSWORD = '//input[@name="password"]'
    SUBMIT = '//button[text()="Войти"]'

    def set_login(self):
        self.driver.find_element_by_xpath(self.LOGIN).send_keys(self.USERNAME_INPUT)

    def set_password(self):
        self.driver.find_element_by_xpath(self.PASSWORD).send_keys(self.PASSWORD_INPUT)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()

    def auth(self):
        self.open()
        self.set_login()
        self.set_password()
        self.submit()
