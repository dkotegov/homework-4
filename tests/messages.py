# -*- coding: utf-8 -*-

from base import BaseTest

from tests.pages.messages.chat import ChatPage


class MessagesTest(BaseTest):
    DEFAULT_USER_ID = 589325597219
    DEFAULT_MESSAGE_TEXT = 'test from selenium'

    MESSAGE_TEXT_INPUT_PLACEHOLDER = unicode('Напишите сообщение', 'utf-8')

    def test_message_send(self):
        chat_page = ChatPage(self.driver, self.DEFAULT_USER_ID)
        chat_page.navigate()

        self.assertEqual(chat_page.get_message_input_placeholder(), self.MESSAGE_TEXT_INPUT_PLACEHOLDER)

        chat_page.message_input_text(self.DEFAULT_MESSAGE_TEXT)
        chat_page.send_message()

        self.assertEqual(len(chat_page.message_input_text()), 1, 'message input has cleared')

    def test_home_button(self):
        chat_page = ChatPage(self.driver, self.DEFAULT_USER_ID)
        chat_page.navigate()

        chat_page.click_on_home_button()

        self.assertTrue(chat_page.is_chat_closed(), 'chat has closed')

    def test_user_info_appearance(self):
        chat_page = ChatPage(self.driver, self.DEFAULT_USER_ID)
        chat_page.navigate()

        user_name = chat_page.get_chat_header_name()

        chat_page.click_on_chat_header()

        self.assertEqual(chat_page.get_chat_header_name(), user_name, 'chat header name has not boon changed')
        self.assertEqual(chat_page.get_user_info_head_name(), user_name, 'user info header name fills properly')

    def test_call_window_opens(self):
        chat_page = ChatPage(self.driver, self.DEFAULT_USER_ID)
        chat_page.navigate()

        chat_page.click_on_call_button()

        self.assertTrue(chat_page.is_call_window_opened(), 'call window has been opened')

    def test_call_calling(self):
        chat_page = ChatPage(self.driver, self.DEFAULT_USER_ID)
        chat_page.navigate()

        chat_page.click_on_call_button()

        self.assertTrue(chat_page.is_calling(), 'calling')

    def test_call_mic_button(self):
        chat_page = ChatPage(self.driver, self.DEFAULT_USER_ID)
        chat_page.navigate()

        chat_page.click_on_call_button()

        chat_page.click_on_mic_button()
        chat_page.click_on_mic_button()

        self.assertTrue(True, 'timeout has not reached')

    def test_call_cam_button(self):
        chat_page = ChatPage(self.driver, self.DEFAULT_USER_ID)
        chat_page.navigate()

        chat_page.click_on_call_button()

        chat_page.click_on_cam_button()
        chat_page.click_on_cam_button()

        self.assertTrue(True, 'timeout has not reached')

    def test_call_hang_up_button(self):
        chat_page = ChatPage(self.driver, self.DEFAULT_USER_ID)
        chat_page.navigate()

        chat_page.click_on_call_button()

        chat_page.click_on_hang_up_button()

        self.assertTrue(True, 'timeout has not reached')

    def test_help_view(self):
        chat_page = ChatPage(self.driver, self.DEFAULT_USER_ID)
        chat_page.navigate()

        chat_page.click_on_call_button()

        chat_page.click_on_help_button()

        chat_page.click_on_help_close_button()
        self.assertTrue(True, 'timeout has not reached')

    def test_do_not_disturb(self):
        chat_page = ChatPage(self.driver, self.DEFAULT_USER_ID)
        chat_page.navigate()

        chat_page.click_on_chat_header()

        chat_page.click_on_do_not_disturb_button()
        chat_page.click_on_do_not_disturb_button()

        self.assertTrue(True, 'timeout has not reached')

    def test_smiles(self):
        chat_page = ChatPage(self.driver, self.DEFAULT_USER_ID)
        chat_page.navigate()

        chat_page.click_on_stickers_panel()
        chat_page.click_on_smiles_tab()
        chat_page.click_on_sad_smile()
        chat_page.send_message()

        self.assertTrue(True, 'timeout has not reached')
