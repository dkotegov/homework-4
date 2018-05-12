# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import os

import unittest
import urlparse

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait


class Page(object):
    BASE_URL = 'https://ok.ru/'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()


class MainPage(Page):
    PATH = ''  
    FEED_BUTTON = '//a[@href="/feed"]'

    @property
    def form(self):
        return AuthForm(self.driver)

    def go_to_feed(self):
        self.driver.find_element_by_xpath(self.FEED_BUTTON).click()


class PostPage(Page):
    PATH = '/post'  

    @property
    def create_post(self):
        return Create_Topic(self.driver) 

class FeedPage(Page):
    PATH = '/feed'
    REPOST_BUTTON = '//button[@class="h-mod widget_cnt"]'
    REPOST_SUBMIT = '//a[@class="u-menu_li js-doNotHide"]'

    def repost_click(self):
        self.driver.find_element_by_xpath(self.REPOST_BUTTON).click()

    def repost_submit(self):
        self.driver.find_element_by_xpath(self.REPOST_SUBMIT).click()


class Component(object):
    def __init__(self, driver):
        self.driver = driver


class AuthForm(Component):
    LOGIN = '//input[@name="st.email"]'
    PASSWORD = '//input[@name="st.password"]'
    SUBMIT = '//input[@value="Войти"]'

    @property
    def form(self):
        return AuthForm(self.driver)  

    def set_login(self, login):
        self.driver.find_element_by_xpath(self.LOGIN).send_keys(login)

    def set_password(self, pwd):
        self.driver.find_element_by_xpath(self.PASSWORD).send_keys(pwd)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()
      


class Create_Topic(Component):
    TEXT = '//div[@class="posting_itx emoji-tx h-mod js-ok-e ok-posting-handler"]'
    SUBMIT = '//div[@class="posting_submit button-pro"]'

    def add_text(self, text):
        self.driver.find_element_by_xpath(self.TEXT).send_keys(text)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()



class ExampleTest(unittest.TestCase):
    LOGIN = 'technopark14'
    PASSWORD = os.environ['PASSWORD']
    TEXT = 'lalalallalalalalaa'
    TEXT2 = ''


    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()


    def test_create_new_post(self):
        main_page = MainPage(self.driver)
        main_page.open()

        auth_form = main_page.form
        auth_form = AuthForm(self.driver)

        auth_form.set_login(self.LOGIN)
        auth_form.set_password(self.PASSWORD)
        auth_form.submit()

        post_page = PostPage(self.driver)
        post_page.open()

        topic_text = post_page.create_post
        topic_text.add_text(self.TEXT)
        topic_text.submit()

    def test_create_empty_topic(self):
        main_page = MainPage(self.driver)
        main_page.open()

        auth_form = main_page.form
        auth_form = AuthForm(self.driver)

        auth_form.set_login(self.LOGIN)
        auth_form.set_password(self.PASSWORD)
        auth_form.submit()

        post_page = PostPage(self.driver)
        post_page.open()

        flag = True
        try:
            self.driver.find_element_by_xpath(Create_Topic.SUBMIT)
        except NoSuchElementException:
            flag = False

        self.assertEquals(flag, False)


    def test_repost_topic(self):
        main_page = MainPage(self.driver)
        main_page.open()

        auth_form = main_page.form
        auth_form = AuthForm(self.driver)

        auth_form.set_login(self.LOGIN)
        auth_form.set_password(self.PASSWORD)
        auth_form.submit()

        feed_page = FeedPage(self.driver)
        feed_page.open()
        feed_page.repost_click()
        feed_page.repost_submit()

        self.driver.refresh()




    
