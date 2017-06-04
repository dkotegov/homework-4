# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class DefPage:

    driver = None
    url = "http://google.com"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.url)


class LoginPage(DefPage):

    url = "http://ftest.tech-mail.ru/pages/index/"

    def login(self, login, password):
        self.driver.find_element_by_xpath('//a[text()="Вход для участников"]').click()
        self.driver.find_element_by_xpath('//input[@name="login"]').send_keys(login)
        self.driver.find_element_by_xpath('//input[@name="password"]').send_keys(password)
        self.driver.find_element_by_xpath('//span[text()="Войти"]').click()
        try:
            WebDriverWait(self.driver, 100).until(lambda driver: driver.find_element_by_class_name("topic-title"))
        except:
            return None
        return MainPage(self.driver)


class MainPage(DefPage):

    url = "http://ftest.tech-mail.ru/feed/"

    def get_post(self):
        self.driver.find_element_by_class_name("topic-title").click()
        try:
            WebDriverWait(self.driver, 100).until(lambda driver: driver.find_elements_by_class_name("comment-rendered"))
        except:
            return None
        return PostPage(self.driver)


class PostPage(DefPage):

    def check_last_comment(self):
        comments = self.driver.find_elements_by_class_name("comment-rendered")
        if len(comments) > 0:
            comment = comments[-1]
            return comment.size['height']
