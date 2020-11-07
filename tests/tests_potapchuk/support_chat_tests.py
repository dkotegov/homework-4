from tests.pages.chat_page import ChatPage

from tests.tests_potapchuk.base_test import BaseTest


class ChatTest(BaseTest):
    def setUp(self):
        super().setUp(auth='user')

        self.chatPage = ChatPage(self.driver)
        self.chatPage.open()
        self.chatPage.wait_visible()
        # guarantee the positive number of messages
        self.chatPage.send_start_message()

    def test_send_message(self):
        message = self.test_send_message.__name__
        self.chatPage.send_message(message)
        self.assertEqual(self.chatPage.last_message, message)

    def test_send_empty_message(self):
        self.chatPage.send_message('')
        self.assertEqual(self.chatPage.last_message, self.chatPage.DEFAULT_MESSAGE)

    def test_long_message(self):
        message = self.test_long_message.__name__
        long_message = 10 * message

        self.chatPage.send_message(long_message)
        self.assertEqual(self.chatPage.last_message, long_message)

    def default_message(self):
        return self.chatPage.DEFAULT_MESSAGE
