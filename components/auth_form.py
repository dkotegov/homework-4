# coding=utf-8
from components.base_component import Component


class AuthForm(Component):
    LOGIN = '//input[@name="Login"]'
    PASSWORD = '//input[@name="Password"]'
    SUBMIT = '//span[text()="Войти"]'
    WRITING_LETTER = '//span[text()="Написать письмо"]'

    def set_login(self, login):
        # здесь может не успеть прогрузиться страница
        self.driver.find_element_by_xpath(self.LOGIN).send_keys(login)

    def set_password(self, pwd):
        self.driver.find_element_by_xpath(self.PASSWORD).send_keys(pwd)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()

    def open_writing_letter(self):
        # здесь скорее всего не прогрузится страница, перед нажатием. Надо добавить wait
        self.driver.find_element_by_xpath(self.WRITING_LETTER).click()
