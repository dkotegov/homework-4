import unittest
import os

from selenium.webdriver import DesiredCapabilities, Remote

from pages.common import Common
from pages.question_page import QuestionPage
from pages.notif_page import NotificationPage


class NotificationTests(unittest.TestCase):
    # browser = webdriver.Chrome('./chromedriver')
    question_topic = "Что означает, что двигатель троит?"
    question_text = ""
    answer = "один из цилиндров мотора не работает"
    like = "Понравился"

    login_1 = os.environ.get('LOGIN_1')
    password_1 = os.environ.get('PASSWORD_1')
    login_2 = os.environ.get('LOGIN_2')
    password_2 = os.environ.get('PASSWORD_2')

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

        NotificationTests.cmn.login(NotificationTests.login_1, NotificationTests.password_1)
        NotificationTests.question_url = NotificationTests.question.ask_question(NotificationTests.question_topic,
                                                                                 NotificationTests.question_text)
        NotificationTests.cmn.logout()

    def test_notification_for_answer_to_question(self):
        self.cmn.login(self.login_2, self.password_2)
        self.question.answer_question(self.question_url, self.answer)
        self.cmn.logout()

        self.cmn.login(self.login_1, self.password_1)
        self.notif.check_notification(self.question_topic)
        self.cmn.logout()

    def test_notification_for_like_to_question(self):
        self.cmn.login(self.login_2, self.password_2)
        self.question.like_question(self.question_url)
        self.cmn.logout()

        self.cmn.login(self.login_1, self.password_1)
        self.notif.check_notification(self.like)
        self.cmn.logout()

    @classmethod
    def tearDownClass(cls):
        NotificationTests.browser.quit()
