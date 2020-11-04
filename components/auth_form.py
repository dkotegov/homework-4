# -*- coding: utf-8 -*-

from selenium.webdriver.support.ui import WebDriverWait
from components.base import Component
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class AuthForm(Component):
    LOGIN = '//input[@name="username"]'
    PASSWORD = '//input[@name="password"]'
    NEXT = '//button[@data-test-id="next-button"]'
    SUBMIT = '//button[@data-test-id="submit-button"]'
    NAME = '//i[text()="{}"]'

    def set_login(self, login):
        """
        Вводит логин в окне авторизации
        :param login: логин пользователя
        """
        username = WebDriverWait(self.driver, 10, 0.1).until(
            EC.presence_of_element_located((By.XPATH, self.LOGIN))
        )
        username.send_keys(login)

    def to_password(self):
        """
        Открывает окно ввода пароля
        """
        next_button = WebDriverWait(self.driver, 10, 0.1).until(
            EC.presence_of_element_located((By.XPATH, self.NEXT))
        )
        next_button.click()

    def set_password(self, pwd):
        """
        Вводит пароль в окне авторизации
        :param pwd: пароль пользователя
        """
        password = WebDriverWait(self.driver, 10, 0.1).until(
            EC.element_to_be_clickable((By.XPATH, self.PASSWORD))
        )
        password.send_keys(pwd)

    def submit(self):
        """
        Завершает авторизацию
        """
        submit = WebDriverWait(self.driver, 10, 0.1).until(
            EC.presence_of_element_located((By.XPATH, self.SUBMIT))
        )
        submit.click()

    def wait_for_email(self):
        """
        Ождиает пока не откроется страница с почтой
        """
        WebDriverWait(self.driver, 10, 0.1).until(
            EC.url_matches("https://e.mail.ru/inbox")
        )
