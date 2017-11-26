# coding=utf-8
from base import BasePage
from tests.elements.main import MessagesButton


class MainPage(BasePage):
    url = 'http://ok.ru'

    def is_authorized(self):
        messages_button = MessagesButton(self.driver)
        element = messages_button.get_button().wait_for_visible().get()
        return element is not None
