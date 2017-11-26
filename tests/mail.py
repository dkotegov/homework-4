# -*- coding: utf-8 -*-
import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from pages.auth import AuthPage
from pages.main import MainPage


class MailTest(unittest.TestCase):
    USEREMAIL = unicode(os.environ['USEREMAIL'], 'utf-8')
    PASSWORD = unicode(os.environ['PASSWORD'], 'utf-8')
    SUBJECT = 'Subject_test'
    TEXT = 'Text_est'

    send_message = False

    def setUp(self):
        # browser = os.environ.get('BROWSER', 'FIREFOX')
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.send_message = False
        auth_page = AuthPage(self.driver)
        auth_page.sign_in(self.USEREMAIL, self.PASSWORD)




    def tearDown(self):
        if self.send_message is True:
            main_page = MainPage(self.driver)
            main_page.delete_sent()
            main_page.delete_recieve()
        self.driver.quit()

    def test_login(self):
        main_page = MainPage(self.driver)
        self.assertEqual(self.USEREMAIL, main_page.get_username(), "Usernames are not the same")

    def test_send_message(self):
        main_page = MainPage(self.driver)
        self.send_message = main_page.send_message(self.USEREMAIL, self.SUBJECT, self.TEXT)
        to, subject, text = main_page.check_sent_message()
        
        self.assertEqual(self.USEREMAIL, to, "Useremail are not the same")
        self.assertEqual(self.SUBJECT, subject, "Subjects are not the same")
        self.assertEqual(self.TEXT, text, "Text are not the same")

    def test_recieve_message(self):
        main_page = MainPage(self.driver)
        self.send_message = main_page.send_message(self.USEREMAIL, self.SUBJECT, self.TEXT)
        to, subject, text = main_page.check_recieve_message()
        
        self.assertEqual(self.USEREMAIL, to, "Useremail are not the same")
        self.assertEqual(self.SUBJECT, subject, "Subjects are not the same")
        self.assertEqual(self.TEXT, text, "Text are not the same")