# coding=utf-8
import re
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from components.base_form import BaseForm


class EmailSendingForm(BaseForm):
    SEND_EMAIL = '//span[@data-id="contact-to-{}"]'
    INVALID_EMAIL = '//div[@data-test-id="error:invalid-addresses"]'
    MY_EMAIL = 'park.test.testovich@mail.ru'
    CORRECT_EMAILS = ['adam404pet@gmail.com', 'headmonster3@yandex.ru']
    WRONG_EMAILS = ['sdvskdvnskldv@mail', 'sdv238y2jkdvn']

    def set_group_correct_recipients(self):
        emails_str = ""
        for i in range(len(self.CORRECT_EMAILS)):
            emails_str += self.CORRECT_EMAILS[i] + "\n"
        self.add_destionation_email(emails_str)

    def check_group_correct_recipients(self):
        for i in range(len(self.CORRECT_EMAILS)):
            span = WebDriverWait(self.driver, 2) \
                .until(lambda driver: driver.find_element_by_xpath(self.SEND_EMAIL.format(i)))
            clean_email_from_ui = re.sub('\s+', '', span.get_attribute('innerHTML'))
            clean_email_from_ui = re.sub(',', '', clean_email_from_ui)
            if clean_email_from_ui != self.CORRECT_EMAILS[i]:
                print 'not correct recipients'
                return False
        print 'correct recipients'
        return True

    def set_correct_recipient(self):
        self.add_destionation_email(self.CORRECT_EMAILS[0])

    def check_correct_recipient(self):
        span = WebDriverWait(self.driver, 2) \
            .until(lambda driver: driver.find_element_by_xpath(self.SEND_EMAIL.format(0)))
        clean_email_from_ui = re.sub('\s+', '', span.get_attribute('innerHTML'))
        clean_email_from_ui = re.sub(',', '', clean_email_from_ui)
        if clean_email_from_ui != self.CORRECT_EMAILS[0]:
            print 'not correct recipient'
            return False
        print 'correct recipient'
        return True

    def set_group_wrong_recipients(self):
        emails_str = ""
        for i in range(len(self.CORRECT_EMAILS)):
            emails_str += self.WRONG_EMAILS[i] + "\n"
        self.add_destionation_email(emails_str)

    def check_wrong_emails(self):
        try:
            div_error = WebDriverWait(self.driver, 10) \
                .until(lambda driver: driver.find_element_by_xpath(self.INVALID_EMAIL))
            print 'error window found'
            return True
        except WebDriverException:
            print 'error window not found'
            return False

    def set_wrong_recipient(self):
        self.add_destionation_email(self.WRONG_EMAILS[0])

    def set_subject_email(self, subject):
        self.click_on_subject_field()
        self.write_some_text(subject)

    def set_message_email(self, message):
        self.click_on_message_field()
        self.write_some_text(message)

    def set_copy_email(self):
        self.click_on_copy_field()
        self.write_some_text(self.MY_EMAIL)

    def checkMessageSentBySubject(self, subject):
        return self.find_letter_by_subject(subject)

    def set_copy_email_correct_recipient(self):
        self.click_on_copy_field()
        self.write_some_text(self.CORRECT_EMAILS[0])

    def set_copy_email_group_wrong_recipients(self, emails):
        emails_str = ""
        for i in range(len(self.WRONG_EMAILS)):
            emails_str += self.WRONG_EMAILS[i] + "\n"
        self.click_on_copy_field()
        self.write_some_text(emails_str)