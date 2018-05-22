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


class TestsGroupDialogs(unittest.TestCase):

    def setUp(self):
        browser = os.environ.get('BROWSER', os.environ['BROWSER'])

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.driver.maximize_window()

        self.MESSAGE_TEXT = "testNumber1"
        self.BOT_1_LOGIN = "technopark3"
        self.PASSWORD = os.environ['PASSWORD']
        self.CURRENT_DIALOG_URL = ""
        self.URL_OF_MESSAGES = "https://ok.ru/messages"
        self.ANOTHER_MESSAGE_TEXT = 'new pinned'
        self.NEW_ENG_TITLE = "Avengers: Infinity War"
        self.NEW_RUS_TITLE = u"Мстители: Война Бесконечности"
        self.NEW_CHINE_TITLE = u"复仇者：无穷的战争"
        self.NEW_TOO_LONG_TITLE = "Avengers: It is really " + "infinity " * 42 + "War"
        self.MAX_TITLE_LENGTH = 200

        self.dialog_page = DialogPage(self.driver)
        self.message_page = MessagePage(self.driver)
        self.auth_page = AuthPage(self.driver)
        self.auth_page.sign_in(self.BOT_1_LOGIN, self.PASSWORD)
        self.main_page = MainPage(self.driver)
        self.main_page.open_messages()
        self.create_dialog()
        self.dialog_page.add_user_to_chat()        

    def create_dialog(self):
        self.message_page.create_dialog()
        self.message_page.choose_companion()
        self.dialog_page.wait_for_loader()

    def tearDown(self):
        self.driver.get(self.CURRENT_DIALOG_URL)
        self.leave_group_chat()
        self.driver.quit()

    def leave_group_chat(self):
        self.dialog_page.open_menu()
        dilog_menu_page = DialogMenuPage(self.driver)
        dilog_menu_page.leave_chat()
        confirm_page = ConfirmPage(self.driver)
        confirm_page.confirm()

    def test_add_user_to_group_chat(self):
        self.CURRENT_DIALOG_URL = self.driver.current_url
        self.assertTrue(
            self.dialog_page.get_exsistance_of_created_group_dialog(),
            "test_add_user_to_group_chat failed")

    def test_delete_user_from_group_chat(self):
        self.dialog_page.delete_user_from_chat()
        self.CURRENT_DIALOG_URL = self.driver.current_url
        self.assertTrue(
            self.dialog_page.get_exsistance_of_delte_companion(),
            "test_delete_user_from_group_chat failed")

    def test_hide_group_chat(self):
        self.dialog_page.wait_for_loader()
        self.dialog_page.open_menu()
        dilog_menu_page = DialogMenuPage(self.driver)
        dilog_menu_page.hide_chat()

        hide_chat_confirm_page = ConfirmPage(self.driver)
        hide_chat_confirm_page.confirm()
        self.CURRENT_DIALOG_URL = self.driver.current_url
        self.driver.get(self.URL_OF_MESSAGES)
        self.assertTrue(
            self.message_page.get_existance_of_dialogs_empty(),
            "test_hide_group_chat failed")

    def test_pin_message(self):
        self.dialog_page.wait_for_loader()
        self.dialog_page.send_message(self.MESSAGE_TEXT)
        self.CURRENT_DIALOG_URL = self.driver.current_url
        self.dialog_page.pin_message()
        self.assertTrue(
            self.dialog_page.exsistance_of_pinned_message(),
            "test_pin_message failed")

    def test_change_pinned_message(self):
        self.dialog_page.wait_for_loader()
        self.dialog_page.send_message(self.MESSAGE_TEXT)
        self.CURRENT_DIALOG_URL = self.driver.current_url
        self.dialog_page.pin_message()
        self.dialog_page.send_message(self.ANOTHER_MESSAGE_TEXT)
        self.dialog_page.delete_message()
        self.CURRENT_DIALOG_URL = self.driver.current_url
        self.dialog_page.pin_message()
        self.assertTrue(
            self.dialog_page.exsistance_of_pinned_message(),
            "test_change_pinned_message failed")

    def test_unpin_message(self):
        self.dialog_page.wait_for_loader()
        self.dialog_page.send_message(self.MESSAGE_TEXT)
        self.CURRENT_DIALOG_URL = self.driver.current_url
        self.dialog_page.pin_message()
        self.dialog_page.unpin_message()
        self.driver.refresh()
        self.assertFalse(
            self.dialog_page.exsistance_of_pinned_message(),
            "test_unpin_message failed")

    # There was an idea, to bring together a group of remarkable people.
    # To see if could become something more. And when they needed us,
    # we can fight the battles, that they never could. (c) Infinity War

    def test_change_title(self):
        self.dialog_page.wait_for_loader()
        self.CURRENT_DIALOG_URL = self.driver.current_url
        self.dialog_page.open_menu()
        dialog_menu_page = DialogMenuPage(self.driver)
        dialog_menu_page.change_title(self.NEW_ENG_TITLE)
        title = dialog_menu_page.get_title()
        self.assertEqual(self.NEW_ENG_TITLE, title)

    def test_set_rus_title(self):
        self.dialog_page.wait_for_loader()
        self.CURRENT_DIALOG_URL = self.driver.current_url
        self.dialog_page.open_menu()
        dialog_menu_page = DialogMenuPage(self.driver)
        dialog_menu_page.change_title(self.NEW_RUS_TITLE)
        title = dialog_menu_page.get_title()
        self.assertEqual(self.NEW_RUS_TITLE, title)

    def test_set_chine_title(self):
        self.dialog_page.wait_for_loader()
        self.CURRENT_DIALOG_URL = self.driver.current_url
        self.dialog_page.open_menu()
        dialog_menu_page = DialogMenuPage(self.driver)
        dialog_menu_page.change_title(self.NEW_CHINE_TITLE)
        title = dialog_menu_page.get_title()
        self.assertEqual(self.NEW_CHINE_TITLE, title)

    def test_set_empty_title(self):
        self.dialog_page.wait_for_loader()
        self.CURRENT_DIALOG_URL = self.driver.current_url
        self.dialog_page.open_menu()
        dialog_menu_page = DialogMenuPage(self.driver)
        old_title = dialog_menu_page.get_title()
        dialog_menu_page.change_title("")
        new_title = dialog_menu_page.get_title()
        self.assertEqual(old_title, new_title)

    def test_set_too_long_title(self):
        self.dialog_page.wait_for_loader()
        self.CURRENT_DIALOG_URL = self.driver.current_url
        self.dialog_page.open_menu()
        dialog_menu_page = DialogMenuPage(self.driver)
        dialog_menu_page.change_title(self.NEW_TOO_LONG_TITLE)
        new_title = dialog_menu_page.get_title()
        cut_title = self.NEW_TOO_LONG_TITLE[:self.MAX_TITLE_LENGTH]
        self.assertEqual(new_title, cut_title)

    def test_change_title_several_times(self):
        self.dialog_page.wait_for_loader()
        self.CURRENT_DIALOG_URL = self.driver.current_url
        self.dialog_page.open_menu()
        dialog_menu_page = DialogMenuPage(self.driver)
        dialog_menu_page.change_title(self.NEW_RUS_TITLE)
        dialog_menu_page.change_title(self.NEW_CHINE_TITLE)
        dialog_menu_page.change_title(self.NEW_ENG_TITLE)
        title = dialog_menu_page.get_title()
        self.assertEqual(self.NEW_ENG_TITLE, title)

    # I know what it’s like to lose. To feel so desperately that you’re right,
    # yet to fail nonetheless. Dread it, run from it, destiny arrives all the same. (c) Thanos

    def test_set_dialog_photo_of_mad_titan(self):
        self.dialog_page.wait_for_loader()
        self.CURRENT_DIALOG_URL = self.driver.current_url
        self.dialog_page.open_menu()
        dialog_menu_page = DialogMenuPage(self.driver)
        dialog_menu_page.change_photo(os.getcwd() + "/tests/static/thanos.jpg")
        self.assertTrue(
            self.dialog_page.existence_change_photo_notification(),
            "Failed to update photo of group dialog")

    def test_update_dialog_photo_2(self):
        self.dialog_page.wait_for_loader()
        self.CURRENT_DIALOG_URL = self.driver.current_url
        self.dialog_page.open_menu()
        dialog_menu_page = DialogMenuPage(self.driver)
        dialog_menu_page.change_photo(os.getcwd() + "/tests/static/sabaton_high.jpg")
        self.assertTrue(
            self.dialog_page.existence_change_photo_notification(),
            "Failed to update photo_2 of group dialog")

    def test_update_dialog_photo_jpeg(self):
        self.dialog_page.wait_for_loader()
        self.CURRENT_DIALOG_URL = self.driver.current_url
        self.dialog_page.open_menu()
        dialog_menu_page = DialogMenuPage(self.driver)
        dialog_menu_page.change_photo(os.getcwd() + "/tests/static/sabaton_low.jpeg")
        self.assertTrue(
            self.dialog_page.existence_change_photo_notification(),
            "Failed to update photo.jpeg of group dialog")

    def test_update_dialog_photo_png(self):
        self.dialog_page.wait_for_loader()
        self.CURRENT_DIALOG_URL = self.driver.current_url
        self.dialog_page.open_menu()
        dialog_menu_page = DialogMenuPage(self.driver)
        dialog_menu_page.change_photo(os.getcwd() + "/tests/static/sabaton_png.png")
        self.assertTrue(
            self.dialog_page.existence_change_photo_notification(),
            "Failed to update photo.png of group dialog")

    def test_update_dialog_photo_invalid_format_1(self):
        self.dialog_page.wait_for_loader()
        self.CURRENT_DIALOG_URL = self.driver.current_url
        self.dialog_page.open_menu()
        dialog_menu_page = DialogMenuPage(self.driver)
        dialog_menu_page.change_photo(os.getcwd() + "/tests/static/awd.txt")
        err_msg = dialog_menu_page.get_message_of_error_notification()
        self.assertEquals(err_msg, u"Файл неверного типа.")

    def test_update_dialog_photo_invalid_format_2(self):
        self.dialog_page.wait_for_loader()
        self.CURRENT_DIALOG_URL = self.driver.current_url
        self.dialog_page.open_menu()
        dialog_menu_page = DialogMenuPage(self.driver)
        dialog_menu_page.change_photo(os.getcwd() + "/tests/static/sabaton_high.mp4")
        err_msg = dialog_menu_page.get_message_of_error_notification()
        self.assertEquals(err_msg, u"Файл неверного типа.")
