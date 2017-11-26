# coding=utf-8

from tests.pages.base import BasePage

from tests.elements.messages.send_panel import SendPanel


class ChatPage(BasePage):
    def __init__(self, driver, id):
        self.url = 'http://ok.ru/messages/' + str(id)

        super(ChatPage, self).__init__(driver)

        self.send_panel = SendPanel(driver)

    def message_input_text(self, text=None):
        if text is not None:
            self.send_panel.message_input().wait_for_presence().get().send_keys(text)

        return self.send_panel.message_input().wait_for_presence().get().get_attribute('innerHTML')

    def send_message(self):
        self.send_panel.send_button().wait_for_clickable().get().click()

    def get_message_input_placeholder(self):
        return self.send_panel.message_input().wait_for_visible().get().get_attribute('data-placeholder')
