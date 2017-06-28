# -*- coding: utf-8 -*-

import os

import unittest
import urlparse
import re

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
        return Articles(self.driver)

    @property
    def statusSelect(self):
        return StatusSelect(self.driver)


class CommentsPage(Page):
    COMMENTS_NUMBER_THAT_PRESENTED_FOR_USER_IN_TEXT_FORM = '//*[@id="count-comments"]'

    def __init__(self, driver, articleId):
        super(CommentsPage, self).__init__(driver)
        self.PATH = 'bugreport/show/%d/' % articleId

    @property
    def comment_form(self):
        return CommentForm(self.driver)

    @property
    def comments(self):
        return Comments(self.driver)

    @property
    def get_number_comments_presented_for_user(self):
        return int(WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.COMMENTS_NUMBER_THAT_PRESENTED_FOR_USER_IN_TEXT_FORM).text
        )) 
    

class CommentForm(Component):
    COMMENT_ADD_LINK = '//a[@class="comment-add-link link-dotted"]'
    SUBMIT_BUTTON = '//form[@id="comment-form"]/button[@type="submit" and @class="button button-primary"]'
    TEXTAREA = '//*[@id="id_text"]'

    def set_text(self, text):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.TEXTAREA)
        )
        self.driver.find_element_by_xpath(self.TEXTAREA).send_keys(text)

    def show_comment_form(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.COMMENT_ADD_LINK)
        )
        self.driver.find_element_by_xpath(self.COMMENT_ADD_LINK).click()

    def submit(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.SUBMIT_BUTTON)
        )
        self.driver.find_element_by_xpath(self.SUBMIT_BUTTON).click()

class StatusSelect(Component):
    Statuses = {
        u'Все': '//a[@href="/bugreport/list/new/park/"]',
        u'Новая': '//a[@href="/bugreport/list/new/park/"]',
        u'Открыта': '//a[@href="/bugreport/list/open/park/"]',
        u'В работе': '//a[@href="/bugreport/list/progress/park/"]',
        u'Ожидание':'//a[@href="/bugreport/list/pending/park/"]',
        u'Закрыта': '//a[@href="/bugreport/list/closed/park/"]',
        u'Отклонена':'//a[@href="/bugreport/list/refused/park/"]'}

    def set_status(self, status):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.Statuses[status])
        ).click()

class SearchForm(Component):
    QUERY_TEXT = '//div[@class="search-input-wrapper"]/input[@class="input-text" and @name="query"]'
    SUBMIT = '//div[@class="search-input-wrapper"]/input[@class="input-submit"]'

    def set_query_text(self, query_text):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.QUERY_TEXT)
        )
        self.driver.find_element_by_xpath(self.QUERY_TEXT).send_keys(query_text)


    def submit(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.SUBMIT)
        )
        self.driver.find_element_by_xpath(self.SUBMIT).click()


class Articles(Component):
    ARTICLE = '//article[@class="topic topic-type-topic js-topic"]'

    def get_articles_count(self):
        return len(self.driver.find_elements_by_xpath(self.ARTICLE))

    def get_article(self, article_number):
        return Article(self.driver, article_number)


class Comments(Component):
    COMMENT = '//div[@class="comment-content "]'
 
    def count_comments(self):
        return len(self.driver.find_elements_by_xpath(self.COMMENT))

    def get_comment(self, comment_number):
        return Comment(self.driver, comment_number)
            
class Comment(Component):
    def __init__(self, driver, articleNumber):
        super(Article, self).__init__(driver)
        self.articleNumber = articleNumber
        self.TOPIC_TITLE_TEXT = '(//h1[@class="topic-title"])[%d]/a' % articleNumber
        self.TOPIC_INFO_SOURCE_TEXT =  '(//div[@class="topic-info"])[%d]/p[1]' % articleNumber
        self.TOPIC_INFO_STATUS_TEXT = '(//div[@class="topic-info"])[%d]/p[2]' % articleNumber
        self.TOPIC_AUTHOR = '(//li[@class="topic-info-author"])[%d]/p/a' % articleNumber
        self.COMMENTS = '(//li[@class="topic-info-comments"])[%d]/a' % articleNumber

    def get_comment_title_text(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.TOPIC_TITLE_TEXT).text
        )

    def get_comment_info_source_text(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.TOPIC_INFO_SOURCE_TEXT).text
        )

    def get_comment_info_status_text(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.TOPIC_INFO_STATUS_TEXT).text
        )

    def get_comment_author(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.TOPIC_AUTHOR).text
        )


class Article(Component):
    def __init__(self, driver, articleNumber):
        super(Article, self).__init__(driver)
        self.articleNumber = articleNumber
        self.TOPIC_TITLE_TEXT = '(//h1[@class="topic-title"])[%d]/a' % articleNumber
        self.TOPIC_INFO_SOURCE_TEXT =  '(//div[@class="topic-info"])[%d]/p[1]' % articleNumber
        self.TOPIC_INFO_STATUS_TEXT = '(//div[@class="topic-info"])[%d]/p[2]' % articleNumber
        self.TOPIC_AUTHOR = '(//li[@class="topic-info-author"])[%d]/p/a' % articleNumber
        self.COMMENTS_COUNT = '(//li[@class="topic-info-comments"])[%d]/a' % articleNumber

    def get_article_title_text(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.TOPIC_TITLE_TEXT).text
        )

    def get_article_info_source_text(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.TOPIC_INFO_SOURCE_TEXT).text
        )

    def get_article_info_status_text(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.TOPIC_INFO_STATUS_TEXT).text
        )

    def get_article_author(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.TOPIC_AUTHOR).text
        )
    
    def click_on_link(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.COMMENTS_COUNT)
        )
        self.driver.find_element_by_xpath(self.COMMENTS_COUNT).click()

    def get_id(self):
        return int(re.match(r'\[id=(\d+)\]', self.get_article_title_text()).group(1))

    def get_comments_count(self):
        return int(WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.COMMENTS_COUNT).text
        ))
         

