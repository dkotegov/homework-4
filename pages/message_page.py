from components.message_dialog import MessageDialog
from components.message_info_bar import MessageInfoBar
from components.page import Page
from constants import dialog


class MessagePage(Page):

    def __init__(self, driver):
        super(MessagePage, self).__init__(driver)
        self.message_info_bar = MessageInfoBar(self.driver)
        self.message_dialog = MessageDialog(self.driver)

    def open_info_bar(self):
        self.message_info_bar.get_info_button().click()

    def add_to_black_list(self):
        self.message_info_bar.get_black_list_button().click()

    def accept_to_adding_to_black_list(self):
        self.message_info_bar.accept_adding_to_black_list().click()

    def type_the_message(self):
        self.message_dialog.get_message_input().send_keys(dialog.TEST_MESSAGE)

    def send_message(self):
        self.type_the_message()
        self.message_dialog.get_message_send_button().click()
