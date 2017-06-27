# -*- coding: utf-8 -*-

import os

import unittest
import urlparse

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait

class Page(object):
    BASE_URL = 'http://ftest.tech-mail.ru/'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()


class Component(object):
    def __init__(self, driver):
        self.driver = driver

class AuthForm(Component):
    LOGIN = '//input[@name="login"]'
    PASSWORD = '//input[@name="password"]'
    SUBMIT = '//span[text()="Войти"]'
    LOGIN_BUTTON = '//a[text()="Вход для участников"]'

    def open_form(self):
        self.driver.find_element_by_xpath(self.LOGIN_BUTTON).click()

    def set_login(self, login):
        self.driver.find_element_by_xpath(self.LOGIN).send_keys(login)

    def set_password(self, pwd):
        self.driver.find_element_by_xpath(self.PASSWORD).send_keys(pwd)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()


class TopMenu(Component):
    USERNAME = '//a[@class="username"]'

    def get_username(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.USERNAME).text
        )


class AuthPage(Page):
    PATH = ''

    @property
    def form(self):
        return AuthForm(self.driver)

    @property
    def top_menu(self):
        return TopMenu(self.driver)

class BugReportPage(Page):
    PATH = 'bugreport/list/all/park/'

    @property
    def search(self):
        return SearchForm(self.driver)

    @property
    def articles(self):
        return {}


class SearchForm(Component):
    QUERY_TEXT = "//form[@class='seach-item seach-item-abs']//input[@class='input-text']"
    SUBMIT = "//form[@class='seach-item seach-item-abs']//input[@class='input-submit']"

    def set_query_text(self, query_text):
        self.driver.find_element_by_xpath(self.QUERY_TEXT).send_keys(query_text)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()


class Article(Component):
    TOPIC_TITLE_TEXT = '//div[@class="topic-title"]/a'
    TOPIC_INFO_SOURCE_TEXT =  '//div[@class="topic-info"]/a[1]'
    TOPIC_INFO_STATUS_TEXT = '//div[@class="topic-info"]/a[2]'

    def get_topic_title_text(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.TOPIC_TITLE_TEXT).text
        )

    def get_topic_info_source_text(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.TOPIC_INFO_SOURCE_TEXT).text
        )

    def get_topic_info_status_text(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.TOPIC_INFO_STATUS_TEXT).text
        )
