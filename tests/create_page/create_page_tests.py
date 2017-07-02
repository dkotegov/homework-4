# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from tests.auth import authenticate, logout
from tests.create_page.create_page import CreatePage
from tests.utils import Test, wait_for_element_load


class CreatePageTests(Test):
    BLOG_DESCRIPTION = u'Выберите блог'

    def setUp(self):
        super(CreatePageTests, self).setUp()
        authenticate(self.driver)
        self.create_page = CreatePage(self.driver)
        self.create_page.open()
        wait_for_element_load(self.driver, (By.XPATH, CreatePage.UNIQUE))

    def test_blog_description(self):
        '''Check the blog description'''
        blog_description_column = self.create_page.blog_description_column
        description = blog_description_column.get_blog_description()
        self.assertEqual(description, self.BLOG_DESCRIPTION, 'Blog description on create page is incorrect')

    def test_poll_options_appear(self):
        '''Check if poll options appear'''
        topic_options = self.create_page.topic_options
        topic_options.add_poll()
        self.assertTrue(topic_options.is_poll_visible(), 'Poll adding: poll options invisible')

    def test_add_poll_answer(self):
        '''Check if answer can be added to poll'''
        topic_options = self.create_page.topic_options
        topic_options.add_poll()
        old_number = topic_options.count_answers()
        topic_options.add_poll_answer()
        new_number = topic_options.count_answers()
        difference = new_number - old_number
        self.assertEqual(difference, 1, 'Poll additional answer doesn\'t appear')
