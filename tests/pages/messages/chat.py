# coding=utf-8

from tests.pages.base import BasePage

from tests.elements.messages.send_panel import SendPanel
from tests.elements.messages.home_button import HomeButton
from tests.elements.messages.settings_button import SettingsButton
from tests.elements.messages.chat_header import ChatHeader


class ChatPage(BasePage):
    def __init__(self, driver, id):
        self.url = 'http://ok.ru/messages/' + str(id)

        super(ChatPage, self).__init__(driver)

        self.send_panel = SendPanel(driver)
        self.home_button = HomeButton(driver)
        self.settings_button = SettingsButton(driver)
        self.chat_header = ChatHeader(driver)

    def message_input_text(self, text=None):
        if text is not None:
            self.send_panel.message_input().wait_for_presence().get().send_keys(text)

        return self.send_panel.message_input().wait_for_presence().get().get_attribute('innerHTML')

    def send_message(self):
        self.send_panel.send_button().wait_for_clickable().get().click()

    def get_message_input_placeholder(self):
        return self.send_panel.message_input().wait_for_visible().get().get_attribute('data-placeholder')

    def click_on_home_button(self):
        self.home_button.button().wait_for_clickable().get().click()

    def is_chat_closed(self):
        element = self.settings_button.button().wait_for_visible().get()
        return element is not None

    def click_on_chat_header(self):
        self.chat_header.head_name().wait_for_clickable().get().click()

    def get_chat_header_name(self):
        return self.chat_header.head_name().wait_for_visible().get().get_attribute('innerHTML')
