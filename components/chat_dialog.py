from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from components.base_component import BaseComponent


class ChatDialogLocators:
    def __init__(self):
        self.root = '//div[@id="singleChat"]'
        self.name = '//div[@class="dialogue-name dialogue-name_chat"]'
        self.sendButton = '//div[@id="sendMessageBtn"]'
        self.textArea = '//textarea[@id="sendMessage"]'
        self.msgs = '//div[@class="single-message__body"]'


class ChatDialog(BaseComponent):
    def __init__(self, driver):
        super(ChatDialog, self).__init__(driver)

        self.wait = WebDriverWait(self.driver, 20)
        self.locators = ChatDialogLocators()

    def get_chat_name(self) -> str:
        element = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.locators.name)))
        return element.get_attribute('innerText')

    def click_send(self, text:str):
        elementText = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.textArea)))
        elementText.send_keys(text)

        elementBtn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.sendButton)))
        elementBtn.click()

    def click_send_by_enter(self, text: str):
        elementText = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.textArea)))
        elementText.send_keys(text)
        elementText.send_keys(u'\ue007')

    def get_last_msg(self) -> str:
        elementStr = self.wait.until(
            EC.presence_of_all_elements_located((By.XPATH, self.locators.msgs)))

        return elementStr[len(elementStr) - 1].get_attribute('innerText')
