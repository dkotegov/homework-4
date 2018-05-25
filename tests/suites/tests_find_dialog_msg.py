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


class TestsFindDialogMsg(unittest.TestCase):

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

        self.dialog_page = DialogPage(self.driver)
        self.message_page = MessagePage(self.driver)
        self.auth_page = AuthPage(self.driver)
        self.auth_page.sign_in(self.BOT_1_LOGIN, self.PASSWORD)
        self.main_page = MainPage(self.driver)
        self.main_page.open_messages()

        self.MESSAGE_TEXT = "testNumber1"
        self.RED_POWER = u"☭☭☭☭☭☭"
        self.URL_OF_MESSAGES = "https://ok.ru/messages"

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

    def test_find_message(self):
        self.dialog_page.send_message(self.MESSAGE_TEXT)
        self.dialog_page.find_message(self.MESSAGE_TEXT)
        self.assertEquals(
            self.MESSAGE_TEXT,
            self.message_page.get_found_message_text())

    def test_wrong_find_message(self):
        self.dialog_page.send_message(self.MESSAGE_TEXT)
        self.driver.get(self.URL_OF_MESSAGES)
        self.dialog_page.find_message(self.RED_POWER)
        self.assertTrue(
            self.message_page.get_existance_of_dialogs_empty(),
            "test_wrong_find_message failed")

    def test_find_dialog(self):
        dialog_name = self.dialog_page.get_dialog_name()
        self.dialog_page.find_dialog(dialog_name)
        self.assertTrue(
            self.message_page.get_existance_of_search_result(),
            "test_find_dialog failed")

    def test_wrong_find_dialog(self):
        self.dialog_page.send_message(self.MESSAGE_TEXT)
        dialog_name = self.dialog_page.get_dialog_name()
        self.driver.get(self.URL_OF_MESSAGES)
        self.dialog_page.find_dialog(self.RED_POWER)
        self.assertTrue(
            self.message_page.get_existance_of_dialogs_empty(),
            "test_find_dialog failed")
