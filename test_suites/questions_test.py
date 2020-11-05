import os
from selenium import webdriver
import unittest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import DesiredCapabilities, Remote

from pages.auth_page import AuthPage
from pages.ask_page import AskPage
from pages.show_question_page import QuestionPage


class QuestionsTests(unittest.TestCase):
    FIRST_USER = (os.environ['LOGIN_1'], os.environ['PASSWORD_1'])
    SECOND_USER = (os.environ['LOGIN_2'], os.environ['PASSWORD_2'])
    THIRD_USER = (os.environ['LOGIN_3'], os.environ['PASSWORD_3'])

    TOPIC = 'Какую породу собаки выбрать?'
    LONG_TOPIC = 'a' * 121
    TEXT = 'Помогите выбрать породу'
    LONG_TEXT = 'a' * 3801
    CATEGORY = 'Животные, Растения'
    SUBCATEGORY = 'Домашние животные'
    IMAGE_LINK = 'https://cs.pikabu.ru/post_img/2013/05/04/11/1367689620_1544760345.jpg'
    WRONG_IMAGE_LINK = 'https://google.com'
    QUESTION_URL = None
    ANSWER = 'Пекинеса'

    @classmethod
    def setUpClass(cls) -> None:
        browser_name = os.environ.get('BROWSER', 'CHROME')
        driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser_name).copy()
        )

        auth_page = AuthPage(driver)
        auth_page.open()
        auth_page.login(*QuestionsTests.THIRD_USER)

        ask_page = AskPage(driver)
        ask_page.open()
        ask_page.set_topic(QuestionsTests.TOPIC)
        ask_page.set_text(QuestionsTests.TEXT)
        ask_page.set_category()
        ask_page.set_subcategory()
        QuestionsTests.QUESTION_URL = ask_page.publish_question()
        driver.quit()

    def setUp(self) -> None:
        browser_name = os.environ.get('BROWSER', 'CHROME')

        self.browser = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser_name).copy()
        )

        name = self.shortDescription()
        if name != 'skip_setup_login':
            auth_page = AuthPage(self.driver)
            auth_page.open()
            auth_page.login(*self.SECOND_USER)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_question_topic(self):
        question_page = QuestionPage(self.driver, QuestionsTests.QUESTION_URL)
        question_page.open()
        self.assertEqual(question_page.get_topic(), self.TOPIC)

    def test_empty_topic(self):
        ask_page = AskPage(self.driver)
        ask_page.open()
        ask_page.set_text(self.TEXT)
        ask_page.set_category()
        ask_page.set_subcategory()
        self.assertEqual(ask_page.is_button_disabled(), True)

    def test_long_topic_error(self):
        ask_page = AskPage(self.driver)
        ask_page.open()
        ask_page.set_topic(self.LONG_TOPIC)
        self.assertEqual(ask_page.topic_has_error(), True)

    def test_long_topic_button_disabled(self):
        ask_page = AskPage(self.driver)
        ask_page.open()
        ask_page.set_topic(self.LONG_TOPIC)
        self.assertEqual(ask_page.is_button_disabled(), True)

    def test_question_text(self):
        question_page = QuestionPage(self.driver, QuestionsTests.QUESTION_URL)
        question_page.open()
        self.assertEqual(question_page.get_text(), self.TEXT)

    def test_long_text_error(self):
        ask_page = AskPage(self.driver)
        ask_page.open()
        ask_page.set_text(self.LONG_TEXT)
        self.assertEqual(ask_page.text_has_error(), True)

    def test_long_text_button_disabled(self):
        ask_page = AskPage(self.driver)
        ask_page.open()
        ask_page.set_topic(self.TOPIC)
        ask_page.set_text(self.LONG_TEXT)
        ask_page.set_category()
        ask_page.set_subcategory()
        self.assertEqual(ask_page.is_button_disabled(), True)

    def test_attach_image_from_computer(self):
        ask_page = AskPage(self.driver)
        ask_page.open()
        ask_page.attach_photo_from_computer()
        self.assertEqual(ask_page.is_media_attached(), True)

    def test_attach_image_by_link(self):
        ask_page = AskPage(self.driver)
        ask_page.open()
        ask_page.attach_photo_by_link(self.IMAGE_LINK)
        self.assertEqual(ask_page.is_media_attached(), True)

    def test_attach_image_by_link_error(self):
        ask_page = AskPage(self.driver)
        ask_page.open()
        ask_page.attach_photo_by_link(self.WRONG_IMAGE_LINK)
        self.assertEqual(ask_page.has_error_modal(), True)

    def test_attach_video_from_computer(self):
        ask_page = AskPage(self.driver)
        ask_page.open()
        try:
            ask_page.attach_video_from_computer()
        except TimeoutException:
            self.fail()

    def test_category(self):
        question_page = QuestionPage(self.driver, QuestionsTests.QUESTION_URL)
        question_page.open()
        self.assertEqual(question_page.get_category(), self.CATEGORY)

    def test_subcategory(self):
        question_page = QuestionPage(self.driver, QuestionsTests.QUESTION_URL)
        question_page.open()
        self.assertEqual(question_page.get_subcategory(), self.SUBCATEGORY)

    def test_answer_empty_field(self):
        question_page = QuestionPage(self.driver, QuestionsTests.QUESTION_URL)
        question_page.open()
        self.assertEqual(question_page.is_submit_button_disabled(), True)

    def test_answer_long_text_error(self):
        question_page = QuestionPage(self.driver, QuestionsTests.QUESTION_URL)
        question_page.open()
        question_page.set_answer(self.LONG_TEXT)
        self.assertEqual(question_page.answer_input_has_error(), True)

    def test_answer_long_text_button_disabled(self):
        question_page = QuestionPage(self.driver, QuestionsTests.QUESTION_URL)
        question_page.open()
        question_page.set_answer(self.LONG_TEXT)
        self.assertEqual(question_page.is_submit_button_disabled(), True)

    def test_answer(self):
        """skip_setup_login"""
        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_page.login(*self.FIRST_USER)

        question_page = QuestionPage(self.driver, QuestionsTests.QUESTION_URL)
        question_page.open()
        question_page.set_answer(self.ANSWER)
        question_page.send_answer()
        self.assertEqual(question_page.contains_answer(self.ANSWER), True)
