from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from components.base_component import BaseComponent


class ChatDialogLocators:
    def __init__(self):
        self.root = '//div[@id="singleChat"]'
        self.name = '//div[@class="dialogue-name dialogue-name_chat"]'


class ChatDialog(BaseComponent):
    def __init__(self, driver):
        super(ChatDialog, self).__init__(driver)

        self.wait = WebDriverWait(self.driver, 20)
        self.locators = ChatDialogLocators()

    def get_chat_name(self) -> str:
        element = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.locators.name)))
        return element.get_attribute('innerText')
