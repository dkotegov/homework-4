from tests.helpers.database import DatabaseFiller
from tests.pages.chat_list_page import ChatListPage
from tests.pages.chat_page import ChatPage

from tests.tests_potapchuk.base_test import BaseTest
from tests.tests_potapchuk.support_chat_tests import ChatTest


class ChatListTest(BaseTest):
    def setUp(self):
        self.sent_message = send_user_message()
        self.user_id = get_user_id()

        super().setUp(auth='support')

        self.chatListPage = ChatListPage(self.driver)
        self.chatListPage.open()
        self.chatListPage.wait_visible()

    def testRecvUserMessage(self):
        self.chatListPage.click_user_chat_card(self.user_id)
        chat_page = ChatPage(self.driver)
        chat_page.wait_message_text_visible()
        self.assertEqual(chat_page.last_message, self.sent_message)


def get_user_id():
    filler = DatabaseFiller()
    filler.user_auth()
    return filler.get_profile_id()


def send_user_message():
    chat = ChatTest()
    chat.setUp()
    chat.tearDown()
    return chat.default_message()
