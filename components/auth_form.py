# coding=utf-8
from selenium.webdriver.support.wait import WebDriverWait

from components.base_component import Component


class AuthForm(Component):
    LOGIN = '//input[@name="Login"]'
    PASSWORD = '//input[@name="Password"]'
    SUBMIT = '//span[text()="Войти"]'

    def set_login(self, login):
        WebDriverWait(self.driver, 10) \
            .until(lambda driver: driver.find_element_by_xpath(self.LOGIN))
        self.driver.find_element_by_xpath(self.LOGIN).send_keys(login)

    def set_password(self, pwd):
        self.driver.find_element_by_xpath(self.PASSWORD).send_keys(pwd)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()

