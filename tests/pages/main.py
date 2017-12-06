# coding=utf-8
from time import sleep

from base import BasePage
from tests.elements.main import MessagesButton
from tests.elements.status import Status


class MainPage(BasePage):
    url = 'http://ok.ru'

    def is_authorized(self):
        messages_button = MessagesButton(self.driver)
        element = messages_button.messages_button().wait_for_visible().get()
        return element is not None

    def create_my_discussions(self,text):
        status = Status(self.driver)
        show_edit = status.show_edit().wait_for_visible().get()
        show_edit.click()
        input = status.status_edit().wait_for_visible().get()
        input.click()
        input.click()
        sleep(2)
        input.clear()
        input.send_keys(unicode(text,"utf-8"))
        sleep(2)
        # chbox = status.in_status_chbx().wait_for_visible().get()
        # chbox.click()
        # sleep(2)
        publish = status.publish().wait_for_clickable().get()
        publish.click()
        sleep(2)