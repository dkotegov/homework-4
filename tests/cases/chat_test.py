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

    def _send_message_positive(self, name, text, **kwargs):
        self.page.form_list.search_user(name)
        assert not self.page.form_list.get_error()

        self.page.form_concrete.wait_for_load()
        assert self.page.form_concrete.get_companion_name() == name
        self.page.form_concrete.send_message_confirmed(text, **kwargs)

    # def test_send_plain_to_existed(self):
    #     name, text = "testTest", "43424342"
    #     self._send_message_positive(name, text)
    #
    # def test_search_non_existent(self):
    #     name = "odjwedjfdjefce"
    #     self.page.form_list.search_user(name)
    #     err = self.page.form_list.get_error(timeout=5)
    #     assert err != ''
    #
    # def test_forgot_to_print_username(self):
    #     name = ""
    #     self.page.form_list.search_user(name)
    #     err = self.page.form_list.get_error(timeout=5)
    #     assert err != ''
    #
    # def test_send_empty_message(self):
    #     name = "testTest"
    #     self.page.form_list.search_user(name)
    #     assert not self.page.form_list.get_error()
    #
    #     self.page.form_concrete.wait_for_load()
    #     assert self.page.form_concrete.get_companion_name() == name
    #     text1 = ""
    #     try:
    #         self.page.form_concrete.send_message_confirmed(text1, timeout=3)
    #     except TimeoutError:
    #         return
    #     assert False, "There must not any message-list alteration be found, but smt has changed"
    #
    # def test_send_smiles_only(self):
    #     name, text = "testTest", "😁😅😊😋😎"
    #     self._send_message_positive(name, text,
    #                                 printer=self.page.form_concrete.enter_smiles)
    #
    # def test_send_smiles_and_text(self):
    #     name, text = "testTest", "😁😅😊kokoko😋😎"
    #     self._send_message_positive(name, text,
    #                                 printer=self.page.form_concrete.enter_smiles)

    # def test_open_saved_dialog(self):
    #     name = 'testTest'
    #     self.page.form_list.open_dialog_from_list(name)
    #     self.page.form_concrete.wait_for_load()
    #     companion = self.page.form_concrete.get_companion_name()
    #     assert companion == name

    def test_send_message_check_update_chats_list(self):
        name, text = 'testTest', 'fkererfrfe'
        self._send_message_positive(name, text)
        self.driver.refresh()
        self.page.form_list.wait_for_load()
        self.page.form_list.check_dialog(name, text)