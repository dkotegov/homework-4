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


class TwoAccauntsManagement(unittest.TestCase):

    def setUp(self):
        browser = os.environ.get('BROWSER', os.environ['BROWSER'])

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.driver.maximize_window()

        self.MESSAGE_TEXT = "testNumber1"
        self.LONG_MESSAGE_TEXT = "test" * 100
        self.RED_POWER = u"☭☭☭☭☭☭"  # special unicode
        self.RUSSIAN_ARMENIAN_MESSAGE = u"привет աշխարհ"
        self.NOT_VALID_MESSAGE = "?" * 4100
        self.EMPTY_MESSAGE = ""

        self.BOT_1_LOGIN = "technopark3"
        self.BOT_2_LOGIN = "technopark2"
        self.PASSWORD = os.environ['PASSWORD']
        self.CURRENT_DIALOG_URL = ""

        self.dialog_page = DialogPage(self.driver)
        self.message_page = MessagePage(self.driver)
        self.auth_page = AuthPage(self.driver)
        self.auth_page.sign_in(self.BOT_1_LOGIN, self.PASSWORD)
        self.main_page = MainPage(self.driver)
        self.main_page.open_messages()
        self.URL_OF_DIALOG_WITH_ME = "https://ok.ru/messages/575662066926"
        self.URL_OF_MESSAGES = "https://ok.ru/messages"

        self.NEED_TO_BLOCK_USER = False
        self.NEED_TO_CHANGE_ACC = False

        self.create_dialog()
        self.CURRENT_DIALOG_URL = self.driver.current_url

    def tearDown(self):
        if(self.NEED_TO_BLOCK_USER):
            self.dialog_page.block_user()
        if(self.NEED_TO_CHANGE_ACC):
            self.auth_page.chage_account(self.BOT_1_LOGIN, self.PASSWORD)
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

    def test_send_message_to_blocked_user(self):
        self.dialog_page.send_message(self.MESSAGE_TEXT)

        self.auth_page.chage_account(self.BOT_2_LOGIN, self.PASSWORD)
        self.assertEquals(
            self.main_page.get_new_message_text(),
            self.MESSAGE_TEXT)
        self.NEED_TO_CHANGE_ACC = True

    def test_send_red_power_message_to_blocked_user(self):
        self.dialog_page.send_message(self.RED_POWER)

        self.auth_page.chage_account(self.BOT_2_LOGIN, self.PASSWORD)
        self.assertEquals(
            self.main_page.get_new_message_text(),
            self.RED_POWER)
        self.NEED_TO_CHANGE_ACC = True

    def test_send_rus_arm_message_to_blocked_user(self):
        self.dialog_page.send_message(self.RUSSIAN_ARMENIAN_MESSAGE)

        self.auth_page.chage_account(self.BOT_2_LOGIN, self.PASSWORD)
        self.assertEquals(
            self.main_page.get_new_message_text(),
            self.RUSSIAN_ARMENIAN_MESSAGE)
        self.NEED_TO_CHANGE_ACC = True

    def test_send_long_message_to_blocked_user(self):
        self.dialog_page.send_message(self.LONG_MESSAGE_TEXT)

        self.auth_page.chage_account(self.BOT_2_LOGIN, self.PASSWORD)
        self.assertEquals(
            self.main_page.get_new_message_text(),
            self.LONG_MESSAGE_TEXT)
        self.NEED_TO_CHANGE_ACC = True

    def test_send_not_valid_message_to_blocked_user(self):
        self.dialog_page.send_message(self.NOT_VALID_MESSAGE)

        self.auth_page.chage_account(self.BOT_2_LOGIN, self.PASSWORD)
        self.assertNotEquals(
            self.main_page.get_new_message_text(),
            self.NOT_VALID_MESSAGE)
        self.NEED_TO_CHANGE_ACC = True

    def test_send_empty_message_to_blocked_user(self):
        self.dialog_page.send_message(self.EMPTY_MESSAGE)

        self.auth_page.chage_account(self.BOT_2_LOGIN, self.PASSWORD)
        self.assertNotEquals(
            self.main_page.get_new_message_text(),
            self.EMPTY_MESSAGE)
        self.NEED_TO_CHANGE_ACC = True

    def test_send_message_to_unblocked_user(self):
        self.dialog_page.unblock_user()
        self.dialog_page.send_message(self.MESSAGE_TEXT)

        self.dialog_page.block_user()
        self.auth_page.chage_account(self.BOT_2_LOGIN, self.PASSWORD)
        self.assertEquals(
            self.main_page.get_new_message_text(),
            self.MESSAGE_TEXT)
        self.NEED_TO_CHANGE_ACC = True

    def test_send_red_power_message_to_unblocked_user(self):
        self.dialog_page.unblock_user()
        self.dialog_page.send_message(self.RED_POWER)

        self.dialog_page.block_user()
        self.auth_page.chage_account(self.BOT_2_LOGIN, self.PASSWORD)
        self.assertEquals(
            self.main_page.get_new_message_text(),
            self.RED_POWER)
        self.NEED_TO_CHANGE_ACC = True

    def test_send_rus_arm_message_to_unblocked_user(self):
        self.dialog_page.unblock_user()
        self.dialog_page.send_message(self.RUSSIAN_ARMENIAN_MESSAGE)

        self.dialog_page.block_user()
        self.auth_page.chage_account(self.BOT_2_LOGIN, self.PASSWORD)
        self.assertEquals(
            self.main_page.get_new_message_text(),
            self.RUSSIAN_ARMENIAN_MESSAGE)
        self.NEED_TO_CHANGE_ACC = True

    def test_send_long_message_to_unblocked_user(self):
        self.dialog_page.unblock_user()
        self.dialog_page.send_message(self.LONG_MESSAGE_TEXT)

        self.dialog_page.block_user()
        self.auth_page.chage_account(self.BOT_2_LOGIN, self.PASSWORD)
        self.assertEquals(
            self.main_page.get_new_message_text(),
            self.LONG_MESSAGE_TEXT)
        self.NEED_TO_CHANGE_ACC = True

    def test_send_not_valid_message_to_unblocked_user(self):
        self.dialog_page.unblock_user()
        self.dialog_page.send_message(self.NOT_VALID_MESSAGE)

        self.dialog_page.block_user()
        self.auth_page.chage_account(self.BOT_2_LOGIN, self.PASSWORD)
        self.assertNotEquals(
            self.main_page.get_new_message_text(),
            self.NOT_VALID_MESSAGE)
        self.NEED_TO_CHANGE_ACC = True

    def test_send_empty_message_to_unblocked_user(self):
        self.dialog_page.unblock_user()
        self.dialog_page.send_message(self.EMPTY_MESSAGE)

        self.dialog_page.block_user()
        self.auth_page.chage_account(self.BOT_2_LOGIN, self.PASSWORD)
        self.assertNotEquals(
            self.main_page.get_new_message_text(),
            self.EMPTY_MESSAGE)
        self.NEED_TO_CHANGE_ACC = True

    def test_get_message_from_blocked_user(self):
        self.auth_page.chage_account(self.BOT_2_LOGIN, self.PASSWORD)
        self.driver.get(self.URL_OF_DIALOG_WITH_ME)
        self.dialog_page.send_message(self.MESSAGE_TEXT)
        self.CURRENT_DIALOG_URL = self.driver.current_url

        self.auth_page.chage_account(self.BOT_1_LOGIN, self.PASSWORD)
        self.assertFalse(
            self.main_page.get_existance_of_new_message(),
            "test_get_message_from_blocked_user failed")
        self.BOT_1_LOGIN = self.BOT_2_LOGIN
        self.NEED_TO_CHANGE_ACC = True

    def test_get_long_message_from_blocked_user(self):
        self.auth_page.chage_account(self.BOT_2_LOGIN, self.PASSWORD)
        self.driver.get(self.URL_OF_DIALOG_WITH_ME)
        self.dialog_page.send_message(self.LONG_MESSAGE_TEXT)
        self.CURRENT_DIALOG_URL = self.driver.current_url

        self.auth_page.chage_account(self.BOT_1_LOGIN, self.PASSWORD)
        self.assertFalse(
            self.main_page.get_existance_of_new_message(),
            "test_get_message_from_blocked_user failed")
        self.BOT_1_LOGIN = self.BOT_2_LOGIN
        self.NEED_TO_CHANGE_ACC = True
