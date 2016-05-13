# -*- coding: utf-8 -*-
from PageObject import Page


class AuthPage(Page):
    PATH = 'https://rabota.mail.ru/'

    @property
    def auth_form(self):
        return AuthForm(self.driver)


class AuthForm(object):
    LOGIN = '//input[@name="Login"]'
    PASSWORD = '//input[@name="Password"]'
    SUBMIT = '//input[@value="Войти в личный кабинет"]'
    LOGIN_BUTTON = '//a[text()="Вход"]'

    def __init__(self, driver):
        self.driver = driver

    def open_form(self):
        self.driver.find_element_by_xpath(self.LOGIN_BUTTON).click()

    def set_email(self, mail):
        self.driver.find_element_by_xpath(self.LOGIN).send_keys(mail)

    def set_password(self, password):
        self.driver.find_element_by_xpath(self.PASSWORD).send_keys(password)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()

