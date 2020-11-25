import unittest
import os

from selenium.webdriver import DesiredCapabilities, Remote

from pages.common import Common
from pages.question_page import QuestionPage
from pages.notif_page import NotificationPage


class NotificationTests(unittest.TestCase):
    LOGIN_1 = os.environ.get('LOGIN_1')
    PASSWORD_1 = os.environ.get('PASSWORD_1')
    LOGIN_2 = os.environ.get('LOGIN_2')
    PASSWORD_2 = os.environ.get('PASSWORD_2')
    QUESTION_TOPIC = os.environ.get('QUESTION')
    QUESTION_TEXT = ""
    ANSWER = os.environ.get('ANSWER')
    COMMENT = 'хороший ответ'
    ANSWER_NOTIF = 'ответ'
    LIKE_QUESTION_NOTIF = 'Понравился ваш вопрос'
    LIKE_ANSWER_NOTIF = 'Понравился ваш ответ'
    COMMENT_NOTIF = "Новые комментарии"

    browser = None
    cmn = None
    question = None
    notif = None
    question_url = None

    @classmethod
    def setUpClass(cls) -> None:
        browser_name = os.environ.get('BROWSER', 'CHROME')

        NotificationTests.browser = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser_name).copy()
        )
        NotificationTests.cmn = Common(NotificationTests.browser)
        NotificationTests.question = QuestionPage(NotificationTests.browser)
        NotificationTests.notif = NotificationPage(NotificationTests.browser)

        NotificationTests.cmn.login(NotificationTests.LOGIN_1, NotificationTests.PASSWORD_1)
        NotificationTests.question_url = NotificationTests.question.ask_question(NotificationTests.QUESTION_TOPIC,
                                                                                 NotificationTests.QUESTION_TEXT)
        NotificationTests.cmn.logout()

    def test_notification_for_answer_to_question(self):
        self.cmn.login(self.LOGIN_2, self.PASSWORD_2)
        self.question.answer_question(self.question_url, self.ANSWER)
        self.cmn.logout()

        self.cmn.login(self.LOGIN_1, self.PASSWORD_1)
        self.notif.check_notification(self.ANSWER_NOTIF)

    def test_notification_for_like_to_question(self):
        self.cmn.login(self.LOGIN_2, self.PASSWORD_2)
        self.question.like_question(self.question_url)
        self.cmn.logout()

        self.cmn.login(self.LOGIN_1, self.PASSWORD_1)
        self.notif.check_notification(self.LIKE_QUESTION_NOTIF)

    def test_notification_for_like_to_answer(self):
        self.cmn.login(self.LOGIN_1, self.PASSWORD_1)
        self.question.like_answer(self.question_url, self.ANSWER)
        self.cmn.logout()

        self.cmn.login(self.LOGIN_2, self.PASSWORD_2)
        self.notif.check_notification(self.LIKE_ANSWER_NOTIF)

    def test_notification_for_comment_to_answer(self):
        self.cmn.login(self.LOGIN_1, self.PASSWORD_1)
        self.question.comment_answer(self.question_url, self.ANSWER, self.COMMENT)
        self.cmn.logout()

        self.cmn.login(self.LOGIN_2, self.PASSWORD_2)
        self.notif.check_notification(self.COMMENT_NOTIF)

    def tearDown(self):
        self.cmn.logout()

    @classmethod
    def tearDownClass(cls):
        NotificationTests.browser.quit()
