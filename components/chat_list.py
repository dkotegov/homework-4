from selenium.webdriver.support.wait import WebDriverWait

from components.base_component import BaseComponent
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ChatListLocators:
    def __init__(self):
        self.root = '//div[@id="chatsList"]'
        self.chats = '//div[@class="chat-lists-single"]'
        self.chat_name = 'single-info__name'
        self.chat_status = '//div[@class="message-body message-body_technical"]'
        self.chat_info_last_msg = '//div[@class="message-body"]'


class ChatList(BaseComponent):
    def __init__(self, driver):
        super(ChatList, self).__init__(driver)

        self.wait = WebDriverWait(self.driver, 20)
        self.locators = ChatListLocators()

    def click_on_another_chat(self, chat: int) -> str:
        element = self.wait.until(
            EC.presence_of_all_elements_located((By.XPATH, self.locators.chats)))
        el = element[chat]
        name = el.find_element_by_class_name(self.locators.chat_name)
        el.click()
        return name.get_attribute('innerText')

    def get_chat_name(self, chat: int) -> str:
        element = self.wait.until(
            EC.presence_of_all_elements_located((By.XPATH, self.locators.chats)))
        el = element[chat]
        name = el.find_element_by_class_name(self.locators.chat_name)
        return name.get_attribute('innerText')

    def get_chat_status(self, chat: int) -> str:
        element = self.wait.until(
            EC.presence_of_all_elements_located((By.XPATH, self.locators.chat_status)))
        el = element[chat]
        return el.get_attribute('innerText')

    def get_chat_info_last_msg(self, chat: int) -> str:
        element = self.wait.until(
            EC.presence_of_all_elements_located((By.XPATH, self.locators.chat_info_last_msg)))
        el = element[chat]
        return el.get_attribute('innerText')

