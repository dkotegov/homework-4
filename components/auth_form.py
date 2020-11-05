# -*- coding: utf-8 -*-

from selenium.webdriver.support.ui import WebDriverWait
from components.base import Component


class AuthForm(Component):
    LOGIN = '//input[@name="username"]'
    PASSWORD = '//input[@name="password"]'
    NEXT = '//span[text()="Ввести пароль"]'
    SUBMIT = '//span[text()="Войти"]'

    def set_login(self, login):
        """
        Вводит логин в окне авторизации
        :param login: логин пользователя
        """
        username = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: self.driver.find_element_by_xpath(self.LOGIN)
        )
        username.send_keys(login)

    def to_password(self):
        """
        Открывает окно ввода пароля
        """
        next_button = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: self.driver.find_element_by_xpath(self.NEXT)
        )
        next_button.click()

    def set_password(self, pwd):
        """
        Вводит пароль в окне авторизации
        :param pwd: пароль пользователя
        """
        password = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: self.driver.find_element_by_xpath(self.PASSWORD)
        )
        password.send_keys(pwd)

    def submit(self):
        """
        Завершает авторизацию
        """
        submit = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: self.driver.find_element_by_xpath(self.SUBMIT)
        )
        submit.click()

    def wait_for_name(self, name):
        """
        Ожидает появления имени на экране
        :param name: Имя, которое должно появиться
        """
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: self.driver.find_element_by_xpath('//i[text()="' + name + '"]')
        )
