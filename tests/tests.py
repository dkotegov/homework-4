# -*- coding: utf-8 -*-
import os

import unittest

from pages.auth import AuthPage
from pages.main import MainPage
from pages.message import MessagePage
from pages.dialog import DialogPage
from pages.dialog_menu import DialogMenuPage
from pages.confirm import ConfirmPage

from selenium.webdriver import DesiredCapabilities, Remote


class Tests(unittest.TestCase):

    def setUp(self):
        browser = os.environ.get('BROWSER', os.environ['BROWSER'])

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.driver.maximize_window()

        self.NEW_TITLE = "New Title"
        self.MESSAGE_TEXT = "testNumber1"
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

        self.SEARCH_REQUEST = "happy birthday"
        self.STICKERS_SET_ID = "2"
        self.APPLICATION_ID = "1241398016"
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
        if(self.CURRENT_DIALOG_URL[23] == 'c'):
            self.leave_group_chat()
        else:
            self.delete_dialog()
        self.driver.quit()

    def leave_group_chat(self):
        self.dialog_page.open_menu()
        dilog_menu_page = DialogMenuPage(self.driver)
        dilog_menu_page.leave_chat()
        confirm_page = ConfirmPage(self.driver)
        confirm_page.confirm()

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

    def send_self_message_from_other_acc(self):
        self.auth_page.chage_account(self.BOT_2_LOGIN, self.PASSWORD)
        self.driver.get(self.URL_OF_DIALOG_WITH_ME)
        self.dialog_page.send_message(self.MESSAGE_TEXT)

        self.auth_page.chage_account(self.BOT_1_LOGIN, self.PASSWORD)
        self.driver.get(self.CURRENT_DIALOG_URL)

    # Во всех тестах где присутвует рефреш - есть два объяснения:
    #  1 - Не динамичнось верстки(без рефреша элементы не меняются)
    # 2 - Не найдены признаки подтверждаюшие действие(рефреш гарантирует 100%
    # точность итоговых ассертов)

    # Crusader727

    def test_create_and_delete_dialog(self):
        self.assertTrue(
            self.dialog_page.send_message_button_exists(),
            "test_create_and_delete_dialog failed")
        self.delete_dialog()
        self.driver.get(self.CURRENT_DIALOG_URL)
        self.assertTrue(
            self.dialog_page.no_messages_text_exists(),
            "test_create_and_delete_dialog failed")

    def test_send_sticker(self):
        self.dialog_page.send_sticker()
        self.assertTrue(
            self.dialog_page.message_with_sticker_exists(),
            "test_send_sticker failed")

    def test_send_music(self):
        self.dialog_page.send_music()
        self.assertTrue(
            self.dialog_page.sent_message_exists(),
            "test_send_music failed")

    def test_send_document(self):
        self.dialog_page.send_document()
        self.assertTrue(
            self.dialog_page.sent_message_exists(),
            "test_send_document failed")

    def test_send_photo(self):
        self.dialog_page.send_photo()
        self.assertTrue(
            self.dialog_page.sent_message_exists(),
            "test_send_photo failed")

    def test_send_video(self):
        self.dialog_page.send_video()
        self.assertTrue(
            self.dialog_page.sent_message_exists(),
            "test_send_video failed")

    def test_find_dialog(self):
        self.dialog_page.find_dialog()
        self.assertTrue(
            self.message_page.get_existance_of_search_result(),
            "test_find_dialog failed")

    def test_send_message_to_blocked_user(self):
        self.dialog_page.send_message(self.MESSAGE_TEXT)

        self.auth_page.chage_account(self.BOT_2_LOGIN, self.PASSWORD)
        self.assertEquals(
            self.main_page.get_new_message_text(),
            self.MESSAGE_TEXT)
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

    def test_get_message_from_blocked_user(self):
        self.auth_page.chage_account(self.BOT_2_LOGIN, self.PASSWORD)
        self.driver.get(self.URL_OF_DIALOG_WITH_ME)
        self.dialog_page.send_message(self.MESSAGE_TEXT)

        self.auth_page.chage_account(self.BOT_1_LOGIN, self.PASSWORD)
        self.assertTrue(
            not self.main_page.get_existance_of_new_message(),
            "test_get_message_from_blocked_user failed")
        self.BOT_1_LOGIN = self.BOT_2_LOGIN
        self.NEED_TO_CHANGE_ACC = True

    # 112Nick

    def test_send_message(self):
        self.dialog_page.send_message(self.MESSAGE_TEXT)
        self.assertTrue(
            self.dialog_page.sent_message_exists(),
            "test send message failed")

    def test_edit_message(self):
        MESSAGE_EDITED_TEXT = ' IS_EDITED'
        self.dialog_page.send_message(self.MESSAGE_TEXT)
        self.dialog_page.edit_and_send_message(MESSAGE_EDITED_TEXT)
        self.driver.refresh()
        self.assertEquals(
            self.dialog_page.get_sent_message_text(),
            self.MESSAGE_TEXT + MESSAGE_EDITED_TEXT)

    def test_delete_message(self):
        self.dialog_page.send_message(self.MESSAGE_TEXT)
        self.dialog_page.delete_message()
        self.driver.refresh()
        self.assertTrue(
            self.dialog_page.no_messages_text_exists(),
            "test_delete_message failed")

    def test_answer_message(self):
        MESSAGE_ANSWERED_TEXT = ' IS_ANSWERED'
        self.dialog_page.send_message(self.MESSAGE_TEXT)
        self.dialog_page.answer_message(MESSAGE_ANSWERED_TEXT)
        self.driver.refresh()
        self.assertTrue(
            self.dialog_page.get_exsistance_of_answered_message(),
            "test_answer_message failed")

    def test_forward_message(self):
        self.dialog_page.send_message(self.MESSAGE_TEXT)
        self.dialog_page.forward_message()
        self.message_page.choose_companion_forward_message()
        self.driver.refresh()
        self.assertTrue(
            self.dialog_page.get_exsistance_of_forwarded_message(),
            "test_forward_message failed")

    def test_find_message(self):
        self.dialog_page.send_message(self.MESSAGE_TEXT)
        self.dialog_page.find_message(self.MESSAGE_TEXT)
        self.assertEquals(
            self.MESSAGE_TEXT,
            self.message_page.get_found_message_text())

    def test_add_user_to_group_chat(self):
        self.dialog_page.add_user_to_chat()
        self.assertTrue(
            self.dialog_page.get_exsistance_of_created_group_dialog(),
            "test_add_user_to_group_chat failed")

    def test_delete_user_from_group_chat(self):
        self.dialog_page.add_user_to_chat()
        self.dialog_page.delete_user_from_chat()
        self.assertTrue(
            self.dialog_page.get_exsistance_of_delte_companion(),
            "test_delete_user_from_group_chat failed")

    def test_hide_group_chat(self):
        self.dialog_page.add_user_to_chat()
        self.dialog_page.wait_for_loader()
        self.dialog_page.open_menu()
        dilog_menu_page = DialogMenuPage(self.driver)
        dilog_menu_page.hide_chat()

        hide_chat_confirm_page = ConfirmPage(self.driver)
        hide_chat_confirm_page.confirm()
        self.driver.get(self.URL_OF_MESSAGES)
        self.assertTrue(
            self.message_page.get_existance_of_dialogs_empty(),
            "test_hide_group_chat failed")

    def test_pin_message(self):
        self.dialog_page.add_user_to_chat()
        self.dialog_page.wait_for_loader()
        self.dialog_page.send_message(self.MESSAGE_TEXT)

        self.dialog_page.pin_message()
        self.assertTrue(
            self.dialog_page.exsistance_of_pinned_message(),
            "test_pin_message failed")

    def test_unpin_message(self):
        self.dialog_page.add_user_to_chat()
        self.dialog_page.wait_for_loader()
        self.dialog_page.send_message(self.MESSAGE_TEXT)

        self.dialog_page.pin_message()
        self.dialog_page.unpin_message()
        self.driver.refresh()
        self.assertFalse(
            self.dialog_page.exsistance_of_pinned_message(),
            "test_unpin_message failed")

    # Trubnikov

    def test_change_title_of_group_chat(self):
        self.dialog_page.add_user_to_chat()
        self.dialog_page.wait_for_loader()
        self.dialog_page.open_menu()
        dialog_menu_page = DialogMenuPage(self.driver)
        dialog_menu_page.change_title(self.NEW_TITLE)

        self.driver.refresh()
        self.dialog_page.open_menu()
        title = dialog_menu_page.get_title()
        self.assertEqual(self.NEW_TITLE, title)

    def test_update_dialog_photo(self):
        self.dialog_page.add_user_to_chat()
        self.dialog_page.wait_for_loader()
        self.dialog_page.open_menu()
        dilog_menu_page = DialogMenuPage(self.driver)
        dilog_menu_page.change_photo(os.getcwd() + "/tests/static/sabaton.jpg")

        self.assertTrue(
            self.dialog_page.existence_change_photo_notification(),
            "test_update_dialog_photo failed")

    def test_not_disturbed(self):
        self.dialog_page.unblock_user()
        self.dialog_page.switch_do_not_disturbed()

        self.send_self_message_from_other_acc()
        self.assertFalse(
            self.main_page.get_existance_of_new_message(),
            "test_not_disturbed failed")
        self.NEED_TO_BLOCK_USER = True
        self.dialog_page.switch_do_not_disturbed()

    def test_send_smile(self):
        self.dialog_page.send_chocolate_smile()
        self.assertTrue(
            self.dialog_page.sent_message_exists(),
            "test_send_smile failed")

    def test_send_postcard(self):
        self.dialog_page.send_postcard()
        self.assertTrue(
            self.dialog_page.check_sending_postcard(),
            "test_send_postcard failed")

    def test_postcards_search(self):
        self.dialog_page.find_and_send_postcard(self.SEARCH_REQUEST)
        self.assertTrue(
            self.dialog_page.check_sending_postcard(),
            "test_postcards_search failed")

    def test_select_stickers_set(self):
        set_id = self.STICKERS_SET_ID
        self.dialog_page.install_stickers_set(set_id)
        self.assertTrue(
            self.dialog_page.check_stickers_set(set_id),
            "test_select_stickers_set failed")
        self.dialog_page.uninstall_stickers_set(set_id)

    def test_open_avatar(self):
        self.dialog_page.open_menu()
        self.dialog_page.open_avatar()
        self.assertTrue(
            self.dialog_page.existence_big_avatar(),
            "test_open_original_photo failed")

    def test_report_message(self):
        self.dialog_page.unblock_user()

        self.send_self_message_from_other_acc()
        self.dialog_page.report_message()
        self.NEED_TO_BLOCK_USER = True
        self.assertTrue(
            self.dialog_page.existence_reported_message(),
            "test_report_message failed")

    def test_game_invite(self):
        self.dialog_page.invite_game(self.APPLICATION_ID)
        self.assertTrue(
            self.dialog_page.existence_game(
                self.APPLICATION_ID),
            "test_game_invite failed")

    # AndersRichter

    def test_video_call(self):
        self.dialog_page.begin_video_call()
        self.assertTrue(
            self.dialog_page.video_call_exists(),
            "test_video_call failed")

    def test_support_window(self):
        self.dialog_page.open_support()
        self.assertTrue(
            self.dialog_page.support_window_exists(),
            "test_support_window failed")

    def test_sticker_bar(self):
        self.dialog_page.hide_sticker_bar()
        self.assertTrue(
            self.dialog_page.sticker_bar_exists(),
            "test_sticker_bar failed")

    def test_present_page(self):
        self.dialog_page.go_to_present_page()
        self.dialog_page.wait_for_nav_loader()
        self.assertTrue(
            self.dialog_page.present_page_exists(),
            "test_present_page failed")
        self.main_page.open_messages()

    def test_money_page(self):
        self.dialog_page.go_to_money_page()
        self.dialog_page.wait_for_payment_loader()

        self.assertTrue(
            self.dialog_page.money_page_exists(),
            "test_money_page failed")
        self.dialog_page.close_money_page()

    def test_money_transfers_page(self):
        self.dialog_page.go_to_money_page()
        self.dialog_page.wait_for_payment_loader()
        self.dialog_page.go_to_transfers_page()

        self.assertTrue(
            self.dialog_page.money_page_exists(),
            "test_money_transfers_page failed")
        self.dialog_page.close_money_page()

    def test_profile_from_dialog(self):
        self.dialog_page.go_to_profile()
        self.dialog_page.wait_for_nav_loader()
        self.assertTrue(
            self.dialog_page.profile_page_exists(),
            "profile_from_dialog failed")
        self.main_page.open_messages()

    def test_delete_sticker_pack(self):
        self.dialog_page.install_stickers_set(self.STICKERS_SET_ID)
        self.dialog_page.uninstall_stickers_set(self.STICKERS_SET_ID)
        self.assertTrue(
            not self.dialog_page.check_stickers_set(
                self.STICKERS_SET_ID),
            "test_delete_sticker_pack failed")

    def test_send_animation_smile(self):
        self.dialog_page.send_animation_smile()
        self.assertTrue(
            self.dialog_page.sent_message_exists(),
            "test_send_animation_smile failed")

    def test_send_sticker_from_bar(self):
        self.dialog_page.send_sticker_from_bar()
        self.assertTrue(
            self.dialog_page.message_with_sticker_exists(),
            "test_send_sticker_from_bar failed")
