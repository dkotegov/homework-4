# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


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
            WebDriverWait(self.driver, 100).until(
                lambda driver: driver.find_elements_by_class_name("comment-rendered")
            )
        except:
            return None
        return PostPage(self.driver)

    def create_post(self, text):
        self.driver.find_element_by_xpath('//a[text()="Создать"]').click()
        self.driver.find_element_by_xpath('//a[text()="Топик"]').click()
        self.driver.find_element_by_xpath('//input[@id="id_title"]').send_keys("TestTitle")
        self.driver.find_element_by_xpath('//textarea[@id="id_text"]').send_keys(text)
        self.driver.find_element_by_xpath('//*[@id="id_blog_chzn"]/a/span').click()
        self.driver.find_element_by_xpath('//li[text()="test"]').click()
        self.driver.find_element_by_xpath('//*[@id="topic-form"]/div/button[2]').click()

    def check_last_post(self):
        topic = self.driver.find_element_by_css_selector(".topic-content.text")
        return topic.text


class NewPosts(MainPage):

    url = "http://ftest.tech-mail.ru/feed/new/"


class PostPage(DefPage):

    def comment_create(self, text):
        create_button = self.driver.find_element_by_xpath('//a[text()="Оставить комментарий"]')
        actions = ActionChains(self.driver)
        actions.move_to_element(create_button).perform()
        actions.move_to_element_with_offset(create_button, 0, 100).perform()
        create_button.click()
        self.driver.find_element_by_xpath('//*[@id="id_text"]').send_keys(text)
        self.driver.find_element_by_xpath('//button[text()="добавить"]').click()
        like_action = self.driver.find_elements_by_css_selector(".vote-up")
        likes_before = len(like_action)
        try:
            WebDriverWait(self.driver, 100).until(
                lambda driver: driver.find_elements_by_xpath('//span[text()="1 секунду назад"]')
                or driver.find_elements_by_xpath('//span[text()="0 секунд назад"]')
            )
            like_action_after = self.driver.find_elements_by_css_selector(".vote-up")
            return len(like_action_after) - likes_before
        except:
            print("Comment wasn't created")

    def check_last_comment(self):
        comments = self.driver.find_elements_by_class_name("comment-rendered")
        if len(comments) > 0:
            comment = comments[-1]
            return comment.size['height']

