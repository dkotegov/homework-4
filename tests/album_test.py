# -*- coding: utf-8 -*-

import os

import unittest

from selenium.webdriver import DesiredCapabilities, Remote


class AlbumTest(unittest.TestCase):
    LOGIN = os.environ['LOGIN']
    PASSWORD = os.environ['PASSWORD']

    def setUp(self):
        browser = os.environ.get('BROWSER', 'FIREFOX')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = auth_page.form
        auth_form.open_form()
        auth_form.set_login(self.USEREMAIL)
        auth_form.set_password(self.PASSWORD)
        auth_form.submit()

        user_name = auth_page.top_menu.get_username()
        self.assertEqual(self.USERNAME, user_name)

        create_page = CreatePage(self.driver)
        create_page.open()

        create_form = create_page.form
        create_form.blog_select_open()
        create_form.blog_select_set_option(self.BLOG)
        create_form.set_title(self.TITLE)
        create_form.set_main_text(self.MAIN_TEXT)
        create_form.set_unpublish()
        create_form.submit()

        topic_page = TopicPage(self.driver)
        topic_title = topic_page.topic.get_title()
        topic_text = topic_page.topic.get_text()
        self.assertEqual(self.TITLE, topic_title)
        self.assertEqual(self.MAIN_TEXT, topic_text)

        blog_page = BlogPage(self.driver)
        blog_page.topic.delete()
        topic_title = blog_page.topic.get_title()
        topic_text = blog_page.topic.get_text()
        self.assertNotEqual(self.TITLE, topic_title)
        self.assertNotEqual(self.MAIN_TEXT, topic_text)
