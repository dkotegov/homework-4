from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from helpers import Page, Component
from components import Login


class ChatsBlock(Component):
    MESSAGE_CARD = ".one-chat"
    MESSAGE_CARD_ID = "//div[@data-chat-id={}]"

    PRODUCT_TITLE = ".chat-message-head-info-product"
    USER_TITLE = ".chat-message-head-info-user"
    PRODUCT_AVATAR = ".chat-message-head-avatar__href"
    SEND_BUTTON = ".chat-message-send-form__sbm"
    MESSAGE_BOX = ".chat-message-send-form__msg"
    MESSAGE_TEXT = "//div[@class=\"user-message-block-inner\"]/span[text()='{}']"

    def get_chat_id(self):
        element = self.helpers.get_element(self.MESSAGE_CARD)
        return element.get_attribute("data-chat-id")

    def click_message_card(self, chat_id):
        self.helpers.click_element(self.MESSAGE_CARD_ID.format(chat_id), self.helpers.SELECTOR.XPATH)

    def wait_message(self, message):
        self.helpers.wait(until=EC.presence_of_element_located((By.XPATH, self.MESSAGE_TEXT.format(message))))

    def is_contains_message(self, message):
        return self.helpers.is_contains(self.MESSAGE_TEXT.format(message), self.helpers.SELECTOR.XPATH)

    def send_message(self, text):
        self.helpers.input_value(self.MESSAGE_BOX, text)
        self.helpers.click_element(self.SEND_BUTTON)

    def get_product_name_url(self):
        element = self.helpers.get_element(self.PRODUCT_TITLE)
        return element.get_attribute("href")

    def click_product_name(self):
        self.helpers.click_element(self.PRODUCT_TITLE)

    def get_product_avatar_url(self):
        element = self.helpers.get_element(self.PRODUCT_AVATAR)
        return element.get_attribute("href")

    def get_user_name_url(self):
        element = self.helpers.get_element(self.USER_TITLE)
        return element.get_attribute("href")

    def click_product_avatar(self):
        self.helpers.click_element(self.PRODUCT_AVATAR)

    def click_user_name(self):
        self.helpers.click_element(self.USER_TITLE)


class UserMessagesPage(Page):
    PATH = "/user/chats"

    TITLE = ".chat-message-head-info-user__name"

    def change_path(self, path):
        self.PATH = "/user/chat/" + path

    def page_exist(self):
        return self.helpers.get_element(self.TITLE) is not None

    @property
    def login(self):
        return Login(self.driver)

    @property
    def chats_block(self):
        return ChatsBlock(self.driver)

