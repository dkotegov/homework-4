from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from helpers import Page
from components import Login, SideBar


class MessagesPage(Page):
    PATH = "user/chats"
    MESSAGE_CARD = ".one-chat-inner"
    PRODUCT_TITLE = ".chat-message-head-info-product"
    USER_TITLE = ".chat-message-head-info-user"
    PRODUCT_AVATAR = ".chat-message-head-avatar__href"
    CHAT = "#chat-message"
    SEND_BUTTON = ".chat-message-send-form__sbm"
    MESSAGE_BOX = ".chat-message-send-form__msg"
    MESSAGE = ".user-message"

    @property
    def login(self):
        return Login(self.driver)

    @property
    def side_bar(self):
        return SideBar(self.driver)

    def click_message_card(self):
        self.helpers.get_elements(self.MESSAGE_CARD)[0].click()

    def click_product_name(self):
        product_title = self.helpers.get_element(self.PRODUCT_TITLE)
        product_url = product_title.get_attribute("href")
        product_title.click()
        return product_url

    def click_user_name(self):
        user_name = self.helpers.get_element(self.USER_TITLE)
        user_url = user_name.get_attribute("href")
        user_name.click()
        return user_url

    def click_product_avatar(self):
        product_avatar = self.helpers.get_element(self.PRODUCT_AVATAR)
        product_url = product_avatar.get_attribute("href")
        product_avatar.click()
        return product_url

    def is_chat_opened(self):
        return self.helpers.is_contains(self.CHAT)

    def send_message(self, text):
        self.helpers.input_value(self.MESSAGE_BOX, text)
        self.helpers.click_button(self.SEND_BUTTON)

    def count_messages(self):
        return len(self.helpers.get_elements(self.MESSAGE))