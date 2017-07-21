# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from tests.auth import TestWithAuth
from tests.create_page.create_page import CreatePage
from tests.utils import wait_for_element_load


class CreatePageTests(TestWithAuth):
    BLOG_DESCRIPTION = u'Выберите блог'
    TOPIC_TITLE = u'Qwerty123'
    TOPIC_TEXT = u'Qwwwwwwerty'

    def setUp(self):
        super(CreatePageTests, self).setUp()
        self.create_page = CreatePage(self.driver)
        self.create_page.open()
        wait_for_element_load(self.driver, (By.XPATH, CreatePage.UNIQUE))

    def test_blog_description(self):
        """Check the blog description"""

        blog_description_column = self.create_page.blog_description_column
        description = blog_description_column.get_blog_description()
        self.assertEqual(description, self.BLOG_DESCRIPTION, 'Blog description on create page is incorrect')

    def _add_poll(self):
        self.create_page.topic_options.add_poll()

    def test_poll_options_appear(self):
        """Check if poll options appear"""

        self._add_poll()
        self.assertTrue(self.create_page.topic_options.is_poll_visible(), 'Poll adding: poll options invisible')

    def test_add_poll_answer(self):
        """Check if answer can be added to poll"""

        self._add_poll()
        to = self.create_page.topic_options
        old_number = to.count_answers()
        to.add_poll_answer()
        new_number = to.count_answers()
        difference = new_number - old_number
        self.assertEqual(difference, 1, 'Poll additional answer doesn\'t appear')

    def test_preview(self):
        """Check the topic header in preview"""

        to = self.create_page.topic_options
        to.set_title(self.TOPIC_TITLE)
        to.set_main_text(self.TOPIC_TEXT)
        to.show_preview()
        self.assertEqual(to.get_previewed_header(), self.TOPIC_TITLE, 'Topic title preview is incorrect!')
        self.assertEqual(to.get_previewed_text(), self.TOPIC_TEXT, 'Topic text preview is incorrect!')
