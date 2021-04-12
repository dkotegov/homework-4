from components.chat_dialog import ChatDialog
from components.chat_list import ChatList
from pages.base_page import BasePage


class ChatPage(BasePage):
    """
    Страница Чатов
    """
    PATH = 'chats'

    def __init__(self, driver):
        self.chat_list = ChatList(driver)
        self.chat_dialog = ChatDialog(driver)
        super(ChatPage, self).__init__(driver, self.chat_list.locators.root)

    def click_on_another_chat(self, chat: int) -> str:
        return self.chat_list.click_on_another_chat(chat)

    def get_current_chat_name(self) -> str:
        return self.chat_dialog.get_chat_name()

    def get_first_chat_name(self) -> str:
        return self.chat_list.get_chat_name(0)

    def click_on_send_msg(self, text: str) -> str:
        return self.chat_dialog.click_send(text)

    def click_on_send_msg_by_enter(self, text: str) -> str:
        return self.chat_dialog.click_send_by_enter(text)

    def get_last_msg(self) -> str:
        return self.chat_dialog.get_last_msg()

    def get_chat_status(self) -> str:
        return self.chat_list.get_chat_status(0)

    def get_chat_info_last_msg(self) -> str:
        return self.chat_list.get_chat_info_last_msg(0)


