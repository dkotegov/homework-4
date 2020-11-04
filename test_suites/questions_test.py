from selenium import webdriver
import unittest
from selenium.common.exceptions import TimeoutException

from pages.auth_page import AuthPage
from pages.ask_page import AskPage


class QuestionsTests(unittest.TestCase):
    TOPIC = 'Какую породу собаки выбрать?'
    LONG_TOPIC = 'a' * 121
    TEXT = 'Помогите выбрать породу'
    LONG_TEXT = 'a' * 3801
    IMAGE_LINK = 'https://cs.pikabu.ru/post_img/2013/05/04/11/1367689620_1544760345.jpg'
    WRONG_IMAGE_LINK = 'https://google.com'

    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')

        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_page.login()

    def tearDown(self):
        self.driver.quit()

    def test_question_topic(self):
        ask_page = AskPage(self.driver)
        ask_page.open()
        ask_page.set_topic(self.TOPIC)
        ask_page.publish_question()
        self.assertEqual(ask_page.question_topic, self.TOPIC)

    def test_empty_topic(self):
        ask_page = AskPage(self.driver)
        ask_page.open()
        ask_page.set_text(self.TEXT)
        ask_page.set_category()
        ask_page.set_subcategory()
        self.assertEqual(ask_page.is_button_disabled, True)

    def test_long_topic_error(self):
        ask_page = AskPage(self.driver)
        ask_page.open()
        ask_page.set_topic(self.LONG_TOPIC)
        self.assertEqual(ask_page.topic_has_error, True)

    def test_long_topic_button_disabled(self):
        ask_page = AskPage(self.driver)
        ask_page.open()
        ask_page.set_topic(self.LONG_TOPIC)
        self.assertEqual(ask_page.is_button_disabled, True)

    def test_long_text_error(self):
        ask_page = AskPage(self.driver)
        ask_page.open()
        ask_page.set_text(self.LONG_TEXT)
        self.assertEqual(ask_page.text_has_error, True)

    def test_long_text_button_disabled(self):
        ask_page = AskPage(self.driver)
        ask_page.open()
        ask_page.set_topic(self.TOPIC)
        ask_page.set_text(self.LONG_TEXT)
        ask_page.set_category()
        ask_page.set_subcategory()
        self.assertEqual(ask_page.is_button_disabled, True)

    def test_attach_image_from_computer(self):
        ask_page = AskPage(self.driver)
        ask_page.open()
        ask_page.attach_photo_from_computer()
        self.assertEqual(ask_page.is_media_attached, True)

    def test_attach_image_by_link(self):
        ask_page = AskPage(self.driver)
        ask_page.open()
        ask_page.attach_photo_by_link(self.IMAGE_LINK)
        self.assertEqual(ask_page.is_media_attached, True)

    def test_attach_image_by_link_error(self):
        ask_page = AskPage(self.driver)
        ask_page.open()
        ask_page.attach_photo_by_link(self.WRONG_MEDIA_LINK)
        self.assertEqual(ask_page.has_error_modal, True)

    def test_attach_video_from_computer(self):
        ask_page = AskPage(self.driver)
        ask_page.open()
        try:
            ask_page.attach_video_from_computer()
        except TimeoutException:
            self.fail()
