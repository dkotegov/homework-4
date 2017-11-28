from selenium.webdriver.common.by import By

from base import BaseElement


class MessagesButton(BaseElement):
    MESSAGES_BUTTON = (By.ID, 'msg_toolbar_button')