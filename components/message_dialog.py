from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from components.base_component import BaseComponent


class MessageDialog(BaseComponent):
    # MESSAGE_INPUT = "//div[@class='itx js-comments_add js-ok-e comments_add-ceditable']"
    MESSAGE_INPUT = "//div[contains(@id, 'field_txt')]"
    MESSAGE_SEND_BUTTON = "//button[@class='button-pro comments_add-controls_save']"
    MESSAGE = "//span[@class='js-copy-text']/span"
    HOVER_ELEMENT_CLASS = "//div[@class='msg_cnt js-msg_cnt']"
    DELETE_MESSAGE_BUTTON = "//a[contains(@data-l,'deleteMsg')]"
    CONFIRM_DELETE_MESSAGE_BUTTON = "//input[contains(@data-l,'confirm')]"

    def get_message_input(self):
        return self.get_visibility_element(self.MESSAGE_INPUT)
        # return self.driver.find_element_by_xpath(self.MESSAGE_INPUT)

    def get_message_send_button(self):
        return self.get_clickable_element(self.MESSAGE_SEND_BUTTON)
        # return self.driver.find_element_by_xpath(self.MESSAGE_SEND_BUTTON)

    # def get_is_element_attached(self):
    #     return self.get_searching_element(self.MESSAGE)

    def get_message(self):
        try:
            el = self.get_element_by_path(self.MESSAGE)
        except TimeoutException:
            return False
        return el

    def hover_element(self):
        return self.get_visibility_element(self.HOVER_ELEMENT_CLASS)

    def get_delete_message_button(self):
        return self.get_clickable_element(self.DELETE_MESSAGE_BUTTON)

    def get_confirm_delete_message_button(self):
        return self.get_clickable_element(self.CONFIRM_DELETE_MESSAGE_BUTTON)
