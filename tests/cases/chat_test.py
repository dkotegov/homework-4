import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import DesiredCapabilities, Remote

from tests.cases.base import TestAuthorized
from tests.pages.chat import ChatPage


class Test(TestAuthorized):
    def setUp(self):
        super().setUp()
        self.page = ChatPage(self.driver)

    def test_search_existed(self):
        name = "testTest"
        self.page.form_list.search_user(name)
        assert self.page.form_list.get_error() == ''

        self.page.form_concrete.wait_for_load()
        assert self.page.form_concrete.get_companion_name() == name
        text1 = "12345"
        self.page.form_concrete.send_message_confirmed(text1)
        # self.page.form_concrete.send_message(text1)
        # self.page.form_concrete.wait_for_my_message()
        # result_message = self.page.form_concrete.get_message()
        # assert result_message['from_me']
        # assert result_message['text'] == text1
        # time.sleep(5)
