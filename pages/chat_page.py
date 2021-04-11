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
