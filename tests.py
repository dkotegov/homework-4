# -*- coding: utf-8 -*-

import os

import unittest
import Pages

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities, Remote


class TestPlan(unittest.TestCase):
    LOGIN = os.environ['LOGIN']
    PASSWORD = os.environ['PASSWORD']

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test(self):
        login_page = Pages.LoginPage(self.driver)
        login_page.open()
        main_page = login_page.login(self.LOGIN, self.PASSWORD)
        post_page = main_page.get_post()
        num_of_likes = post_page.comment_create("<h4></h4>")
        # Проверка на то, не появилось ли возможности
        # проголосовать за свой же коммент
        # при его создании
        self.assertEqual(num_of_likes, 0)

        content_size = post_page.check_last_comment()
        # Тут баг, вообще-то коммент не должен создаваться
        # и в данном тесте проверяется, убран баг или нет
        # Если тест проходит - баг не убран
        self.assertEqual(content_size, 0)

        main_page = Pages.NewPosts(self.driver)
        main_page.open()
        topic_text = "<h></h>"
        main_page.create_post(topic_text)
        main_page.open()
        topic_answer = main_page.check_last_post()
        # Проверяем, создался ли пустой блог
        # (не должен)
        self.assertEqual(topic_answer, topic_text)

        main_page = Pages.MainPage(self.driver)
        main_page.open()
        post_page = main_page.get_post()
        post_page.comment_create("<p></p>")
        content_size = post_page.check_last_comment()
        # Проверяем, есть ли контент у последнего коммента
        self.assertNotEqual(content_size, 0)
