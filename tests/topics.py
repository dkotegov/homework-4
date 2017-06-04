# -*- coding: utf-8 -*-
import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from pages.auth import *
from pages.create_topic import *
from pages.main import *
from pages.remove_topic import *
from pages.show_topic import *


class TopicsTest(unittest.TestCase):
    USERNAME = unicode(os.environ['USERNAME'], 'utf-8')
    USEREMAIL = unicode(os.environ['USEREMAIL'], 'utf-8')
    PASSWORD = unicode(os.environ['PASSWORD'], 'utf-8')
    DEFAULT_BLOG_TITLE = 'Флудилка'
    U_DEFAULT_BLOG_TITLE = unicode('Флудилка', 'utf-8')
    DEFAULT_TOPIC_TITLE = 'Topic Title'
    TOPIC_SIMPLE_TEXT = 'Some simple text'
    TOPIC_SIMPLE_H4 = 'H4 header'
    TOPIC_SIMPLE_H5 = 'H5 header'
    TOPIC_SIMPLE_H6 = 'H6 header'
    TOPIC_SIMPLE_BOLD = 'Bold text'
    TOPIC_SIMPLE_ITALIC = 'Italic text'
    TOPIC_SIMPLE_STROKE = 'Stroke text'
    TOPIC_SIMPLE_UNDERLINE = 'Underline text'
    TOPIC_SIMPLE_QUOTE = 'Quote text'
    TOPIC_SIMPLE_CODE = 'Code'
    TOPIC_SIMPLE_LI = 'Li element'
    TOPIC_SIMPLE_LINK = 'Link Text'
    TOPIC_SIMPLE_PICTURE = 'https://example.com/image.jpeg'
    TOPIC_POLL_HEADER = 'Poll header'
    TOPIC_POLL_FIRST_ANSWER = 'First answer'
    TOPIC_POLL_SECOND_ANSWER = 'Second answer'
    TOPIC_SIMPLE_VIDEO = 'https://www.youtube.com/watch?v=ZEA1Lf38deY'
    TOPIC_SIMPLE_EMBED_VIDEO = unicode('https://www.youtube.com/embed/ZEA1Lf38deY?rel=0', 'utf-8')

    created_topic = None

    def setUp(self):
        # browser = os.environ.get('BROWSER', 'FIREFOX')
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            # command_executor='http://127.0.0.1:4444/wd/hub',
            command_executor='http://192.168.0.102:5555/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        try:
            auth_page = AuthPage(self.driver)
            auth_page.sign_in(self.USEREMAIL, self.PASSWORD)
            main_page = MainPage(self.driver)
            self.assertEqual(self.USERNAME, main_page.get_username(), "Usernames are not the same")
        except Exception as e:
            self.driver.quit()
            raise

    def tearDown(self):
        if self.created_topic is not None:
            remove_page = RemoveTopicPage(self.driver, self.created_topic)
            remove_page.navigate()
            remove_page.submit_remove()
        self.driver.quit()

    def test_create_simple_topic(self):
        create_page = CreateTopicPage(self.driver)
        create_page.navigate()

        self.created_topic = create_page \
            .choose_blog(self.DEFAULT_BLOG_TITLE) \
            .set_title(self.DEFAULT_TOPIC_TITLE) \
            .add_text(self.TOPIC_SIMPLE_TEXT) \
            .create()

        topic_page = ShowTopicPage(self.driver, self.created_topic)
        topic_page.navigate()
        self.assertEqual(topic_page.get_topic_blog_name(), self.U_DEFAULT_BLOG_TITLE)
        self.assertEqual(topic_page.get_topic_title(), self.DEFAULT_TOPIC_TITLE)

        content = topic_page.get_topic_content_el().get().text
        self.assertEqual(content, self.TOPIC_SIMPLE_TEXT)

    def test_not_creating_with_empty_fields(self):
        create_page = CreateTopicPage(self.driver)
        create_page.navigate()

        create_page \
            .choose_blog(self.DEFAULT_BLOG_TITLE) \
            .set_title(self.DEFAULT_TOPIC_TITLE) \
            .click_create_button() \
            .check_error_notice()

    def test_create_topic_with_diff_size_font(self):
        create_page = CreateTopicPage(self.driver)
        create_page.navigate()

        self.created_topic = create_page \
            .choose_blog(self.DEFAULT_BLOG_TITLE) \
            .set_title(self.DEFAULT_TOPIC_TITLE) \
            .add_text(self.TOPIC_SIMPLE_H4, 'h4') \
            .add_text(self.TOPIC_SIMPLE_H5, 'h5') \
            .add_text(self.TOPIC_SIMPLE_H6, 'h6') \
            .add_text(self.TOPIC_SIMPLE_TEXT) \
            .create()

        topic_page = ShowTopicPage(self.driver, self.created_topic)
        topic_page.navigate()
        topic_content = topic_page.get_topic_content_el()
        self.assertEqual(topic_content.get_h4(), self.TOPIC_SIMPLE_H4)
        self.assertEqual(topic_content.get_h5(), self.TOPIC_SIMPLE_H5)
        self.assertEqual(topic_content.get_h6(), self.TOPIC_SIMPLE_H6)

    def test_create_topic_with_disabled_comments(self):
        create_page = CreateTopicPage(self.driver)
        create_page.navigate()

        self.created_topic = create_page \
            .choose_blog(self.DEFAULT_BLOG_TITLE) \
            .set_title(self.DEFAULT_TOPIC_TITLE) \
            .add_text(self.TOPIC_SIMPLE_TEXT) \
            .disable_comments() \
            .create()

        topic_page = ShowTopicPage(self.driver, self.created_topic)
        topic_page.navigate()
        topic_page.check_if_add_comment_button_is_not_exists()

    def test_create_topic_with_diff_fonts(self):
        create_page = CreateTopicPage(self.driver)
        create_page.navigate()

        self.created_topic = create_page \
            .choose_blog(self.DEFAULT_BLOG_TITLE) \
            .set_title(self.DEFAULT_TOPIC_TITLE) \
            .add_text(self.TOPIC_SIMPLE_BOLD, 'bold') \
            .add_text(self.TOPIC_SIMPLE_ITALIC, 'italic') \
            .add_text(self.TOPIC_SIMPLE_STROKE, 'stroke') \
            .add_text(self.TOPIC_SIMPLE_UNDERLINE, 'underline') \
            .add_text(self.TOPIC_SIMPLE_QUOTE, 'quote') \
            .add_text(self.TOPIC_SIMPLE_CODE, 'code') \
            .create()

        topic_page = ShowTopicPage(self.driver, self.created_topic)
        topic_page.navigate()
        topic_content = topic_page.get_topic_content_el()
        self.assertEqual(topic_content.get_strong(), self.TOPIC_SIMPLE_BOLD)
        self.assertEqual(topic_content.get_italic(), self.TOPIC_SIMPLE_ITALIC)
        self.assertEqual(topic_content.get_stroke(), self.TOPIC_SIMPLE_STROKE)
        self.assertEqual(topic_content.get_underline(), self.TOPIC_SIMPLE_UNDERLINE)
        self.assertEqual(topic_content.get_blockquote(), self.TOPIC_SIMPLE_QUOTE)
        self.assertEqual(topic_content.get_code(), self.TOPIC_SIMPLE_CODE)

    def test_create_topic_with_diff_lists(self):
        create_page = CreateTopicPage(self.driver)
        create_page.navigate()
        self.created_topic = create_page \
            .choose_blog(self.DEFAULT_BLOG_TITLE) \
            .set_title(self.DEFAULT_TOPIC_TITLE) \
            .add_text(self.TOPIC_SIMPLE_LI, 'ul') \
            .add_text(self.TOPIC_SIMPLE_LI, 'ol') \
            .create()

        topic_page = ShowTopicPage(self.driver, self.created_topic)
        topic_page.navigate()
        topic_content = topic_page.get_topic_content_el()
        self.assertEqual(topic_content.get_unordered_list(), self.TOPIC_SIMPLE_LI)
        self.assertEqual(topic_content.get_ordered_list(), self.TOPIC_SIMPLE_LI)

    def test_create_topic_with_link(self):
        create_page = CreateTopicPage(self.driver)
        create_page.navigate()

        self.created_topic = create_page \
            .choose_blog(self.DEFAULT_BLOG_TITLE) \
            .set_title(self.DEFAULT_TOPIC_TITLE) \
            .add_text(self.TOPIC_SIMPLE_LINK, 'link') \
            .create()

        topic_page = ShowTopicPage(self.driver, self.created_topic)
        topic_page.navigate()
        topic_content = topic_page.get_topic_content_el()
        self.assertEqual(topic_content.get_link(), self.TOPIC_SIMPLE_LINK)

    def test_create_topic_with_poll(self):
        create_page = CreateTopicPage(self.driver)
        create_page.navigate()

        self.created_topic = create_page \
            .choose_blog(self.DEFAULT_BLOG_TITLE) \
            .set_title(self.DEFAULT_TOPIC_TITLE) \
            .add_text(self.TOPIC_SIMPLE_TEXT) \
            .add_poll(self.TOPIC_POLL_HEADER, self.TOPIC_POLL_FIRST_ANSWER, self.TOPIC_POLL_SECOND_ANSWER) \
            .create()

        topic_page = ShowTopicPage(self.driver, self.created_topic)
        topic_page.navigate()
        self.assertEqual(topic_page.get_topic_poll_title(), self.TOPIC_POLL_HEADER)
        poll_answers = topic_page.get_topic_poll_answers()
        self.assertEqual(poll_answers[0], self.TOPIC_POLL_FIRST_ANSWER)
        self.assertEqual(poll_answers[1], self.TOPIC_POLL_SECOND_ANSWER)

    def test_create_topic_with_picture(self):
        create_page = CreateTopicPage(self.driver)
        create_page.navigate()

        self.created_topic = create_page \
            .choose_blog(self.DEFAULT_BLOG_TITLE) \
            .set_title(self.DEFAULT_TOPIC_TITLE) \
            .add_picture(self.TOPIC_SIMPLE_PICTURE) \
            .create()

        topic_page = ShowTopicPage(self.driver, self.created_topic)
        topic_page.navigate()
        topic_content = topic_page.get_topic_content_el()
        self.assertEqual(topic_content.get_image(), self.TOPIC_SIMPLE_PICTURE)

    def test_create_topic_with_video(self):
        create_page = CreateTopicPage(self.driver)
        create_page.navigate()

        self.created_topic = create_page \
            .choose_blog(self.DEFAULT_BLOG_TITLE) \
            .set_title(self.DEFAULT_TOPIC_TITLE) \
            .add_video(self.TOPIC_SIMPLE_VIDEO) \
            .create()

        topic_page = ShowTopicPage(self.driver, self.created_topic)
        topic_page.navigate()
        topic_content = topic_page.get_topic_content_el()
        self.assertEqual(topic_content.get_embed_video(), self.TOPIC_SIMPLE_EMBED_VIDEO)
