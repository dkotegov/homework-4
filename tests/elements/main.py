from selenium.webdriver.common.by import By

from base import BaseElement


class MessagesButton(BaseElement):
    BUTTON = (By.ID, 'msg_toolbar_button')

    def __init__(self, driver):
        super(MessagesButton, self).__init__(driver)

        self.locator = None

    def get_button(self):
        self.locator = self.BUTTON
        return self
