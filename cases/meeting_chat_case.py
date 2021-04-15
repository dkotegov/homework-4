from cases.base_case import BaseTest
from pages.profile_page import ProfilePage
from steps.meeting_chat_steps import MeetingChatSteps


class MeetingChatTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.auth()
        self.chat_steps = MeetingChatSteps(self.driver)
        self.chat_steps.open_page()

    def test_send_message_to_chat(self):
        expected_msg = "test meeting chat"

        self.chat_steps.open_chat()
        self.chat_steps.send_message(expected_msg)
        self.chat_steps.reopen_chat()
        actual = self.chat_steps.get_last_sent_message()
        self.assertEqual(expected_msg, actual, f'Value {actual} doesn\'t match {expected_msg}')

    def test_redirect_on_click_message_author(self):
        self.chat_steps.open_chat()
        expected_name = self.chat_steps.get_last_sender_name()

        self.chat_steps.open_last_sender_profile()
        sender_profile = ProfilePage(self.driver)

        actual_name = sender_profile.left_column.get_profile_name_text()
        self.assertEqual(expected_name, actual_name, f'Sender name {actual_name} doesn\'t match {expected_name}')

    def test_redirect_on_click_chat_user(self):
        self.chat_steps.open_chat()
        expected_name = self.chat_steps.get_chat_user_name(position=0)

        self.chat_steps.open_chat_user(position=0)
        sender_profile = ProfilePage(self.driver)

        actual_name = sender_profile.left_column.get_profile_name_text()
        self.assertEqual(expected_name, actual_name, f'Sender name {actual_name} doesn\'t match {expected_name}')
