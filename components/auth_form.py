# coding=utf-8
from components.base_component import Component


class AuthForm(Component):
    LOGIN = '//input[@name="Login"]'
    PASSWORD = '//input[@name="Password"]'
    SUBMIT = '//span[text()="Войти"]'
    # WRITING_LETTER = '//div[@id="app-canvas"]//span[@class="compose-button"]'
    WRITING_LETTER = '//div[@class="sidebar__full"]'
    # LOGIN_BUTTON = '//a[text()="Вход для участников"]'

    # def open_form(self):
    #     self.driver.find_element_by_xpath(self.LOGIN_BUTTON).click()

    def set_login(self, login):
        self.driver.find_element_by_xpath(self.LOGIN).send_keys(login)

    def set_password(self, pwd):
        self.driver.find_element_by_xpath(self.PASSWORD).send_keys(pwd)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()

    def open_writing_letter(self):
        content = self.driver.find_element_by_xpath(self.WRITING_LETTER)
        print content
