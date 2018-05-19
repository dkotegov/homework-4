# -*- coding: utf-8 -*-
import os

import unittest

from tests.pages.auth import AuthPage
from tests.pages.main import MainPage
from tests.pages.message import MessagePage
from tests.pages.dialog import DialogPage
from tests.pages.dialog_menu import DialogMenuPage
from tests.pages.confirm import ConfirmPage

from selenium.webdriver import DesiredCapabilities, Remote


class TestsSendMessages(unittest.TestCase):

    def setUp(self):
        browser = os.environ.get('BROWSER', os.environ['BROWSER'])

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.driver.maximize_window()

        self.BOT_1_LOGIN = "technopark3"
        self.PASSWORD = os.environ['PASSWORD']
        self.CURRENT_DIALOG_URL = ""

        self.USUAL_MESSAGE_TEXT = 'USUAL TEXT'
        self.CHINESE_TEXT = u'測試漢字'
        self.EMPTY_MESSAGE_TEXT = ''
        self.LONG_VALID_MESSAGE = '_123' * 512
        self.LONG_INVALID_MESSAGE = '_123' * 1024
        self.MESSAGE_EDITED_TEXT = ' IS_EDITED'
        self.MESSAGE_ANSWERED_TEXT = ' IS_ANSWERED'

        self.dialog_page = DialogPage(self.driver)
        self.message_page = MessagePage(self.driver)
        self.auth_page = AuthPage(self.driver)
        self.auth_page.sign_in(self.BOT_1_LOGIN, self.PASSWORD)
        self.main_page = MainPage(self.driver)
        self.main_page.open_messages()
        self.create_dialog()
        self.CURRENT_DIALOG_URL = self.driver.current_url

    def tearDown(self):
        self.driver.get(self.CURRENT_DIALOG_URL)
        self.delete_dialog()
        self.driver.quit()

    def create_dialog(self):
        self.message_page.create_dialog()
        self.message_page.choose_companion()
        self.dialog_page.wait_for_loader()

    def delete_dialog(self):
        self.dialog_page.open_menu()
        dilog_menu_page = DialogMenuPage(self.driver)
        dilog_menu_page.delete_dialog()
        confirm_page = ConfirmPage(self.driver)
        confirm_page.confirm()

    def test_send_usual_message(self):
        self.dialog_page.send_message(self.USUAL_MESSAGE_TEXT)
        self.assertTrue(
            self.dialog_page.sent_message_exists(),
            "test send usual message failed")

    def test_send_empty_message(self):
        self.dialog_page.send_message(self.EMPTY_MESSAGE_TEXT)
        self.assertFalse(
            self.dialog_page.sent_message_exists(),
            "test send empty message failed")

    def test_send_unicode_message(self):
        self.dialog_page.send_message(self.CHINESE_TEXT)
        self.assertTrue(
            self.dialog_page.sent_message_exists(),
            "test send unicode message failed")

    def test_send_long_valid_message(self):
        self.dialog_page.send_message(self.LONG_VALID_MESSAGE)
        self.assertTrue(
            self.dialog_page.sent_message_exists(),
            "test send long valid message failed")

    def test_send_long_invalid_message(self):
        self.dialog_page.send_message(self.LONG_INVALID_MESSAGE)
        self.assertTrue(
            self.dialog_page.long_message_error_exists(),
            "test send long invalid message failed")

    def test_usual_edit_usual_message(self):
        self.dialog_page.send_message(self.USUAL_MESSAGE_TEXT)
        self.dialog_page.edit_and_send_message(self.MESSAGE_EDITED_TEXT)
        self.driver.refresh()
        self.assertEquals(
            self.dialog_page.get_sent_message_text(),
            self.USUAL_MESSAGE_TEXT + self.MESSAGE_EDITED_TEXT)

    def test_empty_edit_unicode_message(self):
        self.dialog_page.send_message(self.CHINESE_TEXT)
        self.dialog_page.edit_and_send_message(self.EMPTY_MESSAGE_TEXT)
        self.driver.refresh()
        self.assertEquals(
            self.dialog_page.get_sent_message_text(),
            self.CHINESE_TEXT + self.EMPTY_MESSAGE_TEXT)

    def test_unicode_edit_unicode_message(self):
        self.dialog_page.send_message(self.CHINESE_TEXT)
        self.dialog_page.edit_and_send_message(self.CHINESE_TEXT)
        self.driver.refresh()
        self.assertEquals(
            self.dialog_page.get_sent_message_text(),
            self.CHINESE_TEXT + self.CHINESE_TEXT)

    def test_usual_answer_unicode_message(self):
        self.dialog_page.send_message(self.CHINESE_TEXT)
        self.dialog_page.answer_message(self.MESSAGE_ANSWERED_TEXT)
        self.driver.refresh()
        self.assertTrue(
            self.dialog_page.get_exsistance_of_answered_message(),
            "test_usual_answer_message failed")

    def test_unicode_answer_usual_message(self):
        self.dialog_page.send_message(self.USUAL_MESSAGE_TEXT)
        self.dialog_page.answer_message(self.CHINESE_TEXT)
        self.driver.refresh()
        self.assertTrue(
            self.dialog_page.get_exsistance_of_answered_message(),
            "test_unicode_answer_message failed")

    def test_forward_usual_message(self):
        self.dialog_page.send_message(self.USUAL_MESSAGE_TEXT)
        self.dialog_page.forward_message()
        self.message_page.choose_companion_forward_message()
        self.driver.refresh()
        self.assertTrue(
            self.dialog_page.get_exsistance_of_forwarded_message(),
            "test_forward_message failed")

    def test_forward_unicode_message(self):
        self.dialog_page.send_message(self.CHINESE_TEXT)
        self.dialog_page.forward_message()
        self.message_page.choose_companion_forward_message()
        self.driver.refresh()
        self.assertTrue(
            self.dialog_page.get_exsistance_of_forwarded_message(),
            "test_forward_message failed")

    # def test_forward_long_valid_message(self):
    #     LOOP_TEXT = '_123'
    #     LOOP_TEXT *= 512
    #     self.dialog_page.send_message(LOOP_TEXT)
    #     self.dialog_page.forward_message()
    #     self.message_page.choose_companion_forward_message()
    #     self.driver.refresh()
    #     self.assertTrue(
    #         self.dialog_page.get_exsistance_of_forwarded_message(),
    #         "test_forward_message failed")

    def test_delete_usual_message(self):
        self.dialog_page.send_message(self.USUAL_MESSAGE_TEXT)
        self.dialog_page.delete_message()
        self.driver.refresh()
        self.assertTrue(
            self.dialog_page.no_messages_text_exists(),
            "test_delete_message failed")

    # def test_delete_long_valid_message(self):
    #     LOOP_TEXT = '_123'
    #     LOOP_TEXT *= 512
    #     self.dialog_page.send_message(LOOP_TEXT)
    #     self.dialog_page.delete_message()
    #     self.driver.refresh()
    #     self.assertTrue(
    #         self.dialog_page.no_messages_text_exists(),
    #         "test_delete_message failed")

    # def test_delete_long_invalid_message(self):
    #     LOOP_TEXT = '_123'
    #     LOOP_TEXT *= 1024
    #     self.dialog_page.send_message(LOOP_TEXT)
    #     self.dialog_page.delete_message()
    #     self.driver.refresh()
    #     self.assertTrue(
    #         self.dialog_page.no_messages_text_exists(),
    #         "test_delete_message failed")
