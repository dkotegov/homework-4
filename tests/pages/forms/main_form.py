
from base_element import BaseElement


class MainForm(BaseElement):
    MESSAGE_BUTTON = '//div[@id="msg_toolbar_button"]'
    NEW_MESSAGE_TEXT_IN_NOTIFICATION = '//div[contains(@data-l, "lastMessage")]/div[1]'

    def get_message_button(self):
        return self.get_button_by_xpath(self.MESSAGE_BUTTON)

    def get_new_message_text(self):
        return self.get_field_by_xpath(
            self.NEW_MESSAGE_TEXT_IN_NOTIFICATION).get_attribute("innerHTML")

    def get_existance_of_new_message(self):
        return self.existance_of_element_by_xpath(
            self.NEW_MESSAGE_TEXT_IN_NOTIFICATION)
