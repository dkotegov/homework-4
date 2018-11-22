from pages import email_sending_page
from pages.email_sending_page import EmailSendingPage
from tests.base_test import BaseTest


class BaseSend(BaseTest):
    TEXT = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit,\n sed do eiusmod tempor incididunt ut labore et.'
    SUBJECT = 'Test subject'

    def test(self):
        BaseTest.test(self)
        self.email_sending_page = EmailSendingPage(self.driver)
        self.email_sending_form = self.email_sending_page.form
        self.email_sending_page.redirectQA()
