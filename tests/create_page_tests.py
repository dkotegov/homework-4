# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from tests.auth_page import authenticate
from tests.create_page import CreatePage
from tests.utils import Test, wait_for_element_load


class CreatePageTest(Test):

    def test(self):
        authenticate(self.driver)
        self.create_page = CreatePage(self.driver)
        self.create_page.open()
        wait_for_element_load(self.driver, (By.XPATH, CreatePage.UNIQUE))


class Test1(CreatePageTest):
    '''Check the blog description'''

    BLOG_DESCRIPTION = u'Выберите блог'

    def test(self):
        super(Test1, self).test()
        blog_description_column = self.create_page.blog_description_column
        description = blog_description_column.get_blog_description()
        self.assertEqual(description, self.BLOG_DESCRIPTION, 'Blog description on create page is incorrect')


class Test2(CreatePageTest):
    '''Check if poll options appear'''

    def test(self):
        super(Test2, self).test()
        topic_options = self.create_page.topic_options
        topic_options.add_poll()
        self.assertTrue(topic_options.is_poll_visible(), 'Poll adding: poll options invisible')


class Test3(CreatePageTest):
    '''Check if answer can be added to poll'''

    def test(self):
        super(Test3, self).test()
        topic_options = self.create_page.topic_options
        topic_options.add_poll()
        old_number = topic_options.count_answers()
        topic_options.add_poll_answer()
        raw_input()
        new_number = topic_options.count_answers()
        self.assertTrue(new_number > old_number, 'Poll additional answer doesn\'t appear')